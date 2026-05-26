"""
最近一次 feed 拉取状态页面输出模块。

负责生成并写入固定路径的 Markdown 看板页面。
"""

from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent
DEFAULT_STATUS_PAGE = PROJECT_ROOT / "docs" / "status" / "latest-fetch-status.md"


def _escape_table_text(value: object, max_length: int = 200) -> str:
	"""转义 Markdown 表格中的特殊字符，并限制文本长度。"""
	text = str(value or "").strip().replace("\n", " ")
	text = " ".join(text.split())
	if len(text) > max_length:
		text = text[: max_length - 1].rstrip() + "…"
	return text.replace("|", "&#124;")


def _format_link(label: str, url: str) -> str:
	"""格式化 Markdown 链接；URL 为空时回退为纯文本。"""
	safe_label = _escape_table_text(label)
	safe_url = str(url or "").strip()
	if not safe_url:
		return safe_label or "-"
	return f"[{safe_label or safe_url}]({safe_url})"


def _sort_statuses(statuses: list[dict]) -> list[dict]:
	"""将失败项排在前面，其次按标题和 feed URL 排序。"""
	return sorted(
		statuses,
		key=lambda status: (
			bool(status.get("success", False)),
			str(status.get("title", "")).lower(),
			str(status.get("feed_url", "")).lower(),
		),
	)


def format_status_markdown(statuses: list[dict], generated_at: datetime) -> str:
	"""将抓取状态列表格式化为 Markdown 看板。"""
	generated_at = generated_at.astimezone(timezone.utc)
	generated_at_str = generated_at.strftime("%Y-%m-%dT%H:%M:%SZ")
	ordered_statuses = _sort_statuses(statuses)
	total_count = len(ordered_statuses)
	success_count = sum(1 for status in ordered_statuses if status.get("success"))
	failed_count = total_count - success_count

	lines = [
		"---",
		"title: Latest Fetch Status",
		f"created: {generated_at_str}",
		f"modified: {generated_at_str}",
		"description: Latest source-level fetch result for the most recent execution.",
		"tags:",
		"  - ai-notes",
		"  - status",
		"  - generated",
		"---",
		"",
		"# Latest Fetch Status",
		"",
		f"Generated at: {generated_at_str}",
		"",
		f"Total sources: {total_count}",
		f"Successful: {success_count}",
		f"Failed: {failed_count}",
		"",
		"| Status | Source | Feed | Origin | Articles | Error |",
		"| --- | --- | --- | --- | ---: | --- |",
	]

	for status in ordered_statuses:
		success = bool(status.get("success", False))
		lines.append(
			"| {status_label} | {source} | {feed} | {origin} | {articles} | {error} |".format(
				status_label="Success" if success else "Failed",
				source=_escape_table_text(status.get("title", "")) or "-",
				feed=_format_link(str(status.get("feed_url", "")), str(status.get("feed_url", ""))),
				origin=_format_link("Origin", str(status.get("source_url", ""))),
				articles=int(status.get("article_count", 0) or 0),
				error=_escape_table_text(status.get("error", "")) or "-",
			)
		)

	return "\n".join(lines)


def write_status_page(
	statuses: list[dict],
	output_path: Path = DEFAULT_STATUS_PAGE,
	generated_at: datetime | None = None,
) -> Path:
	"""将最近一次抓取状态写入固定 Markdown 文件。"""
	if generated_at is None:
		generated_at = datetime.now(tz=timezone.utc)

	output_path.parent.mkdir(parents=True, exist_ok=True)
	output_path.write_text(
		format_status_markdown(statuses, generated_at=generated_at),
		encoding="utf-8",
	)
	return output_path