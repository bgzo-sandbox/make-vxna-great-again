"""
fetcher.py 的单元测试
"""

import pytest
from pathlib import Path

import httpx

from src.fetcher import fetch_feed, fetch_all_feeds, _parse_date, _entry_to_article

# ---- 测试用 RSS XML ----

RSS_TWO_ARTICLES = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Test Blog</title>
    <link>https://test.example.com</link>
    <item>
      <title>Article A</title>
      <link>https://test.example.com/a</link>
      <pubDate>Thu, 03 Apr 2026 10:00:00 +0000</pubDate>
      <description>Summary A</description>
    </item>
    <item>
      <title>Article B</title>
      <link>https://test.example.com/b</link>
      <pubDate>Wed, 02 Apr 2026 08:00:00 +0000</pubDate>
      <description>Summary B</description>
    </item>
  </channel>
</rss>
"""

RSS_EMPTY = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><title>Empty</title></channel></rss>
"""


def make_mock_client(responses: dict[str, tuple[int, str]]) -> httpx.Client:
    """
    构造 URL → (status_code, body) 映射的 mock client。
    """
    def handler(request: httpx.Request) -> httpx.Response:
        url = str(request.url)
        if url in responses:
            status, body = responses[url]
            return httpx.Response(status, text=body)
        return httpx.Response(404, text="")

    return httpx.Client(transport=httpx.MockTransport(handler))


class TestFetchFeed:
    def test_returns_articles_from_valid_rss(self):
        client = make_mock_client({"https://feed.example.com/rss": (200, RSS_TWO_ARTICLES)})
        articles, status = fetch_feed(
            "https://feed.example.com/rss",
            client,
            title="Test Blog",
            source_url="https://www.v2ex.com/xna/s/1",
        )
        assert len(articles) == 2
        assert articles[0]["title"] == "Article A"
        assert articles[0]["url"] == "https://test.example.com/a"
        assert status["success"] is True
        assert status["article_count"] == 2
        assert status["title"] == "Test Blog"
        assert status["source_url"] == "https://www.v2ex.com/xna/s/1"
        assert status["error"] == ""

    def test_returns_empty_list_on_http_error(self):
        client = make_mock_client({"https://feed.example.com/rss": (500, "")})
        articles, status = fetch_feed("https://feed.example.com/rss", client)
        assert articles == []
        assert status["success"] is False
        assert status["article_count"] == 0
        assert status["error"]

    def test_returns_empty_list_on_network_failure(self):
        def handler(request):
            raise httpx.ConnectError("timeout")
        client = httpx.Client(transport=httpx.MockTransport(handler))
        articles, status = fetch_feed("https://unreachable.example.com/rss", client)
        assert articles == []
        assert status["success"] is False
        assert status["article_count"] == 0
        assert "timeout" in status["error"]

    def test_returns_empty_on_empty_feed(self):
        client = make_mock_client({"https://feed.example.com/rss": (200, RSS_EMPTY)})
        articles, status = fetch_feed("https://feed.example.com/rss", client)
        assert articles == []
        assert status["success"] is True
        assert status["article_count"] == 0

    def test_article_fields_are_present(self):
        client = make_mock_client({"https://feed.example.com/rss": (200, RSS_TWO_ARTICLES)})
        articles, status = fetch_feed("https://feed.example.com/rss", client)
        article = articles[0]
        assert "title" in article
        assert "url" in article
        assert "date" in article
        assert "description" in article
        assert "checked_at" in status


class TestFetchAllFeeds:
    def test_aggregates_from_multiple_feeds(self, tmp_path: Path):
        opml = tmp_path / "rss.opml"
        opml.write_text(
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<opml version="1.0"><head/><body>'
            '<outline title="g" text="g">'
            '<outline xmlUrl="https://feed1.example.com/rss"/>'
            '<outline xmlUrl="https://feed2.example.com/rss"/>'
            '</outline></body></opml>',
            encoding="utf-8",
        )
        client = make_mock_client({
            "https://feed1.example.com/rss": (200, RSS_TWO_ARTICLES),
            "https://feed2.example.com/rss": (200, RSS_TWO_ARTICLES),
        })
        articles, statuses = fetch_all_feeds(opml, client)
        assert len(articles) == 4
        assert len(statuses) == 2
        assert all(status["success"] is True for status in statuses)

    def test_sorted_by_date_descending(self, tmp_path: Path):
        opml = tmp_path / "rss.opml"
        opml.write_text(
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<opml version="1.0"><head/><body>'
            '<outline title="g" text="g">'
            '<outline xmlUrl="https://feed.example.com/rss"/>'
            '</outline></body></opml>',
            encoding="utf-8",
        )
        client = make_mock_client({"https://feed.example.com/rss": (200, RSS_TWO_ARTICLES)})
        articles, statuses = fetch_all_feeds(opml, client)
        dates = [a["date"] for a in articles]
        assert dates == sorted(dates, reverse=True)
        assert len(statuses) == 1
        assert statuses[0]["success"] is True

    def test_single_feed_failure_does_not_break_others(self, tmp_path: Path):
        opml = tmp_path / "rss.opml"
        opml.write_text(
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<opml version="1.0"><head/><body>'
            '<outline title="g" text="g">'
            '<outline xmlUrl="https://good.example.com/rss"/>'
            '<outline xmlUrl="https://bad.example.com/rss"/>'
            '</outline></body></opml>',
            encoding="utf-8",
        )
        client = make_mock_client({
            "https://good.example.com/rss": (200, RSS_TWO_ARTICLES),
            "https://bad.example.com/rss": (500, ""),
        })
        articles, statuses = fetch_all_feeds(opml, client)
        assert len(articles) == 2
        assert len(statuses) == 2
        assert statuses[0]["success"] is True
        assert statuses[1]["success"] is False

    def test_returns_empty_when_opml_has_no_feeds(self, tmp_path: Path):
        opml = tmp_path / "empty.opml"
        opml.write_text(
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<opml version="1.0"><head/><body></body></opml>',
            encoding="utf-8",
        )
        client = make_mock_client({})
        articles, statuses = fetch_all_feeds(opml, client)
        assert articles == []
        assert statuses == []
