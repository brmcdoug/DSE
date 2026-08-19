# Voice & Claim-Strength Guide — DSE Package

Companion to [AGENTS.md](./AGENTS.md). AGENTS.md governs **what goes where**. This file governs **how it reads**.

Sources: `reference/Brenden Buresh Distinguished Architect Final 040122.pdf` (62pp, read in full), `about-me/Bruce McDougall Principal Architect Nomination.docx` (2020 PSE package), `about-me/writing-style.md`, `about-me/standout-report.md`, `about-me/speaker-bio.md`.

---

## The one thing this file exists to fix

From `about-me/writing-style.md`, on the 2020 PSE package:

> *"This is all me, my case for PSE in 2020. Common feedback I got on the document is I'm too modest/humble."*

That feedback is correct, and the pattern is visible on the page. It is not a tone problem — the PSE package is well written. It is a **claim-attribution** problem: Bruce consistently routes his strongest claims through other people, through the industry, or through the passive voice, so the reader has to assemble the argument themselves.

**The correction is not to write more assertively. It is to state the claim in Bruce's own sentence, then support it.** Confidence in this genre comes from declarative sentences with numbers in them, not from adjectives.

---

## Evidence: how the modesty actually shows up

Four distinct mechanisms, all from the 2020 PSE package:

### 1. The quote carries the claim instead of the sentence

The sponsorship letter states *"Bruce has delivered well over $1B in revenue to Cisco."* Bruce's own Executive Summary buries *"$1.3B in Cisco revenue in the last 10 years"* in the sixth bullet, after three bullets of customer-list context. Brenden's package puts **$1.65B in the second sentence of his Business Impact Summary**, in his own voice, and repeats it in the Direct Leader letter.

Quotes should *corroborate* a claim already made. They should never be the first place a reader learns it.

### 2. Deferential framing of his own leadership

> *"Bruce's has always been adept at serving whichever role the account team needs him to fill to be successful and meet their goals."*

This describes a person who led the Segment Routing effort at Google as though he were staffing a gap. Brenden's equivalent: *"Brenden was selected as the lead SME to guide design and architecture"*, *"Brenden took a primary leadership role."*

### 3. Diffuse attribution verbs

The PSE package repeatedly uses **helping to drive, contributed to, has been leveraged by, took hold later, rippled through, spurred**. Example:

> *"These ideas took hold later as data-model driven operations feature sets were developed across Cisco's routing and switching portfolio."*

Something happened; no one did it. Brenden never writes this way — even for outcomes years downstream of his involvement, he keeps himself as the grammatical subject.

### 4. Long context runway before any claim

The Letter from the Candidate spends three paragraphs on COVID, cloud, and an Amin Vahdat quote before the first sentence about Bruce. Brenden's Executive Overview names his role, tenure, and progression in sentence one.

---

## The calibration target: what Brenden actually does

Read these as permissions, not just techniques.

### Claims influenced revenue, not closed revenue — and labels it plainly

Brenden's $1.65B is **total account revenue across 14 accounts over 4 years**, on accounts he supported as an architect. He did not personally close it and does not claim he did. He states the number, breaks it out by FY per account, and lets scope do the work.

**This is direct permission for the $10.9B segment figure** in `01-exec-summary-draft.md`, provided it is labeled with the same precision — segment bookings in Bruce's theater over a stated period, not "revenue Bruce drove." The current draft already labels it correctly. Keep that discipline and the number is defensible.

### States failure plainly and keeps the claim

The most useful thing in Brenden's package, and the thing most likely to unlock Bruce's register:

> *"The first two versions of the integration design had several issues and were abandoned, but positive outcomes were realized from those efforts."*

> *"That initial proposal was ultimately rejected, yet internal and customer demand remained strong. A second effort in direct partnership with NSBU restarted the CEaaS offer."*

> *"However, delivery dates slipped and the customer opted to utilize a competitive product. DNA Spaces finally shipped and is now Cisco's flagship policy discovery, automation, and validation tool."*

That last one: the customer *left*, and he still books the $200M product line as his outcome. The gold-standard package is not a highlight reel — it reports setbacks in the same flat voice as wins, which is precisely what makes the wins credible.

**Applies directly to:** Cisco being late to market on SRv6-for-AI vs. competitor hardware (`todo.md`), the abandoned SR-MPLS path at Province of New Brunswick, the Adobe engagement Bruce rescued after it had failed, Bold Bets rounds not advanced. Write them.

### Four labeled impact types, same order, every time

```
Financial impact: [product/services $, FY breakdown, total]
Competitive impact: [who was displaced, blocked, or kept diminished]
Strategic impact: [reference architecture, BE relationship, repeatability]
Overall customer impact: [what the customer's business got]
```

Brenden runs this on **every** case study without variation. It is the single highest-leverage pattern to copy: it forces a competitive claim and a strategic claim even when the financial number is soft or pending — useful while `[verify]` numbers are outstanding.

### Opens every case study with stakes, in two sentences

> *"Anthem is the largest US health insurance provider in the Blue Cross Blue Shield Association, with 40M network members. Headquartered in Indianapolis, IN, Anthem ranks #23 on the Fortune 500 with $121B in annual revenue."*

Rank, scale, revenue, location. Then the problem, then Brenden's role. **Bruce's accounts are objectively larger than Brenden's and this pattern is currently absent from the drafts** — Microsoft, Meta, and Oracle deserve the same two-sentence stakes treatment, and it costs nothing.

### Verb inventory

**Brenden uses:** led, directed, drove, designed, created, constructed, established, guided, coordinated, partnered, was selected as, took a primary leadership role, made the case for, redirected, restructured.

**Brenden never uses:** helped with, contributed to, was part of, supported the effort, was involved in, assisted with, played a role in.

---

## Rewrite rules

| Bruce's instinct | Write instead |
| :--- | :--- |
| "Bruce helped drive the investment case for SONiC" | "Bruce drove the investment case for SONiC" |
| "These ideas took hold later as…" | "Bruce's advocacy resulted in…" |
| "Bruce contributed to the Meta BBF win" | "Bruce enabled the $17M Meta BBF production order by…" |
| "Bruce has always been adept at serving whichever role is needed" | "Bruce led the Segment Routing effort while other SEs drove telemetry and OpenConfig" |
| Quote from a VP establishing the claim | Bruce's sentence establishing the claim, then the VP quote corroborating it |
| Three sentences of industry context, then the claim | Claim, then one sentence of context if the reader needs it |
| "was influential in" / "was a key enabler for" | Name the specific act: "provided pre-GA patches and VXR POC labs that displaced Arista" |
| "[verify] — number pending, so soften the sentence" | Keep the sentence at full strength; mark only the number `[verify]` |

That last row matters. Pending finance validation should never leak into hedged prose. `"Bruce's SONiC advocacy produced the Geico data center win ($1.6M [verify])"` — the claim is firm, only the figure is provisional.

---

## Accuracy guardrail: do not upgrade plans into accomplishments

Caught in review (Aug 2026): the Personal Development draft asserted that Bruce *"engaged an executive conversation coach and completed the program by March 2026."* The source was a **personal development plan action item recorded as "in progress"** — a goal, not an event. Bruce did not recall it because it had not happened as written.

This is a distinct failure mode from overstating impact. A plan, a target date, or an intention sitting in a status table reads like a fact once the status column is dropped.

**Rule:** when drafting from `todo.md`, a PDP table, or any tracker, carry the status forward. If an item says *in progress*, *planned*, or *target*, the prose must say so too. Only mark something complete when there is an event, a date, and evidence.

---

## Framing guardrail: what drives the innovation record

An early draft of the Innovation section made **declined disclosures the centrepiece** of Bruce's innovation philosophy. He corrected it (Aug 2026), and the correction matters because it changes what the section argues.

**Wrong framing:** *inventions appear as declined disclosures, then reappear years later as products.* This is true sometimes, but it makes the record look like a story about institutional resistance.

**Right framing:** Bruce **was the operator first** — a network engineer and Cisco customer at Expedia before he was a vendor architect. He chooses what to work on by asking *what would I want if I were still the operator: the simplest, most cost-effective, longest-lasting architecture?* — and beyond the single operator, *what fosters a thriving ecosystem, since that is what produces durable growth.* He does **not** start from how Cisco sells more. Being ahead of Cisco, ahead of customers, and occasionally ahead of the hyperscalers is a *consequence* of that starting point, not the point itself.

Most ideas begin as a brainstorm — his own or with a peer — and become an approved disclosure, a paper, or a working demo. Declines are part of the record, not the spine of it.

**Rule:** when framing Bruce's motivation anywhere in the package, start from operator empathy and architectural durability. Institutional resistance is context, never the thesis.

---

## Accuracy guardrail: prescience claims

The "saw it early" argument is this package's strongest asset **and** its highest-risk one. A prescience claim is the most checkable thing in the document — dates are public, product ship dates are internal record, and a reviewer who catches one overstatement will discount the rest.

**The failure mode is generalizing from a true specific to a false general.** Two cases caught in review (Aug 2026):

| Overstated | Actual | Accurate framing |
| :--- | :--- | :--- |
| "trained the field on products that did not yet exist" | SONiC had existed for years and Cisco shipped a SONiC product; the **SRv6 feature set** did not exist on it | "before the capability shipped on Cisco platforms" |
| MRC emulator built "before any product existed" | Built the **week after** OpenAI publicly announced MRC | "within a week of OpenAI's public MRC announcement" — a speed claim, not a prescience claim |

**Rules:**

1. **Name the specific thing that did not exist** — a feature, a capability, a supported platform — never "the product."
2. **A fast-response claim is not weaker than a prescience claim.** Building a working emulator within a week of a spec publishing is verifiable, impressive, and unassailable. Reach for it when it is what actually happened.
3. **Before writing "years ahead," check the date.** The host-networking arc (2013 advocacy → 2021 Isovalent push → 2024 acquisition → 2026 MRC convergence) genuinely supports it. Individual artifacts usually do not.
4. **Declined CPOLs are the safest prescience evidence available** — a filing date cannot be retrofitted. Prefer them to narrative assertions.

---

## What NOT to sand off

Brenden's package has real weaknesses Bruce should not import. Bruce's PSE package is **better** than Brenden's on three dimensions, and those are the differentiators:

1. **Named conceptual frames.** "Fabrics and Planes," "Unified Forwarding Plane," "the host networking air-gap," "the 2030 guy," "SRv6 uSID as a network API." Brenden has no equivalent — his package describes projects, not ideas. Bruce names an idea, and the idea moves through the company. Keep every one of these.

2. **The prediction-that-came-true structure.** Brenden's package cannot say "I saw this three years early." Bruce's can, repeatedly, with dates: host networking (2013–2015) → Isovalent advocacy (2021) → acquisition (2024) → MRC+SRv6 convergence (2026). SDN-to-the-host, elephant flows, SONiC, pizzabox fabrics. **This is the strongest argument in the package and it has no analogue in the gold standard.** It should be visible in the Executive Overview and structurally reinforced by the timeline graphic in `todo.md`.

3. **Operator-peer credibility.** The David Lucey quote — *"In my twenty-five years in this business, I can count the number of vendor engineering reps that got it to that level on one hand"* — is a stronger form of validation than anything in Brenden's package, because it comes from outside Cisco. Prioritize customer and external LoRs in `08-sponsorship.md`.

---

## Tone: resolving "friendly and collaborative"

`todo.md` and `AGENTS.md` both specify a friendly, collaborative tone — "pioneering thought leader who is also exceptional to work with." Read literally, that instruction produces exactly the modest prose the package needs to avoid.

**Resolution: collaborativeness is a finding, not a register.**

The prose stays flat, declarative, third-person, and factual — Brenden's register throughout. Warmth is established by *what gets reported*, not by how sentences are phrased:

- 22 Connected Recognition awards **given** to others (`11-appendix.md`) — Bruce recognizing peers, unprompted, 22 times
- Mentee outcomes with names and dates: Nacho promoted to PSE (Jun 2026), Christopher Luciano in progress, five extended-team PSE promotions 2023–2024
- Three years as a voting member of the PSE Review Committee
- Verbatim collaborator quotes — Brian Shoda's *"I cannot find anyone who is more collaborative, always willing to give credit to others"* is worth more than any adjective Bruce could apply to himself
- Peer-authored LoRs from the DSE community (target >50%)
- The `srv6-labs` / `segmentrouting` repos and GitHub-based CL lab guides: work built for other people to use

The StandOut profile (`about-me/standout-report.md`) independently corroborates this — **Pioneer + Provider**, characterized as *"when you lead the charge, nobody gets left behind"* and the *"classic servant leader profile."* That is the exact combination the package needs to demonstrate: horizon-3 pioneer **and** force multiplier. It is worth one sentence in Personal Development or the Becoming-a-DSE statement.

Note the profile's own warning, which is the modesty problem restated in different language: *"You may not be able to make the tough call for yourself, but so long as the 'ask' is for someone else, you are quite courageous."* Compare the Bob Gisiger recommendation letter in `about-me/writing-style.md` — clear, confident, unhedged advocacy — against the Letter from the Candidate. Same author, very different force.

**Drafting instrument:** when a sentence about Bruce feels overstated, rewrite it as though advocating for a colleague with an identical record. That version is almost always the accurate one.

---

## Voice checklist (apply per section)

- [ ] Does every case study open with customer stakes in ≤2 sentences (rank, scale, revenue)?
- [ ] Is Bruce the grammatical subject of every sentence describing his work?
- [ ] Zero instances of: helped, contributed to, was part of, was involved in, assisted, played a role in
- [ ] Are all four impact types labeled (Financial / Competitive / Strategic / Customer)?
- [ ] Does the claim precede the supporting quote, never follow it as its first statement?
- [ ] Are `[verify]` marks on **numbers only**, never softening the surrounding claim?
- [ ] Is every date range explicit, and every entry post–Aug 2020 (per AGENTS.md)?
- [ ] Are setbacks reported in the same flat voice as wins?
- [ ] Third person throughout, except the Becoming-a-DSE statement?
