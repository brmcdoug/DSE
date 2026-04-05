#!/usr/bin/env python3
"""
Analyze an email CSV (produced by olm_to_csv.py) and produce a structured
summary keyed to DSE promotion categories.

Usage:
    python analyze_emails.py emails.csv [output_summary.json]

The output JSON is intentionally compact so it can be fed to an LLM for
narrative generation without blowing the context window.
"""

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


# ---------------------------------------------------------------------------
# Keyword taxonomy — maps DSE category → list of search terms (case-insensitive)
# ---------------------------------------------------------------------------
TAXONOMY = {
    "segment_routing_srv6": [
        "srv6", "sr-mpls", "srmpls", "segment routing", "segment-routing",
        "sr policy", "srte", "sr-te", "srh", "sid", "locator",
        "binding sid", "flex-algo", "flexalgo", "micro-sid", "microsid",
        "srv6 grt", "srv6 sgt", "srv6 sonic", "srv6 cilium",
        "srv6 vrfid", "sl-api", "sla on-demand",
    ],
    "hyperscale_cloud_ai": [
        "hyperscale", "hyper-scale", "cloud native", "cloud-native",
        "microsoft", "msft", "azure", "oracle", "oci", "aws", "amazon",
        "google", "meta", "facebook", "coreweave", "lambda labs",
        "ai fabric", "ai network", "ai/ml", "gpu cluster", "gpu fabric",
        "1.6t", "400g", "800g", "dragonfly", "slimfly", "hoffman-singleton",
        "physnet", "phynet",
    ],
    "sonic_open_source": [
        "sonic", "dent", "openconfig", "yang", "netconf", "gnmi",
        "open source", "open-source", "github", "linux foundation",
        "single os", "disaggregat",
    ],
    "cilium_isovalent": [
        "cilium", "isovalent", "ebpf", "bpf", "kubernetes", "k8s",
        "service mesh", "microsegmentation", "micro-segmentation",
        "policy plane", "host-based", "host based", "cn-srv6",
    ],
    "jalapeno_programmability": [
        "jalapeno", "jalapeño", "broker", "sr-apps", "sr apps",
        "skylight", "telegraf", "kafka", "graph db", "arango",
        "programmability", "automation", "intent-based", "yukon",
    ],
    "service_provider_telco": [
        "service provider", "sp ", "telco", "operator",
        "bell canada", "bell ", "att ", "at&t", "verizon", "vzw",
        "rakuten", "telstra", "telia", "swisscom", "mtn nigeria", "du uae",
        "softbank", "province of nb", "new brunswick",
        "naas", "sp naas", "network as a service",
        "mpls", "ldp", "rsvp", "bgp-lu", "vpn",
    ],
    "enterprise_customers": [
        "geico", "adobe", "honeywell", "visa", "texas instruments",
        "tx instruments", "equinix", "megaport", "twitch",
        "neo cloud", "neocloud",
    ],
    "innovation_patents": [
        "patent", "cpol", "bold bet", "innovation award", "stldp",
        "defensive publication", "invention", "whitepaper", "white paper",
        "blog post", "publication", "sp360", "segment-routing.net",
    ],
    "cisco_live_speaking": [
        "cisco live", "cleu", "clus", "clam", "cleur",
        "breakout session", "instructor led lab", "ilt",
        "keynote", "speaker", "speaking", "presentation",
        "ebc", "executive briefing", "vt ", "virtual tech",
        "mpls world congress", "mpls-wc", "ietf",
    ],
    "leadership_mentoring": [
        "mentor", "mentee", "pse committee", "pse review",
        "future enterprise", "tiger team", "swat team",
        "sevt", "tech elevate", "stay ready", "lightning talk",
        "enablement", "training", "boot camp", "bootcamp",
        "nacho", "christopher luciano", "dan stacks", "nico michel",
        "arkadiusz", "satoshi yamashita", "rob murphy",
    ],
    "global_international": [
        "apjc", "emea", "latam", "amer",
        "nigeria", "uae", "japan", "canada", "europe", "australia",
        "global", "international", "worldwide", "cross-theater",
    ],
    "revenue_business_impact": [
        r"\$\d",  # dollar amounts
        "million", "billion", r"\bm\b deal", "win", "closed",
        "revenue", "arr", "tkiv", "booking", "pipeline",
        "opportunity", "deal", "contract", "purchase order", "po ",
    ],
    "awards_recognition": [
        "award", "recognition", "pinnacle", "champion", "club cisco",
        "connected recognition", "pioneer award", "distinguished speaker",
        "congratulations", "well done", "kudos",
    ],
}

# Key people to track (internal collaborators, customers, leaders)
KEY_PEOPLE = [
    "john dorval", "brian meaney", "subha dhesikan", "ianik semko",
    "dan bhatt", "thomas graf", "vanessa", "tj ", "sanjay nanda",
    "james munroe", "dan wendlandt", "matt davy", "carlos pereira",
    "nacho", "dan stacks", "nico", "christopher luciano",
    "rakuten", "oracle", "bell", "microsoft", "geico", "adobe",
]


def normalize(text: str) -> str:
    return text.lower()


def find_keywords(text: str, terms: list) -> list:
    norm = normalize(text)
    found = []
    for term in terms:
        try:
            if re.search(term, norm):
                found.append(term)
        except re.error:
            if term.lower() in norm:
                found.append(term)
    return found


def truncate(text: str, max_chars: int = 400) -> str:
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:max_chars] + "…" if len(text) > max_chars else text


def parse_year(date_str: str) -> str:
    if not date_str:
        return "unknown"
    m = re.search(r'\b(20\d{2})\b', date_str)
    return m.group(1) if m else "unknown"


def analyze(csv_path: str) -> dict:
    summary = {
        "total_emails": 0,
        "date_range": {"earliest": None, "latest": None},
        "emails_by_year": Counter(),
        "top_senders": Counter(),
        "top_recipients": Counter(),
        "category_hits": defaultdict(int),
        "category_examples": defaultdict(list),  # up to 8 examples per category
        "key_people_mentions": Counter(),
        "revenue_signals": [],          # emails with dollar amounts / wins
        "global_engagements": [],       # emails with international signals
        "high_signal_subjects": [],     # subjects matching 3+ categories
    }

    MAX_EXAMPLES = 8  # per category
    MAX_REVENUE = 30
    MAX_GLOBAL = 20

    all_years = []

    with open(csv_path, newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            summary["total_emails"] += 1

            subject = row.get("subject", "") or ""
            from_   = row.get("from", "") or ""
            to_     = row.get("to", "") or ""
            date    = row.get("date", "") or ""
            body    = row.get("body", "") or ""

            year = parse_year(date)
            summary["emails_by_year"][year] += 1
            if year != "unknown":
                all_years.append(year)

            # Top senders (extract email address)
            from_emails = re.findall(r'[\w.+-]+@[\w.-]+', from_)
            for e in from_emails:
                summary["top_senders"][e] += 1

            # Top recipients
            to_emails = re.findall(r'[\w.+-]+@[\w.-]+', to_)
            for e in to_emails:
                summary["top_recipients"][e] += 1

            # Combined searchable text (subject + first 1000 chars of body)
            searchable = subject + " " + body[:1000]

            # Category matching
            matched_categories = []
            for cat, terms in TAXONOMY.items():
                hits = find_keywords(searchable, terms)
                if hits:
                    summary["category_hits"][cat] += 1
                    matched_categories.append(cat)
                    if len(summary["category_examples"][cat]) < MAX_EXAMPLES:
                        summary["category_examples"][cat].append({
                            "date": date,
                            "from": from_[:80],
                            "subject": subject[:120],
                            "snippet": truncate(body, 300),
                            "matched_terms": hits[:5],
                        })

            # Revenue signals
            if len(summary["revenue_signals"]) < MAX_REVENUE:
                rev_hits = find_keywords(searchable, TAXONOMY["revenue_business_impact"])
                if rev_hits and any(c in matched_categories for c in
                                    ["hyperscale_cloud_ai", "service_provider_telco",
                                     "enterprise_customers", "segment_routing_srv6"]):
                    summary["revenue_signals"].append({
                        "date": date,
                        "from": from_[:80],
                        "subject": subject[:120],
                        "snippet": truncate(body, 350),
                    })

            # Global engagement signals
            if len(summary["global_engagements"]) < MAX_GLOBAL:
                if "global_international" in matched_categories:
                    summary["global_engagements"].append({
                        "date": date,
                        "from": from_[:80],
                        "subject": subject[:120],
                        "snippet": truncate(body, 300),
                    })

            # Key people
            norm_search = normalize(searchable)
            for person in KEY_PEOPLE:
                if person.lower() in norm_search:
                    summary["key_people_mentions"][person] += 1

            # High signal subjects (3+ categories)
            if len(matched_categories) >= 3:
                summary["high_signal_subjects"].append({
                    "date": date,
                    "subject": subject[:120],
                    "categories": matched_categories,
                })

    # Finalize
    if all_years:
        summary["date_range"]["earliest"] = min(all_years)
        summary["date_range"]["latest"]   = max(all_years)

    summary["emails_by_year"]        = dict(sorted(summary["emails_by_year"].items()))
    summary["top_senders"]           = dict(summary["top_senders"].most_common(30))
    summary["top_recipients"]        = dict(summary["top_recipients"].most_common(20))
    summary["category_hits"]         = dict(sorted(summary["category_hits"].items(),
                                                    key=lambda x: -x[1]))
    summary["category_examples"]     = dict(summary["category_examples"])
    summary["key_people_mentions"]   = dict(summary["key_people_mentions"].most_common(30))

    # Keep only top 50 high-signal subjects (sorted by category count desc)
    summary["high_signal_subjects"] = sorted(
        summary["high_signal_subjects"],
        key=lambda x: -len(x["categories"])
    )[:50]

    return summary


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    csv_path = sys.argv[1]
    if not Path(csv_path).exists():
        print(f"ERROR: File not found: {csv_path}")
        sys.exit(1)

    out_path = sys.argv[2] if len(sys.argv) > 2 else str(Path(csv_path).with_suffix(".summary.json"))

    print(f"Analyzing {csv_path} …")
    summary = analyze(csv_path)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"\nDone. {summary['total_emails']:,} emails analyzed.")
    print(f"Date range: {summary['date_range']['earliest']} – {summary['date_range']['latest']}")
    print(f"\nTop categories by email count:")
    for cat, count in list(summary["category_hits"].items())[:8]:
        print(f"  {cat:40s} {count:>5,}")
    print(f"\nSummary written to: {out_path}")
    print(f"\nNext step: share {out_path} with Claude to generate the DSE impact .md")


if __name__ == "__main__":
    main()
