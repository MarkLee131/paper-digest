#!/usr/bin/env python3
"""
Pull feedback issues from the private paper-digest-feedback repo, parse the
structured body, and append parsed records to .private/feedback.jsonl.

Run before each daily skill execution. Requires `gh` CLI authenticated with
read access to the feedback repo.
"""

from __future__ import annotations
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = "MarkLee131/paper-digest"
ROOT = Path(__file__).resolve().parent.parent
FEEDBACK_FILE = ROOT / ".private" / "feedback.jsonl"


def have_gh() -> bool:
    return shutil.which("gh") is not None


def fetch_open_issues() -> list[dict]:
    """Pull open feedback issues. Returns parsed JSON list."""
    if not have_gh():
        print("gh CLI not found — cannot pull feedback. Skipping.", file=sys.stderr)
        return []
    cmd = [
        "gh", "issue", "list",
        "--repo", REPO,
        "--state", "open",
        "--label", "feedback",
        "--limit", "200",
        "--json", "number,title,body,labels,createdAt,closedAt",
    ]
    try:
        out = subprocess.check_output(cmd, text=True)
    except subprocess.CalledProcessError as ex:
        print(f"gh issue list failed: {ex}", file=sys.stderr)
        return []
    return json.loads(out)


def parse_body(body: str) -> dict:
    """Extract key:value lines from the issue body."""
    fields = {}
    for line in body.splitlines():
        m = re.match(r"^([a-z_]+):\s*(.+)$", line.strip())
        if m:
            fields[m.group(1)] = m.group(2).strip()
    return fields


def close_issue(number: int) -> None:
    if not have_gh():
        return
    subprocess.run(
        ["gh", "issue", "close", str(number), "--repo", REPO, "--comment", "ingested"],
        check=False,
    )


def main() -> int:
    FEEDBACK_FILE.parent.mkdir(parents=True, exist_ok=True)
    issues = fetch_open_issues()
    if not issues:
        print("no open feedback issues")
        return 0

    new_records = []
    closed = 0
    with FEEDBACK_FILE.open("a", encoding="utf-8") as fh:
        for it in issues:
            parsed = parse_body(it.get("body", ""))
            record = {
                "issue": it["number"],
                "createdAt": it["createdAt"],
                "title": it.get("title", ""),
                **parsed,
            }
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
            new_records.append(record)
            close_issue(it["number"])
            closed += 1

    print(f"ingested {len(new_records)} new feedback records (closed {closed} issues)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
