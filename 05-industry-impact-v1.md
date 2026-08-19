## Industry Impact

## Industry Impact Arc

Bruce's external work rests on three positions he has carried publicly since before the industry agreed with them: the network's control point has moved to the host, so Cisco's presence there is a must; investing in open source — for NOS, tooling, and automation — earns industry credibility that drives product revenue, often faster than closed development does; and Segment Routing v6 gives an operator a platform for its own service innovation rather than a vendor feature catalogue. He presented that last argument directly to the Americas SP organization as *Combatting Disaggregation with Network Service Innovation (SRv6)* at the TMC Innovation Hour (Sep 2025, repeated by request Dec 2025).

The criterion asks specifically about standards-body leadership, and Bruce holds that credential — editor of the `draft-srv6ops-addressing-guidelines` IETF draft, an IETF SRv6-Ops contributor, and an editor of four chapters of the book "Segment Routing Part III: SRv6" (Filsfils, et al). But the MRC timeline shows where the industry's weight actually sits: MRC work began in 2024 among OpenAI, AMD, Broadcom, and Intel; SRv6 for the AI backend was discussed publicly at **OCP in November 2024**; the first IETF draft did not appear until **July 2025** — roughly eight months after the open forums had already set the direction. Bruce operates in all three venues — standards, open source, open hardware — and the balance of his record follows the industry's, not the reverse.

---

## 1. Standards and Publications

### IETF and Standards-Adjacent Work — 2020 – Present

| Contribution                            | Date     | Role and significance                                                                                                                   |
| ---------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **draft-srv6ops-addressing-guidelines** | Jun 2025 | **Editor** — Bruce's most formal standards role; sets SRv6 addressing guidance the operator community works from                          |
| **IETF SRv6-Ops**                        | Oct 2025 | Presented host-based SRv6 operator requirements to the working group with Verizon's Nick — strategic impact: shapes the requirements Cisco engineering builds to |
| **SRv6 book**, chapters 12–14            | 2024     | Editor and contributor on Service Programming and SR-Aware/Unaware Services, with Filsfils' team; includes the Verizon SRv6 DC case study (Dec 2023) |
| **IETF Vancouver**                       | 2024     | Ianik Semko: *"I call you the 2030 guys"* — external, unsolicited recognition of the host-based SRv6 position from a standards peer        |
| **NANOG**                                | 2020     | First public presentation of SRv6 uSID *(pre-PSE; exec thru-narrative only)*                                                               |

### Publications — 2021 – 2026

Bruce published the **[first public description and demonstration of SRv6 uSID on SONiC](https://www.segment-routing.net/blogs/srv6-usid-on-sonic/)** (segment-routing.net, May 2023) — the industry's first SRv6-on-open-NOS narrative, and the reference point the later multi-vendor uSID conversation built from. His May 2022 SP360 post introduced **cloud-like consumption of network services**, framing that predated the network-as-a-service movement the SP industry adopted in 2024–2025 by two to three years — a strategy claim, not a revenue one, since NaaS deals route to Business Impact where they land. *(Phoenix Wing note: the multi-vendor SRv6-uSID-on-SONiC push is Alibaba-led; Bruce is not on Alibaba's account team, but his May 2023 publication preceded it and the Cisco-side engineering validation the cross-vendor narrative rests on is his.)*

---

## 2. SRv6 for AI and the MRC Convergence

Multipath Reliable Connection is an open industry specification born from a need OpenAI identified in late 2023, convening AMD, Broadcom, and Intel to solve it. Bruce is not an author of MRC, and the package does not claim otherwise. Its relevance to his record is convergence, not authorship, on two points. First, OpenAI convened **NIC and silicon vendors, not switch vendors** — external confirmation that the industry moved the control point to the host, exactly where Bruce had been arguing it belonged since 2013 and had named the *host-networking air-gap* since 2021. Second, **MRC adopted SRv6 as its path mechanism**, and Oracle's 2026 Acceleron materials cite the same pattern — the architecture Bruce spent five years advocating to hyperscalers became the transport substrate of the industry's AI networking standard.

Bruce made the combined architecture teachable rather than merely correct: he built the **[srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator)** so operators could model MRC-with-SRv6 directly, and opened the SRv6-for-AI-backend conversation at **OCP Summit (Oct 2024)** with Oracle, Microsoft, Voltage Park, Bell, and Cloudflare — the first public customer discussion of the architecture. An OCP Summit 2026 session on SRv6 uSID multi-tenancy, co-presented with Microsoft, extends it to network/host/hybrid encapsulation and two-dimensional ACLs `[verify delivery]`. Strategic impact: this is the arc the **2025 Pinnacle Award** recognized at company level — a roughly 40-person team, almost entirely engineering, of whom Bruce was one of two from sales (detail in Innovation). Bob Gisiger, May 2026: *"this is super cool, it's your vision for years of host based SRv6 coming to life in a big way."*

**References:** [OpenAI — Resilient AI Supercomputer Networking using MRC and SRv6](https://cdn.openai.com/pdf/resilient-ai-supercomputer-networking-using-mrc-and-srv6.pdf) · [Broadcom — MRC: The Journey from Concept to Open Specification](https://www.broadcom.com/company/news/articles/ai-infrastructure/mrc-the-journey-from-concept-to-open-specification) · [Cisco — MRC and SRv6](https://blogs.cisco.com/datacenter/mrc-and-srv6-how-foundational-networking-innovations-are-enabling-the-next-generation-of-ai-supercomputers)

---

## 3. Open Source

Bruce is **administrator and curator of [github.com/segmentrouting](https://github.com/segmentrouting)** and launched **[srv6-labs](https://github.com/segmentrouting/srv6-labs)** (Dec 2023) to remove a real adoption barrier: operators could not reproduce SRv6 scenarios without vendor-specific tooling, so evaluating the architecture meant trusting a vendor's demo instead of running it themselves. The labs reached **~40,000 LinkedIn views in the first week**, drew a citation from **[ipspace.net](https://blog.ipspace.net/2023/12/worth-reading-srv6-labs.html)**, and picked up contributions from engineers at **Verizon and Oracle**. The repository now stands at **74 stars, 15 forks** `[refresh for 2026]`. Companion repos — [srv6-msft](https://github.com/segmentrouting/srv6-msft), [srv6-oci](https://github.com/segmentrouting/srv6-oci), [srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator), [polarfly](https://github.com/segmentrouting/polarfly) — extend the same open method into hyperscaler co-development.

Bruce took **[cisco-open/jalapeno](https://github.com/cisco-open/jalapeno)** through Cisco Legal into public release; it now sits on independent industry maps such as the [Steinzi network automation landscape](https://steinzi.com/network-automation-landscape/), and its BMP demo was referenced for the MPLS World Congress 2026 community by Fred C and Severin Dellsperger. He owns and maintains the **[github.com/jalapeno](https://github.com/jalapeno)** organization (15+ repositories) built on top of it. Strategic impact: Jalapeno functions in the industry as a reference architecture for programmable multi-domain services, taught and demonstrated outside Cisco's own labs *(product/IP detail: Innovation)*.

The pattern repeats at Cisco Live. Bruce and Rob Murphy's **LTRSPG-2212** pioneered using GitHub itself as the lab guide and config store — now common ILT practice — and they declared the lab open source outright, so attendees could fork it and train their own colleagues with it. It carries **16 stars and 7 forks** from customers doing exactly that: [github.com/jalapeno/SRv6_dCloud_Lab](https://github.com/jalapeno/SRv6_dCloud_Lab).

---

## 4. Operator Community

Bruce's strongest form of industry influence is not Cisco presenting as a vendor — it is an **operator presenting architecture Bruce built, or co-built with them, as their own.** As he frames it, a customer making the case at an industry conference lands harder than the vendor making it.

The clearest example is **Dan Bernier, Senior Architect at Bell Canada.** The partnership started when Bruce's Jalapeno and host-based SR/SRv6 session at KubeCon (Nov 2019) drew Bernier in, and grew over years of onsite workshops into a shared vision for turning a traditional tier-1 operator into a cloud-like NaaS business. Bernier has since carried slides and concepts the two developed together into his own industry talks at **KubeCon (2022–2023)** and **MPLS World Congress (2023)** — Cisco's architecture reaching the industry through an operator's mouth rather than a vendor's.

| Year         | Bruce's role                                                                      | Outcome                                                                    |
| ------------ | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Apr 2023** | IPR, slides, diagrams featured in **Bell, Verizon, and Rakuten** presentations      | Three tier-1 operators independently delivered the same architecture `[confirm session titles]` |
| **Mar 2024** | **Editor and advisor**, Verizon's MPLS-WC SRv6 presentation, built on srv6-labs material | Tier-1 operator delivers Bruce's architecture on the main stage; open-source lab methodology carried into it |
| **Mar 2025** | Presented **SRv6 for the AI backend**; Kaliwoda booth demo; KPN consulting          | Global operator visibility on the AI fabric architecture                   |

Cisco SR engineering subsequently invited Bruce into the MPLS-WC lead-operators workshop alongside Microsoft and OCI peers (CLEU 2025). He also coordinated and hosted the **SRv6-for-AI workshop in San Jose (Apr 2025)** for Cisco MIG engineering and Web SE leadership, bringing in **Rita Hue** (SONiC Principal SWE Manager, Microsoft) and **Eddie Ruan** (Director, Network System Software, Alibaba Cloud) as guest speakers — convening two competitors' engineering leadership in front of Cisco's own product organization, so the customers made the case for the architecture more persuasively than Cisco could make it to itself. A December 2025 follow-up took the same audience into use cases against an actual roadmap.

---

## 5. Practitioner Education

Bruce was named **Distinguished Speaker at Cisco Live EMEA 2023** (5.00/5.00) and has held scores between 4.72 and 5.00 across CLEU and CLUS since, including *Beyond the Switchport* with Chris Lapp (CLUS 2026) and a CLUS 2025 lab built on an SRv6 PyTorch plugin he coded himself. Several sessions have been invited back on the strength of their scores alone — LTRSPG-2212 ran at CLEU in 2023, 2024, 2025, and 2026 — and two produced documented outcomes outside Cisco Live itself: a CLEU 2026 Meet-the-Expert conversation led the **Province of New Brunswick** to abandon its SR-MPLS plan for an immediate SRv6 migration (Global Impact), and **Boost Mobile** ran an SRv6 POC after CLUS 2025 (Business Impact). *(Full session log, scores, and ILT delivery mechanics: Leadership section.)*

He co-developed a **four-hour O'Reilly course**, *Open Source Labbing*, with **Russ White** — a collaboration that grew out of the FRR SRv6 L3VPN lab Bruce built for White during the Akamai engagement (Oct 2023), and independent validation of the reproducible-lab method he established with srv6-labs. Delivered live twice to hundreds of engineers worldwide; materials public at [github.com/brmcdoug/open-source-labbing](https://github.com/brmcdoug/open-source-labbing) `[verify catalog link/title]`.

Bruce also established an academic pipeline with **OST University, Zurich** (2020–2022): students built on Jalapeno as a development platform, producing an open-sourced API gateway (2021) and an SRv6 service-chaining demo app (2022) under his guidance. Student **Severin Dellsperger** went on to build **Hawkv6**, a distributed controller Cisco's EU CTO team (Bart Van De Velde, Andreas Enotiadis) has expressed interest in productizing — a research-to-field-validation pipeline, not a one-time guest lecture.

---

## Explicitly Excluded from This Section

| Item                                     | Route to                          |
| ----------------------------------------- | ---------------------------------- |
| Meta $17M, Microsoft pipeline $           | **06-business-impact.md**          |
| Geico, Adobe, Fiserv customer wins        | **03-global-impact.md**            |
| Isovalent acquisition internal advocacy   | **04-span-of-influence.md**        |
| CPOL / patent tables                      | **07-innovation.md**               |
| ILT prep, Stay Ready Friday, mentoring    | **10-se-community-leadership.md**  |
| PSE committee service                     | **04-span-of-influence.md**        |

---

## Open Items

- [ ] Refresh srv6-labs LinkedIn and GitHub metrics for 2026
- [ ] Confirm OCP 2026 session delivered (Microsoft co-presentation)
- [ ] O'Reilly catalog link and exact course title for citation
- [ ] Confirm Bell/Verizon/Rakuten MPLS-WC 2023 session titles are quotable
- [ ] Confirm `draft-srv6ops-addressing-guidelines` status and co-editors
- [ ] Decide whether a compact "external artifacts" reference table belongs in the Appendix instead of here — cut from the body in this pass as the section's main source of repetition (GitHub stars, IETF role, Pinnacle Award, and CL score were each stated twice)
- [ ] Optional timeline graphic for final PDF

**Last body pass:** Aug 2026 — trimmed ~30% for length and redundancy; standards-vs-open-source framing kept as previously resolved (state the shift honestly rather than lead with standards to satisfy the letter of the criterion — flagged as a judgment call, see cover note).
