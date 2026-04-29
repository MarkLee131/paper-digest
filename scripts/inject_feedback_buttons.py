#!/usr/bin/env python3
"""
Inject 👍 / 👎 / 🔖 GitHub-issue links into every paper-card summary line in
a daily report. Each link deep-links to a pre-filled issue creation form on
the private feedback repo. Idempotent: skips summaries that already have buttons.

Usage:
    python scripts/inject_feedback_buttons.py docs/reports/YYYY-MM-DD/index.md
"""

from __future__ import annotations
import re
import sys
import urllib.parse
from pathlib import Path

FEEDBACK_REPO = "MarkLee131/paper-digest"
# `rating` is the backend-stable key (preferences.py keys off "thumbs-down").
# EMOJI is what the reader actually sees — kept neutral so a "not interested"
# vote isn't visually loud.
EMOJI = {"thumbs-up": "👍", "thumbs-down": "🫥", "save-for-later": "🔖"}
TITLE = {"thumbs-up": "thumbs up", "thumbs-down": "less interested", "save-for-later": "save for later"}


def feedback_url(rating: str, paper_id: str, title: str, authors: str, venue: str, topic: str) -> str:
    issue_title = f"[feedback] {paper_id} {title} {EMOJI[rating]}"
    body = (
        f"paper_id: {paper_id}\n"
        f"title: {title}\n"
        f"authors: {authors}\n"
        f"venue: {venue}\n"
        f"topic: {topic}\n"
        f"rating: {rating}\n"
        f"\n"
        f"<!-- Optional notes below this line are read by preferences.py as soft signals. -->\n"
    )
    qs = urllib.parse.urlencode({
        "title": issue_title,
        "body": body,
        "labels": f"feedback,{rating}",
    })
    return f"https://github.com/{FEEDBACK_REPO}/issues/new?{qs}"


def buttons(paper_id: str, title: str, authors: str, venue: str, topic: str) -> str:
    btns = []
    for rating in ("thumbs-up", "thumbs-down", "save-for-later"):
        url = feedback_url(rating, paper_id, title, authors, venue, topic)
        btns.append(
            f'<a href="{url}" target="_blank" rel="noopener" '
            f'class="fb-{rating}" title="{TITLE[rating]}" '
            f'onclick="event.stopPropagation()">{EMOJI[rating]}</a>'
        )
    return f'<span class="feedback-buttons">{"".join(btns)}</span>'


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2

    report_path = Path(argv[1])
    if not report_path.exists():
        print(f"file not found: {report_path}", file=sys.stderr)
        return 1

    # Date is the parent folder name
    date = report_path.parent.name

    text = report_path.read_text(encoding="utf-8")

    # The summary line carries the section number, topic, and a one-line title.
    # Format produced by SKILL.md:
    #   <summary><strong>N.X</strong> · <span class="topic-chip">topic</span> · Title …</summary>
    summary_re = re.compile(
        r'<summary>(<strong>([2-4]\.\d+)</strong>\s*·\s*<span class="topic-chip">([^<]+)</span>\s*·\s*([^<]+))</summary>'
    )

    # Collect minimal metadata per paper from the surrounding section text.
    # Each paper section follows its summary and starts with an `**Authors:** ...`
    # line; we use that to extract authors + venue.
    sections = re.split(r"<details class=\"paper-card\" markdown>", text)
    metadata: dict[str, tuple[str, str]] = {}
    for sec in sections[1:]:
        ms = re.search(r'<summary>.*?<strong>([2-4]\.\d+)</strong>.*?</summary>', sec, re.S)
        if not ms:
            continue
        num = ms.group(1)
        # Authors line if present
        auth = re.search(r"\*\*Authors:\*\*\s*([^\n]+)", sec)
        venue = re.search(r"\*\*Venue:\*\*\s*([^\n]+)", sec)
        if auth and venue:
            metadata[num] = (auth.group(1).strip(), venue.group(1).strip())
        else:
            # For Keep / Borderline single-paragraph sections, parse the first line
            first = sec.split("</summary>", 1)[1].strip().split("\n", 1)[0]
            metadata[num] = (first[:200], "preprint")

    def repl(m: re.Match) -> str:
        full_inner, num, topic, title_fragment = m.group(1), m.group(2), m.group(3), m.group(4).strip(" —–-")
        if "feedback-buttons" in full_inner:
            return m.group(0)
        authors, venue = metadata.get(num, ("(unknown)", "(unknown)"))
        paper_id = f"{date}-{num}"
        bs = buttons(paper_id, title_fragment, authors, venue, topic)
        return f"<summary>{full_inner}{bs}</summary>"

    new_text = summary_re.sub(repl, text)
    report_path.write_text(new_text, encoding="utf-8")

    n_changed = len(re.findall(r"feedback-buttons", new_text)) - len(re.findall(r"feedback-buttons", text))
    print(f"injected feedback buttons into {n_changed} paper cards in {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
