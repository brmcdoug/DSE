# DSE Package — TODO

## Aug 19, 2026 (evening) — Package-wide scaffolding migration

Removed the scope/criteria header blockquote, "Explicitly Excluded" tables, "Vault Harvest Log" blocks, and Open Items sections from **every remaining numbered file** (`01, 02, 03, 04, 07, 08, 09, 10`) — same treatment already applied to `05` and `06` earlier today. `AGENTS.md`'s "Section criteria" section already documents scope/routing for each file in more detail, so nothing is lost; `00-overview-themes.md` and `11-appendix.md` were left untouched (00 is brainstorm material with no such scaffolding; 11 was already clean). All items below are migrated from those files' Open Items blocks, consolidated with what already existed here.

**Cross-file accuracy fixes (same false claim, found in five places):** The `draft-srv6ops-addressing-guidelines` IETF editor credit — already removed from `05-industry-impact.md` in an earlier pass this session — was still live in **`01-exec-summary-draft.md`** (Quantified Highlights table's "Standards" row, and the Industry Impact Summary paragraph) and **`03-global-impact.md`** (2023–2025 transition-table row) and **`04-span-of-influence.md`** (SR brain trust field lead row). All four fixed to match `05`: Bruce is credited as editor/contributor on four *Segment Routing Part III: SRv6* book chapters (contributor acknowledgements, not cover author), with no standalone IETF draft-editor claim anywhere in the package now. **Recommend a final repo-wide text search for "draft-srv6ops" before submission**, in case it surfaces in a file not touched today (`00`, `08`, `11`, or the vault).

**O'Reilly course title** — corrected from the stale "Open Source Labbing" to the actual title, **Build Your Own Networking Lab**, in `09-personal-development.md` and `10-se-community-leadership.md` (already fixed in `05` earlier this session).

**Pinnacle Award duplicate detail** — the "~40-person team, almost entirely engineering, Bruce and Craig Hill the only two from sales" breakdown was stated in full in `01`, `03`, and originally `05`. Left the full version in the Executive Overview (Candidate Portrait and Quantified Highlights); trimmed `03`'s "Cisco's own attribution" note to a one-line pointer back to it. Innovation (`07`) still states it in full in its own flagship entry, which is its primary home per the routing table — that one's correctly placed, not a duplicate.

**One item deliberately left unresolved, flagged rather than silently changed:** `10-se-community-leadership.md` had an inline `//` comment on the EVPN Least Complexity tiger team row — good color about the challenge of surfacing an "obvious to engineers" problem to senior leadership — that would improve that entry but requires turning a table row into prose to use properly. Not applied; worth a look next time that section's open.

**02's "Package criteria / section description" block** (the official Direct Leader Recommendation guidance, quoted from the Nomination Kit) was removed the same way as the others — full text preserved in `AGENTS.md`'s Section 2 criteria if it's ever needed for reference.

---


Working checklist for the Bruce McDougall Distinguished Systems Engineer nomination package.
Section files (`0x-*.md`) are the source of truth for narrative; this file tracks **remaining work**.

**Legend:** `[verify]` = needs finance or external confirmation; `[Brook]` / `[Matt]` = manager action; `[external]` = outside repo.

---

## Full-package sweep — Aug 19, 2026

Every numbered section file (00–11) plus `AGENTS.md` and this file were reviewed in one pass to (a) strip Scope/Cross-ref headers, Open Items, Explicitly Excluded tables, and changelog footers out of the narrative files per the workflow note above, and (b) check the whole package for the same kind of error the false IETF editorship claim turned out to be. Findings:

- [x] **The false `draft-srv6ops-addressing-guidelines` editor credit appeared in four files, not one** — Industry Impact (caught and fixed first), and also the Executive Overview (twice: Quantified Highlights table and the Industry Impact Summary paragraph), Global Impact's transition table, and Span of Influence's "SR brain trust field lead" row. All four corrected to the accurate framing (contributor acknowledgements on three SRv6 book chapters, no standards-editorship claim).
- [x] **The O'Reilly course title was wrong in three more places** after being fixed in Industry Impact — Personal Development, Leadership, and the Executive Overview's Industry Impact Summary. All corrected to *Build Your Own Networking Lab*.
- [x] **A real cross-file contradiction, not just stale text:** Leadership's Executive Presence table stated the executive-coaching engagement as "Completed Mar 2026," while Personal Development (correctly, per your own review) says it's unconfirmed whether a formal external coach was engaged. Aligned both to the cautious version.
- [x] **"Phoenix Wing" label removed from two files**, not one — it was also sitting in Leadership's Explicitly Excluded table, not just Industry Impact's body text. Both now read as plain prose without the internal label.
- [x] **A duplicate CIPOL disclosures table in Innovation** — the same disclosure data appeared twice, once in a full table and again immediately after in a shorter, less complete version. Removed the redundant one.
- [x] **Two of your inline `//` suggestions in Leadership incorporated** rather than left as open questions: the EVPN tiger-team row now explains *why* surfacing an obvious problem to executives was the actual contribution, and the hackathon row now frames sales-org recruitment onto engineering hackathons as the rare thing it is.
- [ ] **New, not yet resolved:** the "filer" attribution comments in Innovation's patents table (`// filer: Bruce`, `// filer: Saswat / SDWAN Eng`, etc.) are written as `//` comments, which per the workflow convention get **stripped automatically before Word insertion** — meaning this attribution evidence currently never reaches the actual document. Decide whether to promote these into a visible "Filer" column in the table, or leave them as working notes only.
- [x] **`AGENTS.md` updated**: removed the stale "lead with the IETF draft editorship" instruction (the exact thing that turned out to be false); added Business Impact's official criteria quote plus the strategic-weight-ordering exception (Bruce decision: keep weight-ordering, update the rule rather than the file); added the workflow note establishing that section files carry narrative only.
- [x] **`00-overview-themes.md` reviewed but left untouched** — it's a working brainstorm/positioning doc, not one of the ten package sections (not in `AGENTS.md`'s page-budget table, never inserted into Word), so the scaffolding-cleanup convention doesn't apply to it. It does contain some stale figures (an old CPOL count, a wrong mentee name, an old acquisition-close date) that would be worth a cleanup pass on their own if useful, but that's a separate, lower-priority task.
- [x] **`11-appendix.md` required no changes** — no header, no scaffolding, no errors found; it was already narrative/data-only.

---

## Package completion (blocking)

- [ ] **Work through [criteria-audit.md](https://github.com/brmcdoug/DSE/blob/main/criteria-audit.md)** (Aug 18, 2026) — ten findings from the official template and Nomination Kit, now in `reference/`. Priority order at the end of that file. Highest value: the **force-multiplier framing** is the panel's own assessment structure and the package does not currently use it

- [x] **US patent numbers** added; patents table re-sorted most-recent-first; **GitHub stars captured** — jalapeno 78/15, srv6-labs 74/15, srv6-mrc-emulator 5. Now cited in Innovation and Industry Impact

- [ ] **Web segment revenue trajectory** — Bruce cites "a couple hundred million annually" in ~2015 growing to $10.9B booked 2022–2026. Get the early-period figure from finance so the before/after is quotable

- [ ] **Arkadiusz Kaliwoda** — confirm the MPLS World Congress demo year (2024 or 2025); he is now a Cilium SME, evangelist, and contributor in EMEA — strongest second-order enablement evidence, LoR candidate

- [ ] **Bruce to gather:** US **patent numbers** (we have Cisco asset IDs only) and **GitHub star/fork counts** — both explicitly named as evidence in Nomination Kit slide 22

- [ ] **Word package assembly** — `Bruce-McDougall-DSE-Package-Aug2026.docx` is the official deliverable. Insert with `scripts/md_to_docx.py`. **Done:** Business Impact, Appendix. **Remaining:** Global Impact, Span of Influence, Industry Impact, Innovation, Personal Development, SE Community Leadership, Sponsorship, Exec Overview

- [ ] **Workflow (Aug 2026):** **markdown is source of truth; Word is a build artifact.** Review and comment in the `.md` files using line-initial `//`; collect with `scripts/review_comments.py`; regenerate Word with `scripts/md_to_docx.py`. Word-side tools (`read_docx_review.py`, `edit_docx.py`) are for the last mile and external reviewers. **Convention as of this session: section files (`0x-*.md`) carry narrative only — no Open Items, no Explicitly Excluded routing tables, no changelog footers, and (new, Aug 19 evening) no scope/cross-ref header blockquote either.** `AGENTS.md`'s "Section criteria" already documents scope, length, and routing per section in more detail than the headers did, and `md_to_docx.py` already filtered the headers out at conversion — so removing them from source is pure deduplication, not a loss of information. `todo.md` is now the only place file-specific working decisions that deviate from or refine `AGENTS.md`'s official guidance get recorded (see the two new entries below). **Still to do:** apply the same header-removal to `00, 01, 03, 04, 07, 08, 09, 10, 11` — only `05` and `06` are cleaned as of this session, since those are the only two opened today. **Suggested addition to `AGENTS.md`'s Writing Conventions section**, to keep future Claude Code passes consistent: *"Section files carry narrative only — no scope/cross-ref header blockquote, no Open Items, no Explicitly Excluded table, no changelog footer. AGENTS.md and todo.md are the sole homes for that scaffolding."*
- [ ] **NEW — file-specific working decisions that deviate from AGENTS.md's official guidance** (previously stated only in now-removed section-file headers, now recorded here so they aren't lost): **Industry Impact's actual working length target is ~4 pages**, not the official 2–3pp — Bruce's explicit call to "split the difference" between the original ~5–6pp draft and the official target, rather than cut all the way down. **Business Impact's accounts are ordered by descending strategic/financial weight, not strict chronology** — an intentional deviation from the "chronological, most recent first" criterion, so the strongest evidence (Microsoft, Meta, Oracle) lands on the first page a reviewer reads.

- [ ] **Strip `[verify]` markers** before submission — they render in **red** in the Word doc so they are easy to find

- [ ] **Decide the evidence pointer convention** for the Word package — vault paths are filtered out on insert; Brenden used "Documents are accessible in the external SharePoint repository"

- [ ] **Finance-validated revenue** — replace `[verify]` placeholders in [06-business-impact.md](https://github.com/brmcdoug/DSE/blob/main/06-business-impact.md) and [03-global-impact.md](https://github.com/brmcdoug/DSE/blob/main/03-global-impact.md); reconcile Meta pipeline vs **$17M BBF booked**

- [ ] **Aggregate headline number** for exec summary (finance-approved ASP+Web total)

- [ ] **Direct Leader Recommendation(s)** — Brook Crossman (ASP/Web, ~5 yrs) and/or **Matt Gillies** (Global, from Jun 2026); edit [02-direct-leader-recommendation.md](https://github.com/brmcdoug/DSE/blob/main/02-direct-leader-recommendation.md). LoR typically same letter or co-authored w/ **John Dorval** / **Tim Carnes**

- [ ] **[Brook] 2HFY26 Talent Assessment** — manager section when cycle closes

- [ ] **Sponsorship** — [08-sponsorship.md](https://github.com/brmcdoug/DSE/blob/main/08-sponsorship.md) restructured Aug 2026 (package table + priority list + tracker). Blocking: **prioritize capped categories** (BE/Sales/Customer each have 2–3× the Kit target); **verify "Former Cisco" list** — several may still be at Cisco; **reconcile name spellings**; quantify global DSE headcount for the ">50%" claim; convert **James Munroe** volunteered testimonial → LoR

---

### Quote distribution — after Exec Overview

- [ ] **Distribute quotes from [12-quotes.md](https://github.com/brmcdoug/DSE/blob/main/12-quotes.md)** into sections. Table there lists each quote, source, date, and proposed placement, marking which are already placed. To do **after** the Executive Overview is drafted, since the strongest quotes may be wanted there
- [x] Brook Crossman's innovation-and-impact quote placed in the Executive Overview
- [ ] Two quotes recovered from the 2020 PSE package worth reusing: **Brian Shoda** on collaboration (corroborates the Leadership opening) and **David Lucey** of Salesforce on hyperscale credibility (external operator validation for Industry Impact)

## Validation & fact-check

### Revenue & accounts

- [ ] **MSFT WAN–SWAN** validation for SWAN / SL-API claims ([06-business-impact.md](https://github.com/brmcdoug/DSE/blob/main/06-business-impact.md))
- [ ] **Geico** ~$1.6M — finance validate
- [ ] **Verizon / AT&T / T-Mobile** pipeline $ where available
- [ ] **Global Impact $** — Adobe, Rakuten, Evroc, Fiserv, Applied Digital, Digital Realty
- [ ] **MSFT/OCI SRv6-for-AI** — document **FY2027 TAM** projection (competitor hardware deployments validate architecture; Cisco late to market)
- [ ] **Akamai** — follow up on SRv6 L3VPN controller POC status (redirect-to-scrubber demo)

### From Bruce's review pass (Aug 15, 2026)

- [ ] **Microsoft route-miles** — the "120,000 fiber miles" figure had no source and is now `[verify route-mile figure]`; Fairwater Phoenix–Milwaukee is ~2,000 miles. Supply the real number or leave it qualitative
- [ ] **Meta competitive framing** — "countered Arista's incumbency / credible second source in a multi-vendor deployment" needs account-team confirmation before it is final
- [ ] **WMP-PolarFly paper** — confirm publication path (internal review, external whitepaper, or conference submission); v0.7 dated Aug 2026
- [ ] **Christian Martin** — confirm he is comfortable being named, and confirm his Cisco MIG title
- [ ] **New account rows** — Apple (~$30M), Nvidia (~$30M), Netflix (~$30M) all `[verify]`; each needs a short-form entry in the body or should stay table-only
- [ ] **OCP 2026 session was declined** — removed from Business Impact; confirm nothing else in the package still implies it was delivered

### Personal Development — remaining (Aug 18, 2026)

- [ ] **Executive coaching claim corrected** — I had asserted Bruce "engaged an executive conversation coach and completed the program by March 2026." The source was a PDP action item recorded as *in progress*, not a completed engagement. Now states what is supported: Brook Crossman coached directly on upleveled messaging (2HFY25–1HFY26) and Bruce read *Conversational Intelligence* on Brook's recommendation. **Confirm whether a formal external coach was engaged, or whether Brook's coaching plus the Vaughn Suazo DSE mentorship satisfied the PDP item**
- [x] Council service removed from Personal Development — as an elected official Bruce sets policy, he does not operate the municipal network. Stays in Leadership
- [ ] **`12-quotes.md`** — new file with Brook Crossman's quote on innovation and impact. Decide placement (Exec Overview, Innovation, or Direct Leader Recommendation) and add remaining quotes

### Leadership — remaining (Aug 18, 2026)

- [x] Renamed **SE Community Leadership → Leadership**; cross-references updated in 5 files; AGENTS.md and README updated
- [x] Cisco Live table rebuilt from `projects/conferences.md` — attendance, scores, repeat-invitation pattern, and the two mentee outcomes (Nico Michel's Distinguished Speaker, Chris Lapp co-developed breakout)
- [x] Added **Technology Programme Leadership** (Cilium-SP, SONiC, Silicon One TAM, SOSIE, Cilium CRD) and **Executive Presence and Communication** — both named in the criteria and previously absent
- [x] **Community / Volunteer** — added: Anacortes City Council since Nov 2017, **Mayor Pro Tem** since Jan 2020, and the city built **the only community-owned FTTH ISP in Washington State** — affordable high-bandwidth service plus a non-tax revenue stream. Also recovered from the PSE package: advisory to **Rep. Rick Larsen's** and **Governor Inslee's** offices on municipal fibre
- [x] **Municipal fibre advisory** — confirmed one-time; wording corrected
- [ ] **SD-WAN hackathon win (Sep 2022)** — confirm the group/category name for accuracy
- [ ] **Municipal fibre advisory** — confirm whether the Larsen / Inslee advisory work continued post-2020 (PSE package cites it as of 2020)
- [ ] **FTTH details** — subscriber count, launch year, or revenue figure would strengthen the entry; confirm what is quotable in a Cisco document
- [ ] **GSX 2026** — confirm the IMI Design Workshop delivered and the ~200 attendee figure; confirm David Jansen presented the AI Scale-Across demo and the ~10,000 audience figure
- [ ] Section is now ~3,800 words but has **no official page limit** — no trim required

### Industry Impact — remaining (updated Aug 19, 2026)

- [x] **Standards vs. open-source framing resolved** — stated directly in-section, anchored on the MRC timeline: work began 2024, SRv6-for-AI discussed at OCP Nov 2024, first IETF draft Jul 2025 *in response to work already under way*. Standards trailed the open forums by ~8 months on the defining transport architecture of the AI era. **Update:** Bruce cut the "standards credentials" framing paragraph entirely — the section no longer makes a standards-leadership claim at all, just the publications/open-source/operator record
- [x] **False `draft-srv6ops-addressing-guidelines` editor credit removed** — Bruce is not named as author or contributor on the published draft (draft-horn-srv6ops-srv6addressing); confirmed directly against the IETF text
- [x] **NANOG 2020 entry removed** — pre-PSE, out of scope per the Aug 2020 date floor; was adding a near-empty table for one row
- [x] **Segment Routing Part III: SRv6 book credit corrected** — Bruce edited the SRv6 services/service-chaining chapters at the SR engineering team's invitation; he is credited in the book's **contributor acknowledgements**, not as a cover author. Confirmed: he is not one of the "& 2 more" unnamed cover credits
- [x] **SP360 post (May 2022) reframed** — it was Bruce's contribution to a Future of SP Networking blog series curated by Brook Crossman's PSE/DSE team, which became a repeat Cisco Live US/EU panel. Was previously presented as a solo post
- [x] **"Phoenix Wing" label removed from body text** — that was an internal task-tracking name for the Alibaba-attribution fact-check (see Done list, below), not a real entity; folded the actual caveat into plain prose
- [x] **srv6-labs metrics confirmed current** — Bruce confirmed 74 stars / 15 forks is up to date as of Aug 2026; `[refresh for 2026]` tag removed
- [x] **O'Reilly course corrected** — actual title is *Build Your Own Networking Lab* (was "Open Source Labbing"); working catalog link added
- [ ] **Confirm exact Future of SP Networking panel name and years** for the Cisco Live US/EU citation
- [ ] **OCP 2026 paper** — session declined; confirm publication venue once the underlying paper is finished
- [ ] **MPLS-WC 2023 session titles** — confirm Bell/Verizon/Rakuten attribution is quotable
- [ ] **Verizon Cilium-SRv6 POC (Nicklous Morris, Luay Jalil)** — planned, not yet delivered. Once it lands: add the outcome in Industry Impact's Operator Community entry, confirm the outcome vs. the existing Business Impact Verizon entry (same relationship, two facets — standards-adjacent origin in Industry Impact, commercial/technical thread in Business Impact), and check whether Luay Jalil (Verizon Fellow) also warrants a Span of Influence mention independent of the POC's commercial outcome
- [ ] **Reverse-chronological reorder** — template asks for most-recent-first; section is still thematic. Bruce decision: reorder, or keep thematic with dated entries (current approach)
- [ ] **Strategy-impact line per entry** — criterion asks for revenue and/or strategy; most entries now have one, a few still state reach without stating what it did for Cisco's position
- [x] **Section trimmed** — cut ~30% in the first editing pass (removed a redundant "External Artifacts" summary table, merged duplicate host-networking framing, cut a standalone era table); down from ~5–6pp toward the 2–3pp target. Second and third passes removed further scaffolding (Open Items, Explicitly Excluded table, changelog footer — all moved here) without adding length back
- [ ] Decide whether a compact "external artifacts" reference table belongs in the Appendix (cut from the body as the section's main earlier source of repetition)
- [ ] Optional timeline graphic for final PDF

### From Bruce's Innovation review (Aug 17, 2026)

- [x] **Pinnacle Award year** — resolved: **2025 award, ceremony early 2026**. Applied consistently across `01`, `03`, `07`
- [x] **6 patent grants confirmed** — Cisco Inventor Portfolio report (`projects/Inventor Portfolio Stats - US-2026-08-17...xlsx`); issued-patents table rebuilt with dates. Four of six issued during the PSE period; Bruce first-named inventor on *Underlay Network Traffic Steering* (Oct 2024)
- [ ] **SR-Apps / CNRS detail** — Bruce to supply CNRS scope and named collaborators, HS-PCE and ACP outcomes, and any SR-Apps features that shipped (entry drafted, marked)
- [ ] **Future Enterprise Segmentation tiger team records** — Bruce to dig up his participation detail; the SGT/uSID 16-bit insight originated there and now anchors the SRv6+SGT entry
- [ ] **SRv6 on Cisco SD-WAN** — listed as forthcoming in the Innovation summary; confirm the release vehicle and timing
- [ ] **SRv6 uSID on Nexus** — confirm shipping status

### Global Technology Adoption — data needed (new chapter, Aug 16 2026)

New Global Impact chapter drafted with attribution discipline: intervention → global adoption as context → who attests. **Every figure is `[pending]`.** To source:

- [ ] **Global SR / SRv6 run rate** — finance or SR product team (Clarence Filsfils' org)
- [ ] **Cisco 8000 global run rate**, and fixed-platform share of MIG revenue — MIG
- [ ] **SONiC global run rate and attach**; count of Cisco 8000 units shipping SONiC vs IOS-XR — SONiC product team
- [ ] **Cilium / Isovalent run rate since acquisition** — Isovalent / Security BE
- [ ] **NaaS-attributed pipeline** across the SP segment
- [ ] **Fixed vs. modular market data** — Dell'Oro / Omdia / 650 Group, SP routing and DC switching, by year back to ~2017 so the **crossover year** is visible. Cisco licenses these; ask MIG product or Competitive Intelligence rather than sourcing externally. **Use it to date the inflection against Bruce's 2017–2018 framing, not to claim revenue share**
- [ ] Confirm which product/engineering leaders will **attest in writing** (Filsfils, Wollenweber, Graf are already sponsorship candidates — an attestation sentence in their LoR is worth more than any figure)

### From Bruce's Global Impact review (Aug 16, 2026)

- [ ] **Fiserv** — single Jan 2026 TOI session, or continued into 2026? Entry can claim more if continued
- [ ] **Texas Instruments** — did revenue follow the workshop? (now a narrative entry; TI tried to recruit Bruce)
- [ ] **NYU / Carnegie Mellon** — any documented outcome (deployment, paper, alumni in operator roles)? Without one this stays two lines
- [ ] **Evroc** — revenue or committed pipeline; the one EMEA account that could carry a number
- [ ] **Adobe** — confirm no Nexus/cloud-native pull-through revenue beyond the ACV renewal noted in Business Impact; confirm re-engagement timeframe
- [ ] **Exec Overview:** Bruce's cross-Cisco relationship habit (senior SEs/PSEs/DSEs, any geography or vertical, sustained for learning and idea exchange) — now in Global Impact and Span of Influence; carry into the Executive Overview

### New accounts to capture — Apple, OpenAI, Anthropic, Google SRv6-for-AI

Bruce is running the same force-multiplier motion (equip the account team; they carry it to the customer) at **Google (SRv6 for AI)**, **Apple**, **OpenAI**, and **Anthropic**. Apple currently appears only as a revenue-table row; **OpenAI and Anthropic appear nowhere in the package**. Both are in the ASP+Web account list in AGENTS.md, and both are principals in the MRC specification this package builds on — engagements there materially strengthen Business Impact and Industry Impact.

To draft entries, need from Bruce:

- [ ] **Apple** — start date; what the Frontend DC / SONiC-on-8000 engagement covers; who on the account team he equips; status of the ~$30M `[verify]`
- [ ] **OpenAI** — start date; scope (MRC? SRv6? SONiC?); who he works through; any booked or pipeline revenue; is the engagement nameable in the package?
- [ ] **Anthropic** — same questions
- [ ] **Google SRv6-for-AI** — already a short bullet in the Google entry (Mar 2026 kickoff with Sischo, Camarillo, Filsfils); does the force-multiplier framing apply, and has it advanced?
- [ ] Confirm whether any of these are under NDA constraints that limit what the package can say

### From Bruce's second review pass (Aug 15, 2026)

- [ ] **Exec Overview — force multiplier framing:** a significant share of Business Impact revenue was earned without Bruce in the room. He equips account SEs and AMs with strategy, education, repositories, code, and labs, and they run it with their customers. **Meta ($17M backbone re-entry) is the proof — he never presented to Meta.** Now stated at the top of Business Impact and in Span of Influence; carry it into the Executive Overview
- [ ] **Exec Overview framing (Bruce's words):** five years ago SP and hyperscale operators largely dismissed SRv6 as not ready; today SPs almost universally name it their strategic direction, and most hyperscalers agree. Bruce has been at the centre of that conversation since day one — **use this as the opening move of the Executive Overview**
- [ ] **Digital Realty customer quote** — confirm wording with account team before it is quoted
- [ ] **Meta competitive framing** — "countered Arista's incumbency / credible second source" still needs account-team sign-off
- [ ] **T-Mobile** — verify which elements were adopted versus deferred
- [ ] **Viasat** — current status with account team
- [ ] **AT&T** — Bruce decision: retain as breadth evidence or cut (ran through 2025 without advancing)
- [ ] **Google** — ~$250M attributed scope (revised up from ~$20M) needs finance validation
- [ ] **Bell Canada** — Isovalent revenue, NCS5500/8000 SRv6-tied revenue
- [ ] **Dan Bernier** — confirm he is comfortable being named, and confirm the KubeCon 2022–2023 / MPLS-WC 2023 presentation dates
- [ ] **Groq** — confirm the "$10s of millions" opportunity figure is quotable

### Business Impact case studies (updated Aug 19, 2026)

- [ ] **Microsoft stakes opener** — confirm Azure scale / Fortune rank figures before final PDF
- [ ] **OCP Summit 2026** — session declined; confirm nothing in Business Impact still implies delivery (checked this session — clear)
- [ ] **Oracle public blog (2026)** — add URL citing SRv6 static routing for MRC (strong external validation)
- [ ] **FY2027 TAM recovery projection** — SRv6-for-AI, Microsoft + Oracle (finance)
- [ ] **Meta BBF / RBB** — validate ~$300M over two years and ~$350M/yr RBB pipeline
- [ ] **Salesforce $38M A9K/Juniper displacement (2022)** — confirm ASP+Web classification, or route to Global Impact
- [ ] **CoreWeave FY27–29 projections** — validate $150M/$245M FY27 and $400M/$600M FY28–29 with finance (largest unvalidated forward number in the section)
- [ ] **Bell Canada cumulative $** — finance validate; C8231-G2 500-unit order value
- [ ] **Akamai revenue** — no figure at all currently; confirm whether any is attributable
- [ ] **Akamai redirect-to-scrubber controller** — production status with account team (strongest host-networking customer proof point)
- [ ] **AWS Q1FY23 VP-level silicon recognition** — confirm and attach $
- [ ] **Verizon Project Yukon / service-chain $** — quantify
- [ ] **Digital Realty** — confirm ASP+Web vs Global Impact assignment (currently drafted in both)
- [ ] **NEW — Verizon Cilium-SRv6 POC** (Nicklous Morris, Luay Jalil) — planned, not yet delivered; added to the Verizon entry Aug 19, 2026. Update with outcome once scheduled/complete; confirm whether it produces its own revenue/pipeline line
- [ ] **NEW — Adobe ACV figure** — account SE reports the contract expanded from $750K to $1.6M ACV one year after the Cilium POC (Aug 2026). Added to the Adobe entry as the Financial Impact line, replacing "no booked revenue," but **needs confirmation**: is this figure accurate, and is it fairly attributable to the POC rather than broader account growth?

### Career, awards, IP

- [ ] **Patents / CPOLs** — **counts corrected upward:** tables yield **36 lifetime disclosures / 24 since Aug 2020 / 9 approved**, vs. "18 total" in prior notes. Still needed: issued-vs-pending split per filing, CPOL portal links, and confirmation that no filing is described as an issued patent ([07-innovation.md](https://github.com/brmcdoug/DSE/blob/main/07-innovation.md))
- [ ] **Policy Plane** — PM attribution; Carlos Pereira / OTel influence confirmation; publication ("need to publish" per MOC)
- [ ] **SONiC + Cisco Secure Workload** — productization status after Jan–Feb 2026 follow-ons
- [ ] **GitHub-first CL labs** — SGM stats on how many ILTs now use the model (quantifies the innovation)
- [x] **O'Reilly catalog link and exact course title** for *Build Your Own Networking Lab* — resolved Aug 19, 2026; link and correct title now in Industry Impact
- [x] Russ White course corrected **Pearson → O'Reilly** across `01`, `05`, `08`, `09`, `10`
- [ ] **Fold remaining `publications/readme.md` content** (blog exec summaries) into `05-industry-impact.md`, then archive it
- [ ] **Confirm ACM 10.1145/3603269.3604860** documents the SL-API/SDN forwarding technique before citing it as evidence in `06-business-impact.md`

### Customer / engagement gaps

- [ ] Softbank, Telstra, Swisscom, Telia, Iliad — confirm post-2020 outcomes or remove from lists
- [ ] **Adobe / Dan Stacks** — testimonial on Cilium EGW/LB impact
- [x] **Ignacio ("Nacho") Sanchez** — promoted to PSE (Jun 2026)

---

## Section content gaps

| Section                                                                                | Open work                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [03-global-impact.md](https://github.com/brmcdoug/DSE/blob/main/03-global-impact.md)                     | **Drafted Aug 2026.** Remaining: finance $ (Geico, Honeywell, Adobe, Fiserv, Evroc); Adobe/Dan Stacks testimonial; MTN/DU figures via Sanjay Nanda; Province of NB quote or LoR; **page-budget decision — section runs 4–5pp vs. 7pp README target** |
| [04-span-of-influence.md](https://github.com/brmcdoug/DSE/blob/main/04-span-of-influence.md)             | **Drafted Aug 2026.** Remaining: SD-WAN/SSE PM quotes; Policy Plane / Carlos Pereira OTel; Will Etherton report; confirm **$500M Edgecore leakage** figure is quotable; confirm VP citations (Knipp, Dorval, Morrissey) attributable by name; **consider Luay Jalil (Verizon Fellow) as an additional external-relationship entry once the Cilium-SRv6 POC outcome is known** |
| [05-industry-impact.md](https://github.com/brmcdoug/DSE/blob/main/05-industry-impact.md)                 | **Two editing passes complete (Aug 19, 2026).** Section is now narrative-only — Open Items, Explicitly Excluded table, and changelog moved here. Remaining: confirm Future of SP Networking panel name/years; OCP 2026 paper publication venue; MPLS-WC 2023 session titles; Verizon POC outcome; reverse-chronological reorder decision; per-entry strategy lines for remaining entries |
| [06-business-impact.md](https://github.com/brmcdoug/DSE/blob/main/06-business-impact.md)                 | **Editing pass complete (Aug 19, 2026).** Revenue placeholders; FY2027 TAM; Verizon POC and Adobe ACV figure both need confirmation (see above); Fiserv single-session-vs-continued question open; consider consolidating this file's own "Vault Harvest Log" section here in a future pass, same as Industry Impact |
| [07-innovation.md](https://github.com/brmcdoug/DSE/blob/main/07-innovation.md)                           | CPOL links; Policy Plane publication                                                                                                                                                                     |
| [09-personal-development.md](https://github.com/brmcdoug/DSE/blob/main/09-personal-development.md)       | OCP 2026; Akamai follow-up                                                                                                                                                                               |
| [10-se-community-leadership.md](https://github.com/brmcdoug/DSE/blob/main/10-se-community-leadership.md) | **Drafted Aug 2026** (leads with **6 PSE promotions**). Remaining: Tech Elevate session list/scores/counts; **GitHub-first CL lab adoption count from SGM**; DCN Champions bootcamp metrics; IMI VT scores (Alex Lanin); P5G SDWAN & SL-OnDemand outcomes; **Kaliwoda quote or LoR** |
| **PSE-time-log.csv**                                                                   | Full-fidelity 2024+ rows + Notes; May–Jun 2026 entries added                                                                                                                                             |

---

## Personal development plan — remaining

- [ ] Non–Cisco Live session / **OCP 2026** prep and delivery
- [ ] Optimize Jalapeno codebase (Jul 2026 target)
- [ ] SRv6 hyperscaler deployment — Cisco revenue catch-up vs validated architecture (Jul 2026)

---

## Optional / polish

- [ ] Innovation **timeline graphic** for final PDF
- [ ] Industry Impact **timeline graphic** for final PDF (added Aug 19, 2026)
- [ ] **Appendix overflow** — track in [11-appendix.md](https://github.com/brmcdoug/DSE/blob/main/11-appendix.md) (CLEU history, Lightning Talks program, etc.)
- [ ] Remove or archive duplicate scratch content in vault MOCs once package is frozen

---

## Done

- [x] **Voice calibration pass** (Aug 2026) — [voice-guide.md](https://github.com/brmcdoug/DSE/blob/main/voice-guide.md) created from Brenden PDF + `about-me/`; AGENTS.md writing conventions, page budget, section order, and canonical exec file reconciled; README links fixed
- [x] **Business Impact — full section drafted** (Aug 2026): 9 flagship case studies + 16 short-form entries, impact-ordered, summary table rebuilt
- [x] **Innovation — full section drafted** (Aug 2026): 8 flagship innovations on Customer Problem / Solution / Business Impact template + IP narrative
- [x] **Span of Influence — full section drafted** (Aug 2026): 5 themes, before/after expansion table, signature-themes close with outcomes attached
- [x] **Industry Impact — full section drafted** (Aug 2026): MRC authorship boundary stated explicitly; IETF draft-editor role and SONiC "industry first" elevated
- [x] **Global Impact — full section drafted** (Aug 2026): restructured by expansion pattern; "field multiplier" chapter added for impact without customer contact
- [x] **SE Community Leadership — full section drafted** (Aug 2026): leads with **6 PSE promotions**; Kaliwoda second-order multiplier promoted to full narrative; "Programs Bruce Built" chapter added
- [x] **All six body sections drafted** — ~22,200 words / ~34 pages
- [x] **Personal Development drafted** (Aug 2026) — compressed to ~1.5pp; **development areas named directly with actions taken** (exec communication; filtering/delegation)
- [x] **Sponsorship restructured** (Aug 2026) — package table, priority-letter recommendations tied to specific claims, solicitation tracker by category
- [ ] **Executive Overview rewrite** — [01-exec-summary-draft.md](https://github.com/brmcdoug/DSE/blob/main/01-exec-summary-draft.md) against finished bodies (**draft last**)
- [ ] **Direct Leader Recommendation** — [02-direct-leader-recommendation.md](https://github.com/brmcdoug/DSE/blob/main/02-direct-leader-recommendation.md); draft the brief Brook/Matt work from
- [x] **Digital Realty assignment resolved** → Business Impact (removed from Global Impact and exec summary)
- [x] Align exec summary with [AGENTS.md](https://github.com/brmcdoug/DSE/blob/main/AGENTS.md) segment rules
- [x] Harvest body sections 03–07, 09–10
- [x] Integrate Talent Assessments 1HFY24–1HFY26 (Brook comments)
- [x] Draft Direct Leader Summary; document Brook + Matt LoR path
- [x] Incorporate timeline from **Your notes** (Jun 2026)
- [x] Career path dates; **Jun 2026 transfer to Global / Matt Gillies**
- [x] **Pinnacle Award 2025**
- [x] **Cilium-SP business case** ($34M / $323M) validated
- [x] **ASP+Web account classification** (Akamai, Equinix, Salesforce, Lambda, etc.)
- [x] **Visa** → Global Impact
- [x] **Province of NB / James Munroe** → Global Impact (CLEU 2026)
- [x] **O'Reilly** *Build Your Own Networking Lab* → 4-hour Russ White lab course (not a book; corrected from "Pearson" Aug 2026; title corrected from "Open Source Labbing" Aug 19, 2026)
- [x] **Education:** BA, University of Washington (1996)
- [x] **"Phoenix Wing" scope clarified** (Alibaba-led; Bruce = Cisco SRv6/SONiC engineering partner) — internal task label; **Aug 19, 2026: removed the label itself from Industry Impact's body text, kept the underlying caveat in plain prose**
- [x] PDP: exec coach, Conversational Intelligence, SRF sessions, MRC (replaces Ultra Ethernet), Adobe Cilium POC, **Nacho promoted to PSE (Jun 2026)**
- [x] DLR Cilium/SRv6 POC + Akamai controller demo (Jalapeno item reframed)
- [x] **Virginia Teixeira** spelling confirmed
- [x] **PSE time log third pass** — full 2024+ Notes integrated into CSV + section narratives (Jun 7 2026)
- [x] **Span of Influence** — thematic restructure (5 chapters, Jun 2026)
- [x] **Industry Impact** — thematic restructure (5 chapters, Jun 2026)
- [x] **Patent wording** — "patent application" → "patent" in exec + innovation CPOL table
- [x] **Aug 19, 2026 — Industry Impact false claim removed:** `draft-srv6ops-addressing-guidelines` editor credit was not accurate (Bruce is not named on the published draft); removed and the section's standards-credentials framing removed with it
- [x] **Aug 19, 2026 — Industry Impact and Business Impact cleanup pass:** book credit corrected to contributor acknowledgements, SP360 post reframed as part of the Future of SP Networking series, srv6-labs metrics confirmed current, O'Reilly course corrected, Verizon Cilium-SRv6 POC added to both files accurately (planned, not delivered), Adobe ACV figure added to Business Impact pending confirmation, all section-file scaffolding (Open Items, Explicitly Excluded, changelogs) consolidated into this file

---

## Reference — incorporated timeline

Full mapping of Bruce's chronological notes → section files is archived in git history (`todo.md`, Jun 7 2026). Primary narratives live in `0x-*.md` files.
