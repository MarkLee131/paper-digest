#!/usr/bin/env python3
"""
Build/refresh artefacts that MkDocs Material doesn't generate by itself:

1. Regenerate the auto-index block in `docs/index.md` — a reverse-chronological
   list of report cards, each with a one-paragraph summary and bucket counts.
2. Regenerate `docs/reports/.pages` — the awesome-pages plugin file that
   controls navigation order in the left sidebar (newest first).

Designed to be idempotent and CI-safe. Run by `.github/workflows/deploy.yml`
before `mkdocs build`, but also runnable locally.
"""

from __future__ import annotations
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"
REPORTS_DIR = DOCS / "reports"
INDEX = DOCS / "index.md"
PAGES_FILE = REPORTS_DIR / ".pages"

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
BEGIN = "<!-- BEGIN AUTO-INDEX -->"
END = "<!-- END AUTO-INDEX -->"


def parse_report(report_md: Path) -> dict:
    """Extract date, executive summary first paragraph, and bucket counts."""
    text = report_md.read_text(encoding="utf-8", errors="replace")

    # Strip front-matter
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4 :]

    date = report_md.parent.name

    # First non-empty paragraph of the Executive Summary section
    summary = ""
    m = re.search(
        r"##\s*0?\.?\s*Executive Summary\s*\n+(.+?)(?=\n##|\Z)",
        text, re.S | re.I,
    )
    if m:
        block = m.group(1).strip()
        para = block.split("\n\n", 1)[0]
        summary = re.sub(r"\s+", " ", para).strip()
        if len(summary) > 360:
            summary = summary[:357].rsplit(" ", 1)[0] + "…"

    # Public-safe bucket counts only — Outstanding / Keep / Borderline.
    counts = {}
    for label in ("Outstanding", "Keep", "Borderline"):
        m = re.search(rf"\*\*{label}[^:]*:\*\*\s*(\d+)", text)
        if m:
            counts[label] = int(m.group(1))

    return {"date": date, "summary": summary, "counts": counts}


def render_index_block(entries: list[dict]) -> str:
    """Render the homepage card list inside the AUTO-INDEX markers."""
    if not entries:
        return "_No reports yet — the index is rebuilt automatically on each push._\n"

    chips_for = {
        "Outstanding": "outstanding",
        "Keep": "keep",
        "Borderline": "borderline",
    }

    out = []
    for e in entries:
        date = e["date"]
        chips = "".join(
            f'<span class="chip {chips_for[k]}">{k} {v}</span>'
            for k, v in e["counts"].items()
        )
        summary = e["summary"] or "_(no executive summary detected)_"
        out.append(
            f'<div class="digest-card" markdown>\n'
            f'### [{date}](reports/{date}/index.md)\n'
            f'<div class="meta">{chips}</div>\n\n'
            f'{summary}\n'
            f'</div>'
        )
    return "\n\n".join(out) + "\n"


def render_pages_yaml(entries: list[dict]) -> str:
    """Generate docs/reports/.pages: reverse-chronological nav order.

    Quote each date so YAML parses it as a string (otherwise `2026-04-26`
    becomes a datetime.date and awesome-pages chokes on it).
    """
    lines = ["title: Reports", "nav:"]
    for e in entries:
        lines.append(f'  - "{e["date"]}"')
    return "\n".join(lines) + "\n"


def collect_entries() -> list[dict]:
    if not REPORTS_DIR.exists():
        return []
    entries = []
    for child in sorted(REPORTS_DIR.iterdir(), reverse=True):
        if not child.is_dir() or not DATE_RE.match(child.name):
            continue
        rpt = child / "index.md"
        if not rpt.exists():
            continue
        try:
            entries.append(parse_report(rpt))
        except Exception as ex:  # pragma: no cover
            print(f"warn: failed to parse {rpt}: {ex}", file=sys.stderr)
    return entries


def update_index(entries: list[dict]) -> None:
    block = render_index_block(entries)
    text = INDEX.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)
    replacement = f"{BEGIN}\n{block}{END}"
    new_text, n = pattern.subn(replacement, text, count=1)
    if n == 0:
        print(f"could not find auto-index markers in {INDEX}", file=sys.stderr)
        sys.exit(1)
    if new_text != text:
        INDEX.write_text(new_text, encoding="utf-8")
        print(f"docs/index.md updated ({len(entries)} reports)")
    else:
        print("docs/index.md unchanged")


def update_pages(entries: list[dict]) -> None:
    if not REPORTS_DIR.exists():
        return
    new_text = render_pages_yaml(entries)
    if PAGES_FILE.exists() and PAGES_FILE.read_text(encoding="utf-8") == new_text:
        print("docs/reports/.pages unchanged")
        return
    PAGES_FILE.write_text(new_text, encoding="utf-8")
    print(f"docs/reports/.pages updated ({len(entries)} entries)")


def main() -> int:
    entries = collect_entries()
    update_index(entries)
    update_pages(entries)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
