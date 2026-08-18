# Criteria Audit — package vs. official sources

**Date:** Aug 18, 2026
**Sources now in repo:** `reference/Template for DSE candidacy Jan2025.docx`, `reference/PSE DSE Nomination Kit FY26.pptx` (criteria on slides 15, 21–22, 24–25)

Findings ordered by consequence. Items marked **[error]** are clear mismatches with official text; **[judgment]** needs Bruce's call.

---

## 1. [error] The role name is wrong throughout the package

Official template title: **"Distinguished Solutions Engineer (DSE)"**. The Nomination Kit is titled **"Principal & Distinguished Solutions Engineer Nomination Kit"**.

Our package says **Systems** Engineer everywhere — including the Word document title and every section header. Bruce's own speaker bio already says *"Principal Solutions Engineer."*

**Proposed:** global replace *Systems Engineer* → *Solutions Engineer* for PSE/DSE role references, in all `.md` files and the `.docx`. Careful not to change "systems engineer" where it refers to the generic job family or to other people's titles (e.g. "APJC systems engineer Sanjay Nanda" — that one is probably also *solutions* engineer now, worth confirming).

---

## 2. [error] Section 10 is now called "Leadership", not "SE Community Leadership"

The template carries an explicit change note: *"(Update SE Community Leadership to Leadership 01092025…)"*.

The official scope is also **broader** than we have drafted. Slide 22:

> *"Demonstrate leadership by driving business outcomes and investments, through collaboration and influence, consolidated inputs from multiple stakeholders based on data. Lead different programs, teams or initiatives (internally and externally to Cisco) around: **Technology, SE Community, Technical Enablement, Community, Volunteer** etc. Demonstrate leadership attributes: **Executive Presence and Communication skills**. Mentors and develops capabilities within others (career mentorship with clear evidence/endorsement)."*

Our section covers SE community, enablement, and mentoring well. It does **not** cover: leadership of *technology* programs (SOSIE, tiger teams — currently in Span), executive presence and communication as an attribute, or volunteer/community work.

**Proposed:** rename to **Leadership**; add a technology-programs subsection cross-referencing Span; add an executive-presence subsection (the coaching completion, ASP-wide presentations, Jeetu Patel readout, EBC delivery); ask Bruce whether there is volunteer or community work to include. Renaming also affects the Word template anchor.

---

## 3. [error] "Force multiplier" is the official framing device for the whole DSE package

Slide 25, the **first row** of the DSE criteria table — above Global Impact, Span, and Industry Impact:

> **General Guideline:** *"Demonstrate how you have been a **force multiplier** throughout the organization (covering multiple criteria aspects). For example: **identification of new technology and industry trends**, **building the necessary field enablement**, **aligning strategic stakeholders (engineering and sales exec.) and investment**, **leading lighthouse customers and driving field adoption**."*

Those four examples describe Bruce's operating model almost exactly:

| Official example | Bruce's evidence |
| :--- | :--- |
| Identification of new technology and industry trends | Host-networking air-gap (2015); SRv6-for-AI (2017 elephant flow); SONiC inflection (2023); flat topologies (2024) |
| Building the necessary field enablement | `srv6-labs`, dCloud labs, MRC emulator, VXR labs, Tech Elevate across three theaters, SRv6 roadshow |
| Aligning strategic stakeholders and investment | SONiC investment case; Isovalent acquisition advocacy; Cilium CRD accepted by engineering; MIG G200 commitment |
| Leading lighthouse customers and driving field adoption | Microsoft, Meta, Oracle, CoreWeave, Bell Canada |

**Proposed:** make this the **spine of the Executive Overview** — state the general guideline, then give the four-part evidence structure above. It is the assessment framework the panel is handed, and the package currently does not use it. This is the single highest-value change in this audit.

---

## 4. [error] Industry Impact — standards bodies are explicitly required

Slide 25:

> *"Influencing and leading not just internally within Cisco, but also externally. **Participate and/or lead standards bodies and represent Cisco within such.**"*

The template adds: *"Describe the candidate's leadership role and the impact to Cisco's businesses in terms of revenue and/or strategy."*

Two mismatches. First, `AGENTS.md` says *"direct revenue not required"* for Industry Impact — the official text asks for revenue **and/or strategy**, so strategy impact must be explicit where revenue is absent. Second, **Bruce edits an IETF draft** (`draft-srv6ops-addressing-guidelines`) and that is currently one row in a table. Standards work is the named criterion.

**Proposed:** restructure Industry Impact to lead with standards — the IETF draft editorship, IETF SRv6-Ops participation, and the SRv6 book chapters — then open source, then conferences and publications. Add a strategy-impact statement to each entry.

---

## 5. [error] Innovation — the criteria name specific evidence we have not gathered

Slide 22:

> *"Evidence of contributions (**Patent # granted**, **GitHub stars**, Sales data, event registration/attendees and speaker score, adoption, endorsement from sponsor and community)."*

- **Patent numbers.** We have Cisco asset IDs (`C/P/1035601/US/ORG/1`) and issue dates, but not US patent numbers. The criteria ask for the number.
- **GitHub stars.** Never captured. Needed for `segmentrouting/srv6-labs`, `cisco-open/jalapeno`, `srv6-mrc-emulator`, `polarfly`, `srv6-msft`, `srv6-oci`.
- **Speaker scores** — we have these, and they are in Leadership.

**Proposed:** Bruce to pull US patent numbers and current GitHub star/fork/contributor counts. Both are quick and both are explicitly requested evidence.

---

## 6. [error] Sponsorship categories do not match the official split

Slide 15 requires:

| Category | Requirement | Our tracker |
| :--- | :--- | :--- |
| BE leadership, **director and above** | 3–5 | 10 candidates |
| Sales leadership, **director and above** | 3–5 | 16 candidates |
| Customers or partners, **key decision makers** | 3–5 | 12 candidates |
| Leaders in other Cisco orgs (CX, P&C), director+ | up to 5 | 4 candidates |
| Engineering **PE / DE / Fellow** | no minimum or limit | *merged with the row below* |
| **Cisco Sales PSEs / DSEs** | **minimum 3, no maximum — weighted heavier** | *merged with the row above* |

Two problems. Our tracker has a single "Fellow / PSE / DSE / PE / DE" category with 44 names, but the official split treats **Engineering PE/DE/Fellow** and **Cisco Sales PSE/DSE** as distinct — and says the Sales PSE/DSE letters are **weighted more heavily** because those communities select by peer committee. Also, BE and Sales leadership both carry a **director-and-above** qualifier we have not screened for.

Also noted: **"No Ghostwriting!"** — worth flagging given the volume of letters being solicited.

**Proposed:** split the tracker into the six official categories; screen BE and Sales candidates for director-and-above; identify at least 3 (ideally more) **Cisco Sales PSE/DSE** letters and prioritize them, since they count most. Bruce's ">50% of the global DSE community" goal aligns well with this — it is the heaviest-weighted category.

---

## 7. [judgment] Page limit — we may be closer than I thought

Official: *"No more than 50 pages, including the cover, **excluding the index and appendix**."*

The appendix does not count. Current body is ~34,200 words (≈52 pages at 650 words/page) with the appendix excluded — so marginally over, not the ~57 I previously reported.

**Proposed:** treat Business Impact (8,970 words) as the trim target if needed. Note it has **no official page limit**, and the template explicitly says it is *"an opportunity to provide more details on items you have summarized in the Global Impact and Span of Influence sections"* — which validates the restructure and argues for leaving it long.

---

## 8. [judgment] "Without restating the PSE journey"

General guideline: *"Focus on telling a concise story of the journey from PSE to DSE **without restating the PSE journey**."*

The Innovation section's *How the thinking developed* subsection covers Expedia 2006, SDN/NFV 2012–13, Segment Routing 2013–16, and the 2015 cloud insight. Two readings: it is **framing** that explains why the post-2020 record looks as it does, or it is **restating** the PSE journey.

**Proposed:** keep it but compress — the 2015 host-networking insight is load-bearing because it explains the Isovalent outcome, so it earns its place. The Expedia and SDN/NFV material could reduce to a single sentence. Bruce's call.

---

## 9. [error] Personal Development has no page limit and wants a table

Template: **"No page limit"** — we had it at ~1 page. It also specifically asks for *"a table format to describe your education, and certifications (Cisco/industry etc.), including a brief description, date, and reference to external links."* We have that table. And: *"This is an opportunity to provide more details on items you have summarized in the Global Impact and Span of Influence sections."*

Slide 22 criteria: *"Demonstrate how your continuous personal development activities contributed to your growth through **alignment to market transitions, Cisco priorities and customers outcomes**."*

**Proposed:** the current section is well-aimed but short. Add explicit alignment-to-market-transition framing to each development item, and note there is room to expand.

---

## 10. [error] Formatting requirements not yet applied

- **Font: CiscoSansTT**, no smaller than **10 pt**, **single spaced**
- **Ensure hyperlinks work**
- Cover page fields: **PICTURE**, NAME, DATE, Theater, DSE Sponsor, DSE Direct Leader, DSE Mentor, Location
- *"Delete this page before submission"* — the guidance page in the template
- The template notes best practices for converting to PDF (added 03112025)

Our Word document currently has no picture, and the tables I inserted are set at 8.5 pt — **below the 10 pt minimum**.

**Proposed:** set all inserted table text to 10 pt (this will widen the revenue tables — may need landscape or fewer columns); apply CiscoSansTT throughout; add the cover photo; confirm Theater field wording ("Global Systems Engineering" — should this be a theater?).

---

## Priority order

1. **Force-multiplier framing** into the Executive Overview (#3) — highest value, and it is the panel's own framework
2. **Solutions Engineer** naming fix (#1) — mechanical but appears in the document title
3. **Sponsorship re-split** (#6) — affects who Bruce asks, so it gates outreach
4. **Section 10 rename and scope expansion** (#2)
5. **Industry Impact standards-first restructure** (#4)
6. **Patent numbers and GitHub stars** (#5) — Bruce to gather
7. Formatting: 10 pt minimum, CiscoSansTT, cover photo (#10)
8. Personal Development expansion (#9)
9. Page-limit and PSE-restatement judgment calls (#7, #8)
