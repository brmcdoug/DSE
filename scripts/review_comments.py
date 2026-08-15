#!/usr/bin/env python3
"""
List reviewer comments left in the markdown section files.

Comments are lines beginning with `//` (line-initial only, so URLs are safe),
or HTML comments on their own line. Each is reported with the nearest heading
and the paragraph it follows, so the intent is unambiguous.

Usage:
    review_comments.py                # all section files
    review_comments.py 06-*.md        # specific files
    review_comments.py --count        # just the tally
"""
import argparse
import glob
import os
import re
import sys

DEFAULT = sorted(glob.glob("0*.md") + glob.glob("1*.md"))


def scan(path):
    out = []
    heading = "(top)"
    prev = ""
    for n, raw in enumerate(open(path, encoding="utf-8"), 1):
        line = raw.rstrip("\n")
        s = line.strip()
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            heading = m.group(2).strip()
            prev = ""
            continue
        if s.startswith("//"):
            out.append((n, heading, s[2:].strip(), prev))
            continue
        if s.startswith("<!--") and s.endswith("-->"):
            out.append((n, heading, s[4:-3].strip(), prev))
            continue
        if s and not s.startswith(("|", ">", "-", "*", "!")):
            prev = s
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*", default=None)
    ap.add_argument("--count", action="store_true")
    a = ap.parse_args()

    files = a.files or DEFAULT
    files = [f for f in files if os.path.exists(f)]

    total = 0
    for f in files:
        items = scan(f)
        if not items:
            continue
        total += len(items)
        if a.count:
            print("%-34s %d" % (f, len(items)))
            continue
        print("=" * 76)
        print("%s  (%d comment%s)" % (f, len(items), "" if len(items) == 1 else "s"))
        print("=" * 76)
        for n, heading, comment, prev in items:
            print("\n  line %-5d  under: %s" % (n, heading[:60]))
            if prev:
                p = re.sub(r"\*\*|`", "", prev)
                print("             on: %s" % (p[:130] + ("…" if len(p) > 130 else "")))
            print("             ->  %s" % comment)
        print()

    if a.count or not total:
        print("\ntotal: %d comment(s)" % total)
    else:
        print("total: %d comment(s) across %d file(s)" % (total, len([f for f in files if scan(f)])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
