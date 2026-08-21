# Bruce McDougall — DSE Package, Merged Review Draft

**Purpose:** the four most-iterated sections, combined into one file for holistic review — catching cross-section redundancy, voice drift, and pacing issues that are hard to see one file at a time. This is a **review artifact**, not a new source file — keep editing the individual numbered `.md` files as the source of truth; regenerate this merge whenever you want another full-package read.

**Included, in package order:**
- `01-exec-summary-draft-v5.md` — Executive Overview *(Bruce: ready for first-draft Word insert)*
- `03-global-impact-v1.md` — Global Impact *(Bruce: solid)*
- `04-span-of-influence-v4.md` — Span of Influence *(just completed this pass)*
- `05-industry-impact.md` — Industry Impact *(two full editing passes, no open items since)*

**Not included — still mid-review or not yet deeply worked:**
- `02-direct-leader-recommendation.md` — scaffolding cleaned up only, no narrative pass
- `06-business-impact.md` — Bruce is actively reviewing (through Oracle as of the last note)
- `07` through `11` — scaffolding cleaned up only

**Known open item spanning this merge:** the Executive Overview restates a fair amount of Span of Influence and Industry Impact detail (flagged in `todo.md`, Aug 19). Worth reading the Exec Overview against the sections below with that specifically in mind — this merge is a good place to mark exactly which sentences feel redundant.

---

# Executive Overview and General Information about Candidate

**Cisco Distinguished Solutions Engineer Nomination — Bruce McDougall** *August 2026. Finance-validated Web/Hyperscale segment bookings (2022–2026) integrated; account-level, SP, and product run-rate figures marked where pending.*

---

## The Case in Brief

The DSE criteria open with a general guideline that sits above every other category: *demonstrate how you have been a **force multiplier** throughout the organization — identifying new technology and industry trends, building the necessary field enablement, aligning strategic stakeholders and investment, and leading lighthouse customers to drive field adoption.*

That is a description of how Bruce McDougall works.

| The criterion                                    | Bruce's record                                                                                                                                                                                           |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Identify new technology and industry trends**  | Identified in 2016 that hyperscalers had moved the network's control point into the host. Designed a data center elephant-flow balancer concept in 2017 for the problem the industry took up in 2024 as SRv6-for-AI. In 2021 recognized Cilium/eBPF as a disruptive and strategic technology and advocated Cisco acquire Isovalent. Called the SONiC market credibility inflection in 2023. Saw that micro-segmentation and identity could be merged with transport (SRv6 + SGT) in 2024. |
| **Build the necessary field enablement**         | `srv6-labs` (74 stars), `cisco-open/jalapeno` (78 stars), the MRC emulator built within a week of OpenAI's announcement, VXR and Containerlab environments, dCloud labs, and SRv6, SONiC, Cisco 8000, and Cilium training delivered across NA, EMEA, and APJC. |
| **Align strategic stakeholders and investment**  | The SONiC SRv6 investment case that reversed engineering scepticism and **shipped on the Cisco 8122 in June 2026**. The Cilium-SP CRD and business case built from worldwide account data — **~$34M Isovalent / ~$323M MIG** pullthrough, finance-validated. Isovalent acquisition advocacy from 2021. Ongoing work co-leading the Single-Secure-OS (SSOS), Unified Forwarding Architecture (UFA), and Secure Network Policy Framework (SNPF) tiger teams|
| **Lead lighthouse customers and drive adoption** | Microsoft, Meta, Oracle, CoreWeave, and Bell Canada — the accounts where SRv6, SONiC, and host networking went from argument to production.                                                              |

Two things about how he works are worth stating plainly at the outset.

**Bruce loves working directly with customers.** He is also a force multiplier: he transfers ideas, knowledge, and tools to account systems engineers, and that empowerment sometimes means he isn't in the room when a team goes on to win a deal or a franchise. The **$17M Meta backbone re-entry** is one example — Bruce pioneered the SL-API technique at Microsoft, taught it to the Meta account team, built the labs they validated it in, and never presented to Meta himself.

**And the industry moved to where he was standing.** Five years ago service provider and hyperscale operators largely dismissed SRv6 as not ready. Today SPs almost universally name it their strategic direction and most hyperscalers agree. Bruce has been at the centre of that conversation from the beginning — as a globally recognized SME in Cisco's sales organization, an inner-circle member of Cisco's SR engineering brain trust, and in the operator and open source communities.
> *"Bruce continues to have a significant impact leading frontier projects in AI forwarding and teaching others. His innovation is on pace to break (ASP) records with patents being filed and awarded and he sets the standard for teamwork and technical depth. The recent recognition he received in the Pinnacle awards speaks to his technical capabilities and his strong reputation for teamwork. Cisco is lucky to have him teaching our teams and customers, representing us externally and driving innovation in the portfolio."* — **Brook Crossman**, VP Systems Engineering, ASP and Web — Bruce's direct leader for five years through June 2026

// i'm inclined to remove the 'two things about how he works' sentence and the paragraph that follows. it feels like it was written as a response to agent conversation rather than an impactful point for my DSE candidacy. the 'And the industry moved' paragraph is good, but feels out of place. The intro isn't reading like a real narrative, but rather like we copy/pasted a bunch of ideas in without a plan or outline
---

## Four Big Rocks: Repositioning Cisco for the Hyperscale and AI Era

Underneath the initiatives, tiger teams, and account wins in this package is a single throughline. Bruce is pushing four strategic architectural shifts that reposition Cisco for the market as it exists today and well into the future. Each began as a minority position he argued years ahead of the company; each is now a company-level initiative because he built the coalition and the evidence to make it one.

1. **A unified network operating system.** Cisco's software is fragmented across NX-OS, IOS-XR, and IOS-XE even though its hardware has converged on Silicon One — a gap competitors including Arista and Juniper actively sell against with a single-OS, single-management-platform story. Bruce co-founded the **Single-Secure-OS (SSOS)** tiger team to close it: one Linux-based NOS with routing, switching, and policy as containerized applications, and secured by Cilium-Tetragon on eBPF.
2. **One forwarding architecture, end to end.** Cisco's transport story is a different encapsulation in every domain. Bruce co-founded the **Unified Forwarding Architecture (UFA)** to replace that with a single model — SRv6 uSID — spanning the campus, WAN, the data centre and the Cloud, the host, and now the NIC.
3. **Unified Policy and Identity.** Identity and segmentation are just as fragmented as transport: ISE, TrustSec, SASE, and SD-WAN each carry their own version. Service Providers can't reconcile when a broadband customer and wireless customer are the same individual. Bruce recognized that a Security Group Tag and an SRv6 uSID are both 16 bits, and co-founded the **Secure Network Policy Framework (SNPF)** tiger team to carry a single identity-and-policy model on top of UFA's forwarding plane. The ISE organization committed to it in December 2025. `[verify]`
4. **Closing the host-networking air-gap.** Bruce coined the term in 2016, after observing that hyperscale operators had moved the network's real control point into the host — a position Cisco's acquisition of Isovalent in 2024 has begun to close. The gap is not fully closed: he is now advocating that Cisco build SmartNICs and a scale-up Ethernet solution to compete directly with Nvidia, AMD, and Broadcom, so Cisco's host-networking position extends all the way to the rack-scale AI architecture the industry is building today.

Pushing these rocks required building relationships with business entities, and with sales DSE and PSE peers outside Bruce's traditional circles within ASP/Web and MIG (Mass-Scale Infrastructure Group). He created the vision behind each rock and took the initiative to found or co-found the tiger team that carries it forward — collaborating with peers across the company to build each into a real, ongoing effort rather than a proposal. That pattern is, in the end, the case this package is making — argued from a decade spent deeply enmeshed in the architectures actually driving the industry, which is why he has been early and right often enough that his expertise is asked for by name across the company.

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

**Education:** BA, University of Washington (1996) **Certifications:** CCIE Service Provider #35169 (2012) **Public service:** Anacortes City Council since 2017; Mayor Pro Tem, 2020 – 2021

---

## Candidate Portrait

Bruce McDougall was a network operator before he was the Solutions Engineer. As a network engineer at the Expedia Group he was evaluating MPLS in the data centre in 2006, hunting for scale beyond the enterprise tooling of the era. That origin still governs how he tackles challenges today: he asks what he would want if he were still the operator — the simplest, most cost-effective, most extensible, longest-lasting architecture — and what would sustain a healthy industry ecosystem. **Only then does he ask how Cisco gets to the centre of that future.** The order is the discipline, and it is why he is so credible with the most technologically sophisticated customers in the world.

His expertise spans hyperscale and cloud-native networking, AI/ML fabrics, Linux and Kubernetes, open network operating systems, network-as-a-service, and SRv6. Combined with deep service provider architecture experience, that dual SP and Web/hyperscale specialization is **unique** in Cisco's sales organization.

The operators he works with do not think of themselves as customers. They are deeply technical teams building infrastructure at enormous scale and speed. Bruce meets them as a peer, which is why an operator will present his architecture as their own — Bell Canada's Dan Bernier has carried concepts they developed together to KubeCon and MPLS World Congress, and for a vendor architect that is worth more than presenting it himself.

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
| **Talent**                | **Six systems engineers promoted to PSE** — one where Bruce was official mentor, five where Bruce was an advisor to the candidate; three years on the PSE review subcommittee           |

---

## Global Impact Summary

Bruce's impact moved from account, to region, to segment, to global — and by June 2026 into a global role.

The work that carries it is not a list of overseas customers but a set of architectures adopted across theaters: **global field lead for SR-Apps**, where Cisco's SR engineering adopted his open-source Jalapeno project as the development platform; **end-to-end SRv6 including host-based and cloud-native SRv6**, now being developed across Cisco product lines and the transport substrate of the industry's MRC specification; **open NOS and SONiC**, from the first public description of SRv6 uSID on SONiC in May 2023 to product shipping in June 2026; **host networking and Cilium**, from acquisition advocacy in 2021 to a customer requirements document Cisco engineering has accepted; **SP network-as-a-service**, whose framing predated the industry NaaS movement by two to three years; and **SRv6 with SGT**, now committed to by the ISE organization.

Bruce has developed and delivered training sessions that have reached a global audience (Tech Elevate, GSX) and has served as SONiC or SRv6 SME for several engagements outside North America: Evroc, Rakuten, NTT East, Softbank, Telstra, Telia, MTN Nigeria.

*More details: [03-global-impact.md](https://github.com/brmcdoug/DSE/blob/main/03-global-impact.md)*

---

## Span of Influence Summary

In August 2020 Bruce was a production routing and data center SME for Web and service provider accounts. He now shapes product roadmaps well beyond MIG, and his technical judgment and subject matter expertise is solicited for engagements across enterprise, public sector, and EMEA and APJC.

Bruce's technical expertise spans **Five technology domains**: Hyperscale routing and data center architecture, programmable transport (SRv6, IOS-XR Service-Layer API), cloud-native and host networking (eBPF, Cilium, Kubernetes CNI), open network operating systems (SONiC, Linux NOS strategy), and enterprise identity and policy (SGT, segmentation, the Secure Network Policy Framework (SNPF)). Since 2024 he has driven SRv6 feature development across **eight platforms in five business entities** — IOS-XR, IOS-XE, NX-OS, SONiC, SD-WAN, SASE, ThousandEyes, and Cilium.

He co-founded three company-direction tiger teams: **Single-Secure-OS (SSOS)**, addressing NOS fragmentation no business entity owned; the **Unified Forwarding Architecture (UFA)**; and the **Secure Network Policy Framework (SNPF)**. He is the Web and Hyperscale representative for **executive BU interlocks**, co-owns the FY26 Global Sales Technical Roadmap with Web SE Director Tyler Nielson and Web PSEs Rob Murphy and Masi Mohammed, and was engaged by **corporate development** on neo-cloud equity investments. He also co-prepared the EVPN Least Complexity readout with an informal group of PSEs and DSEs; Brook Crossman delivered it to **CPO Jeetu Patel**, who committed to fixing the underlying problem.

Sustained relationships run to Cisco Fellows **Clarence Filsfils** (SR/SRv6) and **Praveen Bhagwatula** (SONiC), to **Thomas Graf** (Cilium co-creator, Isovalent founder), and to **Vijay Tapaskar** and **Mani Veerachamy** in SONiC engineering. Underneath it is a habit rather than an assignment: over two decades Bruce has built and kept working relationships with senior SEs, PSEs, and DSEs across Cisco regardless of geography or vertical, sustained for the learning as much as for any engagement.

*More details: [04-span-of-influence.md](https://github.com/brmcdoug/DSE/blob/main/04-span-of-influence.md)*

---

## Industry Impact Summary

Bruce advances a sustained vision externally, built on three elements: **host networking**, **open source** — for NOS but also for tooling and automation, and because visible open-source commitment earns the trust that drives product revenue — and **source routing** as a platform for the operator's own service innovation rather than a vendor feature catalogue.

Bruce's strongest external evidence is in open source and the operator community. He published the **first public description and demonstration of SRv6 uSID on SONiC** (May 2023). He is curator of `github.com/segmentrouting` where he launched `srv6-labs` in 2023. The announcement on LinkedIn garnered ~40,000 first-week views, an ipspace.net citation, and the project features contributors from Verizon and Oracle. He open-sourced his Cisco Live lab so customers could fork it and train their own colleagues. He authored the **WMP-PolarFly** paper contesting Amazon's published RNG architecture on the same terms Amazon used — and on ground Cisco can sell, since WMP-PolarFly builds only on FRR, SONiC, and standard SRv6. He co-developed a four-hour **O'Reilly** course, *Build Your Own Networking Lab*, with **Russ White**. And multiple operators have presented ideas and concepts he heavily influenced at major industry conferences as their own — the strongest form external influence can take.

*More details: [05-industry-impact.md](https://github.com/brmcdoug/DSE/blob/main/05-industry-impact.md)*

---

## Business Impact Summary

Bruce's Web/Hyperscale accounts alone booked **$10.9B from 2022 to 2026, with $5.3B in 2026 alone** — the segment where SRv6, SONiC, and host networking went from Bruce's argument to shipping architecture.

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
| **Microsoft**        | SRv6 on SONiC **8122** shipped (Jun 2026); PhyNet, dRH; 1.6T WAN                        | Primary field architect since 2021; multi-tenant AI fabric specification                           |
| **Oracle**           | SRv6 in limited production by end-2025; Acceleron and MRC                                       | Lead SRv6-for-AI architect; low-diameter fabric studies                                            |
| **CoreWeave**        | Scope grew to ~10–12k switches                                                                  | SONiC SME; lead SRv6-for-AI architect; self-service labs                                           |
| **Bell Canada**      | **500× C8231-G2** first order (May 2026)                                                        | End-to-end SRv6, Cilium, and NaaS architecture — a partnership dating to 2019                      |
| **Out-of-territory** | Geico ~$1.6M; Honeywell ~$2M; Province of New Brunswick migrated to SRv6 after one conversation | SONiC and SRv6 SME to theaters and accounts outside his assignment                                 |

**Beyond bookings.** Cisco's Web sales team has grown revenue enormously in recent years, and Bruce was instrumental in building the foundations that made that possible: when he joined the Web team Cisco was barely selling into hyperscale production networks and was read as an enterprise networking company. He established Cisco's credibility with those operators and helped build the bench alongside it — the Web team now has three PSEs and multiple grade-12 SEs on each major account.

The revenue above is real, and it could be substantially larger: Cisco has arrived late across successive switch-silicon generations — 12.8T, 25.6T, 51.2T — and lateness at that layer removes Cisco from consideration entirely rather than costing a feature comparison. Microsoft and Oracle both began SRv6-for-AI deployments on competitor hardware, on the architecture Bruce had specified. The architecture was validated; the timing was not.

*More details: [06-business-impact.md](https://github.com/brmcdoug/DSE/blob/main/06-business-impact.md)*

---

## Innovation Summary

Bruce's innovation often comes from making connections not previously made (Host-based Segment Routing, SRv6 + SDWAN) or identifying trends in motion and developing a vision for where they'll lead. Many start as a brainstorm — his own or with a peer — that becomes an approved disclosure, a paper, or a working demonstration. Some begin as a declined disclosure and reappear years later as a shipping product, an acquisition, or an industry specification. Both paths are in the record, and the declines are among the strongest evidence in the package: *SRv6 uSID Scheduled Fabric for AI/ML Clusters*, declined in 2023, describes the architecture the industry standardized in 2025–2026, and a filing date cannot be retrofitted.

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

Bruce took the PSE committee's feedback — expand beyond the Web and SP comfort zone — as a work plan. What followed was deliberate and intentional as he developed relationships and active collaborations across different engineering organizations (NXOS, SD-WAN, Cisco Secure Access, Isovalent, Cisco Security, and ThousandEyes), with DSE and PSE peers across Cisco Sales (Enterprise, Public Sector, EMEA, APJC, the Future Enterprise Segmentation tiger team, co-founding SSOS), and with CX, and the OST Zurich university collaboration.

The second choice was technical. Rather than remaining a routing architect, he invested in production-grade builder skills — Kubernetes, Cilium and eBPF, Containerlab, Git workflows, dCloud publishing — which is why the labs, tools, and POC repositories in this package are running code that other people use. That investment compounds: years of self-training in Python, Go, and DevOps practice make him markedly more effective with agent-assisted development, because knowing precisely what he is building is what turns an agent into a development partner.

*More details: [09-personal-development.md](https://github.com/brmcdoug/DSE/blob/main/09-personal-development.md)*

---

## Leadership Summary

Bruce is known as a collaborative partner who shares credit and creates opportunities for other engineers.

- **Six systems engineers promoted to PSE** — Nacho Sanchez as his official mentee, and he has been an advisor to Rob Murphy, Roberta Maglione, Masiuddin Mohammed, Marina Ferreira, and Alessandro Breccia in their successful PSE candidacies. He is currently **Christopher Luciano's** official mentor. Three years as a **voting member of the PSE review subcommittee**
- **An engineer he had never worked with** — EMEA SE Arkadiusz Kaliwoda — built a Cilium SRv6 demo from Bruce's dCloud lab, showed it at MPLS World Congress, and now contributes production code to the Cilium project
- **A co-presenter who won Distinguished Speaker** — Nico Michel, at CLEU 2026, co-proctoring Bruce's lab
- **Programs with lasting impact** — ASP Lightning Talks, co-created with DSE John Mullooly, a forum for SE's to present on their good work, is at Episode 25 after five years; the GitHub-first Cisco Live lab model is now common practice
- **Investment cases built from multi-stakeholder data** — Cilium-SP (~$34M / ~$323M), SONiC SRv6, and the Silicon One generational TAM model
- **Community leadership** — Anacortes City Council since 2017 and Mayor Pro Tem, 2020–2021, during which the city built **the only community-owned fibre-to-the-home ISP in Washington State**

*More details: [10-se-community-leadership.md](https://github.com/brmcdoug/DSE/blob/main/10-se-community-leadership.md)*

---

## Becoming a Distinguished Solutions Engineer *(candidate statement)*

When I put together my Principal package, I realised the work I was drawn to could change Cisco's trajectory and maybe the industry's. That is still the goal. Networks should be a delight to the operators, the users, and the applications that depend on them. Roads don't have value unless they are used. Roads should be easy to use. For every network device running a network operating system, there are 10s, 100s, maybe 1000s of devices that run Linux, Windows, Android, iOS, etc. The Network has been a snowflake for a long time, but that is changing, and Cisco has an incredible opportunity to win that change.

Promotion would not change the mission; it would widen the platform. As a DSE I would keep bridging MIG, SONiC, cloud-native security, and SP transport into one coherent story for AI factories and open NOS adoption. I would scale the lab-and-GitHub enablement model so more engineers can co-develop with hyperscalers ahead of feature availability. I would stay a peer architect to operators on horizon-2 and horizon-3 problems. And I would keep publishing open artifacts that accelerate adoption and hold Cisco accountable to the future we claim.

At the core, I see myself as a force multiplier. The best outcomes in this package are not mine alone — they belong to account teams who ran with an architecture, to systems engineers who took a lab and made it theirs, and to operators who presented the idea better than I could have. That is the role I want to keep playing as a DSE: finding the people already doing good work, and giving them what they need to take it further.

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
-e 

---

# 03 — Global Impact


## Global Impact

## How Bruce's Impact Moved from Regional to Global

| Period        | Scope of impact                                                                                                                                         | Evidence                                                                                                                                                                                               |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2008–2014** | Account, then Americas region                                                                                                                           | SP routing, Carrier Ethernet, and Unified MPLS across US service provider accounts                                                                                                                     |
| **2015–2020** | Americas Web / hyperscale segment                                                                                                                       | Hyperscale production networks; first public NANOG presentation of SRv6 uSID; established Cisco's production-network credibility with hyperscale operators, and built the SE bench that scaled with it |
| **2020–2023** | Cross-theater technology lead                                                                                                                           | **Global field lead for SR-Apps**; `github.com/segmentrouting`; global SRv6 workshops; APJC and EMEA operator support                                                                                  |
| **2023–2025** | Global architecture and product direction; **globally recognized SME** for SRv6, SONiC, hyperscale architecture, and cloud-native / Kubernetes / Cilium | SONiC investment case; Isovalent acquisition advocacy; SRv6+SGT across business entities; editorial contributor on three SRv6 book chapters                                                            |
| **2025–2026** | Global role; globally recognized SME across SRv6, SONiC, hyperscale architecture, cloud-native / Kubernetes / Cilium, and **AI networking**             | **Lead Cloud-SP architect, Global Solutions Engineering** (Matt Gillies, from Jun 2026); Pinnacle Award for SRv6 uSID market impact; Multi-tenant AI Backend Architecture and Weighted Multi-Path PolarFly topology papers |

---

## Global Initiatives

| Initiative and date                                                         | Impact                                                                                                                                                                                                   |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Global field lead, SR-Apps** — 2020 – 2023                                | Bruce was Cisco's global field lead for SR-Apps, co-developing with Clarence Filsfils' Segment Routing engineering organization to decouple SRv6 application development from hardware and open an agile path to new features and revenue. The effort shaped SR IPM (Integrated Performance Measurement/Monitoring), path tracing, Cisco's SP-NaaS direction, and host-based SRv6 extensibility, and SR engineering subsequently adopted his open-source Jalapeno project as the SR-Apps development platform. He also built and maintains a university research partnership with OST University of Applied Sciences in Zurich (Professor Laurent Metzger), which has produced several SR/SRv6 bachelor's and master's theses, the open-source Hawkv6 distributed controller, and a pipeline of engineering graduates who carry SR and Cisco expertise into their careers. *More details are located in the Innovation section of this document.* |
| **End-to-end SRv6, including host-based and cloud-native** — 2015 – present | Bruce identified that hyperscale operators had moved the network control point into the host, coined the term **Cisco's host-networking air-gap**, and spent a decade arguing that Cisco needed a credible presence there. The architecture he advocated is now supported across **six product lines spanning five business entities** — IOS-XR, IOS-XE, NX-OS, SONiC, SD-WAN, and Cilium — and has been **adopted by operators on four continents**, underpinning the MRC-plus-SRv6 convergence in AI infrastructure. *More details are located in the Innovation and Industry Impact sections of this document.* |
| **Host networking — Isovalent and Cilium evangelism** — 2021 – present      | Bruce has been Cisco's most persistent Isovalent and Cilium evangelist, advocating for the acquisition starting in 2021, three years before it closed, and authoring the multi-use-case Cilium customer requirements document that Cisco engineering has since accepted. The resulting product path now spans deployments and POCs across multiple Cisco business entities and account teams. *More details, including the investment case and Thomas Graf's attestation, are located in the Innovation and Span of Influence sections of this document.* |
| **SP Network-as-a-Service as an architectural solution** — 2021 – present   | Bruce's May 2022 SP360 publication introduced **cloud-like consumption of network services**, framing that predated the industry NaaS movement of 2024–2025 by two to three years. He carried it into Project Yukon at Verizon and AT&T, the SRv6 SD-WAN underlay design at **Rakuten** in Japan, and the Bell Canada NaaS architecture that produced an initial purchase of 400 CPE plus $1.8M in core revenue for Bell's first NaaS deployment. *More details are located in the Business Impact section of this document.* |
| **SRv6 with SGT — unified identity and policy** — 2022 – present            | Working the Future Enterprise Segmentation tiger team, Bruce recognized that a Security Group Tag and an SRv6 uSID are both 16 bits, so an SGT fits as a trailing argument after locator and function — extending the network programming model to *Locator : Function : SGT*. The architecture spans ISE, SASE, SD-WAN, and MIG transport, reaching beyond service providers into large enterprise and public-sector customers wherever those Cisco identity and transport products are deployed. Bruce and Josh Merrill evangelized the concept across Cisco's business units and account teams to broad enthusiasm, and **by December 2025 the ISE organization had committed** to SRv6 SGT and a Secure Network Policy Framework (SNPF). *More details are located in the Innovation and Span of Influence sections of this document.* |
| **Chassis to pizza-box fabrics** — 2017 – present                           | Bruce articulated the hyperscaler shift toward building fabrics from fixed-form-factor routers — the *Fabrics and Planes* framing — which fed SP Compass Designs and Cisco's decision to release the 8000 initially as a fixed-chassis platform. Tim Carnes, then VP Worldwide Systems Engineering: *"His 'fabric architectures' concepts helped jumpstart the Compass Design effort and led to BU prioritization of pizzabox platforms from both the Fretta and Spitfire product lines."* The same shift is now visible industry-wide, as Hyperscale Web, SP, and large enterprises disaggregate network layers that were previously chassis-based (Microsoft's T2 spine and DCI, Meta's RBB) `[pending — non-North America citations of large-scale pizza-box adoption, via Dell'Oro / Omdia or MIG / Competitive Intelligence]`. *More details are located in the Business Impact section of this document.* |
| **Global training and enablement** — 2020 – present                         | Bruce delivers SRv6, SONiC, and cloud-native enablement across all three theaters: Tech Elevate sessions in NA, EMEA, and APJC; the December 2025 SRv6 operator roadshow and companion SE enablement workshop; SRv6 DC/AI workshops drawing ~80 attendees across Sales and BU; and a published **Cisco dCloud catalog** of self-service labs authored with Rob Murphy — a Cilium-SRv6 lab that walks a user through Cilium deployment and configuration from first principles, the SRv6 Cisco Live lab LTRSPG-2212, and SONiC-101 — alongside the public `srv6-labs` repository (**74 stars, 15 forks**). He also delivered *Intro to Isovalent* presentations to the Web and global SP data centre teams. His Cilium dCloud lab prompted an EMEA systems engineer to build a demonstration that reached the Cisco booth at MPLS World Congress, after which that engineer contributed production code to the Cilium project. *More details are located in the Leadership section of this document.* |
| **Cross-theater operator engagements** — 2024 – present                     | Bruce serves as architecture consultant to operators outside the Americas where greater subject-matter expertise is needed than the local team carries: **Evroc** (EMEA sovereign cloud — SONiC spine and leaf, Cilium, inter-site design without Layer 2 stretch), **Rakuten** (APJC — SRv6 SD-WAN underlay high-level design and the Unified SRv6 Fabric case), **NTT East** (APJC — SRv6 and Cilium consultation across two Cisco Live engagements), and **MTN Nigeria** and **DU UAE**, where topology and migration designs delivered through APJC systems engineer Sanjay Nanda produced approximately **$85,000 in avoided customer lab expenditure** and a **2,300-node SRv6 POC** — two national operators on two continents, for customers Bruce never met. `[verify figures with Sanjay Nanda]` *More details are located in the Business Impact section of this document.* |
| **Systems integrator enablement — World Wide Technology** — 2026            | Bruce is collaborating with **Dave Clough** to build WWT's own systems engineering strength in SONiC, SRv6, and AI network architecture — developing one of Cisco's largest integration partners' technical bench directly, rather than delivering a single workshop. Capability built this way propagates across WWT's entire customer base. `[verify scope; LoR candidate]` |

---

## Global Product and Technology Run Rate

Bruce has pushed each of the technology areas below forward at global scale — with customers directly, and inside Cisco through SE enablement, training, and close collaboration with engineering on roadmap and direction. The figures show the scale at which these technologies now operate; they are Cisco product-line figures, not individually attributed revenue, and each initiative above states the specific dated intervention behind them. Figures are `[pending]` until sourced from finance or the relevant product team.

| Technology area                         | Global run rate                  | Source                     |
| ----------------------------------------- | ----------------------------------- | ----------------------------- |
| Segment Routing / SRv6                  | `[pending]`                      | Finance or SR product team |
| Cisco 8000                              | `[pending]`                      | MIG                        |
| SONiC                                   | `[pending]`                      | SONiC product team         |
| Cilium / Isovalent since acquisition    | `[pending]`                      | Isovalent / Security BE    |
| **Cilium-SP pullthrough** *(validated)* | **~$34M Isovalent / ~$323M MIG** | Bruce's business case      |
| NaaS-attributed SP pipeline             | `[pending]`                      | —                           |

Cisco's own attribution to this arc: a **2025 Pinnacle Award to the SRv6 uSID team** for the technology's global market impact, presented at the ceremony in early 2026. The team numbered roughly 40 and was almost entirely Cisco engineering; **Bruce and DSE Craig Hill were the only two recipients from the sales organization.**
-e 

---


## Span of Influence

## How Bruce's Span of Influence Expanded

| Period           | Altitude and scope                                             | Evidence                                                                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2020**         | Production routing and data centre SME for Web and SP accounts | Account and theater engagements through MIG engineering                                                                                                                                     |
| **2021–2022**    | Cross-BU advisor                                                | SD-WAN product direction with SP-services API spec and CNWAN; SP Edge tiger team co-lead; PSE review subcommittee                                                                          |
| **2023–2024**    | Architecture-organization altitude                             | SR brain trust field lead; SONiC investment case; Americas PA/DA SONiC forum; Future Enterprise Segmentation tiger team; corporate development advisory                                     |
| **2024–present** | Cross-platform engineering engagement                          | SRv6 feature development across **IOS-XR, IOS-XE, NX-OS, SONiC, SD-WAN, SASE, ThousandEyes** (Synthetic Path Tracing patent) **and Cilium** — eight platforms, five business entities       |
| **2025–2026**    | Company and executive altitude                                 | Co-founder, **SSOS**, **UFA**, and **UPM** tiger teams; Web/Hyperscale representative for executive BU interlocks; FY26 Global Sales Technical Roadmap co-owner; EVPN Least Complexity issue reaches CPO Jeetu Patel via Brook Crossman; Cilium CRD accepted by engineering |

Bruce's influence inside Cisco comes from a specific vantage point: he has spent the better part of a decade deeply enmeshed in the architectures actually driving the industry — hyperscale DC and WAN, open NOS, host networking, and now AI fabrics — and that proximity to where the industry is headed is why he has been right often enough, early enough, that people from across the company ask what he thinks.

### How he thinks about it

Bruce reasons about networks the way a hyperscale architect does: holistically, and independent of vendor org charts and product silos. A data centre platform and a backbone platform are fundamentally the same kind of thing. Linux is an operating system; routing and switching are apps. In some places the topology is highly symmetric and concentrated into a small physical space; in others it is asymmetric, with far lower available bandwidth per square kilometre. The difference is one of degree, not of kind.

Cisco's engineering organization is divided into places in the network — campus, DC, WAN, security — a structure that mirrors how the industry organized itself a decade ago. Competitors including Arista, Juniper, and Nokia have identified the gap that structure now creates and sell directly against it, offering a single, unified architecture across campus, DC, and WAN where Cisco sells several. Much of Bruce's internal-facing work has been a sustained effort to close that gap from the inside, bringing Cisco's architecture into line with where the hyperscaler and AI-driven market has already gone: **unified SRv6 forwarding** end to end rather than per-domain encapsulations, **fixed-form-factor fabrics** in roles convention reserved for chassis, **flat low-diameter topologies** in place of hierarchy, and **the host as a first-class network participant**. He applies the same reduction to policy — a firewall, an access control list, and a Layer 3 VPN are all ways of forwarding data *intentionally* rather than blindly, one problem rather than several.

That thinking is now formalized in three tiger teams Bruce co-founded. **Single-Secure-OS (SSOS)** argues for a single Linux-based network operating system in place of NX-OS, IOS-XR, and IOS-XE. The **Unified Forwarding Architecture (UFA)** is the SRv6-end-to-end effort described above, carried as a named initiative. The **Secure Network Policy Framework (SNPF)** embeds identity into that same forwarding plane so enterprise segmentation (SGT) and hyperscale transport share one policy model rather than two. Bruce is also advocating — a position still in progress, not yet realized — that Cisco invest directly in AI host networking, developing SmartNICs and a scale-up Ethernet solution to compete directly with Nvidia, AMD, and Broadcom, and pushing each successive silicon generation to market on a competitive timeline so Cisco does not concede addressable market to those competitors by arriving late.

### Technology domain expertise

1. **Mass Scale Infrastructure** - Hyperscale routing, data center, and AI network architecture
2. **Programmable transport** — Segment Routing and SRv6 uSID, end to end
3. **Cloud-native and host networking** — eBPF, Cilium, Kubernetes CNI
4. **Open network operating systems** — SONiC, Linux NOS strategy, disaggregation
5. **Enterprise identity and policy** — SGT, segmentation, the Secure Network Policy Framework (SNPF)

---

## Internal Influence — Initiatives and Relationships

| Initiative and date                                                | Impact                                                                                                                                                                                                   |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **SR field lead** — 2020 – present                     | Cisco's Segment Routing engineering organization under Fellow **Clarence Filsfils** sets architecture direction for the transport portfolio and, increasingly, for how Cisco competes in AI infrastructure. Bruce has been one of a small number of trusted field voices in it for nearly a decade. After his *Scaling the Cloud to a Billion Servers* presentation at an internal workshop in 2020, Filsfils tasked him with leading Cisco's **hyperscale SRv6 market entry**. He acts as the field broker between SEs and Clarence's team, is credited in the contributor acknowledgements of three chapters of the SRv6 book, and has driven product decisions including uSID block scale and static uSIDs in IOS-XR and uSID support in SONiC. *More details are located in the Innovation section of this document.* |
| **Host networking and the Isovalent acquisition** — 2021 – present | Bruce has argued for years that Cisco needed a presence at the workload boundary. He advocated acquiring Isovalent from 2021, recently built the Cilium-SP investment case (**~$34M Isovalent / ~$323M MIG pullthrough**), and authored the multi-use-case Cilium CRD that **Cisco engineering has accepted and is working to prioritize**. **Thomas Graf**, Cilium co-creator and Isovalent founder, can attest. *More details are located in the Innovation section of this document.* |
| **SD-WAN, SSE, and enterprise platforms** — 2020 – present         | Bruce developed relationships and influence with senior engineers in the SD-WAN, Cisco Secure Access, and the enterprise security portfolio. He established himself as a strategic advisor and SR/SRv6 SME to Alberto Rodriguez-Natal leading the CNWAN project, and proposed the SD-WAN Service-Provider-API use the SR Binding-SID approach rather than legacy DSCP mappings, collaborated with Rupak Chandra on SRv6 for Cisco Secure Access, and served as cloud-native SME on demand to security and SD-WAN Distinguished Engineers Steve Wood and Errol Roberts. Bruce is a named inventor on the resulting patent, *Underlay Network Traffic Steering* (granted October 2024), filed by SD-WAN engineering — a business entity he does not belong to. *More details are located in the Innovation section of this document.* |
| **SRv6 with SGT and the Secure Network Policy Framework (SNPF)** — 2022 – present | Cisco carried identity in one architecture and scale in another, and the two never met. Working the Future Enterprise Segmentation tiger team, Bruce recognized that an SGT and a uSID are both 16 bits, and designed the architecture that unifies them. He co-founded the **Secure Network Policy Framework (SNPF)** tiger team with PSE Josh Merrill to carry the idea forward, and the two presented SRv6+SGT to Matt Gillies, and brought in ISE Distinguished Engineer Darren Miller. **By December 2025 the ISE organization had committed** to SRv6 SGT and a Secure Network Policy Framework (SNPF). Over the course of several mindshare-building engagements at Verizon, AT&T, and T-Mobile the concept has been enthusiastically received. *More details are located in the Innovation section of this document.* |
| **Single-Secure OS (SSOS) working group co-founder** — 2024 – present    | Cisco had converged its hardware on Silicon One while its software remained fragmented across NX-OS, IOS-XR, and IOS-XE, a fact that is ruthlessly exploited by competitors like Arista and Juniper with stories built around single-OS + single management platforms. No business entity owned the problem and no forum existed to raise it. Bruce co-founded SSOS with DSE and PSE peers **Brenden Buresh, Craig Hill, Virginia Teixeira, and Rob Murphy**, framing the multi-year path toward a Linux-based NOS with containerized routing, switching, and policy applications driving NPUs and Cilium/Tetragon/eBPF to secure the OS. |
| **Open NOS and SONiC strategy** — 2023 – present                   | Bruce led the Americas PA/DA SONiC forum (Dec 2023), building field-architect consensus across Cloud, SP, Enterprise, and Public Sector, and bridges Silicon One, Cisco 8000, SONiC, and AI-backend engineering. Sustained relationships with **Vijay Tapaskar** and **Mani Veerachamy** (SONiC on Cisco 8000) and Cisco Fellow **Praveen Bhagwatula**. He also drove the SONiC with Cisco Secure Workload and SONiC with Cilium/Tetragon POCs, demonstrating to MIG engineering leadership a path to aligning SONiC with Cisco's Live Protect strategy on NX-OS, IOS-XE, and IOS-XR. *More details are located in the Innovation section of this document.* |
| **SP Network-as-a-Service and Project Yukon** — 2021 – 2024        | Bruce originated the internal argument that service providers should expose network capability for **cloud-like consumption** rather than just selling commodity circuits, and carried it through the NetCo/ServCo work with EU DSEs Brian Meaney and Virginia Teixeira. SP NaaS architecture has been adopted by Bell Canada and is being planned at Verizon and AT&T. *More details are located in the Business Impact section of this document.* |
| **Executive interlocks and roadmap ownership** — 2025 – present    | Bruce is the **Web and Hyperscale representative for executive business entity interlocks**, and co-owns **FY26 Global Sales Technical Roadmap** and BE Interlock Process responsibilities alongside Web SE Director **Tyler Nielson** and Web PSEs **Rob Murphy** and **Masi Mohammed**, setting the technical asks for AI, SRv6, and SONiC at sales-organization altitude. He also co-prepared the **EVPN Least Complexity readout** with an informal group of PSEs and DSEs; **Brook Crossman delivered it to Chief Product Officer Jeetu Patel**, who committed to fixing the underlying problem and scheduled regular check-ins with Brook to track it. |
| **Corporate development advisory** — Jun 2024                      | Cisco corporate development engaged Bruce as technical consultant on **AI tier-2 and neo-cloud equity investments** (Vladimirs Sazonovs, and sales leaders Lauren Johnson, Ryan Houska). `[Bruce to confirm outcome with Ryan and Vladimirs]` |
| **Competitive and portfolio intelligence** — 2023 – 2026           | **Only member from the sales organization** on Cisco CX's SL-OnDemand tiger team, led by CX DE Subha Dhesikan. Bruce collaborated with CX architects on a proposal for a CX-managed *cloud-like consumption of network services* solution and delivered the readout to CX executives in March 2024. Consultant to the Security business entity on Portfolio Innovation Areas (Feb 2026, with Craig Connors, Mike Lake, Errol Roberts). Authored and delivered *Combatting Disaggregation with Network Service Innovation (SRv6)* to the full ASP organization, repeated at TMC Innovation Hour by request. |
| **PSE review subcommittee** — 2021 – 2024                          | **Three years as a voting member**, evaluating PSE candidates against the promotion standard rather than only preparing them to meet it. *More details are located in the Leadership section of this document.* |

---

## Executive and Fellow Relationships — Engineering and Product

| Name                     | Role                                                        | Domain                                    |
| --------------------------- | ---------------------------------------------------------------- | -------------------------------------------- |
| **Clarence Filsfils**    | Cisco Fellow                                                 | Segment Routing and SRv6                  |
| **Praveen Bhagwatula**   | Cisco Fellow                                                 | SONiC                                      |
| **Rakesh Chopra**        | SVP Engineering, Silicon                                     | Silicon One and future generations        |
| **Kevin Wollenweber**    | SVP/GM Engineering, MIG and Data Center                      | SONiC and SRv6 investment                 |
| **Gurudatt Shenoy**      | SVP Product Management, MIG                                  | Product direction                         |
| **Vijay Tapaskar**       | VP Engineering, MIG                                          | SONiC on Cisco 8000                       |
| **Thomas Graf**          | VP Engineering, Security (Isovalent founder)                 | Host networking, eBPF                     |
| **Samir Parikh**         | VP Product and Strategy, AI Infrastructure (MIG/DC/Cloud)    | *Developing relationship* — AI infrastructure direction |
| **Craig Connors**        | CTO, Infrastructure and Security Group                       | *Developing relationship*                 |

## Sales Leadership Relationships

| Name                | Role                                    |
| ---------------------- | ------------------------------------------ |
| **Marcus Moffett**  | VP Solutions Engineering, Americas      |
| **Mike Witzman**    | VP Solutions Engineering, Public Sector |
| **Brad Bonin**      | VP Solutions Engineering, Enterprise    |

*Plus the DSE/PSE peer network below, and the sponsorship candidates in [08-sponsorship.md](https://github.com/brmcdoug/DSE/blob/main/08-sponsorship.md).*

## Customer and Partner Relationships

These are sustained working relationships with senior customer architects — most have been carried across multiple engagements documented in Business and Global Impact.

| Name                                    | Role                                          | Account            |
| ------------------------------------------ | -------------------------------------------------- | --------------------- |
| **Mohan Nanduri**, **Gaurav Thareja**   | AI and Frontend DC architects                  | Microsoft           |
| **Abderrahman Jouhari**                 | Senior Architect                                | Oracle              |
| **Shiv Patel**                          | VP, Architecture                                | CoreWeave           |
| **Luay Jalil**                          | Fellow                                          | Verizon             |
| **Gyan Mishra**                         | Associate Fellow                                | Verizon             |
| **Nicklous Morris**                     | Senior Architect                                | Verizon             |
| **Mike McNamara**                       | VP, Network Engineering                         | Dish / Boost Mobile |
| **Dave Clough**                         | Director, Solutions Engineering                 | WWT (partner)       |

## Cross-Organization Peer Network

Bruce's span rests on a habit rather than an assignment: over two decades he has built and maintained working relationships with senior SEs, PSEs, and DSEs across Cisco without regard to geography or vertical alignment, sustaining them for the learning and idea exchange as much as for any engagement. Most of the Global Impact section is downstream of this.

| Peer                  | Role                                                | Shared work                                                                                               |
| ------------------------ | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| **Brenden Buresh**    | DA, GES Office of the CTO                           | SSOS co-founder; DC/NX-OS tiger team; Adobe Cilium POC                                                    |
| **Craig Hill**        | DSE, US Public Sector                               | SSOS co-founder; Future Enterprise Segmentation; co-recipient, 2025 Pinnacle Award                        |
| **Virginia Teixeira** | DSE, EMEA                                           | SSOS co-founder; DCN and transport/AI convergence                                                         |
| **David Jansen**      | DSE                                                 | SP Edge tiger team; Americas SONiC forum                                                                  |
| **Brian Meaney**      | DA, EMEA CTO                                        | MCNS, NetCo/ServCo, NaaS architecture                                                                     |
| **Mike McPhee**       | DSE                                                 | PSE review subcommittee                                                                                   |
| **Marina Ferreira**   | PSE                                                 | Future Enterprise Segmentation; DC/NX-OS tiger team                                                       |
| **Brian Shlisky**     | DSE                                                 | Host-networking, Cilium/Tetragon on SONiC POC                                                             |
| **Jeffry Handel**     | DSE                                                 | UFA co-founder                                                                                             |
| **Christian Martin**  | Cisco MIG hyperscaler architecture *(formerly OCI)* | Low-diameter fabric research; WMP-PolarFly — an external research partnership that became an internal one |

---

## The Four Rocks, from the Inside

The same four architectural campaigns summarized in the Executive Overview are where this section's influence actually concentrates:

1. **A unified network operating system (SSOS)** — one Linux-based NOS in place of NX-OS, IOS-XR, and IOS-XE. *Outcome: SONiC is the proof of concept; SRv6 on SONiC shipped for the Cisco 8122, June 2026.*
2. **One forwarding architecture, end to end (UFA)** — SRv6 uSID across IOS-XR, IOS-XE, NX-OS, SONiC, SD-WAN, and the host. *Outcome: 2025 Pinnacle Award; platform alignment across six product lines.*
3. **Unified Policy and Identity** — one identity-and-policy model on top of UFA's forwarding plane. *Outcome: ISE committed, December 2025.* `[verify PM attribution]`
4. **Host networking** — closing the gap Bruce identified between the network's control point and the workload. *Outcome: Isovalent acquisition, 2024; SmartNIC and scale-up Ethernet advocacy in progress.*
-e 

---


## Industry Impact

## Industry Impact Arc

Bruce's external work rests on three positions he has carried publicly since before the industry agreed with them: the network's control point has moved to the host, so Cisco's presence there is a must; investing in open source — for NOS, tooling, and automation — earns industry credibility that drives product revenue, often faster than closed development does; and SRv6 is much more than a feature set, it's a platform for operator service innovation. His partnership with the SR engineering team includes many examples of this thinking (SR-Apps, etc.), and he presented the argument directly to the Americas SP organization as *Combatting Disaggregation with Network Service Innovation (SRv6)* at the TMC Innovation Hour (Sep 2025, repeated by request Dec 2025).

---

## 1. Publications and Standards-Adjacent Work

Bruce published the **[first public description and demonstration of SRv6 uSID on SONiC](https://www.segment-routing.net/blogs/srv6-usid-on-sonic/)** (segment-routing.net, May 2023) — the industry's first SRv6-on-open-NOS narrative, and the reference point the later multi-vendor uSID conversation built from. That later conversation is Alibaba-led; Bruce is not on Alibaba's account team, but his May 2023 publication preceded it, and the Cisco-side engineering validation the cross-vendor narrative rests on is his.

His close work with the SR engineering team led to an invitation to edit chapters of *Segment Routing Part III: SRv6* (Filsfils et al.) — specifically the SRv6 services and service-chaining chapters, the material closest to his own "platform for innovation" framing. He is credited in the book's contributor acknowledgements rather than as a cover author. [Publisher listing](https://www.amazon.com/Segment-Routing-Part-III-SRv6/dp/B0DNNCMLD3)

Bruce's May 2022 SP360 post was his contribution to a blog series on the Future of SP Networking, curated by Brook Crossman's PSE/DSE team — the post introduced **cloud-like consumption of network services**, framing that predated the network-as-a-service movement the SP industry adopted in 2024–2025 by two to three years. The series went on to become a repeat panel session at Cisco Live US and EU. `[confirm exact panel name and years for citation]`

---

## 2. SRv6 for AI and the MRC Convergence

Multipath Reliable Connection is an open industry specification born from a need OpenAI identified in late 2023, convening AMD, Broadcom, and Intel to solve it. Bruce is not an author of MRC, and the package does not claim otherwise. Its relevance to his record is convergence, not authorship, on two points. First, OpenAI convened **NIC and silicon vendors, not switch vendors** — external confirmation that the industry moved the control point to the host, exactly where Bruce had been arguing it belonged since 2013 and had named the *host-networking air-gap* since 2021. Second, **MRC adopted SRv6 as its path mechanism**, and Oracle's 2026 Acceleron materials cite the same pattern — the architecture Bruce spent five years advocating internally at Cisco and to hyperscalers became the transport substrate of the industry's AI networking standard.

Bruce made the combined architecture teachable rather than merely correct: he built the **[srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator)** so operators could model MRC-with-SRv6 directly, and engaged in numerous SRv6-for-AI-backend "kickoff" conversations at **OCP Summit (Oct 2024)** with Oracle, Microsoft, Voltage Park, Bell Canada, and Cloudflare — the first public customer discussion of the architecture. A proposed **OCP Summit 2026** session on SRv6 uSID multi-tenancy, co-authored with Microsoft, was declined; the underlying paper is still being finished for publication elsewhere. This is the same arc the **2025 Pinnacle Award** recognized at company level (detail: Executive Overview and Innovation section).

External recognition of the arc has come from people close to the work rather than from Cisco marketing. Ianik Semko, Cisco's SR product manager, at IETF Vancouver (2024): *"I call you the 2030 guys."* Bob Gisiger, May 2026: *"this is super cool, it's your vision for years of host based SRv6 coming to life in a big way."*

**References:** [OpenAI — Resilient AI Supercomputer Networking using MRC and SRv6](https://cdn.openai.com/pdf/resilient-ai-supercomputer-networking-using-mrc-and-srv6.pdf) · [Broadcom — MRC: The Journey from Concept to Open Specification](https://www.broadcom.com/company/news/articles/ai-infrastructure/mrc-the-journey-from-concept-to-open-specification) · [Cisco — MRC and SRv6](https://blogs.cisco.com/datacenter/mrc-and-srv6-how-foundational-networking-innovations-are-enabling-the-next-generation-of-ai-supercomputers)

---

## 3. Open Source

Bruce is **administrator and curator of [github.com/segmentrouting](https://github.com/segmentrouting)** and launched **[srv6-labs](https://github.com/segmentrouting/srv6-labs)** (Dec 2023), offering operators the ability to rapidly deploy and validate SRv6 scenarios without vendor-specific tooling or hardware — to operate it themselves rather than trusting a vendor demo. The labs reached **~40,000 LinkedIn views in the first week**, drew a citation from **[ipspace.net](https://blog.ipspace.net/2023/12/worth-reading-srv6-labs.html)**, and picked up contributions from engineers at **Verizon and Oracle**. The repository stands at **74 stars, 15 forks**. Companion repos — [srv6-msft](https://github.com/segmentrouting/srv6-msft), [srv6-oci](https://github.com/segmentrouting/srv6-oci), [srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator), [polarfly](https://github.com/segmentrouting/polarfly) — extend the same open method into hyperscaler co-development.

Bruce took **[cisco-open/jalapeno](https://github.com/cisco-open/jalapeno)** through Cisco Legal into public release; it now sits on independent industry maps such as the [Steinzi network automation landscape](https://steinzi.com/network-automation-landscape/), and its BMP demo was referenced for the MPLS World Congress 2026 community by Cisco Principal TME Fred Cuilar and Severin Dellsperger, associate professor at OST University in Zurich. Bruce also owns and maintains the **[github.com/jalapeno](https://github.com/jalapeno)** organization (15+ repositories) built on top of it. Strategic impact: Jalapeno functions in the industry as a reference architecture for programmable multi-domain services, taught and demonstrated outside Cisco's own labs *(product/IP detail: Innovation)*.

The pattern repeats at Cisco Live. Bruce and Rob Murphy's **LTRSPG-2212** pioneered using GitHub itself as the lab guide and config store — now common ILT practice — and they declared the lab open source outright, so attendees could fork it and train their own colleagues with it. It carries **16 stars and 7 forks** from customers doing exactly that: [github.com/jalapeno/SRv6_dCloud_Lab](https://github.com/jalapeno/SRv6_dCloud_Lab).

---

## 4. Operator Community

Perhaps Bruce's strongest form of industry influence is not Cisco presenting as a vendor — it is an **operator presenting architecture Bruce built, or co-built with them, as their own.** As he frames it, a customer making the case at an industry conference is much more impactful than the vendor making it.

The clearest example is **Dan Bernier, Senior Architect at Bell Canada.** The partnership started when Bruce's Jalapeno and host-based SR/SRv6 session at KubeCon (Nov 2019) drew Bernier in, and grew over years of onsite workshops and regular brainstorming sessions into a shared vision for turning a traditional tier-1 operator into a cloud-like NaaS business. Bernier has since carried slides and concepts the two developed together into his own industry talks at **KubeCon (2022–2023)** and **MPLS World Congress (2023)** — Cisco's architecture reaching the industry through an operator's mouth rather than a vendor's.

| Year         | Bruce's role                                                                      | Outcome                                                                    |
| ------------ | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **MPLS World Congress, Apr 2023** | IPR, slides, diagrams featured in **Bell, Verizon, and Rakuten** presentations      | Three tier-1 operators independently delivered the same architecture `[confirm session titles]` |
| **MPLS World Congress, Mar 2024** | **Editor and advisor**, Verizon's MPLS-WC SRv6 presentation, built on srv6-labs material | Tier-1 operator delivers Bruce's architecture on the main stage; open-source lab methodology carried into it |
| **Mar 2025** | Presented **SRv6 for the AI backend**; Kaliwoda booth demo; KPN consulting          | Global operator visibility on the AI fabric architecture                   |

Bruce is a **recurring invitee to Cisco SR engineering's lead-operators workshops** alongside Microsoft and OCI peers — not always as a formal presenter, but relied on to drive mindshare and surface new ideas in the working sessions and hallway discussions that set the agenda for what those operators hear next. A second relationship began the same way: an in-person conversation with Verizon's **Nicklous Morris** at an IETF meeting, about host-based SRv6 — not a working-group presentation, but the kind of hallway exchange IETF exists to enable. That conversation has continued through multiple follow-on discussions, now including Verizon Fellow **Luay Jalil**, and the group is planning a **Cilium-SRv6 proof-of-concept/demo** in the coming months *(tracked in todo.md; also carried in Business Impact's Verizon entry)*. He also coordinated and hosted the **SRv6-for-AI workshop in San Jose (Apr 2025)** for Cisco MIG engineering and Web SE leadership, bringing in **Rita Hue** (SONiC Principal SWE Manager, Microsoft) and **Eddie Ruan** (Director, Network System Software, Alibaba Cloud) as guest speakers — convening two competitors' engineering leadership in front of Cisco's own product organization, so the customers made the case for the architecture more persuasively than Cisco could make it to itself. A December 2025 follow-up took the same audience into use cases against an actual roadmap.

---

## 5. Practitioner Education

Bruce was named **Distinguished Speaker at Cisco Live EMEA 2023** (5.00/5.00) and has held scores between 4.72 and 5.00 across CLEU and CLUS since, including *Beyond the Switchport* with Chris Lapp (CLUS 2026) and a CLUS 2025 lab built on an SRv6 PyTorch plugin he coded himself. Several sessions have been invited back on the strength of their feedback and scores — LTRSPG-2212 ran at CLEU in 2023, 2024, 2025, and 2026 — and two produced documented outcomes outside Cisco Live itself: a CLEU 2026 Meet-the-Expert conversation led the **Province of New Brunswick** to abandon its SR-MPLS plan for an immediate SRv6 migration (Global Impact), and **Boost Mobile** ran a Cilium SRv6 POC after CLUS 2025 (Business Impact). *(Full session log, scores, and ILT delivery mechanics: Leadership section.)*

Bruce co-developed and co-taught an O'Reilly Live Event, **[Build Your Own Networking Lab](https://www.oreilly.com/live-events/build-your-own-networking-lab/0642572002817/)**, with **Russ White** — a collaboration that grew out of the FRR SRv6 L3VPN lab Bruce built for White during the Akamai engagement (Oct 2023), and independent validation of the reproducible-lab method he established with srv6-labs. The course teaches ContainerLab-based multi-vendor lab building (Cisco, Juniper, FRR) through to Segment Routing and telemetry, and O'Reilly's own instructor bio credits Bruce's "14 years working with some of the world's largest Web/OTT and Telco operators." Delivered live to hundreds of engineers worldwide; materials also public at [github.com/brmcdoug/open-source-labbing](https://github.com/brmcdoug/open-source-labbing).

Bruce also established an academic pipeline with **OST University, Zurich** (2020–2022): students built on Jalapeno as a development platform, producing an open-sourced API gateway (2021) and an SRv6 service-chaining demo app (2022) under his guidance. Student **Severin Dellsperger** went on to build **Hawkv6**, a distributed controller Cisco's EU CTO team (Bart Van De Velde, Andreas Enotiadis) has expressed interest in productizing — a research-to-field-validation pipeline, not a one-time guest lecture.
