# OLM converter

Small Python utilities to turn **Outlook for Mac (`.olm`)** archives into tabular data, then summarize **email content against DSE promotion categories** for reporting or LLM-assisted narrative drafts.

**Requirements:** Python 3.9+ (stdlib only — no `pip install`).

## `olm_to_csv.py`

An `.olm` file is a ZIP bundle of XML message files. This script walks every `*.xml` entry, parses Outlook’s `<email>` elements (namespace-tolerant), and writes one CSV row per message.

**Columns:** `date`, `from`, `to`, `cc`, `bcc`, `subject`, `has_attachments`, `body`, `source_path`

- **Body** is taken from `OPFMessageCopyPreview` (plain-text preview), not full HTML body — keeps CSV size manageable.
- **Source path** is the path inside the archive (useful for debugging odd messages).

```bash
python olm_to_csv.py archive.olm                 # writes archive.csv
python olm_to_csv.py archive.olm out/emails.csv
python olm_to_csv.py archive.olm --inspect       # print first XML file (debug)
```

## `analyze_emails.py`

Reads a CSV produced by `olm_to_csv.py`, scans **subject + first 1000 characters of body** against a fixed keyword taxonomy (`TAXONOMY` in the script), and emits a **compact JSON summary**: counts by year, top senders/recipients, per-category hit counts with example snippets, optional “revenue” and “global” email lists, key-person mentions, and subjects that match many categories at once.

```bash
python analyze_emails.py emails.csv                    # writes emails.summary.json
python analyze_emails.py emails.csv analysis/out.json
```

The JSON is sized so it can be pasted into or uploaded for an LLM to generate markdown summaries (as noted in the script’s help text).

## Typical workflow

1. Export or locate your `.olm` from Outlook for Mac.
2. Run `olm_to_csv.py` → CSV.
3. Run `analyze_emails.py` on that CSV → JSON summary.
4. Use the JSON (or CSV) in downstream reporting or narrative generation.

## Customization

- **Categories and keywords** live in `analyze_emails.py` (`TAXONOMY`, `KEY_PEOPLE`). Edit there to match your org or campaign.
- **Other Outlook versions** may differ; this code targets the Mac OLM XML shape described in `olm_to_csv.py`.

## Limitations

- Only **Outlook for Mac–style OLM** XML is tested; other exporters may differ.
- Message bodies are **preview text**, not full thread/HTML content.
- Empty or non-message XML inside the archive is skipped silently (with a count at the end of conversion).
