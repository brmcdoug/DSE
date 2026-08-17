# DSE Package — TODO

Working checklist for the Bruce McDougall Distinguished Systems Engineer nomination package.  
Section files (`0x-*.md`) are the source of truth for narrative; this file tracks **remaining work**.

**Legend:** `[verify]` = needs finance or external confirmation; `[Brook]` / `[Matt]` = manager action; `[external]` = outside repo.

---

## Package completion (blocking)

- [ ] **Word package assembly** — `Bruce-McDougall-DSE-Package-Aug2026.docx` is the official deliverable. Insert with `scripts/md_to_docx.py`. **Done:** Business Impact, Appendix. **Remaining:** Global Impact, Span of Influence, Industry Impact, Innovation, Personal Development, SE Community Leadership, Sponsorship, Exec Overview
- [ ] **Workflow (Aug 2026):** **markdown is source of truth; Word is a build artifact.** Review and comment in the `.md` files using line-initial `//`; collect with `scripts/review_comments.py`; regenerate Word with `scripts/md_to_docx.py`. Word-side tools (`read_docx_review.py`, `edit_docx.py`) are for the last mile and external reviewers
- [ ] **Strip `[verify]` markers** before submission — they render in **red** in the Word doc so they are easy to find
- [ ] **Decide the evidence pointer convention** for the Word package — vault paths are filtered out on insert; Brenden used "Documents are accessible in the external SharePoint repository"
- [ ] **Finance-validated revenue** — replace `[verify]` placeholders in [06-business-impact.md](./06-business-impact.md) and [03-global-impact.md](./03-global-impact.md); reconcile Meta pipeline vs **$17M BBF booked**
- [ ] **Aggregate headline number** for exec summary (finance-approved ASP+Web total)
- [ ] **Direct Leader Recommendation(s)** — Brook Crossman (ASP/Web, ~5 yrs) and/or **Matt Gillies** (Global, from Jun 2026); edit [02-direct-leader-recommendation.md](./02-direct-leader-recommendation.md). LoR typically same letter or co-authored w/ **John Dorval** / **Tim Carnes**
- [ ] **[Brook] 2HFY26 Talent Assessment** — manager section when cycle closes
- [ ] **Sponsorship** — [08-sponsorship.md](./08-sponsorship.md) restructured Aug 2026 (package table + priority list + tracker). Blocking: **prioritize capped categories** (BE/Sales/Customer each have 2–3× the Kit target); **verify "Former Cisco" list** — several may still be at Cisco; **reconcile name spellings**; quantify global DSE headcount for the ">50%" claim; convert **James Munroe** volunteered testimonial → LoR

---

## Validation & fact-check

### Revenue & accounts
- [ ] **MSFT WAN–SWAN** validation for SWAN / SL-API claims ([06-business-impact.md](./06-business-impact.md))
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

### Global Technology Adoption — data needed (new chapter, Aug 16 2026)
New Global Impact chapter drafted with attribution discipline: intervention → global adoption as context → who attests. **Every figure is `[pending]`.** To source:
- [ ] **Global SR / SRv6 run rate** — finance or SR product team (Clarence Filsfils' org)
- [ ] **Cisco 8000 global run rate**, and fixed-platform share of MIG revenue — MIG
- [ ] **SONiC global run rate and attach**; count of Cisco 8000 units shipping SONiC vs IOS-XR — SONiC product team
- [ ] **Cilium / Isovalent run rate since acquisition** — Isovalent / Security BE
- [ ] **NaaS-attributed pipeline** across the SP segment
- [ ] Confirm which product/engineering leaders will **attest in writing** (Filsfils, Wollenweber, Graf are already sponsorship candidates — an attestation sentence in their LoR is worth more than any figure)

### From Bruce's Global Impact review (Aug 16, 2026)
- [ ] **Fiserv** — single Jan 2026 TOI session, or continued into 2026? Entry can claim more if continued
- [ ] **Texas Instruments** — did revenue follow the workshop? (now a narrative entry; TI tried to recruit Bruce)
- [ ] **NYU / Carnegie Mellon** — any documented outcome (deployment, paper, alumni in operator roles)? Without one this stays two lines
- [ ] **Evroc** — revenue or committed pipeline; the one EMEA account that could carry a number
- [ ] **Adobe** — confirm no Nexus/cloud-native pull-through revenue; confirm re-engagement timeframe
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

### Business Impact case studies (new — Aug 2026 drafting pass)
- [ ] **Microsoft stakes opener** — confirm Azure scale / Fortune rank figures before final PDF
- [ ] **OCP Summit 2026** — confirm SRv6 multi-tenant AI fabric co-presentation was delivered
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

### Career, awards, IP
- [ ] **Patents / CPOLs** — **counts corrected upward:** tables yield **36 lifetime disclosures / 24 since Aug 2020 / 9 approved**, vs. "18 total" in prior notes. Still needed: issued-vs-pending split per filing, CPOL portal links, and confirmation that no filing is described as an issued patent ([07-innovation.md](./07-innovation.md))
- [ ] **Policy Plane** — PM attribution; Carlos Pereira / OTel influence confirmation; publication ("need to publish" per MOC)
- [ ] **SONiC + Cisco Secure Workload** — productization status after Jan–Feb 2026 follow-ons
- [ ] **GitHub-first CL labs** — SGM stats on how many ILTs now use the model (quantifies the innovation)
- [ ] **O'Reilly catalog link and exact course title** for *Open Source Labbing* — repo link now cited: [github.com/brmcdoug/open-source-labbing](https://github.com/brmcdoug/open-source-labbing)
- [x] Russ White course corrected **Pearson → O'Reilly** across `01`, `05`, `08`, `09`, `10`
- [ ] **Fold remaining `publications/readme.md` content** (blog exec summaries) into `05-industry-impact.md`, then archive it
- [ ] **Confirm ACM 10.1145/3603269.3604860** documents the SL-API/SDN forwarding technique before citing it as evidence in `06-business-impact.md`

### Customer / engagement gaps
- [ ] Softbank, Telstra, Swisscom, Telia, Iliad — confirm post-2020 outcomes or remove from lists
- [ ] **Adobe / Dan Stacks** — testimonial on Cilium EGW/LB impact
- [x] **Ignacio (“Nacho”) Sanchez** — promoted to PSE (Jun 2026)

---

## Section content gaps

| Section | Open work |
| :--- | :--- |
| [03-global-impact.md](./03-global-impact.md) | **Drafted Aug 2026.** Remaining: finance $ (Geico, Honeywell, Adobe, Fiserv, Evroc); Adobe/Dan Stacks testimonial; MTN/DU figures via Sanjay Nanda; Province of NB quote or LoR; **page-budget decision — section runs 4–5pp vs. 7pp README target** |
| [04-span-of-influence.md](./04-span-of-influence.md) | **Drafted Aug 2026.** Remaining: SD-WAN/SSE PM quotes; Policy Plane / Carlos Pereira OTel; Will Etherton report; confirm **$500M Edgecore leakage** figure is quotable; confirm VP citations (Knipp, Dorval, Morrissey) attributable by name |
| [05-industry-impact.md](./05-industry-impact.md) | **Drafted Aug 2026** (page target corrected 5–6 → 3 per README). Remaining: refresh srv6-labs metrics; OCP URLs/dates + confirm 2026 session delivered; MPLS-WC 2023 session titles (confirm Bell/Verizon/Rakuten attribution quotable); O'Reilly catalog link; **confirm `draft-srv6ops-addressing-guidelines` status and co-editors** |
| [06-business-impact.md](./06-business-impact.md) | Revenue placeholders; FY2027 TAM |
| [07-innovation.md](./07-innovation.md) | CPOL links; Policy Plane publication |
| [09-personal-development.md](./09-personal-development.md) | OCP 2026; Akamai follow-up |
| [10-se-community-leadership.md](./10-se-community-leadership.md) | **Drafted Aug 2026** (leads with **6 PSE promotions**). Remaining: Tech Elevate session list/scores/counts; **GitHub-first CL lab adoption count from SGM**; DCN Champions bootcamp metrics; IMI VT scores (Alex Lanin); P5G SDWAN & SL-OnDemand outcomes; **Kaliwoda quote or LoR** |
| **PSE-time-log.csv** | Full-fidelity 2024+ rows + Notes; May–Jun 2026 entries added |

---

## Personal development plan — remaining

- [ ] Non–Cisco Live session / **OCP 2026** prep and delivery
- [ ] Optimize Jalapeno codebase (Jul 2026 target)
- [ ] SRv6 hyperscaler deployment — Cisco revenue catch-up vs validated architecture (Jul 2026)

---

## Optional / polish

- [ ] Innovation **timeline graphic** for final PDF
- [ ] **Appendix overflow** — track in [11-appendix.md](./11-appendix.md) (CLEU history, Lightning Talks program, etc.)
- [ ] Remove or archive duplicate scratch content in vault MOCs once package is frozen

---

## Done

- [x] **Voice calibration pass** (Aug 2026) — [voice-guide.md](./voice-guide.md) created from Brenden PDF + `about-me/`; AGENTS.md writing conventions, page budget, section order, and canonical exec file reconciled; README links fixed
- [x] **Business Impact — full section drafted** (Aug 2026): 9 flagship case studies + 16 short-form entries, impact-ordered, summary table rebuilt
- [x] **Innovation — full section drafted** (Aug 2026): 8 flagship innovations on Customer Problem / Solution / Business Impact template + IP narrative
- [x] **Span of Influence — full section drafted** (Aug 2026): 5 themes, before/after expansion table, signature-themes close with outcomes attached
- [x] **Industry Impact — full section drafted** (Aug 2026): MRC authorship boundary stated explicitly; IETF draft-editor role and SONiC "industry first" elevated
- [x] **Global Impact — full section drafted** (Aug 2026): restructured by expansion pattern; "field multiplier" chapter added for impact without customer contact
- [x] **SE Community Leadership — full section drafted** (Aug 2026): leads with **6 PSE promotions**; Kaliwoda second-order multiplier promoted to full narrative; "Programs Bruce Built" chapter added
- [x] **All six body sections drafted** — ~22,200 words / ~34 pages
- [x] **Personal Development drafted** (Aug 2026) — compressed to ~1.5pp; **development areas named directly with actions taken** (exec communication; filtering/delegation)
- [x] **Sponsorship restructured** (Aug 2026) — package table, priority-letter recommendations tied to specific claims, solicitation tracker by category
- [ ] **Executive Overview rewrite** — [01-exec-summary-draft.md](./01-exec-summary-draft.md) against finished bodies (**draft last**)
- [ ] **Direct Leader Recommendation** — [02-direct-leader-recommendation.md](./02-direct-leader-recommendation.md); draft the brief Brook/Matt work from
- [x] **Digital Realty assignment resolved** → Business Impact (removed from Global Impact and exec summary)
- [x] Align exec summary with [AGENTS.md](./AGENTS.md) segment rules
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
- [x] **O'Reilly** *Open Source Labbing* → 4-hour Russ White lab course (not a book; corrected from "Pearson" Aug 2026)
- [x] **Education:** BA, University of Washington (1996)
- [x] **Phoenix Wing** scope clarified (Alibaba-led; Bruce = Cisco SRv6/SONiC engineering partner)
- [x] PDP: exec coach, Conversational Intelligence, SRF sessions, MRC (replaces Ultra Ethernet), Adobe Cilium POC, **Nacho promoted to PSE (Jun 2026)**
- [x] DLR Cilium/SRv6 POC + Akamai controller demo (Jalapeno item reframed)
- [x] **Virginia Teixeira** spelling confirmed
- [x] **PSE time log third pass** — full 2024+ Notes integrated into CSV + section narratives (Jun 7 2026)
- [x] **Span of Influence** — thematic restructure (5 chapters, Jun 2026)
- [x] **Industry Impact** — thematic restructure (5 chapters, Jun 2026)
- [x] **Patent wording** — “patent application” → “patent” in exec + innovation CPOL table

---

## Reference — incorporated timeline

Full mapping of Bruce’s chronological notes → section files is archived in git history (`todo.md`, Jun 7 2026). Primary narratives live in `0x-*.md` files.
