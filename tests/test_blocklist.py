"""
blocklist.py 的单元测试
"""

from pathlib import Path

from src.blocklist import (
    extract_root_domain,
    is_blocked_url,
    read_blocked_root_domains,
)


class TestReadBlockedRootDomains:
    def test_returns_empty_set_for_empty_file(self, tmp_path: Path):
        blocklist = tmp_path / "block.yaml"
        blocklist.write_text("", encoding="utf-8")

        assert read_blocked_root_domains(blocklist) == set()

    def test_normalizes_case_and_deduplicates_values(self, tmp_path: Path):
        blocklist = tmp_path / "block.yaml"
        blocklist.write_text(
            "blocked_root_domains:\n"
            "  - Example.com\n"
            "  - example.com\n"
            "  - BLOG.EXAMPLE.COM.\n",
            encoding="utf-8",
        )

        assert read_blocked_root_domains(blocklist) == {
            "example.com",
            "blog.example.com",
        }

    def test_ignores_invalid_top_level_structure(self, tmp_path: Path):
        blocklist = tmp_path / "block.yaml"
        blocklist.write_text("unexpected_key:\n  - example.com\n", encoding="utf-8")

        assert read_blocked_root_domains(blocklist) == set()


class TestExtractRootDomain:
    def test_extracts_root_domain_from_subdomain_url(self):
        assert extract_root_domain("https://blog.example.com/feed.xml") == "example.com"

    def test_returns_empty_string_for_invalid_url(self):
        assert extract_root_domain("not a url") == ""

    def test_preserves_private_suffix_domains(self):
        assert extract_root_domain("https://foo.github.io/rss.xml") == "foo.github.io"


class TestIsBlockedUrl:
    def test_returns_true_for_blocked_root_domain(self):
        blocked_domains = {"example.com"}

        assert is_blocked_url("https://news.example.com/feed", blocked_domains) is True

    def test_returns_false_for_unblocked_or_invalid_url(self):
        blocked_domains = {"example.com"}

        assert is_blocked_url("https://example.net/feed", blocked_domains) is False
        assert is_blocked_url("not a url", blocked_domains) is False