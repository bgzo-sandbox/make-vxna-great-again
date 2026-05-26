"""status_page.py 的单元测试"""

from datetime import datetime, timezone
from pathlib import Path

from src.status_page import format_status_markdown, write_status_page


FIXED_TIME = datetime(2026, 5, 26, 3, 0, tzinfo=timezone.utc)


STATUSES = [
    {
        "title": "Success Feed",
        "feed_url": "https://ok.example.com/rss",
        "source_url": "https://www.v2ex.com/xna/s/1",
        "success": True,
        "article_count": 2,
        "error": "",
        "checked_at": "2026-05-26T03:00:00Z",
    },
    {
        "title": "Failed|Feed",
        "feed_url": "https://bad.example.com/rss",
        "source_url": "",
        "success": False,
        "article_count": 0,
        "error": "boom|timeout",
        "checked_at": "2026-05-26T03:00:00Z",
    },
]


class TestFormatStatusMarkdown:
    def test_includes_summary_and_fixed_columns(self):
        content = format_status_markdown(STATUSES, FIXED_TIME)

        assert content.startswith("---\ntitle: Latest Fetch Status")
        assert "# Latest Fetch Status" in content
        assert "Generated at: 2026-05-26T03:00:00Z" in content
        assert "Total sources: 2" in content
        assert "Successful: 1" in content
        assert "Failed: 1" in content
        assert "| Status | Source | Feed | Origin | Articles | Error |" in content

    def test_places_failed_rows_before_successful_rows(self):
        content = format_status_markdown(STATUSES, FIXED_TIME)

        assert content.index("Failed&#124;Feed") < content.index("Success Feed")

    def test_escapes_pipe_characters_in_cells(self):
        content = format_status_markdown(STATUSES, FIXED_TIME)

        assert "Failed&#124;Feed" in content
        assert "boom&#124;timeout" in content

    def test_returns_zero_summary_for_empty_statuses(self):
        content = format_status_markdown([], FIXED_TIME)

        assert "Total sources: 0" in content
        assert "Successful: 0" in content
        assert "Failed: 0" in content


class TestWriteStatusPage:
    def test_overwrites_existing_file(self, tmp_path: Path):
        output = tmp_path / "status" / "latest-fetch-status.md"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text("old content", encoding="utf-8")

        result = write_status_page(STATUSES, output_path=output, generated_at=FIXED_TIME)

        content = output.read_text(encoding="utf-8")
        assert result == output
        assert "old content" not in content
        assert "Latest Fetch Status" in content

    def test_creates_parent_directory(self, tmp_path: Path):
        output = tmp_path / "nested" / "latest-fetch-status.md"

        write_status_page(STATUSES, output_path=output, generated_at=FIXED_TIME)

        assert output.exists()