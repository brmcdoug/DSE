#!/usr/bin/env python3
"""
Convert an Outlook for Mac .olm archive to CSV.

Usage:
    python olm_to_csv.py <file.olm> [output.csv]
    python olm_to_csv.py <file.olm> --inspect   # dump first message XML for debugging
"""

import csv
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


def strip_ns(tag: str) -> str:
    """Strip XML namespace prefix from a tag name."""
    return tag.split("}")[-1] if "}" in tag else tag


def child_text(elem, *local_names: str) -> str:
    """Return text of the first direct child element matching any of the local names."""
    for child in elem:
        if strip_ns(child.tag) in local_names:
            return (child.text or "").strip()
    return ""


def collect_addresses(email_elem, container_name: str) -> str:
    """
    Collect addresses from a container like OPFMessageCopyFromAddresses.
    Addresses are stored as attributes on <emailAddress> child elements:
        OPFContactEmailAddressAddress  — the email address
        OPFContactEmailAddressName     — the display name
    """
    for child in email_elem:
        if strip_ns(child.tag) == container_name:
            parts = []
            for addr in child:
                # Attributes may carry any namespace prefix; strip them too
                attrs = {strip_ns(k): v for k, v in addr.attrib.items()}
                email = attrs.get("OPFContactEmailAddressAddress", "").strip()
                name  = attrs.get("OPFContactEmailAddressName", "").strip()
                if email:
                    parts.append(f"{name} <{email}>" if name else email)
                elif name:
                    parts.append(name)
            return "; ".join(parts)
    return ""


def parse_email_element(email_elem, source_path: str) -> dict:
    """Parse a single <email> element into a dict of fields."""
    m = {}
    m["subject"]        = child_text(email_elem, "OPFMessageCopySubject")
    m["date"]           = child_text(email_elem, "OPFMessageCopySentTime",
                                                  "OPFMessageCopyReceivedTime")
    m["from"]           = collect_addresses(email_elem, "OPFMessageCopyFromAddresses") \
                          or collect_addresses(email_elem, "OPFMessageCopySenderAddress")
    m["to"]             = collect_addresses(email_elem, "OPFMessageCopyToAddresses")
    m["cc"]             = collect_addresses(email_elem, "OPFMessageCopyCCAddresses")
    m["bcc"]            = collect_addresses(email_elem, "OPFMessageCopyBCCAddresses")

    # Plain-text preview is compact and already readable — prefer it for the body column.
    # OPFMessageCopyBody / OPFMessageCopyHTMLBody contain HTML-escaped HTML blobs.
    m["body"]           = child_text(email_elem, "OPFMessageCopyPreview")

    has_attach = any(strip_ns(c.tag) == "OPFMessageCopyAttachmentList"
                     for c in email_elem)
    m["has_attachments"] = "yes" if has_attach else "no"
    m["source_path"]    = source_path
    return m


def parse_xml_file(xml_bytes: bytes, source_path: str) -> list[dict]:
    """
    Parse one XML file from the OLM archive.
    Structure: <emails elementCount="N"><email>...</email>...</emails>
    Returns a list of message dicts (usually just one per file).
    """
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return []

    local_root = strip_ns(root.tag)

    # Normal case: root is <emails>, children are <email>
    if local_root == "emails":
        messages = []
        for child in root:
            if strip_ns(child.tag) == "email":
                m = parse_email_element(child, source_path)
                if m.get("subject") or m.get("from") or m.get("date"):
                    messages.append(m)
        return messages

    # Fallback: root is <email> directly
    if local_root == "email":
        m = parse_email_element(root, source_path)
        return [m] if (m.get("subject") or m.get("from") or m.get("date")) else []

    return []


def inspect_first(olm_path: str):
    """Print the raw XML of the first message file — useful for debugging."""
    with zipfile.ZipFile(olm_path) as zf:
        for name in zf.namelist():
            if name.lower().endswith(".xml"):
                print(f"=== {name} ===\n")
                print(zf.read(name).decode("utf-8", errors="replace"))
                return
    print("No XML files found in the OLM archive.")


def convert(olm_path: str, csv_path: str):
    FIELDS = ["date", "from", "to", "cc", "bcc", "subject",
              "has_attachments", "body", "source_path"]

    total = 0
    skipped_files = 0

    with zipfile.ZipFile(olm_path) as zf:
        xml_files = [n for n in zf.namelist() if n.lower().endswith(".xml")]
        if not xml_files:
            print("ERROR: No XML files found inside the OLM archive.")
            sys.exit(1)

        print(f"Found {len(xml_files)} XML file(s) in archive…")

        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
            writer.writeheader()

            for name in xml_files:
                raw = zf.read(name)
                messages = parse_xml_file(raw, name)
                if not messages:
                    skipped_files += 1
                    continue
                writer.writerows(messages)
                total += len(messages)

    print(f"Parsed {total:,} message(s), skipped {skipped_files} non-message XML file(s).")
    print(f"Written to: {csv_path}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    olm_path = sys.argv[1]
    if not Path(olm_path).exists():
        print(f"ERROR: File not found: {olm_path}")
        sys.exit(1)

    if "--inspect" in sys.argv:
        inspect_first(olm_path)
        return

    csv_path = sys.argv[2] if len(sys.argv) > 2 else str(Path(olm_path).with_suffix(".csv"))
    convert(olm_path, csv_path)


if __name__ == "__main__":
    main()
