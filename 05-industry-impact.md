## Industry Impact

> **Scope ([AGENTS.md](./AGENTS.md)):** Leadership and visibility **outside Cisco** among operators, architects, open-source communities, and standards-adjacent forums since **August 1, 2020**. **Direct revenue not required.**  
> **Cross-ref:** Same artifact drove account $ → **06-business-impact.md** / **03-global-impact.md**. Internal BU persuasion → **04-span-of-influence.md**. Patents/CPOL detail → **07-innovation.md**. CL **ILT scores and SE training delivery** → **10-se-community-leadership.md**.

**Suggested package length:** ~3 pages weighted (README). Organized by industry theme; third person, most recent activity first. Voice and claim-strength rules: [voice-guide.md](./voice-guide.md).

---

## Industry Impact Arc

Bruce's external work follows one sustained argument, advanced publicly since before the market was ready for it: that the network's control point is moving to the host, that programmable source routing is how operators will reach it, and that open network operating systems are how they will run it. He has made that case in open-source repositories, operator conferences, standards drafts, and practitioner training — building artifacts that practitioners use independently of any Cisco account team.

| Era | Industry-facing theme | Representative artifacts |
| :--- | :--- | :--- |
| **2020–2022** | SRv6 uSID simplification; programmability as API | First public uSID presentation (NANOG); SR-Apps; Jalapeno open source; OST Zurich |
| **2023** | Reproducible SRv6 labs; SONiC uSID narrative | **srv6-labs** launch; first public SRv6-on-SONiC publication; MPLS-WC operator IPR |
| **2024–2025** | Host networking and eBPF; MRC industry alignment | Cisco Live Distinguished Speaker; OCP AI-backend kickoff; O'Reilly lab course; IETF draft editor |
| **2025–2026** | SRv6 for AI; multi-tenant fabrics; operator roadshow | **2025 Pinnacle Award**; MRC emulator; OCP 2026; MPLS-WC AI backend |

---

## 1. Open Source and the Reproducible Lab Ecosystem

### segmentrouting and srv6-labs — Dec 2023 – Present

SRv6 adoption stalled at a practical barrier: operators could not reproduce lab scenarios without vendor-specific tooling and opaque topologies, so evaluating the architecture required trusting a vendor's demonstration. Bruce is **administrator and curator of [github.com/segmentrouting](https://github.com/segmentrouting)** and launched **[srv6-labs](https://github.com/segmentrouting/srv6-labs)** in December 2023 — Containerlab topologies with starter and use-case labs that any engineer can run on a laptop.

External validation and reach:

- LinkedIn launch reached approximately **40,000 views in the first week**; the January 2024 snapshot recorded **37,822 views, 267 reactions, and 13 reposts** `[refresh for 2026]`
- Cited as "worth reading" by **[ipspace.net](https://blog.ipspace.net/2023/12/worth-reading-srv6-labs.html)**, one of the most respected independent networking publications
- Engineers at **Verizon** and **Oracle** extended and contributed to the labs
- February 2025 GitHub traffic: 333 views from 46 unique visitors, referred from segment-routing.net, Google, and ipspace

The companion repositories — [srv6-msft](https://github.com/segmentrouting/srv6-msft), [srv6-oci](https://github.com/segmentrouting/srv6-oci), [srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator), and [polarfly](https://github.com/segmentrouting/polarfly) — extend the same open method to hyperscaler co-development. The result is a shared lab vocabulary for SRv6 that belongs to the operator community rather than to any single vendor engagement.

---

### Jalapeno — Open-Source Network Automation — 2021 – Present

Bruce open-sourced **[cisco-open/jalapeno](https://github.com/cisco-open/jalapeno)** through Cisco Legal, taking a field-initiated project into public availability. It appears on independent industry automation landscape maps including the [Steinzi network automation landscape](https://steinzi.com/network-automation-landscape/), and the `jalapeno-bmp-demo` was referenced for the MPLS World Congress 2026 community by Fred C and Severin Dellsperger. Jalapeno functions in the industry as a reference architecture for programmable multi-domain services, used in teaching and community demonstrations rather than only Cisco labs.

*More details are located in the Innovation section of this document.*

---

## 2. SRv6 for AI and Convergence with MRC

### Multipath Reliable Connection — 2023 – 2026

Multipath Reliable Connection is an open industry specification. Per Broadcom's published account, *"The MRC journey began in late 2023, when the rapid emergence of large-scale AI clusters exposed the need for a new transport architecture... OpenAI brought together AMD, Broadcom, and Intel to explore a solution."* Bruce is not an author of that specification, and the package does not claim otherwise.

Its significance to Bruce's candidacy is convergence. Two facts matter:

**First, OpenAI convened NIC and silicon vendors — not switch vendors.** The industry's answer to AI-scale transport was built at the host and the network interface card, which is precisely the relocation of the control point Bruce had been arguing since 2013 and naming the *host-networking air-gap* since 2021. The composition of that founding group is external evidence for the thesis, independent of anything Cisco published.

**Second, MRC adopted SRv6 as its path mechanism.** The published specification uses SRv6 static routing for multipath, and Oracle's Acceleron materials (2026) cite the same pattern. The architecture Bruce had spent five years advocating to hyperscalers became the transport substrate of the industry's AI networking standard.

Bruce's public contribution is making the combined architecture teachable. He built the **[srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator)** so operators and architects could model MRC with SRv6 static routing directly, and opened the SRv6-for-AI-backend conversation at **OCP Summit in October 2024** with Oracle, Microsoft, Voltage Park, Bell, and Cloudflare — the first public customer discussions of the architecture. An **OCP Summit 2026** session abstract on SRv6 uSID multi-tenancy covers network, host, and hybrid encapsulation, two-dimensional ACLs, and multi-planar MRC extension, to be co-presented with Microsoft `[verify delivery]`.

**References:** [OpenAI — Resilient AI Supercomputer Networking using MRC and SRv6](https://cdn.openai.com/pdf/resilient-ai-supercomputer-networking-using-mrc-and-srv6.pdf); [Broadcom — MRC: The Journey from Concept to Open Specification](https://www.broadcom.com/company/news/articles/ai-infrastructure/mrc-the-journey-from-concept-to-open-specification); [Cisco — MRC and SRv6](https://blogs.cisco.com/datacenter/mrc-and-srv6-how-foundational-networking-innovations-are-enabling-the-next-generation-of-ai-supercomputers)

---

### Host-Based Networking as an Industry Narrative — 2020 – Present

Bruce named and evangelized the **host-networking air-gap** and **host-based SRv6** externally for years before the market moved. That framing now appears in the MRC specification's NIC-controlled paths, in Cilium and eBPF SRv6 community work, and in his Cisco Live session *Beyond the Switchport*, which traces the arc from kernel to CNI to eBPF to SmartNIC.

Bob Gisiger, May 2026: *"this is super cool, it's your vision for years of host based SRv6 coming to life in a big way…"*

The **2025 Pinnacle Award** for SRv6 uSID market impact recognized this arc at company level; detail in the Innovation section.

---

## 3. Standards and Publications

### IETF and Standards-Adjacent Work — 2020 – Present

| Contribution | Date | Role and significance |
| :--- | :--- | :--- |
| **draft-srv6ops-addressing-guidelines** | Jun 2025 | **Editor** — SRv6 addressing guidance for the operator community, the most formal standards role in Bruce's record |
| **SRv6 book** — chapters 12–14 | 2024 | **Editor and contributor** on Service Programming and SR-Aware/Unaware Services, with Clarence Filsfils' team; includes the Verizon SRv6 DC case study (Dec 2023) |
| **IETF SRv6-Ops** | Oct 2025 | Collaborated with Verizon's Nick on host-based SRv6 operator requirements presented to the working group |
| **IETF Vancouver** | 2024 | Ianik Semko: *"I call you the 2030 guys"* — external recognition of the host-based SRv6 and endpoint-service position |
| **NANOG** | 2020 | First public presentation of SRv6 uSID *(pre-PSE; exec thru-narrative)* |

### Publications — 2021 – 2026

Bruce published the **[first public description and demonstration of SRv6 uSID on SONiC](https://www.segment-routing.net/blogs/srv6-usid-on-sonic/)** (segment-routing.net, May 2023) — the first SRv6-for-data-center-on-SONiC narrative in the industry, and the reference point for the multi-vendor open-NOS uSID conversation that followed. He publishes regularly to segment-routing.net, Cisco SP360, and LinkedIn. His May 2022 SP360 post *Perspectives on the Future of Service Provider Networking: Evolved Connectivity* introduced the term **cloud-like consumption of network services** — framing that predated by two to three years the network-as-a-service movement that took hold across the service provider industry in 2024–2025.

*Phoenix Wing context:* the multi-vendor SRv6 uSID on SONiC initiative is Alibaba-led. Bruce is not on Alibaba account teams. He published the May 2023 description that preceded it and drove the Cisco-side engineering validation the cross-vendor narrative rests on.

---

## 4. Operator Community

### Operators Carrying the Architecture — 2019 – Present

Bruce's strongest form of industry influence is not Cisco presenting as a vendor — it is **operators presenting architecture Bruce developed, or co-developed with them, as their own**. As he puts it: for an architect working for a vendor, it is almost universally more impactful when a customer presents the idea at an industry conference than when the vendor does.

The clearest case is **Dan Bernier, Senior Architect at Bell Canada**. The partnership began when Bruce's Jalapeno and host-based SR/SRv6 session at KubeCon (Nov 2019) drew Bernier in, and developed over years of onsite workshops and bi-weekly sessions into a shared vision for turning a traditional tier-1 operator into a cloud-like network-as-a-service business. Bernier has since used slides and concepts Bruce developed — or that the two developed together — in his own industry presentations at **KubeCon (2022–2023)** and **MPLS World Congress (2023)**, evangelizing end-to-end SRv6 including host-based SRv6. Cisco's architecture reached the industry through the mouth of an operator rather than a vendor.

### MPLS World Congress — 2023 – 2025

| Year | Bruce's role | Industry outcome |
| :--- | :--- | :--- |
| **Apr 2023** | IPR, slides, and diagrams featured in **Bell, Verizon, and Rakuten** presentations | Three tier-1 operators independently delivering the same architecture `[confirm session titles]` |
| **Mar 2024** | **Editor and advisor** for Verizon's MPLS-WC SRv6 presentation | Tier-1 operator delivers Bruce's architecture on main stage |
| **Apr 2024** | Verizon presentation built on **srv6-labs** material | Open-source lab methodology carried into operator production narrative |
| **Mar 2025** | Presented **SRv6 for the AI backend**; Arkadiusz Kaliwoda booth demonstration; KPN consulting | Global operator visibility on AI fabric architecture |

Cisco SR engineering subsequently invited Bruce to join the MPLS-WC lead operators workshop alongside Microsoft and OCI peers (CLEU 2025).

### SRv6 Operator Roadshow — Dec 2025

Bruce built the SRv6 operator workshop program in Austin — deliberately structured at 50% customer and 50% Cisco content across hyperscale, enterprise, public sector, and service provider segments, with a companion SE enablement workshop covering platforms, gaps, objections, and competition. The design scales the SRv6 adoption narrative across operator segments rather than through individual account engagements.

---

## 5. Practitioner Education

### Cisco Live — Industry-Facing Sessions — 2023 – 2026

Bruce's Cisco Live work reaches global practitioners rather than Cisco field teams alone. He was named **Distinguished Speaker at Cisco Live EMEA 2023**, scoring **5.00 / 5.00**, and has sustained scores between 4.72 and 5.00 across CLEU and CLUS sessions since. Sessions with industry reach include LTRSPG-2212 (2023–2026), *Beyond the Switchport* with Chris Lapp (CLUS 2026), the BTSP panel (CLUS 2026, 5.0), and IBOSPG-2013 (CLUS 2025, 5.00). Following CLUS 2025 he coded a demonstration **SRv6 PyTorch plugin**, highlighted by Bob Gisiger in the November 2025 SRF session.

Two sessions produced documented external outcomes: a Meet-the-Expert conversation at CLEU 2026 led the Province of New Brunswick to abandon its SR-MPLS plan for an immediate SRv6 migration (Global Impact), and Boost Mobile ran an SRv6 POC after CLUS 2025 (Business Impact).

*Session preparation, ILT delivery mechanics, and full score tables are located in the SE Community Leadership section of this document.*

### O'Reilly — *Open Source Labbing* — 2024 – 2025

The collaboration began in Bruce's Akamai engagement: the FRR SRv6 L3VPN image and lab he built for Russ White (Oct 2023) led directly to this course. Bruce co-developed a **four-hour O'Reilly training course** with **Russ White** — author of some of the most influential IP networking books in the industry — covering Containerlab, FRR, SRv6, and open-source lab methodology. It was delivered live twice to hundreds of engineers worldwide, and both sessions are recorded in the O'Reilly catalog for subscribers. Course materials are public at [github.com/brmcdoug/open-source-labbing](https://github.com/brmcdoug/open-source-labbing). Co-authorship with Russ White — one of the industry's most recognized networking authors — is independent validation of the reproducible-lab method Bruce established with srv6-labs. `[verify catalog link/title]`

### Pour-Man's Networking Podcast — May 2022

Guest on the inaugural episode, providing early external visibility for the SRv6 and programmability narrative.

---

## Academic Partnership — OST Zurich, 2020 – 2022

Bruce established the collaboration with **OST Zurich**, open-sourcing the Jalapeno API gateway (2021) and producing an SRv6 service-chaining demonstration (2022). He advised master's thesis work with Professor Laurent Metzger; student Severin Dellsperger went on to build **Hawkv6**, a distributed controller application, with Bart Van De Velde and Andreas Enotiadis. The partnership operates as a pipeline from operator-relevant academic research into field architecture validation.

---

## Summary Table — External Artifacts

| Artifact | Type | Industry reach |
| :--- | :--- | :--- |
| [segmentrouting/srv6-labs](https://github.com/segmentrouting/srv6-labs) | Open source | ~40K first-week views; ipspace.net citation; Verizon and Oracle contributors |
| [SRv6 uSID on SONiC](https://www.segment-routing.net/blogs/srv6-usid-on-sonic/) | Publication | **First public SRv6-for-DC-on-SONiC description in the industry** |
| **draft-srv6ops-addressing-guidelines** | IETF draft | **Editor** |
| **SRv6 book**, chapters 12–14 | Publication | Editor/contributor with Cisco SR engineering |
| [cisco-open/jalapeno](https://github.com/cisco-open/jalapeno) | Open source | Independent automation landscape listings |
| [srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator) | Open source | MRC + SRv6 teaching implementation |
| MPLS-WC 2023–2025 | Conference | Bell, Verizon, and Rakuten delivered the architecture |
| OCP Summit 2024 / 2026 | Conference | Hyperscale AI fabric audience |
| Cisco Live EMEA 2023 | Recognition | **Distinguished Speaker**, 5.00 / 5.00 |
| [O'Reilly *Open Source Labbing*](https://github.com/brmcdoug/open-source-labbing) (with Russ White) | Training | O'Reilly catalog; delivered live twice |
| **2025 Pinnacle Award** | Recognition | SRv6 uSID global market impact |

---

## Explicitly Excluded from This Section

| Item | Route to |
| :--- | :--- |
| Meta $17M, Microsoft pipeline $ | **06-business-impact.md** |
| Geico, Adobe, Fiserv customer wins | **03-global-impact.md** |
| Isovalent acquisition internal advocacy | **04-span-of-influence.md** |
| CPOL / patent tables | **07-innovation.md** |
| ILT prep, Stay Ready Friday, mentoring | **10-se-community-leadership.md** |
| PSE committee service | **04-span-of-influence.md** |

---

## Open Items

- [ ] Refresh srv6-labs LinkedIn and GitHub metrics for 2026
- [ ] OCP 2024 confirmed dates/URLs; confirm OCP 2026 session delivered
- [ ] O'Reilly catalog link and exact course title for citation
- [ ] MPLS-WC 2023 session titles — confirm Bell/Verizon/Rakuten attribution is quotable
- [ ] Confirm `draft-srv6ops-addressing-guidelines` status and co-editors
- [ ] Optional timeline graphic for final PDF

**Last body pass:** Aug 2026 — rewritten to [voice-guide.md](./voice-guide.md) register; page target corrected to 3 (README weighting).
