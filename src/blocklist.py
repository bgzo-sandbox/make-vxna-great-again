"""
黑名单配置读取模块。

负责读取 config/block.yaml，并将根域名黑名单清洗为统一的小写集合。
"""

import logging
from pathlib import Path

import tldextract

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).parent.parent
DEFAULT_BLOCKLIST_PATH = PROJECT_ROOT / "config" / "block.yaml"
BLOCKED_ROOT_DOMAINS_KEY = "blocked_root_domains"
_EXTRACTOR = tldextract.TLDExtract(
    suffix_list_urls=(),
    include_psl_private_domains=True,
)


def _normalize_domain(value: str) -> str:
    """将根域名字符串归一化为可比较形式。"""
    return value.strip().lower().rstrip(".")


def extract_root_domain(url: str) -> str:
    """从 URL 或域名字符串中提取根域名。"""
    value = str(url or "").strip()
    if not value:
        return ""

    extracted = _EXTRACTOR(value)
    if not extracted.domain or not extracted.suffix:
        return ""

    return _normalize_domain(f"{extracted.domain}.{extracted.suffix}")


def is_blocked_url(url: str, blocked_domains: set[str]) -> bool:
    """判断 URL 的根域名是否命中黑名单。"""
    root_domain = extract_root_domain(url)
    if not root_domain:
        return False
    return root_domain in blocked_domains


def read_blocked_root_domains(
    blocklist_path: Path = DEFAULT_BLOCKLIST_PATH,
) -> set[str]:
    """读取黑名单配置，返回去重后的根域名集合。"""
    if not blocklist_path.exists():
        return set()

    content = blocklist_path.read_text(encoding="utf-8").strip()
    if not content:
        return set()

    lines = []
    for raw_line in content.splitlines():
        line = raw_line.split("#", 1)[0].rstrip()
        if line:
            lines.append(line)

    if not lines:
        return set()

    first_line = lines[0].strip()
    if not first_line.startswith(f"{BLOCKED_ROOT_DOMAINS_KEY}:"):
        logger.warning("黑名单配置缺少顶层键 %s，已忽略", BLOCKED_ROOT_DOMAINS_KEY)
        return set()

    inline_value = first_line.split(":", 1)[1].strip()
    if inline_value:
        if inline_value != "[]":
            logger.warning("黑名单配置格式无效，已忽略: %s", blocklist_path)
        return set()

    blocked_domains: set[str] = set()
    for raw_line in lines[1:]:
        stripped = raw_line.strip()
        if not stripped.startswith("-"):
            logger.warning("黑名单配置包含无法识别的条目，已忽略: %s", stripped)
            continue
        value = stripped[1:].strip().strip('"').strip("'")
        if not value:
            continue
        normalized = _normalize_domain(value)
        if normalized:
            blocked_domains.add(normalized)

    return blocked_domains
