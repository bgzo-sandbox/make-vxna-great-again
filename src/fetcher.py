"""
Feed 抓取与聚合模块

读取 config/rss.opml，并发抓取所有 RSS/Atom feed，
将所有文章按发布时间降序聚合后返回。

每篇文章数据结构：
    {
        "title":       str,
        "url":         str,
        "date":        str,   # ISO 8601，例如 "2026-04-04T08:00:00Z"
        "description": str,
        "source_root_domain": str,
    }

失败策略：单个 feed 抓取或解析失败时打印日志并跳过，不影响整体。
"""

import logging
from datetime import datetime, timezone
from pathlib import Path

import feedparser
import httpx

from src.blocklist import extract_root_domain, read_blocked_root_domains
from src.opml import DEFAULT_OPML_PATH, read_feed_sources
from src.text_utils import clean_description

logger = logging.getLogger(__name__)

# 单篇文章的类型别名
Article = dict[str, str]

# 单个 feed 源的抓取状态
FeedFetchStatus = dict[str, str | int | bool]


def _resolve_source_root_domain(source_url: str, feed_url: str) -> str:
    """优先使用 feed URL 提取博客根域名，缺失时回退到源页面 URL。"""
    return extract_root_domain(feed_url) or extract_root_domain(source_url)


def _build_feed_status(
    feed_url: str,
    *,
    title: str = "",
    source_url: str = "",
    success: bool,
    article_count: int,
    error: str,
) -> FeedFetchStatus:
    """构造统一的 feed 抓取状态对象。"""
    return {
        "title": title,
        "feed_url": feed_url,
        "source_url": source_url,
        "success": success,
        "article_count": article_count,
        "error": error,
        "checked_at": datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def _parse_date(entry: feedparser.FeedParserDict) -> datetime:
    """
    从 feedparser entry 中提取发布时间，解析为带时区的 datetime。
    若无法解析则返回 Unix 纪元（排序时置于末尾）。
    """
    # feedparser 将时间解析为 time.struct_time 存入 published_parsed / updated_parsed
    for attr in ("published_parsed", "updated_parsed"):
        t = getattr(entry, attr, None) or entry.get(attr)
        if t:
            try:
                return datetime(*t[:6], tzinfo=timezone.utc)
            except Exception:
                pass
    return datetime(1970, 1, 1, tzinfo=timezone.utc)


def _entry_to_article(
    entry: feedparser.FeedParserDict,
    *,
    source_root_domain: str = "",
) -> Article:
    """
    将 feedparser entry 转换为统一的 Article 字典。
    """
    title = entry.get("title", "").strip()
    url = entry.get("link", "").strip()
    date = _parse_date(entry).strftime("%Y-%m-%dT%H:%M:%SZ")

    # description 优先取 summary，其次取 content[0].value；清理富文本，限制 500 字符
    raw = ""
    if entry.get("summary"):
        raw = entry.summary.strip()
    elif entry.get("content"):
        raw = entry.content[0].get("value", "").strip()

    return {
        "title": title,
        "url": url,
        "date": date,
        "description": clean_description(raw)[:500],
        "source_root_domain": source_root_domain,
    }


def fetch_feed(
    url: str,
    client: httpx.Client,
    *,
    title: str = "",
    source_url: str = "",
    source_root_domain: str = "",
) -> tuple[list[Article], FeedFetchStatus]:
    """
    抓取单个 feed URL，返回文章列表。
    失败时打印日志并返回空列表。

    Args:
        url:    RSS/Atom feed 地址
        client: 已初始化的 httpx.Client

    Returns:
        (Article 列表, feed 抓取状态)
    """
    try:
        resp = client.get(url)
        resp.raise_for_status()
    except Exception as exc:
        logger.warning("抓取 feed 失败，跳过 %s: %s", url, exc)
        return [], _build_feed_status(
            url,
            title=title,
            source_url=source_url,
            success=False,
            article_count=0,
            error=str(exc),
        )

    try:
        parsed = feedparser.parse(resp.text)
    except Exception as exc:
        logger.warning("解析 feed 失败，跳过 %s: %s", url, exc)
        return [], _build_feed_status(
            url,
            title=title,
            source_url=source_url,
            success=False,
            article_count=0,
            error=str(exc),
        )

    if parsed.bozo and not parsed.entries:
        logger.warning("feed 解析异常，跳过 %s", url)
        return [], _build_feed_status(
            url,
            title=title,
            source_url=source_url,
            success=False,
            article_count=0,
            error="feed parse error",
        )

    articles = [
        _entry_to_article(e, source_root_domain=source_root_domain)
        for e in parsed.entries
    ]
    return articles, _build_feed_status(
        url,
        title=title,
        source_url=source_url,
        success=True,
        article_count=len(articles),
        error="",
    )


def fetch_all_feeds(
    opml_path: Path = DEFAULT_OPML_PATH,
    client: httpx.Client | None = None,
    blocked_domains: set[str] | None = None,
) -> tuple[list[Article], list[FeedFetchStatus]]:
    """
    读取 OPML，抓取所有 feed，聚合并按日期降序排序。

    Args:
        opml_path: OPML 文件路径
        client:    可注入的 httpx.Client（用于测试 mock）

    Returns:
        所有文章的聚合列表，按 date 降序排列
    """
    feed_sources = read_feed_sources(opml_path)
    if not feed_sources:
        logger.info("OPML 中无 feed，跳过抓取")
        return [], []

    if blocked_domains is None:
        blocked_domains = read_blocked_root_domains()
    articles: list[Article] = []
    statuses: list[FeedFetchStatus] = []
    _owns_client = client is None
    if _owns_client:
        client = httpx.Client(timeout=15, follow_redirects=True)

    try:
        for source in feed_sources:
            source_root_domain = _resolve_source_root_domain(
                source["html_url"],
                source["xml_url"],
            )
            if source_root_domain and source_root_domain in blocked_domains:
                logger.info(
                    "黑名单命中，跳过源 %s (%s)",
                    source["title"] or source["xml_url"],
                    source_root_domain,
                )
                continue

            feed_articles, status = fetch_feed(
                source["xml_url"],
                client,
                title=source["title"],
                source_url=source["html_url"],
                source_root_domain=source_root_domain,
            )
            articles.extend(feed_articles)
            statuses.append(status)
    finally:
        if _owns_client:
            client.close()

    # 按 date 字符串降序排列（ISO 8601 字符串可直接字符串比较）
    articles.sort(key=lambda a: a["date"], reverse=True)
    return articles, statuses
