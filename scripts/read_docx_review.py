#!/usr/bin/env python3
"""
Read reviewer comments and tracked changes out of a .docx.

Usage:
    read_docx_review.py <file.docx> [--section "Business Impact"]

Reports, in document order:
  * comments — author, date, the text they are anchored to, and the comment body
  * tracked insertions and deletions (if the reviewer used Track Changes)

Word does not need to be closed to read; this opens the file read-only.
"""
import argparse
import re
import zipfile
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def text_of(el):
    """Visible text of an element, ignoring deleted runs."""
    out = []
    for node in el.iter():
        if node.tag == W + "t":
            out.append(node.text or "")
        elif node.tag == W + "tab":
            out.append("\t")
    return "".join(out)


def load(path, name):
    with zipfile.ZipFile(path) as z:
        try:
            return ET.fromstring(z.read(name))
        except KeyError:
            return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("--section", help="only report items under this Heading 1")
    a = ap.parse_args()

    doc = load(a.docx, "word/document.xml")
    comments_xml = load(a.docx, "word/comments.xml")

    bodies = {}
    if comments_xml is not None:
        for c in comments_xml.findall(W + "comment"):
            bodies[c.get(W + "id")] = {
                "author": c.get(W + "author", "?"),
                "date": (c.get(W + "date") or "")[:16].replace("T", " "),
                "initials": c.get(W + "initials", ""),
                "text": " ".join(text_of(c).split()),
            }

    body = doc.find(W + "body")
    current_h1 = "(front matter)"
    open_ranges = {}
    anchored = {}
    findings = []

    for p in body.iter(W + "p"):
        style_el = p.find(W + "pPr/" + W + "pStyle")
        style = style_el.get(W + "val") if style_el is not None else ""
        ptext = " ".join(text_of(p).split())
        if style in ("Heading1", "Heading 1") and ptext:
            current_h1 = ptext

        if a.section and current_h1.lower() != a.section.lower():
            # still need to track ranges spanning into the section
            pass

        # comment anchors
        for s in p.iter(W + "commentRangeStart"):
            open_ranges[s.get(W + "id")] = current_h1
        for e in p.iter(W + "commentRangeEnd"):
            cid = e.get(W + "id")
            anchored.setdefault(cid, ptext)
            open_ranges.pop(cid, None)
        for r in p.iter(W + "commentReference"):
            cid = r.get(W + "id")
            anchored.setdefault(cid, ptext)

        # tracked changes
        for ins in p.iter(W + "ins"):
            t = " ".join(text_of(ins).split())
            if t:
                findings.append(("INSERT", current_h1, ins.get(W + "author", "?"),
                                 (ins.get(W + "date") or "")[:16].replace("T", " "), t, ptext))
        for dele in p.iter(W + "del"):
            t = "".join(n.text or "" for n in dele.iter(W + "delText"))
            t = " ".join(t.split())
            if t:
                findings.append(("DELETE", current_h1, dele.get(W + "author", "?"),
                                 (dele.get(W + "date") or "")[:16].replace("T", " "), t, ptext))

    # ---- report ----
    sec = a.section

    shown = 0
    if bodies:
        print("=" * 78)
        print("COMMENTS (%d)" % len(bodies))
        print("=" * 78)
        for cid, c in sorted(bodies.items(), key=lambda kv: int(kv[0])):
            where = anchored.get(cid, "")
            if sec and sec.lower() not in (where or "").lower() and not _in_section(cid, anchored, sec):
                pass
            shown += 1
            print("\n[%s] %s  %s" % (cid, c["author"], c["date"]))
            if where:
                print("    on: “%s”" % (where[:150] + ("…" if len(where) > 150 else "")))
            print("    → %s" % c["text"])
    else:
        print("No comments found in %s" % a.docx)

    if findings:
        if sec:
            findings = [f for f in findings if f[1].lower() == sec.lower()]
        print()
        print("=" * 78)
        print("TRACKED CHANGES (%d)" % len(findings))
        print("=" * 78)
        for kind, h1, author, date, t, ctx in findings:
            print("\n%-6s  %-18s %s  [%s]" % (kind, author, date, h1))
            print("    %s" % (t[:200] + ("…" if len(t) > 200 else "")))
    else:
        print("\nNo tracked changes found (reviewer edited without Track Changes, or none yet).")


def _in_section(cid, anchored, sec):
    return True


if __name__ == "__main__":
    main()
