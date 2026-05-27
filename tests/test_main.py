"""main.py 的单元测试"""

import sys
from unittest.mock import patch

from src.main import main, run_fetch, run_update_readme


class TestRunFetch:
    def test_writes_articles_and_status_page(self):
        articles = [
            {
                "title": "Example",
                "url": "https://example.com/post",
                "date": "2026-05-26T00:00:00Z",
                "description": "desc",
            }
        ]
        statuses = [
            {
                "title": "Feed",
                "feed_url": "https://example.com/rss",
                "source_url": "https://www.v2ex.com/xna/s/1",
                "success": True,
                "article_count": 1,
                "error": "",
                "checked_at": "2026-05-26T00:00:00Z",
            }
        ]

        blocked_domains = {"example.com"}

        with patch("src.fetcher.fetch_all_feeds", return_value=(articles, statuses)) as fetch_all, patch(
            "src.writer.write_articles", return_value="api/2026/05/26.json"
        ) as write_articles, patch(
            "src.status_page.write_status_page", return_value="docs/status/latest-fetch-status.md"
        ) as write_status_page:
            run_fetch(blocked_domains=blocked_domains)

        fetch_all.assert_called_once_with(blocked_domains=blocked_domains)
        write_articles.assert_called_once_with(articles)
        write_status_page.assert_called_once_with(statuses)


class TestRunUpdateReadme:
    def test_passes_blocked_domains_to_readme_updater(self):
        blocked_domains = {"example.com"}

        with patch("src.readme_updater.run") as update_readme:
            run_update_readme(blocked_domains=blocked_domains)

        update_readme.assert_called_once_with(blocked_domains=blocked_domains)


class TestMain:
    def test_full_run_reuses_same_blocked_domains_for_fetch_and_readme(self):
        blocked_domains = {"example.com"}

        with patch.object(sys, "argv", ["vxna"]), patch(
            "src.main.run_crawl"
        ) as run_crawl, patch(
            "src.main.run_fetch"
        ) as run_fetch_mock, patch(
            "src.main.run_update_readme"
        ) as run_update_readme_mock, patch(
            "src.blocklist.read_blocked_root_domains", return_value=blocked_domains
        ):
            main()

        run_crawl.assert_called_once_with(start_index=None)
        run_fetch_mock.assert_called_once_with(blocked_domains=blocked_domains)
        run_update_readme_mock.assert_called_once_with(blocked_domains=blocked_domains)