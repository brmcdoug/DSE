# xarchive — superseded material

Archived **August 14, 2026**, after all six DSE package body sections were drafted.

Nothing here is referenced by the active package. Agents: **do not draft from these files** — see [../AGENTS.md](../AGENTS.md) for the current repo file map and [../voice-guide.md](../voice-guide.md) for drafting rules.

| Item | Was | Superseded by | Notes |
| :--- | :--- | :--- | :--- |
| `email-analysis/` | 16 files of Apr 2026 email mining — CSVs, JSON summaries, per-topic markdown | Content synthesized into `03`–`07`, `10` | Largest artifact of the data-gathering phase |
| `olm-converter/` | Python tooling that produced `email-analysis/` (`olm_to_csv.py`, `analyze_emails.py`) | — | Re-runnable if the mailbox is re-mined |
| `00-outline.md` | Section-by-section content plan | All six body sections now drafted; page budget and section order live in `AGENTS.md` | Its section order for 8–10 conflicted with README; README order governs |
| `01-exec-summary.md` | Working notes for the executive section | `01-exec-summary-draft.md` | See extraction note below |
| `prompts.md` | The prompt that generated the Brenden package analysis | `reference/brenden-dse-package-template-outline.md` | |
| `notebooklm/` | NotebookLM mind-map PNG from the planning phase | The drafted package | |
| `speaking-engagements/` | `readme.md` containing only "coming soon" | `05-industry-impact.md`, `10-se-community-leadership.md` | Never populated |

---

## Extracted before archiving

Two items were pulled out of `01-exec-summary.md` into the active package rather than archived with it:

1. **ACM paper citation** — [10.1145/3603269.3604860](https://dl.acm.org/doi/pdf/10.1145/3603269.3604860), documenting the Microsoft SWAN architecture and supporting the SL-API claim. Added to the Microsoft and Meta evidence lines in `06-business-impact.md`. *Still to confirm the paper documents the specific SL-API/SDN forwarding technique.*
2. **SL-API adoption sequence** — Meta was the **second** customer after Microsoft to adopt the technique; Google (Alphanet) is the third. Added as a note under the Meta case study.

---

## Still live — not archived

`publications/readme.md` looks like a stub but holds executive summaries of three key publications plus `github.com/brmcdoug/open-source-labbing`, a URL that appears nowhere else. It also records the Russ White course as **O'Reilly** training, while `todo.md` and three drafted sections call it **Pearson**. Resolve that discrepancy and fold the content into `05-industry-impact.md` and `09-personal-development.md` before archiving it.
