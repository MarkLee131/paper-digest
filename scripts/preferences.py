#!/usr/bin/env python3
"""
Compute per-attribute preferences from .private/feedback.jsonl using a Beta-
distribution posterior with Laplace smoothing. Outputs .private/preferences.json
which the SKILL pipeline consumes during Stage-1 / Stage-2 screening.

Per-attribute posterior:
    p(prefer | a) = (alpha + up_a) / (alpha + beta + up_a + down_a)
with alpha = beta = 1 (Laplace).

Attributes tracked: author, venue, topic, methodology (free-form), rating
(thumbs-up / thumbs-down / save-for-later — the last one counts as half-up).
"""

from __future__ import annotations
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FEEDBACK_FILE = ROOT / ".private" / "feedback.jsonl"
PREF_FILE = ROOT / ".private" / "preferences.json"

ALPHA = 1.0
BETA = 1.0


def split_authors(authors_field: str) -> list[str]:
    """Split a comma- or 'and'-separated author list into individual names.
    Any 'et al.' / parenthetical group names are dropped."""
    raw = authors_field.replace(" and ", ",")
    parts = []
    for chunk in raw.split(","):
        chunk = chunk.strip()
        if not chunk or "et al" in chunk.lower():
            continue
        # Strip trailing parens like "(Z. Lin)"
        chunk = chunk.split("(")[0].strip()
        if chunk:
            parts.append(chunk)
    return parts


def main() -> int:
    if not FEEDBACK_FILE.exists():
        PREF_FILE.parent.mkdir(parents=True, exist_ok=True)
        PREF_FILE.write_text(json.dumps({"empty": True}), encoding="utf-8")
        print("no feedback yet — wrote empty preferences")
        return 0

    counts = defaultdict(lambda: {"up": 0.0, "down": 0.0})

    with FEEDBACK_FILE.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            rating = r.get("rating", "")
            if rating == "thumbs-up":
                up, down = 1.0, 0.0
            elif rating == "thumbs-down":
                up, down = 0.0, 1.0
            elif rating == "save-for-later":
                up, down = 0.5, 0.0
            else:
                continue

            attrs = []
            if "venue" in r:
                attrs.append(("venue", r["venue"]))
            if "topic" in r:
                attrs.append(("topic", r["topic"]))
            for a in split_authors(r.get("authors", "")):
                attrs.append(("author", a))

            for kind, value in attrs:
                key = f"{kind}::{value}"
                counts[key]["up"] += up
                counts[key]["down"] += down

    posteriors = {}
    for key, c in counts.items():
        n = c["up"] + c["down"]
        post = (ALPHA + c["up"]) / (ALPHA + BETA + n)
        posteriors[key] = {
            "up": c["up"],
            "down": c["down"],
            "n": n,
            "posterior": round(post, 4),
        }

    PREF_FILE.parent.mkdir(parents=True, exist_ok=True)
    PREF_FILE.write_text(json.dumps(posteriors, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {len(posteriors)} attribute posteriors to {PREF_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
