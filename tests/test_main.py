"""main.py 的单元测试"""

from unittest.mock import patch

from src.main import run_fetch


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

        with patch("src.fetcher.fetch_all_feeds", return_value=(articles, statuses)) as fetch_all, patch(
            "src.writer.write_articles", return_value="api/2026/05/26.json"
        ) as write_articles, patch(
            "src.status_page.write_status_page", return_value="docs/status/latest-fetch-status.md"
        ) as write_status_page:
            run_fetch()

        fetch_all.assert_called_once_with()
        write_articles.assert_called_once_with(articles)
        write_status_page.assert_called_once_with(statuses)