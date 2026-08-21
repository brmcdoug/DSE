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

---

## Global Impact — theater-scope correction (Aug 19, 2026, v1)

Bruce's review caught something the previous drafting pass missed: several "Global Initiatives" entries were ASP+Web or Business Impact content relabeled as global, rather than genuine cross-geography reach. Produced as `03-global-impact-v1.md`.

- [x] **Cut "Building the Web segment's technical foundation"** — this is literally the assigned theater, not outside it, and duplicates Business Impact's "Beyond bookings" paragraph verbatim. No content lost; it already has a proper home.
- [x] **Cut "Architectures adopted globally — open NOS and SONiC"** — the described activity (PA/DA SONiC forum, Tapaskar/Veerachamy relationships) is ASP/Web field advocacy, not global reach. Already covered properly in Span of Influence and Innovation. Could return as a genuine one-line Global Impact entry once a real global SONiC run-rate figure exists.
- [x] **Cut "Architecture that outlives the engagement" (SL-API)** — three named ASP+Web accounts (Microsoft, Meta, Google), no geography crossed. Pure Business Impact content, already told there in full.
- [x] **Tightened "End-to-end SRv6"** to lead with the actual global markers (four continents, six product lines/five business entities) instead of restating Innovation/Industry Impact detail.
- [x] **Shortened "Isovalent and Cilium evangelism"** per Bruce's instruction.
- [ ] **Open categorization question, not resolved:** the Isovalent/Cilium entry's "global" claim rests on cross-business-entity breadth (Bell, Boost, Adobe, Digital Realty, NSight, T-Mobile — all Americas accounts), not cross-geography. That's Span of Influence's axis, not Global Impact's. Decide whether this entry belongs here at all, or should move to Span with only a cross-reference left in Global Impact.
- [x] **Strengthened "SRv6 with SGT"** to lead with cross-vertical reach (enterprise, public sector, not just SP).
- [x] **Reframed WWT entry** as a collaboration with Dave Clough building WWT's own bench, not a one-off workshop.
- [x] **Rewrote the Run Rate section intro** in a positive, achievement-oriented frame (Bruce pushing the technologies forward, at global scale) rather than the defensive "does not own / does not claim" framing.
- [ ] **New:** find NaaS citations outside North America — the entry currently has one (Rakuten, Japan) but could use more
- [ ] **New:** find non-North America citations of large-scale pizza-box/fixed-form-factor fabric adoption for the Chassis-to-Pizzabox entry's pending marker

---

---

## Span of Influence — scope check against AGENTS.md (Aug 19, 2026, v1)

Checked the section against its own criteria in `AGENTS.md` (altitude + breadth across ≥2 domains, horizon 2–3; explicitly not revenue tables, external reach, or patent/product detail). Produced as `04-span-of-influence-v1.md`.

- [x] **Cut the duplicate "Global field lead, SR-Apps" row** — near-verbatim copy of Global Impact's SR-Apps entry, and redundant within this same file with the "SR brain trust field lead" row just above it (both cover Filsfils' org, Jalapeno, hyperscale SRv6). `AGENTS.md`'s own SR-Apps worked example calls for *different facets* in each section, not the same text twice — SR-Apps' Span-of-Influence angle (co-development altitude with Filsfils' org) is already carried by "SR brain trust field lead."
- [x] **Everything else checked out** — the four technology domains, the "how he thinks about it" framing, the executive/Fellow relationships, and the peer network are all genuinely altitude-and-breadth material, not revenue or external-reach content mislabeled. No further miscategorization found.
- [ ] **New:** find citations of the Isovalent/Cilium evangelism reaching outside Bruce's own theater — flagged in the Global Impact pass (Aug 19, 2026) as resting entirely on cross-BU breadth rather than geography; left in Global Impact for now per Bruce's decision, but citations outside-theater would strengthen it there or justify a fuller Span entry instead

---

---

## Span of Influence — second review pass (Aug 19, 2026, v2)

Bruce's own review surfaced a real overclaim and a substantial content gap. Produced as `04-span-of-influence-v2.md`.

- [x] **EVPN/Jeetu Patel corrected** — the draft said Bruce delivered the readout to the CPO directly. He co-prepared it with an informal PSE/DSE group; **Brook Crossman delivered it**; outcome was Jeetu committing to fix the issue with regular check-ins with Brook. Corrected in the Internal Influence table and removed the standalone (inaccurate) Jeetu Patel row from the relationships table.
- [ ] **Propagate the same EVPN/Jeetu correction to `01-exec-summary-draft.md`** (Span of Influence Summary) **and `10-se-community-leadership.md`** (Executive Presence table and Tiger Teams table) — both currently say or imply Bruce delivered the readout directly to Jeetu Patel.
- [x] **"How he thinks about it" rewritten** — the causal claim was wrong ("settles architecture on its merits") and has been replaced with Bruce's actual framing: deeply enmeshed in the industry's defining architectures for a decade, hence early and often right. Also now names the three co-founded tiger teams (SOSIE, UFA, UPM) explicitly and adds the in-progress SmartNIC/scale-up Ethernet advocacy.
- [x] **UPM formally named** — the "Policy Plane" entry is now framed as the co-founded Unified Policy Model tiger team.
- [ ] **Naming reconciliation needed:** `07-innovation.md` and `10-se-community-leadership.md` still use "Policy Plane" as the name for this work, not "Unified Policy Model (UPM)." Decide whether to rename throughout for consistency, or treat "Policy Plane" as the internal/informal name and UPM as the tiger-team's formal name (in which case both can coexist, but should say so explicitly wherever both appear).
- [x] **Added a Customer and Partner Relationships table** — this file previously had zero external relationships despite the criterion explicitly asking for "internally *and externally* with customers and partners." Added Microsoft (Nanduri, Thareja), Oracle (Jouhari), CoreWeave (Shiv Patel), Verizon (Jalil — Fellow, Mishra — Associate Fellow, Morris), Dish/Boost (McNamara), and WWT (Clough), from Bruce's own notes.
- [x] **Expanded the executive relationships table** with more precise/senior titles from Bruce's notes (Wollenweber, Tapaskar) and added Rakesh Chopra, Gurudatt Shenoy, Samir Parikh, and Craig Connors — the latter two marked explicitly as *developing* relationships, not established ones.
- [x] **Added a Sales Leadership Relationships table** — Marcus Moffett, Mike Witzman, Brad Bonin.
- [ ] **New Sponsorship candidates surfaced, not yet added to `08-sponsorship.md`:** Mohan Nanduri, Gaurav Thareja, Abderrahman Jouhari, Mike McNamara, Rakesh Chopra, Gurudatt Shenoy, Samir Parikh, Craig Connors, Marcus Moffett, Mike Witzman, Brad Bonin. Several overlap with names already in `08`'s solicitation tracker under different titles — reconcile before adding.
- [ ] **SmartNIC / scale-up Ethernet advocacy is work in progress** — no outcome to report yet. Revisit once there's a product or roadmap commitment to point to.
- [ ] **Samir Parikh and Craig Connors relationships are early-stage** — revisit the "developing relationship" framing as they mature; don't let it calcify into an overclaim later.

---

---

## Span of Influence — third review pass (Aug 19, 2026, v3)

Produced as `04-span-of-influence-v3.md`. This pass was mostly precision and framing fixes rather than structural ones — the section is close to final per Bruce.

- [x] **Conway's Law framing corrected** — the old version claimed "like every large vendor's," which is factually wrong; Arista, Juniper, and Nokia actively exploit Cisco's siloed structure with a unified-architecture pitch. Reframed to name that competitive reality directly rather than softening it into a generic industry statement.
- [x] **SOSIE renamed to Single-Secure-OS (SSOS)** throughout this file.
- [ ] **Propagate the SOSIE → SSOS rename package-wide** — `01-exec-summary-draft.md`, `07-innovation.md`, `09-personal-development.md`, and `10-se-community-leadership.md` all still say "SOSIE."
- [x] **"Host-networking air-gap" removed from this file** — Bruce coined the term and wants it mentioned once, likely in the Executive Overview, and referred to as plain "host networking" everywhere else.
- [ ] **Propagate the air-gap wording fix package-wide** — confirm/add the single canonical mention (with attribution) in `01-exec-summary-draft.md`, and sweep `03-global-impact-v1.md` (still has "coined the term Cisco's host-networking air-gap"), `07-innovation.md`, `09-personal-development.md`, and `10-se-community-leadership.md` for the same phrase, replacing with plain "host networking."
- [x] **UPM entry reframed** around "Cisco's identity architecture has been fragmented," with SRv6's scale/extensibility positioned as the bonus UPM ties into, per Bruce's framing.
- [x] **"First inventor position" question answered, not just resolved** — see cover note above; kept the claim but made the reasoning explicit (inventor order reflects conception credit) rather than just asserting it matters.
- [x] **Cross-Domain Broker/Beesely reference dropped** from the NaaS/Yukon entry — produced no outcome.
- [x] **Executive-interlocks overclaim fixed** — "owned" → "co-owns," naming Tyler Nielson, Rob Murphy, and Masi Mohammed as co-owners.
- [ ] **New:** Bruce to confirm the corporate-development advisory outcome with Ryan Houska and Vladimirs Sazonovs.
- [x] **PSE review subcommittee softened** — "shaping the promotion standard" (implies authored/changed it) → "evaluating candidates against the promotion standard" (voting member applying it).
- [x] **Cross-Organization Peer Network corrected** — removed Rob Murphy and Josh Merrill, both same-org (ASP/Web) as Bruce, which undercut the table's own "cross-organization" claim. Their contributions are still captured correctly in the Internal Influence table entries (SSOS, UPM) where they were already named. Added Brian Shlisky and Jeffry Handel, both genuinely cross-org (DSE, outside ASP/Web).
- [x] **Signature Themes renumbered 1–6** (source had a numbering duplicate) and de-branded #1 to plain "Host networking" per the air-gap decision above.
- [ ] **Flag, not yet resolved:** the Eric Knipp / John Dorval / Patrick Morrissey ">$1B" sales-VP row was present in the pre-v2 draft and is now missing — it was dropped during the v2 restructuring into three separate relationship tables, not deliberately cut. Confirm whether that was intentional or should be restored (it was already marked `[verify attributable by name]` before it disappeared).

---

---

## Executive Overview — Four Big Rocks frame added (Aug 19, 2026, v1)

Bruce's own synthesis: four architectural campaigns (not five — cut the silicon-cadence idea as engineering execution, not company redirection) that describe what his Span of Influence and Innovation work actually adds up to. Added as a new section in `01-exec-summary-draft-v1.md`, positioned right after "The Case in Brief" and before Career Path, so it functions as the master frame for the rest of the document.

**The four rocks:** (1) Unified NOS — SSOS tiger team, SONiC as proof of concept, not the whole scope; (2) Unified Forwarding Architecture (UFA) — SRv6 end to end; (3) Unified Policy Model (UPM) — SRv6+SGT, one identity/policy model; (4) Closing the host-networking air-gap — Isovalent/Cilium as the first move, SmartNIC and scale-up Ethernet advocacy to complete it.

- [x] **Synced three stale references while in this file** (all previously flagged): Candidate Portrait's topological-reasoning paragraph (removed the "like every large vendor's" inaccuracy, added the Arista/Juniper/Nokia competitive framing, matching Span v3), Span of Influence Summary paragraph (SOSIE → SSOS, added UFA/UPM by name, corrected the EVPN/Jeetu Patel attribution to match the Business/Span correction, corrected "owned" → "co-owns" the roadmap with named co-owners), Personal Development Summary (SOSIE → SSOS).
- [x] **Consolidated "host-networking air-gap" to a single mention** — it now appears once, in Rock 4, with the coining attribution. The Quantified Highlights table's reference was rewritten to point to Rock 4 instead of repeating the branded term.
- [ ] **Not yet done, flagged for next passes:** restructure `04-span-of-influence.md` itself explicitly around the Four Big Rocks (three of the four already exist there as tiger teams — this would make the connection explicit rather than implicit); light-touch tagging in `07-innovation.md` noting which patents/products serve which rock; decide whether Rock 4's "SmartNIC and scale-up Ethernet" advocacy should also get a one-line mention in Business Impact's "Cisco arrived late on 12.8T/25.6T/51.2T" passages, since that's the retrospective evidence the *urgency* of Rock 4 rests on even though the formal advocacy itself isn't part of the four-rocks frame.
- [ ] **Confirm the SOSIE → SSOS and air-gap-wording sweep is now fully done in `01`** — still outstanding in `07-innovation.md`, `09-personal-development.md`, and `10-se-community-leadership.md` per the last tracker entry.

---

---

## Executive Overview — fourth pass (Aug 19, 2026, v2)

Produced as `01-exec-summary-draft-v2.md`.

- [x] **Reframed the "unusual record" opening** — the previous version led with "a significant share was earned without Bruce in the room," which understated how genuinely customer-facing he is. Now leads with both truths: he's deeply customer-facing and enjoys it, *and* he's a force multiplier whose tools and knowledge transfer produces wins he's not present for. The Meta example now illustrates the second mode rather than standing in for the whole record.
- [x] **Big Rocks closing paragraph rewritten** — the old framing ("persuading business entities Bruce does not belong to... no organizational authority") was wrong on the facts: Bruce is in sales and doesn't belong to any BE. Corrected to the real story: building relationships outside his traditional MIG alignment, and — the stronger point — that he already assumed DSE-level scope and authority before having the title, which is literally what the promotion standard asks for.
- [x] **Candidate Portrait tightened**: "why his positions survive customer scrutiny" → "why he is so credible with the most technologically sophisticated customers in the world"; "rare" → **"unique"**.
- [x] **Career Path date corrected** — Mayor Pro Tem was a fixed 2020–2021 term, not open-ended "since January 2020."
- [ ] **Propagate the Mayor Pro Tem date correction** — `10-se-community-leadership.md` and any other file citing "Mayor Pro Tem since January 2020" or similar open-ended phrasing need the same fix (it's a two-year term, not an ongoing role).
- [ ] **Quantified Highlights table not yet updated** — Bruce is still reviewing Business Impact (through Oracle as of this pass) and asked for a full revenue/major-item review before this table gets touched. Holding until that review is complete rather than updating piecemeal.
- [ ] **Flag, not resolved:** Rock 1 now says "Cisco 8000" (Bruce's edit) while the Quantified Highlights table two sections later still says "Cisco 8122" specifically, as do `05`, `06`, and `07`. These may both be correct at different levels of precision (8000 is the platform family, 8122 the specific box) — confirm whether that's intentional or whether one should change to match the other.

---

---

## Business Impact — first review pass, through Microsoft (Aug 19, 2026, v1)

Bruce's review is in progress and has reached Oracle; produced as `06-business-impact-v1.md`. Only the top framing and the Microsoft entry were edited — Meta through the Vault Harvest Log are carried forward unchanged pending his continued review.

- [x] **Same customer-facing reframe as the Executive Overview** applied to the top-of-section framing paragraph — Bruce is genuinely customer-facing, and is also a force multiplier; the two aren't in tension.
- [x] **srv6-msft repo accuracy fix** — the repo is private, shared only with Microsoft architects, not public like srv6-mrc-emulator. The body previously implied both were "published," and the private one was hyperlinked as if publicly accessible. Corrected, and answered Bruce's question directly: yes, a screenshot in the DSE OneDrive evidence folder is the right move since a reviewer can't reach a private repo — added as an action item.
- [x] **New evidence added:** the "9-POCs-at-once" recognition on the global PSE/DSE call, crediting Bruce's agent-assisted development speed — folded into the dRH bullet it was attached to.
- [x] **Microsoft platform naming generalized** from "Cisco 8122 (G200 51.2T ASIC)" to "Cisco 8000 platforms (G-series and P-series silicon)" throughout the Microsoft entry, and trimmed the redundancy between the last bullet and the paragraph announcing the June 2026 release.
- [x] **Cisco 8000 vs 8122 — now resolved**, at least for Microsoft: Bruce's own instruction settles the ambiguity flagged in the last Exec Overview pass. **Propagate this generalization**: `01-exec-summary-draft-v2.md`'s Quantified Highlights table, `05-industry-impact.md`, `07-innovation.md`, and the Summary Table at the bottom of this same file (already fixed there) all still say "8122" in places — sweep for consistency once Bruce confirms this should apply package-wide and not just to Microsoft.
- [x] **Microsoft WAN revenue updated** with Bruce's precise figure — Cisco 8000 WAN revenue has totaled $306.4M since 2021 (previously only the FY25/FY26 individual-year figures were shown). Applied to the italic scope line, the "1.6T WAN backbone and SWAN" paragraph, and the Financial Impact line.
- [ ] **New precise figures provided, not yet integrated into body text (see the bracketed note at the bottom of the Revenue Summary table for exact numbers):**
  - Meta Silicon One since 2021: $178,275,649.89
  - Meta Cisco 8000 since 2021: $579,891,328.84 — **Bruce is separating DC from WAN/Metro and will not claim credit for the DC portion**; hold until that split is done
  - Microsoft AI/DC Cisco 8000 since 2021: $1,743,557,527.06 — **Bruce to confirm his attributable contribution with the account team** before this is stated as his scope (vs. the current ~$2.0B placeholder)
- [ ] **Reconciliation flag:** the Microsoft entry's italic scope line still says "~$500M WAN" as a placeholder estimate, sitting right next to the new, more precise "$306.4M since 2021" actual figure — these aren't the same thing (estimate vs. actual) and should be reconciled once Bruce is ready, rather than left as two different numbers for the same claim.
- [ ] **Not yet reached:** Meta, Oracle, CoreWeave, Bell, Google, AWS, Verizon, Akamai, all Additional/Out-of-Territory entries, the Summary Table, and the Vault Harvest Log are unchanged from the prior draft. Continue the review from Oracle onward next pass.

---

---

## Executive Overview — diff/reconciliation pass (Aug 19, 2026, v3)

Bruce flagged that a direct-edit pass may not have been fully captured in v2 — confirmed, and re-diffed the whole file line by line against his pasted version rather than re-scanning for `//` comments only. Produced as `01-exec-summary-draft-v3.md`.

- [x] **Missed edit found and applied:** the "Identify new technology and industry trends" row — Bruce had replaced "Contested Amazon's published flat-fabric architecture in 2026" with the 2021 Cilium/eBPF recognition and Isovalent advocacy. v2 still had the old sentence; this was a genuine miss, not a judgment call.
- [x] **Two internal inconsistencies found and fixed (not Bruce edits — my own incomplete propagation):** Span of Influence Summary's "Four technology domains" sentence still said "the Policy Plane" instead of "the Unified Policy Model," and the Leadership Summary bullet still said "Mayor Pro Tem since 2020" instead of the corrected 2020–2021 term fixed elsewhere in the same file.
- [ ] **Flagged, not changed:** the Span of Influence Summary paragraph ("None of that influence came with authority attached...") uses the same framing Bruce corrected in the Big Rocks closing paragraph last pass, but this specific occurrence wasn't commented on this round. Confirm whether it should get the same treatment for tone consistency, since it now reads differently from the paragraph just above it.
- [x] **Confirmed no other misses** — diffed Global Impact, Industry Impact, Business Impact, Innovation, Personal Development, Becoming a DSE, Direct Leader, and Sponsorship summaries word-for-word against the pasted version; all matched v2 exactly.

---

---

## Executive Overview — targeted comment pass (Aug 19, 2026, v4)

Bruce's instruction this round was explicit: touch only paragraphs with a `//` comment, preserve everything else exactly as pasted (including his own direct edits made without comments — the Five domains update, the Leadership bullet rewrites, dropping "Octans" from Microsoft's row, etc.). Produced as `01-exec-summary-draft-v4.md`.

- [x] **"Two things about how he works" paragraph 1** — de-heavied per Bruce's note; now leads with "Bruce loves working directly with customers" rather than framing the force-multiplier pattern as the headline fact.
- [x] **Big Rocks closing paragraph** — replaced "he assumed the scope and the authority a DSE is expected to carry" with lighter language ("took the initiative," "collaborating with peers... to build each into a real, ongoing effort").
- [ ] **Open question, not resolved:** Bruce deleted the SD-WAN patent sentence (12,120,027) from the Span of Influence Summary and noted he was lead author/filer on it — meaning it may be a weaker "outside-BU credited him" example than patent **12009998** (*Core Network Support for Application-Requested Network Service Level Objectives*, filed by SD-WAN engineering with Praharaj as lead per `07-innovation.md`'s filer note), which he offered as an alternative if a patent citation is wanted here. Left the sentence out entirely for now, per the letter of his edit — confirm whether either patent should be reintroduced in this summary paragraph, and whether the "first inventor position" claim on 12,120,027 in `04-span-of-influence.md` and `07-innovation.md` needs a second look given he says he was lead author on it (that actually *supports* the "he originated it" reading, but worth him confirming the framing still lands the way he wants there).
- [x] **Standards-body paragraph deleted** from Industry Impact Summary, per Bruce's note that he'd already asked for this and it may not have been carried through.
- [x] **"Beyond bookings" paragraph reframed** — "He does not claim the revenue" replaced with Bruce's suggested positive framing (Cisco's Web revenue growth, Bruce built the foundation).
- [x] **"Stated plainly" paragraph reframed** — confirmed Bruce's read of the intent (the revenue is real and could be larger with better silicon timing) and rewrote the opening to say that directly instead of the unexplained "Stated plainly:" lead-in.
- [x] **Innovation Summary opener rewritten** — "operator empathy rather than product strategy" (which didn't reflect how Bruce describes his own process) replaced with "mental connections and insights he reaches before others do."
- [x] **Personal Development's "Two development areas" paragraph deleted**, per Bruce's request.

---

---

## Executive Overview — fifth pass (Aug 19, 2026, v5)

Produced as `01-exec-summary-draft-v5.md`. All of Bruce's uncommented direct edits carried forward verbatim (date changes to 2016, the Rock 1/2/3/4 trims and additions, the rewritten Global Impact and Industry Impact paragraphs, the Becoming a DSE rewrite, etc.) — one silent typo fix only ("Telsta" → "Telstra").

- [x] **Candidate Portrait's "how he thinks about it" paragraph cut** — this was a genuine judgment call, not a comment resolution. It substantially restated ground the Big Rocks section now covers in more detail with the tiger teams named explicitly; keeping both meant hitting the same point twice in quick succession. Cut rather than trimmed.
- [x] **"Carry his architecture" clarified** in Industry Impact Summary — now explicitly states operators presenting ideas/concepts Bruce heavily influenced at major conferences as their own, per his clarifying question.
- [x] **Business Impact intro replaced** — Bruce asked for a suggested alternative or a cut; wrote a new opener leading with the actual numbers ($10.9B / $5.3B) instead of an abstract "pattern" statement. Worth Bruce's own read since I made a specific creative call here rather than just following an instruction.
- [x] **Becoming a DSE closing reframed around "force multiplier"** — replaced the "most satisfying" framing with an explicit force-multiplier statement carrying the same underlying content (account teams, SEs, operators), tying back to the DSE criteria's own language used throughout the package.

---

---

## Span of Influence — fourth pass (Aug 19, 2026, v4)

Produced as `04-span-of-influence-v4.md`.

- [ ] **Version-drift flag for Bruce:** this pass's pasted document had reverted to a pre-v3 state on several points already fixed in v3 — the "like every large vendor's" line, the FY26 roadmap "owned" vs "co-owns" wording, "shaping the promotion standard," Rob Murphy/Josh Merrill still on the Cross-Org peer table, the air-gap wording rule, and "SOSIE" surviving in the transition table and Signature Themes even though the rest of that same document correctly said "SSOS." All reapplied in v4. Worth checking which local copy is the working one before the next round, so fixes don't keep getting lost.
- [x] **Conway's Law / "like every large vendor's" refixed** — same correction as v3 (removed the inaccurate claim, named Arista/Juniper/Nokia's exploitation, softened the framing so it doesn't read as blaming current Cisco execs for an inherited structure).
- [x] **New todo, per Bruce's request:** flagging that the Executive Overview restates significant Span of Influence detail (the Isovalent/Cilium paragraph is the clearest example) — this points to the Exec Overview needing a tightening pass for brevity once the body sections are more settled, rather than Span needing to change. **Action:** revisit `01-exec-summary-draft-v5.md` for a length/redundancy pass once more sections are stable.
- [x] **"First-named inventor" claim on patent 12,120,027 confirmed incorrect by Bruce** — removed the ordinal claim from this file (now just "a named inventor... filed by SD-WAN engineering, a business entity he does not belong to," no "first" and no "reflects conception" reasoning). **New: audit `07-innovation.md`'s patents table and prose for the same claim** — the table's co-inventor listing doesn't explicitly say "first" but check the actual inventor order is represented accurately. Confirmed already absent from `01-exec-summary-draft` (removed in an earlier pass and not reintroduced).
- [x] **UPM/SGT entry** — Bruce's own edits preserved (Josh Merrill named as UPM co-founder, Verizon/AT&T/T-Mobile mindshare-building outcome replacing the narrower Verizon-only sentence); fixed a duplicate "the the" typo.
- [x] **Executive interlocks "owned" → "co-owns"** — refixed (see version-drift note above).
- [x] **PSE review subcommittee "oversell" wording refixed** — refixed (see version-drift note above).
- [x] **Cross-Org Peer Network — Rob Murphy and Josh Merrill removed again** (same-org as Bruce, undercuts the table's cross-org claim; see version-drift note).
- [x] **Air-gap wording refixed** in Signature Themes / new Four Rocks section (see version-drift note); also silently corrected "SOSIE" → "SSOS" in the transition table and theme list for internal consistency, since the rest of the document already used SSOS correctly.
- [x] **"Signature Internal Influence Themes" replaced with "The Four Rocks, from the Inside"** — collapsed from 5 items to 4, aligned names and order exactly with the Executive Overview's Four Big Rocks, and compressed each to a single outcome line rather than a full paragraph, since the full explanation now lives in the Exec Overview and doesn't need restating here.

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
