# Executive Overview and General Information about Candidate

**Cisco Distinguished Solutions Engineer Nomination — Bruce McDougall** *August 2026. Finance-validated Web/Hyperscale segment bookings (2022–2026) integrated; account-level, SP, and product run-rate figures marked where pending.*

---

## The Case in Brief

The DSE criteria open with a general guideline that sits above every other category: *demonstrate how you have been a **force multiplier** throughout the organization — identifying new technology and industry trends, building the necessary field enablement, aligning strategic stakeholders and investment, and leading lighthouse customers to drive field adoption.*

That is a description of how Bruce McDougall works.

| The criterion                                    | Bruce's record                                                                                                                                                                                           |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Identify new technology and industry trends**  | Identified in 2015 that hyperscalers had moved the network's control point into the host — the gap Rock 4 below closes. Designed an elephant-flow balancer in 2017 for the problem the industry took up in 2024 as SRv6-for-AI. Called the SONiC inflection in 2023. Contested Amazon's published flat-fabric architecture in 2026. |
| **Build the necessary field enablement**         | `srv6-labs` (74 stars), `cisco-open/jalapeno` (78 stars), the MRC emulator built within a week of OpenAI's announcement, VXR and Containerlab environments, dCloud labs, and SRv6 training delivered across NA, EMEA, and APJC. |
| **Align strategic stakeholders and investment**  | The SONiC SRv6 investment case that reversed engineering scepticism and **shipped on the Cisco 8122 in June 2026**. The Cilium-SP case built from worldwide account data — **~$34M Isovalent / ~$323M MIG** pullthrough, finance-validated. Isovalent acquisition advocacy from 2021. The Cilium CRD **accepted by Cisco engineering**. |
| **Lead lighthouse customers and drive adoption** | Microsoft, Meta, Oracle, CoreWeave, and Bell Canada — the accounts where SRv6, SONiC, and host networking went from argument to production.                                                              |

Two things about that record are unusual enough to state plainly at the outset.

**A significant share of it was earned without Bruce in the room.** His most common mode is not customer-facing: he equips account systems engineers with the architecture, the education, the repositories, and the labs, and they carry it to their customers themselves. The **$17M Meta backbone re-entry** is the clearest case — Bruce pioneered the SL-API technique at Microsoft, taught it to the Meta account team, built the labs they validated it in, and **never presented to Meta himself.**

**And the industry moved to where he was standing.** Five years ago service provider and hyperscale operators largely dismissed SRv6 as not ready. Today SPs almost universally name it their strategic direction and most hyperscalers agree. Bruce has been at the centre of that conversation from the beginning — in Cisco's SR brain trust, in the operator community, in open source, and in the room when OpenAI's MRC specification adopted SRv6 as its path mechanism.
> *"Bruce continues to have a significant impact leading frontier projects in AI forwarding and teaching others. His innovation is on pace to break (ASP) records with patents being filed and awarded and he sets the standard for teamwork and technical depth. The recent recognition he received in the Pinnacle awards speaks to his technical capabilities and his strong reputation for teamwork. Cisco is lucky to have him teaching our teams and customers, representing us externally and driving innovation in the portfolio."* — **Brook Crossman**, VP Systems Engineering, ASP and Web — Bruce's direct leader for five years through June 2026
---

## Four Big Rocks: Repositioning Cisco for the Hyperscale and AI Era

Underneath the initiatives, tiger teams, and account wins in this package is a single throughline. Bruce is not pursuing four unrelated technical interests — he is pushing four specific architectural changes that reposition Cisco for the market that now exists, rather than the one Cisco's product lines and organization chart were built for. Each began as a minority position he argued years ahead of the company; each is now a company-level initiative because he built the coalition and the evidence to make it one.

1. **A unified network operating system.** Cisco's software is fragmented across NX-OS, IOS-XR, and IOS-XE even though its hardware has converged on Silicon One — a gap competitors including Arista and Juniper actively sell against with a single-OS, single-management-platform story. Bruce co-founded the **Single-Secure-OS (SSOS)** tiger team to close it: one Linux-based NOS running routing, switching, and policy as containerized, hardware-accelerated applications, secured by Cilium, Tetragon, and eBPF. SONiC is the platform where he has already proven the model works — SRv6 on SONiC shipped for the Cisco 8122 in June 2026 — but SSOS's scope is the operating system strategy itself, not one product.
2. **One forwarding architecture, end to end.** Cisco's transport story is a different encapsulation in every domain. Bruce co-founded the **Unified Forwarding Architecture (UFA)** to replace that with a single model — SRv6 uSID — spanning the WAN, the data centre, the host, and now the NIC, across six product lines and five business entities.
3. **One policy model, not several.** Identity and segmentation are just as fragmented as transport: ISE, TrustSec, SASE, and SD-WAN each carry their own version, with no shared path to the forwarding layer. Bruce recognized that a Security Group Tag and an SRv6 uSID are both 16 bits, and co-founded the **Unified Policy Model (UPM)** tiger team to carry a single identity-and-policy model on top of UFA's forwarding plane. The ISE organization committed to it in December 2025.
4. **Closing the host-networking air-gap.** Bruce named this gap in 2015, after observing that hyperscale operators had moved the network's real control point into the host — a position Cisco's acquisition of Isovalent in 2024 has begun to close. The gap is not fully closed: he is now advocating that Cisco build SmartNICs and a scale-up Ethernet solution to compete directly with Nvidia, AMD, and Broadcom, so Cisco's host-networking position extends all the way to the rack-scale AI architecture the industry is building today.

Each rock required persuading business entities Bruce does not belong to, none of it came with organizational authority attached, and all four are argued from the same place: a decade spent deeply enmeshed in the architectures actually driving the industry, which is why he has been early and right often enough that people who do not report to him keep asking what he thinks.

---

## Career Path

| Role / Title                                                                                     | Dates               |
| ---------------------------------------------------------------------------------------------------- | --------------------- |
| Customer Engineer, Siemens Business Communications                                               | 1997 – 2004         |
| Network Architect, Expedia Group                                                                 | 2004 – 2007         |
| Systems Engineer II / III, Cisco — TW Telecom account team                                       | 2007 – 2012         |
| Consulting Systems Engineer, Cisco — USSP TCS Select                                             | 2012 – 2015         |
| Systems Architect, Cisco — Americas Web / Hyperscale                                             | 2015 – 2020         |
| **Principal Systems Engineer**, Americas Service Provider + Web                                  | Aug 2020 – Jun 2026 |
| **Principal Solutions Engineer**, Global — Lead Cloud-SP Architect, Global Solutions Engineering | Jun 2026 – present  |

**Education:** BA, University of Washington (1996) **Certifications:** CCIE Service Provider #35169 (2012) **Public service:** Anacortes City Council since 2017; Mayor Pro Tem since January 2020

---

## Candidate Portrait

Bruce McDougall was the operator before he was the architect. As a network engineer at the Expedia Group he was evaluating MPLS in the data centre in 2006, hunting for scale beyond the enterprise tooling of the era. That origin still governs how he chooses what to work on: he asks what he would want if he were still the operator — the simplest, most cost-effective, most extensible, longest-lasting architecture — and what would sustain a healthy industry ecosystem. **Only then does he ask how Cisco gets to the centre of that future.** The order is the discipline, and it is why his positions survive customer scrutiny.

His expertise spans hyperscale and cloud-native networking, AI/ML fabrics, Linux and Kubernetes, open network operating systems, network-as-a-service, and Segment Routing v6. Combined with deep service provider architecture experience, that dual SP and Web/hyperscale specialization is rare in Cisco's sales organization.

He reasons about networks holistically, independent of vendor org charts and product silos — a data centre platform and a backbone platform are fundamentally the same kind of thing, and the difference between them is topology and scale, not category. Cisco's engineering organization is divided into places in the network — campus, DC, WAN, security — a structure built for how networking worked a decade ago, and competitors including Arista, Juniper, and Nokia have identified the gap that structure creates and sell directly against it: a single, unified architecture where Cisco sells several. Much of Bruce's internal-facing work has been a sustained effort to close that gap from the inside: unified SRv6 forwarding end to end, fixed-form-factor fabrics in roles convention reserved for chassis, flat low-diameter topologies in place of hierarchy, and the host as a first-class network participant. He applies the same reduction to policy — a firewall, an access control list, and a Layer 3 VPN are all ways of forwarding data *intentionally* rather than blindly, which is what produced the Unified Policy Model and SRv6-with-SGT.

The operators he works with do not think of themselves as customers. They are deeply technical teams building infrastructure at enormous scale and speed, and they choose the technologies that make their own organizations successful. Bruce meets them as a peer, which is why an operator will present his architecture as their own — Bell Canada's Dan Bernier has carried concepts they developed together to KubeCon and MPLS World Congress, and for a vendor architect that is worth more than presenting it himself.

For nearly a decade Bruce has been one of a small number of trusted field voices in Clarence Filsfils' Segment Routing engineering organization. Cisco awarded a **2025 Pinnacle Award to the SRv6 uSID team** for the technology's global market impact; the team numbered roughly 40 and was almost entirely Cisco engineering, and **Bruce and DSE Craig Hill were the only two recipients from the sales organization.**

He is also, by consistent report, exceptional to work with. Brook Crossman's assessments return to it cycle after cycle — *"many report how collaborative he is"*, *"simply put, everybody wants to work with him."* Bruce has issued **22 Connected Recognition awards to peers** and received 37. In June 2026 he moved from Brook Crossman's Americas ASP and Web organization to Matt Gillies' Global Solutions Engineering team as lead Cloud-SP architect — formal recognition that his impact already operated globally.

### Quantified highlights *(Aug 2020 – present)*

| Dimension                 | Evidence                                                                                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Segment revenue**       | **$10.9B** Americas Web/Hyperscale bookings **2022–2026** in Bruce's theater; **$5.3B** in 2026 alone. Org-level figures, not individual attribution    |
| **Production wins**       | Meta **$17M** BBF first production order (Feb 2026); Bell Canada **500× C8231-G2** first order (May 2026)                                               |
| **Product delivery**      | **SRv6 on SONiC, Cisco 8122** (Jun 2026); SRv6 uSID on Nexus; SRv6 on Cisco SD-WAN forthcoming                                                          |
| **Intellectual property** | **6 issued US patents, 9 pending, 1 defensive publication** from **24 invention disclosures since Aug 2020**; four patents issued during the PSE period |
| **Recognition**           | **2025 Pinnacle Award** — SRv6 uSID team; **Distinguished Speaker**, Cisco Live EMEA 2023                                                               |
| **Open source**           | `srv6-labs` 74 stars · `cisco-open/jalapeno` 78 stars · owner of the `jalapeno` org (15+ repos) · co-owner of `cisco-asp-web` (14 repos)                |
| **Publications**          | Contributor, three chapters of *Segment Routing Part III: SRv6*; first public description and demonstration of SRv6 uSID on SONiC (May 2023)           |
| **Talent**                | **Six systems engineers promoted to PSE** — one as official mentee, five as extended-team advisor; three years on the PSE review subcommittee           |

---

## Global Impact Summary

Bruce's impact moved from account, to region, to segment, to global — and by June 2026 into a global role.

The work that carries it is not a list of overseas customers but a set of architectures adopted across theaters: **global field lead for SR-Apps**, where Cisco's SR engineering adopted his open-source Jalapeno project as the platform; **end-to-end SRv6 including host-based and cloud-native**, now Cisco's direction across six product lines and the transport substrate of the industry's MRC specification; **open NOS and SONiC**, from the first public description of SRv6 uSID on SONiC in May 2023 to product shipping in June 2026; **host networking and Cilium**, from acquisition advocacy in 2021 to a customer requirements document Cisco engineering has accepted; **SP network-as-a-service**, whose framing predated the industry NaaS movement by two to three years; and **SRv6 with SGT**, now committed to by the ISE organization.

Global training and enablement reaches all three theaters. Cross-theater operator engagements — Evroc, Rakuten, NTT East, MTN Nigeria, DU UAE — are consulted where local depth does not extend that far; the MTN and DU designs were delivered entirely through an APJC systems engineer, for two national operators on two continents Bruce never met.

*More details: [03-global-impact.md](https://github.com/brmcdoug/DSE/blob/main/03-global-impact.md)*

---

## Span of Influence Summary

In August 2020 Bruce was a production routing and data centre SME for Web and service provider accounts. He now shapes product roadmaps in organizations with no reporting relationship to his own, and his technical judgment is solicited by corporate development, security, enterprise networking, and the office of the CTO.

**Four technology domains** — the criteria require at least two: programmable transport (SRv6 uSID end to end), cloud-native and host networking (eBPF, Cilium, Kubernetes CNI), open network operating systems (SONiC, Linux NOS strategy), and enterprise identity and policy (SGT, segmentation, the Policy Plane). Since 2024 he has driven SRv6 feature development across **eight platforms in five business entities** — IOS-XR, IOS-XE, NX-OS, SONiC, SD-WAN, SASE, ThousandEyes, and Cilium.

None of that influence came with authority attached. The hardest evidence is issued intellectual property: Bruce is an inventor on **Underlay Network Traffic Steering** (12,120,027, granted October 2024), filed by SD-WAN engineering — a business entity he does not belong to. He co-founded three company-direction tiger teams: **Single-Secure-OS (SSOS)**, addressing NOS fragmentation no business entity owned; the **Unified Forwarding Architecture (UFA)**; and the **Unified Policy Model (UPM)**. He is the Web and Hyperscale representative for **executive BU interlocks**, co-owns the FY26 Global Sales Technical Roadmap with Web SE Director Tyler Nielson and Web PSEs Rob Murphy and Masi Mohammed, and was engaged by **corporate development** on neo-cloud equity investments. He also co-prepared the EVPN Least Complexity readout with an informal group of PSEs and DSEs; Brook Crossman delivered it to **CPO Jeetu Patel**, who committed to fixing the underlying problem.

Sustained relationships run to Cisco Fellows **Clarence Filsfils** (SR/SRv6) and **Praveen Bhagwatula** (SONiC), to **Thomas Graf** (Cilium co-creator, Isovalent founder), and to **Vijay Tapaskar** and **Mani Veerachamy** in SONiC engineering. Underneath it is a habit rather than an assignment: over two decades Bruce has built and kept working relationships with senior SEs, PSEs, and DSEs across Cisco regardless of geography or vertical, sustained for the learning as much as for any engagement.

*More details: [04-span-of-influence.md](https://github.com/brmcdoug/DSE/blob/main/04-span-of-influence.md)*

---

## Industry Impact Summary

Bruce advances a sustained vision externally, built on three elements: **host networking**, **open source** — for NOS but also for tooling and automation, and because visible open-source commitment earns the trust that drives product revenue — and **source routing** as a platform for the operator's own service innovation rather than a vendor feature catalogue.

His formal standards-body record is thin relative to his open-source and operator-community record, and the honest statement is the stronger one. The MRC timeline shows where the industry's weight actually sits: the work began in 2024, SRv6 for the AI backend was discussed publicly at **OCP in November 2024**, and the first IETF draft appeared in **July 2025 — largely in response to work already well under way**, authored by others. The standards process trailed the open forums by roughly eight months on the defining transport architecture of the AI era.

Bruce's strongest external evidence is in open source and the operator community. He published the **first public description and demonstration of SRv6 uSID on SONiC** (May 2023). He curates `github.com/segmentrouting`, launched `srv6-labs` (~40,000 first-week views, an ipspace.net citation, contributors from Verizon and Oracle), and open-sourced his Cisco Live lab so customers could fork it and train their own colleagues. He authored the **WMP-PolarFly** paper contesting Amazon's published RNG architecture on the same terms Amazon used — and on ground Cisco can sell, since WMP-PolarFly builds only on FRR, SONiC, and standard SRv6. He co-developed a four-hour **O'Reilly** course, *Build Your Own Networking Lab*, with **Russ White**. And operators carry his architecture themselves, which is the strongest form the influence takes.

*More details: [05-industry-impact.md](https://github.com/brmcdoug/DSE/blob/main/05-industry-impact.md)*

---

## Business Impact Summary

Bruce's business impact follows one pattern: train the field and the customer on architectures before they ship, build the labs that make them testable, then co-develop until the revenue matures. These are multiyear partnerships, not sales cycles.

### Americas Web/Hyperscale segment bookings *(2022–2026, finance)*

Org-level figures for Bruce's theater. Not individual attribution.

| Customer              | 2022       | 2023       | 2024      | 2025       | 2026       | Total       |
| ------------------------ | ------------ | ------------ | ----------- | ------------ | ------------ | ------------- |
| Microsoft             | $603M      | $714M      | $226M     | $861M      | $1.57B     | **$3.97B**  |
| Meta                  | $277M      | $367M      | $54M      | $510M      | $1.91B     | **$3.11B**  |
| Google                | $404M      | $103M      | $108M     | $287M      | $1.05B     | **$1.95B**  |
| Amazon                | $127M      | $69M       | $196M     | $296M      | $717M      | **$1.41B**  |
| Oracle                | $4M        | $45M       | $230M     | $146M      | $21M       | **$446M**   |
| Apple + Web Platforms | $1M        | $8M        | $11M      | $9M        | $14M       | **$42M**    |
| **Total**             | **$1.42B** | **$1.30B** | **$824M** | **$2.11B** | **$5.28B** | **$10.94B** |

Tier-1 SP bookings and out-of-territory accounts are not in this extract.

| Customer             | Signature outcome                                                                               | Bruce's role                                                                                       |
| ----------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Meta**             | **$17M** BBF production order (Feb 2026); RBB committed to SRv6                                 | SL-API pioneer; VXR co-validation labs; pre-GA 8223 patch — **without presenting to the customer** |
| **Microsoft**        | SRv6 on SONiC **8122** shipped (Jun 2026); PhyNet, Octans, dRH; 1.6T WAN                        | Primary field architect since 2021; multi-tenant AI fabric specification                           |
| **Oracle**           | SRv6 in limited production by end-2025; Acceleron and MRC                                       | Lead SRv6-for-AI architect; low-diameter fabric studies                                            |
| **CoreWeave**        | Scope grew to ~10–12k switches                                                                  | SONiC SME; lead SRv6-for-AI architect; self-service labs                                           |
| **Bell Canada**      | **500× C8231-G2** first order (May 2026)                                                        | End-to-end SRv6, Cilium, and NaaS architecture — a partnership dating to 2019                      |
| **Out-of-territory** | Geico ~$1.6M; Honeywell ~$2M; Province of New Brunswick migrated to SRv6 after one conversation | SONiC and SRv6 SME to theaters and accounts outside his assignment                                 |

**Beyond bookings.** Bruce built part of the foundation the segment runs on: when he joined the Web team Cisco was barely selling into hyperscale production networks and was read as an enterprise networking company. He established Cisco's credibility with those operators and built the bench alongside it — the Web team now has three PSEs and multiple grade-12 SEs on each major account. He does not claim the revenue; he built part of what it stands on.

**Stated plainly:** Cisco has arrived late across successive switch-silicon generations — 12.8T, 25.6T, 51.2T — and lateness at that layer removes Cisco from consideration entirely rather than costing a feature comparison. Microsoft and Oracle both began SRv6-for-AI deployments on competitor hardware, on the architecture Bruce had specified. The architecture was validated; the timing was not.

*More details: [06-business-impact.md](https://github.com/brmcdoug/DSE/blob/main/06-business-impact.md)*

---

## Innovation Summary

Bruce's inventions begin from operator empathy rather than product strategy, and most start as a brainstorm — his own or with a peer — that becomes an approved disclosure, a paper, or a working demonstration. Some begin as a declined disclosure and reappear years later as a shipping product, an acquisition, or an industry specification. Both paths are in the record, and the declines are among the strongest evidence in the package: *SRv6 uSID Scheduled Fabric for AI/ML Clusters*, declined in 2023, describes the architecture the industry standardized in 2025–2026, and a filing date cannot be retrofitted.

| Category           | Evidence                                                                                                                                                    |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Patents**        | **6 issued, 9 pending, 1 defensive publication** — four issued during the PSE period; five continuations on the SmartTOR / NIC-based segment routing family |
| **Disclosures**    | **24 since Aug 2020** (36 lifetime) — a pace Brook Crossman called *"on pace to break (ASP) records"*                                                       |
| **Products**       | SRv6 on SONiC (8122, Jun 2026); SRv6 uSID on Nexus; SRv6 on SD-WAN forthcoming; Cilium SRv6 CRD accepted by engineering                                     |
| **Acquisition**    | **Isovalent / Cilium** — advocated from 2021; announced Dec 2023, closed 2024                                                                               |
| **Bold Bets**      | **Jalapeno** — the only field-submitted project to advance past the first evaluation round; SR engineering adopted it as the SR-Apps platform               |
| **Specifications** | SRv6 uSID multi-tenancy for AI factories (131k GPUs per cluster); **WMP-PolarFly** contesting Amazon's RNG                                                  |
| **Awards**         | **2025 Pinnacle Award**; Cisco EN Hackathon 2022 winner                                                                                                     |

*More details: [07-innovation.md](https://github.com/brmcdoug/DSE/blob/main/07-innovation.md)*

---

## Personal Development Summary

Bruce took the PSE committee's feedback — expand beyond the Web and SP comfort zone — as a work plan. What followed was deliberate and unassigned: SD-WAN and Cisco Secure Access, Future Enterprise Segmentation, co-founding SSOS, Isovalent and security engineering, ThousandEyes, the EMEA peer network, CX, and the OST Zurich university collaboration.

The second choice was technical. Rather than remaining a routing architect who presents slides, he invested in production-grade builder skills — Kubernetes, Cilium and eBPF, Containerlab, Git workflows, dCloud publishing — which is why the labs, emulators, and POC repositories in this package are running code that other people use. That investment compounds: years of self-training in Python, Go, and DevOps practice make him markedly more effective with agent-assisted development, because knowing precisely what he is building is what turns an agent into a development partner.

Two development areas run through his assessments, both named openly in the section: **executive communication**, coached directly by Brook Crossman through 2HFY25–1HFY26 and applied in venues up to a CPO readout; and **filtering demand and delegating for others' visibility**, where his response has taken a consistent shape — spot something good an engineer is already doing, then find them a stage for it. **Vaughn Suazo** is his DSE mentor.

*More details: [09-personal-development.md](https://github.com/brmcdoug/DSE/blob/main/09-personal-development.md)*

---

## Leadership Summary

Bruce is known as a collaborative partner who shares credit and creates opportunities for other engineers. The measure is not sessions delivered:

- **Six systems engineers promoted to PSE** — Nacho Sanchez as his official mentee, and Rob Murphy, Roberta Maglione, Masiuddin Mohammed, Marina Ferreira, and Alessandro Breccia as extended-team advisory roles. **Christopher Luciano** is in progress. Three years as a **voting member of the PSE review subcommittee**
- **An engineer he had never worked with** — EMEA SE Arkadiusz Kaliwoda — built a Cilium SRv6 demo from Bruce's dCloud lab, showed it at MPLS World Congress, and now contributes production code to the Cilium project
- **A co-presenter who won Distinguished Speaker** — Nico Michel, at CLEU 2026, presenting Bruce's lab
- **Programmes that outlived their launch** — ASP Lightning Talks, co-created with DSE John Mullooly, at Episode 23 after five years; the GitHub-first Cisco Live lab model, now common practice
- **Investment cases built from multi-stakeholder data** — Cilium-SP (~$34M / ~$323M), SONiC SRv6, and the Silicon One generational TAM model
- **Community leadership** — Anacortes City Council since 2017 and Mayor Pro Tem since 2020, during which the city built **the only community-owned fibre-to-the-home ISP in Washington State**: affordable high-bandwidth service for residents and a revenue stream not based on taxation

*More details: [10-se-community-leadership.md](https://github.com/brmcdoug/DSE/blob/main/10-se-community-leadership.md)*

---

## Becoming a Distinguished Solutions Engineer *(candidate statement)*

When I put together my Principal package, I realised the work I was drawn to could change Cisco's trajectory and maybe the industry's. That is still the goal. Networks should be a delight to the operators, the users, and the applications that depend on them — not a snowflake tax on every new workload. The network exists to serve, and roads have no value unless they are easy to use.

I came into this from the other side of the table. I was a network engineer and a Cisco customer before I was an architect, and I still decide what to work on by asking what I would want if I were the one operating it, and what would leave the industry healthier. Then I ask how Cisco gets to the centre of that. Doing it in that order is why customers trust the answer.

I have chased that through host networking, SRv6, open network operating systems, and AI fabrics — usually years before the products caught up, and often while being told the market was not ready. Being early is only useful if you stay long enough to be useful, so I build the labs, publish the code, teach the field, and keep making the case until the architecture ships.

Promotion would not change the mission; it would widen the platform. As a DSE I would keep bridging IMI, SONiC, cloud-native security, and SP transport into one coherent story for AI factories and open NOS adoption. I would scale the lab-and-GitHub enablement model so more engineers can co-develop with hyperscalers ahead of feature availability. I would stay a peer architect to operators on horizon-2 and horizon-3 problems. And I would keep publishing open artifacts that accelerate adoption and hold Cisco accountable to the future we claim.

Mostly I would keep doing what I find most satisfying: seeing something good an engineer is doing and finding them a stage for it. The best outcomes in this package are not mine alone — they belong to account teams who ran with an architecture, to systems engineers who took a lab and made it theirs, and to operators who presented the idea better than I could have. That is the job I want to keep doing.

---

## Direct Leader Summary

Bruce reported to **Brook Crossman** (VP, Systems Engineering, ASP and Web) for five years through June 2026, and to **Matt Gillies** (Global Solutions Engineering) since. The package may carry input from both.

Across six talent assessment cycles Brook has rated Bruce as meeting expectations on Business Outcomes and Guiding Principles, describing him as ASP's **centre of gravity for SRv6 and AI-forwarding innovation**, the leader in the Segment Routing domain on the direct field team, and someone who *"represents Cisco incredibly well in front of customers inside and outside of ASP."* Brook notes the volume of requests for Bruce's help from outside the segment, that engineering forums trust him as a representative, and that *"simply put, everybody wants to work with him."* On development he and Bruce aligned on **executive-ready communication** and on **routing work to others as visibility opportunities** — both addressed in Personal Development.

Brook and Bruce are aligned on the DSE-scope priorities: SONiC SRv6 on Cisco 8000 G200 and P200 for Microsoft and Oracle, the Microsoft disaggregated franchises, the Isovalent SRv6 path to GA, a comprehensive SRv6-for-AI demonstrator, repeatable cloud-native segmentation, and continued SE community multiplication.

*Full letter: [02-direct-leader-recommendation.md](https://github.com/brmcdoug/DSE/blob/main/02-direct-leader-recommendation.md)*

---

## Sponsorship Summary

Letters of recommendation span BE leadership, sales leadership, customers and partners, other Cisco organizations, engineering Principal Engineers, Distinguished Engineers and Fellows, and the Cisco Sales PSE and DSE community — the category the Nomination Kit weights most heavily. Bruce's goal is letters from more than half the global DSE community. `[table in progress]`

*Table: [08-sponsorship.md](https://github.com/brmcdoug/DSE/blob/main/08-sponsorship.md)*
