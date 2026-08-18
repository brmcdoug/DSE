# AGENTS.md — DSE Package (Bruce McDougall)

Instructions for AI agents (and humans) working on this repository. Read this file before drafting or harvesting content for any section.

---

## Purpose

This repo is the **publication layer** for a ~50-page Distinguished Systems Engineer (DSE) nomination package. Raw evidence lives in the Obsidian vault at `../../../go/notes/`. This repo holds polished, third-person, verifiable package text.

**Obsidian vault:** `/Users/brucemcdougall/go/notes/` (see that vault’s `AGENTS.md` for wikilink/MOC conventions)

**OFFICIAL SOURCES — cite these, do not paraphrase from memory:**
- `reference/Template for DSE candidacy Jan2025.docx` — section order, suggested lengths, formatting rules
- `reference/PSE DSE Nomination Kit FY26.pptx` — criteria on **slide 15** (LoR requirements), **slides 21–22** (PSE criteria), **slides 24–25** (DSE criteria)
- **Audit of package vs. these sources:** [criteria-audit.md](./criteria-audit.md) (Aug 2026)

**Role name:** the official title is **Solutions** Engineer (PSE / DSE), not *Systems* Engineer. `[package-wide correction pending]`

**Section 10 is named "Leadership"**, not "SE Community Leadership" (template change note, 01092025).

**Formatting (official):** ≤50 pages including cover, **excluding index and appendix**; **CiscoSansTT**; **no smaller than 10 pt**; single spaced; working hyperlinks.

**The DSE general guideline — the panel's own framing device (Nomination Kit slide 25, first row):**
> *"Demonstrate how you have been a **force multiplier** throughout the organization (covering multiple criteria aspects). For example: identification of new technology and industry trends, building the necessary field enablement, aligning strategic stakeholders (engineering and sales exec.) and investment, leading lighthouse customers and driving field adoption."*

This sits **above** Global Impact, Span of Influence, and Industry Impact in the criteria table. Use its four examples as the structure of the Executive Overview.

**Industry Impact (slide 25):** *"Influencing and leading not just internally within Cisco, but also externally. **Participate and/or lead standards bodies and represent Cisco within such.**"* Standards work is a named criterion — lead with the IETF draft editorship.

**Innovation evidence types the criteria name explicitly (slide 22):** *patent # granted, GitHub stars, sales data, event registration/attendees and speaker score, adoption, endorsement from sponsor and community.*

**Gold-standard reference:** `reference/Brenden Buresh Distinguished Architect Final 040122.pdf`  
**Template analysis (structure):** `reference/brenden-dse-package-template-outline.md`  
**Voice & claim strength (prose):** `voice-guide.md` — **read before drafting**

**Candidate background:** `about-me/` — 2020 PSE nomination package (writing sample), StandOut assessment, speaker bio, writing-style notes.

---

## Candidate context

| Field | Value |
| :--- | :--- |
| **Name** | Bruce McDougall |
| **Current role** | Principal Systems Engineer (PSE) |
| **Target** | Distinguished Systems Engineer (DSE) |
| **Manager (DSE period)** | Brook Crossman (ASP/Web VP, Systems Engineering, ~5 years through Jun 2026); **Matt Gillies** (Global team, from Jun 2026) |
| **Assignment** | **Americas Service Provider and Web (ASP + Web)** through Jun 2026; **Global** PSE from Jun 2026 |
| **DSE mentor** | Vaughn Suazo |
| **PSE start date (package time scope)** | **August 1, 2020** |
| **Voice** | Third person throughout the package, except **“Becoming a DSE”** candidate statement (first person allowed) |
| **Evidence standard** | SMART claims; factual, verifiable; chronology most-recent-first |

---

## Time scope (critical)

The DSE package documents work and impact **since becoming PSE** — from **August 1, 2020** onward.

| Rule | Guidance |
| :--- | :--- |
| **Default** | Include only activities, outcomes, and evidence **on or after 2020-08-01** |
| **Executive Overview exception** | Pre-2020 references are OK in **high-level “thru-narrative”** only (career arc, origin of host-networking/SRv6 vision, patents rooted earlier). Keep to a few sentences—not full case studies |
| **All other sections** | **No pre-2020 body content.** If a patent was filed earlier but *impact* landed after PSE promotion, document the post-2020 impact |
| **Career path table** | May show roles before 2020 for context; narrative focus stays on PSE→DSE journey |

**Agent rule:** When harvesting Obsidian, check dates. Archive notes (`xarchive-2021-2022/`, etc.) may describe pre-2020 origins—extract only post-2020 impact unless writing exec overview thru-line.

---

## How the criteria relate

```text
                    ┌─────────────────────────────────────┐
                    │     Executive Overview (all)        │
                    └─────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        ▼                             ▼                             ▼
  CUSTOMER / REVENUE              INTERNAL CISCO              EXTERNAL INDUSTRY
        │                             │                             │
   ┌────┴────┐                   Span of Influence              Industry Impact
   │         │                   (higher altitude,             (may have no direct $)
Business   Global                   ≥2 domains, H2-3)                │
Impact     Impact                      │                             │
(all named  (global reach:             ▼                             │
 accounts)  initiatives,          Innovation ◄── often led by Span
            architectures,
            training)
        │         │               (IPR, product/strategy)            │
        └────┬────┘                      │                             │
             │    cross-reference when Span / Innovation /           │
             │    SE Leadership contributed to revenue                 │
             ▼                             ▼                             ▼
                    SE Community Leadership (force multiplier)
                    Personal Development (PSE→DSE growth journey)
                    Sponsorship (letters of recommendation)
```

**Cross-referencing:** Global Impact and Business Impact are **customer/revenue** sections. They may reference Span of Influence, Innovation, or SE Community Leadership when those activities **directly contributed** to a revenue or customer outcome (e.g., “Isovalent acquisition enabled Adobe engagement”—Innovation + Global/Business).

**Do not double-count:** One story has one **primary** home; other sections get a cross-reference or one-line summary only.

---

## ASP + Web vs MIG (engineering alignment)

ASP + Web works primarily with **MIG** (Mass-Scale Infrastructure Group) product/engineering:

| **In-scope / “home” (MIG)** | **Outside ASP+Web primary orbit (Span / Innovation)** |
| :--- | :--- |
| IOS-XR | Cilium / Isovalent (eBPF, host networking) |
| NCS 5xxx | SD-WAN (Viptela / SD-WAN BE) |
| Cisco 8000 | SASE / SSE / Cisco Secure Access |
| SONiC | Catalyst, Nexus (DC/campus) |
| Silicon One | Security portfolio (beyond transport) |
| SR / SRv6 (MIG platforms) | ThousandEyes |
| | Single OS (SOSIE) working group |
| | Future Enterprise Segmentation, FE tiger teams |
| | Enterprise BEs, cloud/security BEs generally |

**Span of Influence** = expanding impact **inside Cisco** beyond the ASP+Web + MIG orbit—other BUs, other theaters’ leaders, and peer **DSE/PSE** collaborators.

**Key cross-org peers (Span):** Brenden Buresh, Craig Hill, David Jansen, Brian Meaney, Virginia Teixeira, Mike McPhee, Rob Murphy, Clarence Filsfils, David Jansen, Marina Ferreira *(extend list as needed)*.

**Innovation** often **follows** Span: internal advocacy outside MIG → patents, product features, architectural direction, acquisition influence (e.g., Isovalent).

---

### What “ASP + Web” means for this package

**In-scope (home territory)** — primary home for **Business Impact** and day-to-day PSE account work:

- **Web / Hyperscale:** Americas-based cloud providers, neo-clouds, and large internet/web operators (e.g., Microsoft, Oracle, Meta, CoreWeave, Google, Amazon, Apple, OpenAI, Anthropic, xAI, Nvidia, Lambda Labs).
- **Service Provider:** Americas-based telecom and cable operators (e.g., Verizon, AT&T, Bell Canada, Digital Realty, Equinix, Videotron).

> **RETIRED RULE (Aug 17, 2026).** Earlier versions of this file stated that *"Global Impact is not 'other geographies.' It is any customer/revenue engagement outside the ASP + Web assignment."* **No citation exists for that rule** and it contradicts the official criteria. It has been removed. Two sections were drafted on it and were restructured on 2026-08-17.

## Official criteria — quote these, do not paraphrase

**Global Impact (DSE nomination PPT):**
- *Demonstrate global impact outside the immediate area*
- *Examples include leading global accounts, creating and delivering global training, developing new architectures that are adopted globally*

**Span of Influence (DSE nomination PPT):**
- *Interact and impact at higher levels internally in Cisco and externally with customers and partners*
- *Specialization and focus for at least two technology domains / architectures*
- *The impact is more strategic and focuses on horizon 2–3*

**Structural rule (DSE nomination Word guide, applies to BOTH sections):** *"Provide a high-level summary… using a bulleted list or a table to show the transition. **A detailed version can be added to the appropriate section of the package (business impact, innovation, SE leadership, etc.)**"*

**Consequence:** Global Impact and Span of Influence are **summary sections that index into the detail sections**, in two-column table form (initiative + date | impact prose ending with a cross-reference). This is exactly Brenden's structure, and it explains his page split: ~2 pages Global, ~2 pages Span, ~17 pages Business Impact.

## Which section does a project go in?

Detail lives in **exactly one** section; every other section gets a short entry pointing there. That is not double-counting — it is the intended structure.

| Section | Question it answers | Axis |
| :--- | :--- | :--- |
| **Business Impact** | Did it produce revenue at a named account? | Money |
| **Global Impact** | Did it reach outside the immediate area, or get adopted globally? | Reach |
| **Span of Influence** | Did it lift Bruce to higher altitude, across ≥2 domains, at horizon 2–3? | Altitude + breadth |
| **Innovation** | Is there an invention, artifact, or product outcome? | Novelty |
| **Industry Impact** | Did it land outside Cisco? | External |
| **SE Community Leadership** | Did it make other SEs more capable? | Multiplier |

Detail goes where the **strongest evidence** sits. Worked example — **SR-Apps**: detail in Innovation (invention, artifact, SR engineering adoption); one-entry pointers from Global Impact (global field lead), Span (co-development with Filsfils' org), Industry Impact (open source), and Business Impact (account outcomes it enabled).

**Do not double-count:** A single engagement should appear in **one** primary section. Summaries in the Executive Overview may reference both; detail lives in one body section.

---

## Package structure and page budget

**Section order follows Brenden's package** (README order) — reviewers expect this sequence.

**Page budget: the official Word template governs.** It specifies **2–3 pages** for Global Impact, Span of Influence, and Industry Impact, and *no page limit* for Business Impact, Innovation, Sponsorship, Personal Development, and SE Community Leadership. README's weighting (7 pages Global, 6 Span) is Bruce's own and is **superseded**.

| Order | Section | Repo file | Weight (1–5) | Target pages |
| :---: | :--- | :--- | :---: | :---: |
| 1 | Executive Overview | `01-exec-summary-draft.md` **(canonical)** | 6 | 7 |
| 2 | Direct Leader Recommendation | `02-direct-leader-recommendation.md` | — | 1–2 |
| 3 | **Global Impact** | `03-global-impact.md` | 5 | **2–3** *(official)* |
| 4 | Span of Influence | `04-span-of-influence.md` | 4 | **2–3** *(official)* |
| 5 | Industry Impact | `05-industry-impact.md` | 3 | **2–3** *(official)* |
| 6 | Business Impact | `06-business-impact.md` | 5 | 7 |
| 7 | Innovation | `07-innovation.md` | 4 | 6 |
| 8 | Sponsorship | `08-sponsorship.md` | 2 | 1 |
| 9 | Personal Development | `09-personal-development.md` | 1 | 1 |
| 10 | SE Community Leadership | `10-se-community-leadership.md` | 4 | 6 |
| — | Appendix (optional) | `11-appendix.md` | — | as needed |

**Max package length:** ~50 pages. Body total above is ~45–46, leaving room for cover, TOC, timeline graphic, and appendix.

**Canonical exec file:** `01-exec-summary-draft.md`. Earlier working notes were archived to `xarchive/01-exec-summary.md` (Aug 2026) — do not draft from them.

---

## Section criteria (what belongs where)

### 1. Executive Overview — `01-exec-summary-draft.md`

**Suggested length:** 3–4 pages in criteria text; **~7 pages** in README weighting.

**Must include:**
- Summary of body of work across **all** criteria categories
- Candidate background and career path **table** (role/title, dates)
- **Becoming a DSE** — what promotion means to candidate, SE community, Cisco, customers/partners
- **Direct leader summary** (short; full letter in section 2)
- Per-category summaries: Global Impact, Span of Influence, Industry Impact, Business Impact, Innovation, Personal Development, SE Community Leadership

**Agent notes:** Use SMART metrics in summaries. Distinguish ASP+Web business impact from global impact in the Global Impact summary paragraph. **Thru-narrative** may cite pre-2020 milestones (SDN 2012, early host-networking, first patents); all other summaries should emphasize **Aug 2020–present**.

---

### 2. Direct Leader Recommendation — `02-direct-leader-recommendation.md`

**Suggested length:** 1–2 pages. **Written by direct leader**, not the candidate.

**Time scope:** Focus on performance since **PSE promotion (Aug 2020)**.

**Must include:**
- Performance, achievements, progressive improvement since PSE promotion
- Transparent areas of development and actions taken
- **Future role plan** if promoted to DSE
- Optional: past managers / chain input
- Separate LoR not required if leader is sponsor; sponsor LoR rules per Nomination Kit slide 15

---

### 3. Global Impact — `03-global-impact.md`

**Official length:** 2–3 pages.

**Primary lens:** impact **outside the immediate area** — global accounts, global training, and architectures adopted globally (quote the PPT bullets above).

**Format:** a transition table (regional → theater → global) plus a two-column initiative table. Each entry ends with *"More details are located in the X section of this document."*

**Belongs here:** global initiatives and globally adopted architectures — SR-Apps global field lead, end-to-end SRv6, SONiC, Cilium, SP NaaS, SRv6+SGT, chassis-to-pizzabox, global training and enablement, and operators outside the Americas (Rakuten, Evroc, NTT East, MTN, DU).

**Does NOT belong here:** named customer case studies of any territory — those go to **Business Impact**, marked in-territory or out-of-territory. Americas enterprise accounts with no global dimension (Geico, Honeywell, Fiserv, Disney, TI, The Trade Desk, Morgan Stanley, NSight) were moved out on 2026-08-17.

---

### 4. Span of Influence — `04-span-of-influence.md`

**Official length:** 2–3 pages.

**Primary lens:** interaction and impact at **higher levels** internally and externally; **≥2 technology domains**; strategic, **horizon 2–3**.

**Format:** a transition table (altitude over time) plus a two-column initiative table, same as Global Impact. Name the technology domains explicitly — the PPT requires at least two. Bruce has four: programmable transport, cloud-native/host networking, open NOS, enterprise identity and policy.

**Frame it around horizon 2–3 architecture leadership, not organizational boundaries.** Per Bruce (Aug 2026): do not lead with what was or was not his area of responsibility; lead with the architectural visionary working three to five years ahead, the executive and Fellow relationships, and the named initiatives.

**Does NOT belong here:** revenue tables → Business Impact; external reach → Industry Impact; patent and product detail → Innovation.

---

### 5. Industry Impact — `05-industry-impact.md`

**Suggested length:** 2–3 pages.

**Official length:** 2–3 pages. **Standalone section** — unlike Global Impact and Span, it neither summarizes into other sections nor receives detail from them; its references point to **external links**.

**Primary lens:** influence and leadership **externally**, not only inside Cisco; the criterion explicitly names **standards bodies**. The template asks for *"the impact to Cisco's businesses in terms of revenue and/or strategy in a factual, verifiable way"* — the same wording as Business Impact. **Earlier guidance in this file said "direct revenue not required"; that was wrong.** Where revenue is absent, state the **strategy** impact explicitly.

**Must include:**
- Leadership and visibility **outside Cisco** among operators, architects, open-source community, standards-adjacent forums
- Chronological, most recent first
- External links and references

**Belongs here:**
- **Open source:** segmentrouting GitHub org, srv6-labs, Jalapeno (cisco-open), MRC emulator repos
- **Conferences:** NANOG (e.g., uSID), **OCP**, MPLS World Congress, **Cisco Live** (breakouts/labs as industry-facing thought leadership)
- **Publications:** SP360, segment-routing.net blogs, LinkedIn posts, whitepapers, vidcasts
- **Industry alignment:** Phoenix Wing / multi-vendor SONiC uSID narrative, MRC/OpenAI/Microsoft/NVIDIA papers citing SRv6 direction
- **IETF** participation, operator workshops where Bruce represented Cisco to the **industry**, not a single account win

**Relationship to other sections:**
- If the **same activity** also drove **assigned customer revenue**, put revenue in Business Impact and industry visibility here (cross-reference).
- Internal BU persuasion (SONiC investment **inside Cisco**) → Span + Innovation, not Industry.

---

### 6. Business Impact — `06-business-impact.md`

**Suggested length:** No page limit; **~7 pages** weighted.

**Primary lens:** **Customer and revenue impact within ASP + Web assignment** (Aug 2020–present).

**Must include:**
- Leadership role and impact on Cisco **revenue and/or strategy** — factual, verifiable
- Chronological, most recent first
- Detail for in-territory accounts summarized in Executive Overview
- May **cross-reference** Span / Innovation / SE Leadership when those enabled the account outcome (e.g., SONiC SRv6 productization → Microsoft AI backend win)

**Belongs here:** All **ASP+Web** customers (see list below)—Microsoft, Meta, AWS, Google, OCI, CoreWeave, Verizon, Bell, Videotron, Dish/Boost, AT&T, T-Mobile, Viasat, etc.

**Case study pattern:** Customer profile → problem/competition → Bruce’s actions (bullets) → financial / competitive / strategic / customer impact.

**Does NOT belong here:**
- Non-assigned theater customers → Global Impact
- Pure industry visibility with no account tie → Industry Impact

---

### 7. Innovation — `07-innovation.md`

**Suggested length:** No page limit; **~6 pages** weighted.

**Primary lens:** **IPR and Cisco product/technology innovation** (Aug 2020–present)—often **downstream of Span of Influence** advocacy outside MIG.

**Must include:**
- Leadership in innovation; impact on Cisco **strategy, product, or revenue** where verifiable
- Chronological, most recent first
- Tables OK; patent/CPOL links, architectural artifacts, labs

**Belongs here:**
- **Patents / CPOLs** (issued, pending, defensive publications) — post-2020 submissions and **impact** of earlier work if realized after PSE
- **Architectural designs & labs:** SRv6 multi-tenant AI fabric spec, MRC emulator, srv6-msft/srv6-oci POC repos, Hoffman-Singleton study
- **Product features & direction:** host-based networking, host-based SRv6, SRv6 on SONiC, Cisco **strategic investment in SONiC**, SRv6 for AI, **SRv6+SGT** end-to-end identity/policy (multi-BU)
- **Major outcomes:** **Isovalent/Cilium acquisition influence**; Bold Bets/Jalapeno; Pinnacle Award (SRv6 uSID); EN hackathon; Policy Plane
- **Whitepapers** when they drove **product or strategy** (not merely industry visibility—those also touch Industry Impact)

**Span → Innovation examples:**
- Host-networking advocacy → Isovalent acquisition → Cilium SRv6 product path
- Single OS working group → company NOS strategy discourse
- SD-WAN/SSE SRv6 positioning → engineering roadmap commitments

**Does NOT belong here:**
- Account revenue without inventive/IP component → Business Impact
- External blog reach alone → Industry Impact

---

### 8. Sponsorship — `08-sponsorship.md`

**Format:** Table — name, role, organization, date; **letters of recommendation stored externally**.

**Owner:** Bruce (candidate)—not drafted by agents except table scaffolding.

**Categories:** Direct leadership, BE leadership, sales leadership, customer/partner, DSE/PSE community (ex-Cisco OK).

**Note:** Target >50% of global DSE community letters (per candidate notes).

---

### 9. Personal Development — `09-personal-development.md`

**Suggested length:** ~1 page.

**Primary lens:** **Journey from PSE (Aug 2020) toward DSE** — technical and personal growth that enabled broader impact.

**Must include:**
- How development increased **span and global influence beyond ASP+Web** (new BUs, open source, cloud-native tooling, exec communication)
- How Bruce continued to **push the technical envelope** as an industry pioneer (not comfort-zone MIG-only depth)
- Chronological, most recent first
- **Table:** education & certifications (description, date, link)
- Tie **learning → application → measurable impact** (even if impact is documented in other sections)

**Belongs here:** Executive coaching, Cilium/K8s depth, Containerlab/GitHub labbing, Ultra Ethernet study, PSE-committee feedback response, cross-theater relationship building, “vibe-labbing” for faster customer POCs.

**Not a bare cert laundry list** without impact narrative.

---

### 10. SE Community Leadership — `10-se-community-leadership.md`

**Suggested length:** No page limit; **~6 pages** weighted.

**Primary lens:** **Force multiplier** for the SE community (Aug 2020–present)—training, mentoring, and enablement that helps SEs **grow capabilities, grow careers, and sell more**.

**Closely related to:** Business Impact, Global Impact, and Span of Influence—document **outcomes** (mentee promotions, account wins enabled, labs reused globally) where possible.

**Must include:**
- **Tables:** initiatives, mentoring, enablement, internal speaking, publications used for SE training
- Dates, links, survey scores, attendee counts
- Chronological, most recent first

**Belongs here:**
- **Mentoring:** **Official PSE mentor:** Ignacio (“Nacho”) Sanchez (promoted Jun 2026); **Christopher Luciano (in progress, since Dec 2024)**. **PSE candidate extended team** (advisor / package reviewer): Rob Murphy & Roberta Maglione (**2023**); Masiuddin Mohammed, Marina Ferreira & Alessandro Breccia (**2024**). Dan Stacks (STLDP), Satoshi Yamashita, etc.
- **Enablement:** Stay Ready Friday, Tech Elevate, TMC innovation hours, SONiC/SRv6/Cilium dCloud labs, MIG specialist walkthroughs
- **Cisco Live:** instructor-led labs (scores), breakouts, panels (BTSP 2026)
- **PSE review committee** (3 years)
- **STLDP** innovation-award coaching
- **Lightning talks**, SEVT panels, ASP 8K enablement series

**Split with other sections:**
- CL lab at **CLEU** with **Evroc customer** outcome → Global Impact for customer; SE Leadership for lab delivery metrics
- **srv6-labs** as public artifact → Industry Impact; SE Leadership if framed as SE enablement asset

**Embed throughout package where applicable:**
- Publications & professional affiliations (README list)
- External & internal speaking (CL, EBCs, bootcamps, VTs, tiger teams)
- Awards & recognition (Connected Recognition, CL Distinguished Speaker, etc.) — also `11-appendix.md`

---

## Cross-cutting content (from README)

Embed in relevant sections, not a standalone section:

**Publications:** books, CEC/CCO, whitepapers, EBC papers, knowledge shares, magazines/blogs, videos, EDCS, IETF/external, case studies, user guides, professional affiliations.

**Speaking:** Cisco Live, EBCs, industry events, customer forums, demos, bootcamps, VTs, tiger/advisory teams.

**Awards:** Connected Recognition, theatre awards, Cisco awards, sales awards, speaker awards, external awards.

---

## ASP + Web — assigned customers (in-scope for Business Impact)

*Bruce confirmed Jun 2026: **Akamai, Equinix, Salesforce, Lambda Labs, Groq, Roblox, Netflix, eBay, ServiceNow, Riot Games, Viasat, Comcast** are ASP/Web accounts. Agents: do **not** treat this list as exhaustive.*

### Web / Hyperscale / Neo-cloud (Americas)

- [x] **Microsoft** (Azure, SWAN, AI backend, SONiC, PhyNet/dRH)
- [x] **Meta** (WAN, EBB, RBB, BBF, SL-API)
- [x] **Amazon Web Services (AWS)** (Silicon One, Direct Connect)
- [x] **Google** (GDC, B4 SR-MPLS, Alphanet / SL-API)
- [x] **Oracle Cloud Infrastructure (OCI)** (AI backend, Acceleron, SRv6)
- [x] **CoreWeave**
- [x] **Lambda Labs**
- [x] **Groq**
- [x] **Roblox**
- [x] **Netflix**
- [x] **eBay**
- [x] **Salesforce**
- [x] **ServiceNow**

### Service Provider — Americas

- [x] **AT&T**
- [x] **Verizon**
- [x] **T-Mobile**
- [x] **Bell Canada**
- [x] **Videotron**
- [x] **Dish / Boost Mobile**
- [x] **Viasat**
- [x] **Riot Games**
- [x] **Akamai**
- [x] **Equinix**
- [x] **Comcast**
- [ ] **Lumen / CenturyLink** *(add if applicable)*
- [ ] **Charter / Spectrum** *(add if applicable)*

---

## Global Impact — seed list (outside ASP + Web assignment)

*Not “outside Americas”—outside **ASP+Web segment**. Bruce to extend.*

### Americas — Enterprise / Financial / Education / Regional

- [ ] **Geico** — SONiC DC, Colorado colo
- [ ] **Fiserv** — SRv6 TOI, banking infrastructure
- [ ] **Adobe** — Cilium + Cloud-Native SRv6
- [ ] **Honeywell** — NCS5501 backbone, Flex-Algo interest
- [ ] **Texas Instruments** — global POP ring, SRv6 direction
- [ ] **Disney** — DGN / SR-MPLS
- [ ] **NYU** — HSRN SONiC research net
- [ ] **The Trade Desk** — SONiC evaluation
- [ ] **NSight** — Cilium/AI services (regional SP, Green Bay)
- [ ] **Visa** — Isovalent intro (Oct 2025); **Global Impact**

### APJC

- [ ] **Rakuten** (Japan — SRv6 SD-WAN HLD, Jul 2025)
- [ ] **Softbank** *(confirm engagements)*
- [ ] **NTT East** (Japan — SR win)
- [ ] **Indosat Ooredoo** (ASEAN — first SRv6 deployment claim; verify)

### EMEA

- [ ] **Evroc** (Sweden/EU hyperscaler — CLEU 2025, SONiC/Cilium-SRv6)
- [ ] **MTN Nigeria** (via APJC SE Sanjay Nanda — topology/$85k lab savings)
- [ ] **DU UAE** (2300-node SRv6 POC topology)
- [ ] **Telia, Swisscom, Telstra** *(confirm — listed in notes; add detail)*
- [ ] **Iliad** *(CLEU 2025 interest — confirm ongoing)*

### Global enablement (only if tied to non-assigned **customer/revenue** outcome)

- [ ] **Field SE support** — e.g., Sanjay Nanda / MTN Nigeria, DU UAE (APJC/EMEA operators)
- [ ] **SRv6 Roadshow** — if outcomes on non-ASP+Web customers *(otherwise SE Leadership / Industry)*

*Moved to other sections by default:*
- `segmentrouting` / srv6-labs → **Industry Impact** (+ SE Leadership if SE-training framed)
- CLEU/CLUS labs without non-assigned customer win → **SE Community Leadership** / **Industry Impact**
- MPLS-WC / NANOG / OCP → **Industry Impact**
- CNRS / SR-Apps university partners → **Innovation** or **Industry Impact** unless tied to named global customer win

---

## Repo file map

| File | Purpose |
| :--- | :--- |
| `voice-guide.md` | **Voice & claim strength — read before drafting** |
| `00-overview-themes.md` | Brand, themes, candidacy positioning |
| `01-exec-summary-draft.md` | **Canonical** executive section |
| `Bruce-McDougall-DSE-Package-Aug2026.docx` | **Official Word package template** — final deliverable |
| `scripts/md_to_docx.py` | Inserts a drafted section into the Word template (see below) |
| `xarchive/` | Superseded material — do not draft from |
| `02-direct-leader-recommendation.md` | Leader letter placeholder |
| `03-global-impact.md` | **Outside ASP+Web** impact |
| `04-span-of-influence.md` | **Internal Cisco** influence outside ASP+Web / MIG |
| `05-industry-impact.md` | **External industry** visibility (revenue optional) |
| `06-business-impact.md` | **ASP+Web customers** and revenue |
| `07-innovation.md` | Patents, products, acquisitions, inventions |
| `08-sponsorship.md` | LoR table |
| `09-personal-development.md` | Certs, training, growth |
| `10-se-community-leadership.md` | Mentoring, enablement, CL |
| `11-appendix.md` | CL scores, Connected Recognition |
| `PSE-time-log.csv` | **Chronological activity log** (2020–present); route by DSE criteria column → section files |
| `reference/` | Brenden package PDF + template outline |
| `projects/` | Deep-dive project write-ups (MRC, SRv6 AI fabric) |

---

## Agent workflows

### Harvest pass (Obsidian → repo)

1. Read this `AGENTS.md` for section scope and **Aug 2020 floor date**.
2. **Also harvest** `PSE-time-log.csv` — map **DSE criteria** column to sections: `biz` → 06 (if ASP+Web account); `global`/`glob` → 03; `span` → 04; `innov` → 07; `industry`/`indust` → 05; `lead` → 10; `personal`/`pd` → 09. One story = one primary home.
3. Start from vault `dse/<Section>-MOC.md` and follow `[[wikilinks]]`.
4. **Tag each finding:** `Business (ASP+Web)` | `Global (customer $)` | `Span (internal)` | `Industry` | `Innovation` | `SE Leadership` | `Personal Dev`.
5. **Filter pre-2020** unless drafting exec overview thru-narrative.
6. Write polished third-person narratives into the matching repo file.
7. Append **open items** and **vault source paths** at bottom of section file.
8. **Global Impact** = non-assigned customers with revenue/pipeline story only.
9. **Span** = non-MIG / cross-BU / cross-peer influence inside Cisco.

### Section routing quick check

| Evidence type | Primary section |
| :--- | :--- |
| MSFT account revenue | Business Impact |
| Rakuten APJC engagement | Global Impact |
| Isovalent acquisition advocacy | Span → Innovation |
| srv6-labs LinkedIn views | Industry Impact |
| CLEU lab scores + mentoring | SE Community Leadership |
| Patent / AI fabric spec | Innovation |
| PSE committee, Single OS WG | Span of Influence |
| Post-2020 skills → cross-BU work | Personal Development |

### Review workflow

**Markdown is the source of truth. The Word document is a build artifact.** Bruce reviews, edits, and comments in the `.md` files; sections are regenerated into Word from there. This is one-directional — never edit prose in Word and expect it to survive.

**Comment notation:** a line beginning with `//` (line-initial only, so `https://` in prose is safe). HTML comments on their own line work too.

```markdown
Bruce served as SONiC subject-matter expert for the Colorado colocation architecture.
// is "subject-matter expert" right here? I was effectively the lead architect
```

Place the comment **after** the paragraph or table it refers to. Comments are stripped automatically on insert and never reach the Word document.

**Collect them with:**

```
scripts/review_comments.py            # all sections, with heading + anchor paragraph
scripts/review_comments.py --count    # tally only
```

**Word-side tools** remain for the last mile — page counts, table widths, and external reviewers:

- `scripts/read_docx_review.py` — read comments and tracked changes from a `.docx` (works while Word is open). Use for feedback from Brook, Matt, and sponsors.
- `scripts/edit_docx.py` — surgical find/replace inside a `.docx`, preserving comments and formatting. Use for late fixes once the document is final.

### Assembling the Word package

The official deliverable is `Bruce-McDougall-DSE-Package-Aug2026.docx`. Insert a drafted section with:

```
scripts/md_to_docx.py <section.md> Bruce-McDougall-DSE-Package-Aug2026.docx \
    --after "<template Heading 1>" --before "<next template Heading 1>"
```

**Close the file in Word first** — a `~$…docx` lock file means Word has it open and edits will be lost.

The converter maps `##`→Heading 2, `###`→Heading 3, renders bold/italic/code/hyperlinks, converts markdown tables to `Table Grid`, and bullets to `List Paragraph`. It **filters repo-internal scaffolding**: scope blockquotes, "Suggested package length", vault paths, `**Evidence:**` lines, harvest logs, open items, and "Explicitly Excluded" tables. Cross-reference lines are **kept** — they are the gold-standard package pattern. `[verify]` markers render in **red** so they are obvious during final cleanup.

Use `--before END` to append to the end of the document (used for the Appendix).

Re-running against the same anchors **fully replaces** the section — paragraphs *and* tables — so it is safe to iterate.

> **Once a section has been edited in Word, Word is the source of truth for it. Do not re-insert that section — it will discard those edits.** Late global changes (find/replace, stripping `[verify]` markers) can be scripted against the `.docx` directly instead.

### Writing conventions

**Read [voice-guide.md](./voice-guide.md) before drafting any section.** It governs claim strength, verb choice, case-study openings, and the four labeled impact types, and it documents the candidate's known failure mode (understating his own claims). The rules below are the summary; the guide is the authority.

- Third person: “Bruce led…”, “McDougall authored…” — first person only in **Becoming a DSE**
- **Register:** Flat, declarative, factual — Brenden's register throughout. "Friendly and collaborative" is a **finding demonstrated by evidence** (mentee promotions, 22 Connected Recognition awards given, peer quotes), *not* a prose style. Do not soften sentences to sound collaborative.
- **Bruce is the grammatical subject** of every sentence describing his work. Banned verbs: helped, contributed to, was part of, was involved in, assisted, played a role in.
- **Claim first, quote second.** A quote corroborates a claim already stated in Bruce's own sentence; it is never the first place the reader learns it.
- **Every case study:** ≤2 sentences of customer stakes (rank, scale, revenue) → problem/competition → Bruce's actions (bullets) → four labeled impact types → evidence pointer.
- **Report setbacks in the same flat voice as wins** — the gold-standard package does this repeatedly and it is what makes the wins credible.
- **Date floor:** Aug 1, 2020 except exec thru-narrative
- Active verbs; separate **financial / competitive / strategic / customer** impact where possible
- Mark unverified claims: `[verify]` or `[pending finance validation]`
- Cross-reference: *“More details in the Innovation section.”*
- Prefer tables for career path, revenue summary, sponsorship, mentoring, speaking

### Open items (maintain in section files or README)

- Finance-validated revenue figures
- Complete ASP+Web customer list (this file)
- Re-filter `03-global-impact.md` for **customer/revenue-only, non-ASP+Web**
- Re-filter `01-exec-summary-draft.md` for pre-2020 content outside thru-narrative
- Career path dates; direct leader letters (Brook Crossman + Matt Gillies)
- Broken vault wikilinks (`2023 sonic-blog-alibaba_msft`, etc.)
- Confirm Virginia Teixeira spelling; extend cross-org peer list

---

## Brand themes (from `00-overview-themes.md`)

- Technical visionary for cloud + AI era; horizon 2–3
- Unique **SP + hyperscale/cloud-native** combination in Cisco sales
- Foundations: **SRv6 end-to-end**, **Linux/open source (SONiC)**, **host networking & security**
- Collaborator, listener, operator empathy; evangelize where the puck is going
- Tie innovations to **quantified outcomes** when they land
