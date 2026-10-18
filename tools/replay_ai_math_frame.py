#!/usr/bin/env python3
"""Replay the frozen openai/math family frame from exact CONTENTS.md bytes.

No network access and no repository/Git commands are performed.
Retrieve CONTENTS.md at the pinned revision through the GitHub connector,
preserve its UTF-8 bytes, then run:
  python tools/replay_ai_math_frame.py /path/to/CONTENTS.md > /tmp/replayed.json

This parser verifies the Git blob SHA before parsing. Output contains only
family/manuscript metadata, never abstracts or other prose body text.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

REVISION = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
EXPECTED_BLOB = "2c68c086fff36a5806c936ad1659cf1a8d0b6dd9"
HEADER = re.compile(r"^\*\*(\d{3})\.\s+(.+?)\.\*\*(.*)$", re.MULTILINE)
PAPER = re.compile(r"^&emsp;\[(.*)\]\((preprints/.*\.pdf)\)(.*)$", re.MULTILINE)
SCOPE = re.compile(r"\[Lean\]\((lean/docs/\d+\.md)\)")

def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()

def parse(text, blob_sha=EXPECTED_BLOB):
    headers = list(HEADER.finditer(text))
    families = []
    for i, match in enumerate(headers):
        stop = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        block = text[match.start():stop]
        papers = [
            {
                "title": row.group(1),
                "path": row.group(2),
                "annotation": row.group(3).strip() or None,
                "source_contents_blob_sha": blob_sha,
            }
            for row in PAPER.finditer(block)
        ]
        raw_row_count = len(re.findall(r"^&emsp;\[", block, re.MULTILINE))
        if raw_row_count != len(papers):
            raise ValueError(f"Family {match.group(1)} has an unparsed manuscript row")
        scope = SCOPE.search(block)
        families.append({
            "id": match.group(1),
            "title": match.group(2),
            "domain": None,
            "domain_note": "not coded; CONTENTS has no explicit family discipline label",
            "scope_doc": scope.group(1) if scope else None,
            "source_line": text.count("\n", 0, match.start()) + 1,
            "manuscripts": papers,
        })
    ids = [family["id"] for family in families]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate family ID")
    paths = [paper["path"] for family in families for paper in family["manuscripts"]]
    max_id = max(map(int, ids), default=0)
    return {
        "schema": 1,
        "repository": "openai/math",
        "revision": REVISION,
        "source_path": "CONTENTS.md",
        "source_blob_sha": blob_sha,
        "source_url": f"https://github.com/openai/math/blob/{REVISION}/CONTENTS.md",
        "read_date": "2026-10-18",
        "selection_performed": False,
        "representativeness": "not sampled or mechanism-coded",
        "counts": {
            "families": len(families),
            "manuscript_rows": len(paths),
            "unique_manuscript_paths": len(set(paths)),
            "scope_doc_links": sum(family["scope_doc"] is not None for family in families),
        },
        "absent_integer_labels": [n for n in range(1, max_id + 1) if f"{n:03d}" not in ids],
        "families": families,
    }

def self_test():
    # These two edge cases caused the initial naive 718-row undercount.
    fixture = (
        "**001. A test family.** Description excluded from output.\n"
        "&emsp;[Sharp integral fillings in CAT(0) spaces]"
        "(preprints/Sharp-integral-fillings-in-CAT(0)-spaces/paper.pdf)\n"
        "&emsp;[A second writeup](preprints/Second/paper.pdf) — secondary writeup\n"
        "An abstract that must never appear in the metadata output.\n"
        "**003. Another family.** ([Lean](lean/docs/003.md))\n"
        "&emsp;[Third manuscript](preprints/Third/paper.pdf)\n"
    )
    result = parse(fixture, "fixture")
    assert result["counts"] == {
        "families": 2, "manuscript_rows": 3,
        "unique_manuscript_paths": 3, "scope_doc_links": 1,
    }
    assert result["absent_integer_labels"] == [2]
    assert result["families"][0]["manuscripts"][0]["path"].endswith("CAT(0)-spaces/paper.pdf")
    assert result["families"][0]["manuscripts"][1]["annotation"] == "— secondary writeup"
    assert "Description excluded" not in json.dumps(result)
    assert "An abstract" not in json.dumps(result)
    print("Parser edge cases passed: parentheses, row suffix, labels, no abstracts.")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contents", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if args.contents is None:
        parser.error("provide exact CONTENTS.md bytes or --self-test")
    data = args.contents.read_bytes()
    observed = git_blob_sha(data)
    if observed != EXPECTED_BLOB:
        raise SystemExit(f"Blob mismatch: expected {EXPECTED_BLOB}, observed {observed}")
    result = parse(data.decode("utf-8"), observed)
    expected = {"families": 372, "manuscript_rows": 719, "unique_manuscript_paths": 719, "scope_doc_links": 242}
    if result["counts"] != expected:
        raise SystemExit(f"Count mismatch: {result['counts']}")
    if result["absent_integer_labels"] != [45, 61, 70, 123, 163]:
        raise SystemExit("Unexpected family label gaps")
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
