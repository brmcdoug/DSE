# Executive Overview and General Information about Candidate

**Cisco Distinguished Solutions Engineer Nomination — Bruce McDougall**
*August 2026. Finance-validated Web/Hyperscale segment bookings (2022–2026) integrated; account-level, SP, and product run-rate figures marked where pending.*

---

## The Case in Brief

Ask the people who work with Bruce McDougall what he does, and the answers arrive from three different directions. Account teams describe an architect who tells them what is coming two and three years out and gets them ready for it. Customer architects at the largest operators in the world describe a peer who understands their scale, their tooling, and the business pressure behind their requirements. Cisco's product engineers describe a field voice who arrives with the roadmap argument already made, and the evidence to back it.

He has been doing that from the same three positions for a decade, and it has produced a consistent pattern: an architecture Bruce argued for early, that Cisco was not ready to build, that eventually shipped.

The DSE criteria open with a general guideline placed above every other category — *demonstrate how you have been a force multiplier throughout the organization: identifying new technology and industry trends, building the necessary field enablement, aligning strategic stakeholders and investment, and leading lighthouse customers to drive field adoption.* Bruce's record maps onto it closely enough to use as the structure of this overview.

| The criterion | Bruce's record |
| :--- | :--- |
| **Identify new technology and industry trends** | Identified Cisco's **host-networking air-gap** in 2015, after observing that hyperscalers had moved the network control point into the host. Designed an SR elephant-flow balancer in 2017 for the problem the industry took up in 2024 as SRv6-for-AI. Recognized in 2019 that SRv6 was not a protocol improvement but a platform for scale and operator service innovation, and has been all-in since. Called the SONiC credibility inflection in 2023. |
| **Build the necessary field enablement** | Owner or developer of `github.com/segmentrouting`, `cisco-open/jalapeno`, the `jalapeno` org (15+ repos), and `cisco-asp-web` (co-owner, 14 repos); the MRC emulator built within a week of OpenAI's announcement; VXR and Containerlab environments; dCloud labs; and Cisco 8000, SONiC, and SRv6 training delivered across NA, EMEA, and APJC. |
| **Align strategic stakeholders and investment** | The SONiC SRv6 investment case that reversed engineering's position — the objection was that **nobody runs SRv6 in the data centre** — and **shipped on the Cisco 8122 in June 2026**. The Cilium-SP case built from worldwide account data: **~$34M Isovalent / ~$323M MIG** pullthrough, finance-validated. Isovalent acquisition advocacy from 2021. |
| **Lead lighthouse customers and drive adoption** | The hyperscalers were already running host networking and open NOS — Meta on FBOSS, Microsoft on SONiC. Bruce's contribution was the other direction: **bringing Cisco to where hyperscaler thinking already was**, then proving it at Microsoft, Meta, Oracle, CoreWeave, and Bell Canada. |

Two things about the record are worth stating at the outset.

**Much of it compounds through other people.** Bruce is in the sales organization and spends as much time with customers as he can. But his highest-leverage mode is equipping colleagues: he gives account systems engineers the architecture, the education, the repositories, and the labs, and they carry it to their customers and win with it. The **$17M Meta backbone re-entry** is the clearest instance — Bruce pioneered the SL-API technique at Microsoft, taught it to the Meta account team, built the environment they validated it in, and never presented to Meta himself.

**And the industry arrived where he had been standing.** Five years ago service provider and hyperscale operators largely dismissed SRv6 as not ready. Today SPs almost universally name it their strategic direction, and most hyperscalers agree. When OpenAI, AMD, Broadcom, and Intel published the MRC specification for AI-scale transport, they chose SRv6 as the path mechanism — independent confirmation of a position Bruce had been arguing inside Cisco and with operators since 2019.

> *"Bruce continues to have a significant impact leading frontier projects in AI forwarding and teaching others. His innovation is on pace to break (ASP) records with patents being filed and awarded and he sets the standard for teamwork and technical depth. The recent recognition he received in the Pinnacle awards speaks to his technical capabilities and his strong reputation for teamwork. Cisco is lucky to have him teaching our teams and customers, representing us externally and driving innovation in the portfolio."*
> — **Brook Crossman**, VP Systems Engineering, ASP and Web — Bruce's direct leader for five years through June 2026

---

## Career Path

| Role / Title | Dates |
| :--- | :--- |
| Customer Engineer, Siemens Business Communications | 1997 – 1999 |
| Network Engineer, Affiliated Computer Services | 1999 – 2003 |
| Network Architect, Expedia Group | 2004 – 2007 |
| Systems Engineer II / III, Cisco — TW Telecom account team | 2007 – 2012 |
| Consulting Systems Engineer, Cisco — USSP TCS Select | 2012 – 2015 |
| Systems Architect, Cisco — Americas Web / Hyperscale | 2015 – 2020 |
| **Principal Systems Engineer**, Americas Service Provider + Web | Aug 2020 – Jun 2026 |
| **Principal Solutions Engineer**, Global — Lead Cloud-SP Architect, Global Solutions Engineering | Jun 2026 – present |

**Education:** BA, University of Washington (1996)
**Certifications:** CCIE Service Provider #35169 (2012)
**Public service:** Anacortes City Council since 2017; Mayor Pro Tem 2020–2021

---

## Candidate Portrait

Bruce McDougall was a network operator before he became a solutions engineer. At the Expedia Group he was evaluating MPLS in the data centre in 2006, hunting for scale beyond the enterprise tooling of the era. That origin still shapes how he decides what to work on. He starts from the operator's chair — what would be simplest to run, cheapest to own, most extensible, and longest-lived — and from what would leave the industry healthier. **Then he asks how Cisco gets to the centre of it.** Working in that order is why operators trust the answer.

His expertise spans hyperscale and cloud-native networking, AI/ML fabrics, Linux and Kubernetes, open network operating systems, network-as-a-service, and Segment Routing and SRv6. Combined with deep service provider architecture experience, that dual SP and Web/hyperscale specialization is unique in Cisco's sales organization.

He reasons about networks topologically rather than by product category. A data centre platform and a backbone platform are not different kinds of thing — both move data, and the difference is symmetry and density. Every large vendor organizes its portfolio into places in the network, and its engineering teams mirror that division; working outside that framing is what lets Bruce see the seams. It is also how he thinks about policy: a firewall, an access control list, and a Layer 3 VPN are all ways of forwarding data *intentionally* rather than blindly, which is what produced the Policy Plane and SRv6-with-SGT.

Hyperscale operators do not think of themselves as customers. They are deeply technical teams making purchasing decisions worth hundreds of millions or billions of dollars, driven by time to market. Bruce meets them as a peer because he can hold both halves of their problem at once: the architecture — fabrics, disaggregation, open source, SRv6 — and the operations, where the objective is to simplify and to make the network fit the dominant Linux toolchains rather than sit in its own isolated silo.

For nearly a decade Bruce has been one of a small number of trusted field voices in Clarence Filsfils' Segment Routing engineering organization. Cisco awarded a **2025 Pinnacle Award to the SRv6 uSID team** for the technology's global market impact; the team numbered roughly 40 and was almost entirely Cisco engineering, and **Bruce and DSE Craig Hill were the only two recipients from the sales organization.**

He is also, by consistent report, exceptional to work with. Brook Crossman's assessments return to it cycle after cycle — *"many report how collaborative he is"*, *"simply put, everybody wants to work with him."* Bruce has issued **22 Connected Recognition awards to peers** and received 37. In June 2026 he moved to Matt Gillies' Global Solutions Engineering team as lead Cloud-SP architect — formal recognition that his impact already operated globally.

### Quantified highlights *(Aug 2020 – present)*

| Dimension | Evidence |
| :--- | :--- |
| **Segment revenue** | **$10.9B** Americas Web/Hyperscale bookings **2022–2026** in Bruce's theater; **$5.3B** in 2026 alone. Org-level figures, not individual attribution |
| **Sustained account growth** | **Microsoft Cisco 8000 WAN revenue of ~$65.9M (FY25) and ~$60M (FY26)**, sustained through a multi-year partnership with Senior SE Pan Chou and the Microsoft WAN team. Frontend data centre growth on SONiC and Cisco 8000 `[finance figures pending]` |
| **Silicon One component sales** | Direct Silicon One ASIC sales of **$35.6M (FY25)** and **$44.3M (FY26)**. Bruce was SE technical lead with MIG and Amazon developing the silicon and SDK functionality to Amazon's specification; Amazon itself bought only a few hundred thousand dollars' worth, but the motion it matured went on to sell **~$80M combined to Meta and Alibaba** in 2025–2026 |
| **Production wins** | Meta **$17M** BBF first production order (Feb 2026); Bell Canada **400 CPE initial purchase plus $1.8M core revenue** (May 2026) |
| **Product delivery** | **SRv6 on SONiC, Cisco 8122** (Jun 2026); SRv6 uSID on Nexus; SRv6 on Cisco SD-WAN forthcoming |
| **Intellectual property** | **6 issued US patents, 9 pending, 1 defensive publication** from **24 invention disclosures since Aug 2020** |
| **Recognition** | **2025 Pinnacle Award** — SRv6 uSID team; **Distinguished Speaker**, Cisco Live EMEA 2023 |
| **Open source** | `srv6-labs` 74 stars · `cisco-open/jalapeno` 78 stars · owner of the `jalapeno` org (15+ repos) · co-owner of `cisco-asp-web` (14 repos) |
| **Standards** | Editor, `draft-srv6ops-addressing-guidelines`; contributing editor, *Segment Routing Part III: SRv6* |
| **Talent** | **Six systems engineers promoted to PSE** — one as official mentee, five as advisor to their candidacies; three years on the PSE review subcommittee |

---

## Global Impact Summary

Bruce's impact moved from account, to region, to segment, to global — and in June 2026 into a global role.

What carries it is not a list of overseas customers but a set of architectures adopted across theaters. As **global field lead for SR-Apps**, Bruce co-developed with Cisco's SR engineering organization, which adopted his open-source Jalapeno project as its **development platform** during the R&D phase. On **end-to-end SRv6, including host-based and cloud-native**, Cisco's business units have agreed to support and join the end-to-end architecture — alongside the architectures they already support — and SRv6 is the transport substrate of the industry's MRC specification. On **open NOS and SONiC**, he published the first public description of SRv6 uSID on SONiC in May 2023 and the product shipped in June 2026. On **host networking**, he has been Cisco's most persistent **Isovalent and Cilium evangelist** since before the acquisition, carrying the case across business units and account teams, with SRv6 as one part of it. On **SP network-as-a-service**, his framing predated the industry NaaS movement by two to three years. And on **SRv6 with SGT**, he and Josh Merrill evangelized the concept across Cisco's business units and account teams to broad enthusiasm — including a commitment from the ISE organization.

Global training and enablement reaches all three theaters. Cross-theater operator engagements — Evroc, Rakuten, NTT East, Telia, Telstra, MTN Nigeria, DU UAE — draw him in where local depth does not extend that far.

*More details: [03-global-impact.md](./03-global-impact.md)*

---

## Span of Influence Summary

In August 2020 Bruce was a production routing and data centre SME for Web and service provider accounts. He now shapes product roadmaps in organizations with no reporting relationship to his own, and his technical judgment is solicited by corporate development, security, enterprise networking, and the office of the CTO.

**Four technology domains** — the criteria require at least two: programmable transport (SRv6 uSID end to end), cloud-native and host networking (eBPF, Cilium, Kubernetes CNI), open network operating systems (SONiC, Linux NOS strategy), and enterprise identity and policy (SGT, segmentation, the Policy Plane). Since 2024 he has driven SRv6 feature development across **eight platforms** — IOS-XR, IOS-XE, NX-OS, SONiC, SD-WAN, SASE, ThousandEyes, and Cilium.

The hardest evidence of that reach is co-authored intellectual property. Bruce has filed patents with several different engineering groups: **Underlay Network Traffic Steering** (12,120,027, granted Oct 2024), which he filed; **Core Network Support for Application-Requested Network SLOs** (12,009,998), filed by the SD-WAN engineering team with Bruce as co-inventor; **Synthetic Path Tracing of Segment Routed Networks** (12,289,210) with ThousandEyes engineers; and continuing work with the SR engineering team. He co-founded the **Single OS (SOSIE) working group** with DSE and PSE peers to address NOS fragmentation spanning Cisco's business units. He is the Web and Hyperscale representative for **executive BU interlocks**, owned the FY26 Global Sales Technical Roadmap, briefed **CPO Jeetu Patel**, and was engaged by **corporate development** on neo-cloud equity investments.

Sustained relationships run to Cisco Fellows **Clarence Filsfils** (SR/SRv6) and **Praveen Bhagwatula** (SONiC), to **Thomas Graf** (Cilium co-creator, Isovalent founder), and to **Vijay Tapaskar** and **Mani Veerachamy** in SONiC engineering. Underneath it is a habit rather than an assignment: over two decades Bruce has built and kept working relationships with senior SEs, PSEs, and DSEs across Cisco regardless of geography or vertical, sustained for the learning as much as for any engagement.

*More details: [04-span-of-influence.md](./04-span-of-influence.md)*

---

## Industry Impact Summary

Bruce advances a sustained vision externally, built on three elements. **Host networking** — the control point has moved to where the workload runs. **Open source** — for network operating systems, and equally for tooling, automation, and SDN; a visible open-source commitment also earns industry trust, and that trust drives product revenue. And **source routing**, which gives operators a platform for their own service innovation rather than a catalogue of vendor features.

He holds standards credentials: **editor** of the `draft-srv6ops-addressing-guidelines` IETF draft, participant in IETF SRv6-Ops, and contributing editor on *Segment Routing Part III: SRv6* (Filsfils, Abdelsalam, Camarillo, Clad, Michielsen). But the venues that now set direction in this field are open source and open hardware consortia, and the MRC timeline shows it: the work began in 2024, SRv6 for the AI backend was discussed publicly at **OCP in November 2024**, and the first IETF draft appeared in **July 2025 — largely in response to work already well under way.**

Bruce operates in all three venues. He published the **first public description and demonstration of SRv6 uSID on SONiC** (May 2023). He curates `github.com/segmentrouting`, launched `srv6-labs` (~40,000 first-week views, an ipspace.net citation, contributors from Verizon and Oracle), and open-sourced his Cisco Live lab so customers could fork it and train their own colleagues. He co-developed a four-hour **O'Reilly** course with **Russ White**.

The most durable form his external influence takes is other people advancing his architecture as their own. Bell Canada's **Dan Bernier** has presented concepts the two developed together at KubeCon and MPLS World Congress. Verizon's MPLS-WC presentation was built on Bruce's `srv6-labs` material. An EMEA systems engineer built a Cilium SRv6 demonstration from Bruce's lab, showed it at MPLS World Congress, and now contributes production code to the Cilium project. For a vendor architect, an operator making the argument is worth more than making it himself.

*More details: [05-industry-impact.md](./05-industry-impact.md)*

---

## Business Impact Summary

Bruce works three relationships at once, and the business impact comes from connecting them.

With **account teams**, mostly hyperscale, he works on technical and architectural strategy — educating and guiding them on what is coming and what to be ready for on a two-to-three-year horizon, while the teams run the near-term business. With **customer architects**, he works to understand requirements at a deep technical level, including the operational and commercial pressures behind them, and to extract as much horizon-2 and horizon-3 intelligence as those conversations will yield. With **Cisco product engineering**, principally MIG (the Mass-Scale Infrastructure Group), he works on long-term roadmap and product strategy, carrying what he has learned from the first two into investment decisions. Proof-of-concept and lab work, including customer co-development, is how he makes those arguments testable.

### Americas Web/Hyperscale segment bookings *(2022–2026, finance)*

Org-level figures for Bruce's theater. Not individual attribution.

| Customer | 2022 | 2023 | 2024 | 2025 | 2026 | Total |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Microsoft | $603M | $714M | $226M | $861M | $1.57B | **$3.97B** |
| Meta | $277M | $367M | $54M | $510M | $1.91B | **$3.11B** |
| Google | $404M | $103M | $108M | $287M | $1.05B | **$1.95B** |
| Amazon | $127M | $69M | $196M | $296M | $717M | **$1.41B** |
| Oracle | $4M | $45M | $230M | $146M | $21M | **$446M** |
| Apple + Web Platforms | $1M | $8M | $11M | $9M | $14M | **$42M** |
| **Total** | **$1.42B** | **$1.30B** | **$824M** | **$2.11B** | **$5.28B** | **$10.94B** |

| Customer | Signature outcome | Bruce's role |
| :--- | :--- | :--- |
| **Microsoft** | **Cisco 8000 WAN revenue ~$65.9M (FY25), ~$60M (FY26)**; SRv6 on SONiC **8122** shipped (Jun 2026); PhyNet, Octans, dRH; 1.6T WAN | Primary field architect since 2021; SL-API SWAN controller integration; multi-tenant AI fabric specification; sustained support to Senior SE Pan Chou and the WAN team |
| **Meta** | **$17M** BBF production order (Feb 2026); RBB committed to SRv6 | SL-API pioneer; VXR co-validation environment; pre-GA 8223 patch — delivered entirely through the account team |
| **Oracle** | SRv6 in limited production by end-2025; Acceleron and MRC | Lead SRv6-for-AI architect; low-diameter fabric studies |
| **Amazon** | Silicon One SDK and silicon functionality to Amazon's specification | SE technical lead with MIG; matured a component sales motion that later sold ~$80M to Meta and Alibaba |
| **CoreWeave** | Scope grew to ~10–12k switches | SONiC SME; lead SRv6-for-AI architect |
| **Bell Canada** | **400 CPE initial purchase plus $1.8M core revenue** (May 2026) | End-to-end SRv6, Cilium, and NaaS architecture — a partnership dating to 2019 |
| **Out-of-territory** | Geico ~$1.6M; Honeywell ~$2M; Province of New Brunswick migrated to SRv6 after one conversation | SONiC and SRv6 SME to theaters and accounts outside his assignment |

**Beyond bookings.** Bruce built part of the foundation the segment runs on. When he joined the Web team in 2016, Cisco was barely selling into hyperscale production networks and was read as an enterprise networking company. He established Cisco's credibility with those operators and was instrumental in building the systems engineering bench alongside it — the Web team now has three PSEs and multiple grade-12 SEs on each major account. He does not claim the revenue; he built part of what it stands on.

**On timing.** Several of the architectures in this package were validated by customers before Cisco could supply them. Microsoft and Oracle both began SRv6-for-AI deployments on competitor hardware, on the architecture Bruce had specified, because Cisco's silicon arrived after the decision window. Being early is only valuable if the portfolio can follow, and closing that gap is where Bruce believes his next few years of leverage sit.

*More details: [06-business-impact.md](./06-business-impact.md)*

---

## Innovation Summary

Bruce's inventions begin from operator empathy rather than product strategy, and most start as a brainstorm — his own or with a peer — that becomes an approved patent, a paper, or a working demonstration. Some begin as a declined disclosure and reappear years later in a shipping product, an acquisition, or an industry specification. Both paths are in the record, and the declines are among the strongest evidence in it: *SRv6 uSID Scheduled Fabric for AI/ML Clusters*, declined in 2023, describes the architecture that OpenAI, Microsoft, and Oracle converged on in 2025–2026, and a filing date cannot be retrofitted.

| Category | Evidence |
| :--- | :--- |
| **Patents** | **6 issued, 9 pending, 1 defensive publication** — four issued during the PSE period |
| **Disclosures** | **24 since Aug 2020** (36 lifetime) — a pace Brook Crossman called *"on pace to break (ASP) records"* |
| **Products** | SRv6 on SONiC (8122, Jun 2026); SRv6 uSID on Nexus; SRv6 on SD-WAN forthcoming; Cilium SRv6 features planned by engineering; SR-Apps, the precursor to SR IPM, path tracing, and the forthcoming D-SDN TE controller |
| **Acquisition** | **Isovalent / Cilium** — advocated from 2021; announced Dec 2023, closed 2024 |
| **Bold Bets** | **Jalapeno** — the only field-submitted project to advance past the first evaluation round; adopted by SR engineering as its SR-Apps development platform |
| **Specifications** | SRv6 uSID multi-tenancy for AI factories (131k GPUs per cluster); low-diameter fabric studies with Oracle |
| **Awards** | **2025 Pinnacle Award**; Cisco EN Hackathon 2022 winner |

*More details: [07-innovation.md](./07-innovation.md)*

---

## Personal Development Summary

Bruce took the PSE committee's feedback — expand beyond your Web and SP comfort zone — as a work plan, and proactively took on work nobody assigned him: SD-WAN and Cisco Secure Access, the Future Enterprise Segmentation tiger team, co-founding the Single OS (SOSIE) tiger team, Isovalent and security engineering, ThousandEyes, the EMEA peer network, CX, and the OST Zurich university collaboration.

The second choice was technical. A CCIE since 2012 with deep routing and transport expertise, Bruce chose to keep building rather than narrow — Kubernetes, Cilium and eBPF, Containerlab, Git workflows, dCloud publishing — which is why the labs and POC repositories in this package are running code that other people use. That investment compounds: years of self-training in Python, Go, and DevOps practice make him markedly more effective with agent-assisted development, because knowing precisely what he is building is what turns an agent into a development partner.

**Vaughn Suazo** is his DSE mentor.

*More details: [09-personal-development.md](./09-personal-development.md)*

---

## Leadership Summary

Bruce is known as a collaborative partner who shares credit and creates opportunities for other engineers.

- **Six systems engineers promoted to PSE** — Nacho Sanchez as his official mentee, and advisor to the successful candidacies of Rob Murphy, Roberta Maglione, Masiuddin Mohammed, Marina Ferreira, and Alessandro Breccia. He is **Christopher Luciano's** official mentor, targeting PSE in FY2028–2029. Three years on the **PSE review subcommittee**
- **Inspiring great work from others** — EMEA SE **Arkadiusz Kaliwoda** built a Cilium SRv6 demonstration after seeing Bruce's DCN Champions *Intro to Isovalent* presentation and working with his dCloud lab. He showed it at MPLS World Congress and now contributes production code to the Cilium project
- **A co-presenter who won Distinguished Speaker** — **Nico Michel**, at CLEU 2026, co-presenting and co-proctoring Bruce's lab
- **Programmes that continue to generate impact well beyond expectation** — ASP Lightning Talks, co-created with DSE John Mullooly, at Episode 23 after five years; the GitHub-first Cisco Live lab model, now common practice
- **Investment cases built from multi-stakeholder data** — Cilium-SP (~$34M / ~$323M), SONiC SRv6, and the Silicon One NPU generational TAM model
- **Community leadership** — Anacortes City Council since 2017, Mayor Pro Tem 2020–2021, during which the city built **the only community-owned fibre-to-the-home ISP in Washington State**

*More details: [10-se-community-leadership.md](./10-se-community-leadership.md)*

---

## Becoming a Distinguished Solutions Engineer *(candidate statement)*

Early in my career I was a network engineer and a Cisco customer before I joined the vendor side and became a solutions engineer. That background left me with real empathy for the operator experience. When I look at a question of technology or architecture I start with what I would want if I were the one operating it, and what would be the best outcome for the industry as a whole. Then I work out how Cisco becomes the centre of that. Doing right by the customer and helping the industry thrive is a credibility multiplier for Cisco, and it is something I work on every day.

I think of that work as **skating to where the puck will be** — and then staying there long enough to matter. Host networking, SRv6, open network operating systems, AI fabrics: in each case I formed a view years before the products caught up, usually while knowing full well the market was not ready yet. Being early is the easy part. The hard part is patience — spending years building credibility with engineering and with operators, making the same argument in a hundred rooms, and being willing to be the only person in a meeting who thinks a thing matters. I have been wrong about timing more than once. I have not yet been wrong about direction.

Promotion would not change the mission; it would widen the platform. As a DSE I would keep bridging IMI, SONiC, cloud-native security, and SP transport into one coherent story for AI factories and open NOS adoption. I would keep working the three relationships that make this job work — account teams on strategy, customer architects on requirements, and Cisco engineering on roadmap — with a larger remit on each. I would scale the enablement model so more engineers can co-develop with hyperscalers ahead of feature availability. And I would keep publishing open artifacts that accelerate adoption and hold Cisco accountable to the future we claim.

There is one more thing I want to keep doing. The best outcomes in this package are not mine alone. They belong to account teams who took an architecture and ran with it, to systems engineers who took a lab and made it their own, and to operators who made the argument better than I could have. Finding those opportunities for other people and then getting out of their way has produced more impact than anything I have done by myself, and I intend to keep at it.

---

## Direct Leader Summary

Bruce reported to **Brook Crossman** (VP, Systems Engineering, ASP and Web) for five years through June 2026, and to **Matt Gillies** (Global Solutions Engineering) since. The package may carry input from both.

Across six talent assessment cycles Brook has rated Bruce as meeting expectations on Business Outcomes and Guiding Principles, describing him as ASP's **centre of gravity for SRv6 and AI-forwarding innovation**, the leader in the Segment Routing domain on the direct field team, and someone who *"represents Cisco incredibly well in front of customers inside and outside of ASP."* Brook notes the volume of requests for Bruce's help from outside the segment, that engineering forums trust him as a representative, and that *"simply put, everybody wants to work with him."* On development, he and Bruce aligned on **executive-ready communication** and on **routing work to others as visibility opportunities** — both addressed in Personal Development and Leadership.

Brook and Bruce are aligned on the DSE-scope priorities: SONiC SRv6 on Cisco 8000 G200 and P200 for Microsoft and Oracle, the Microsoft disaggregated franchises, the Isovalent SRv6 path to GA, a comprehensive SRv6-for-AI demonstrator, repeatable cloud-native segmentation, and continued SE community multiplication.

*Full letter: [02-direct-leader-recommendation.md](./02-direct-leader-recommendation.md)*

---

## Sponsorship Summary

Letters of recommendation span BE leadership, sales leadership, customers and partners, other Cisco organizations, engineering Principal Engineers, Distinguished Engineers and Fellows, and the Cisco Sales PSE and DSE community — the category the Nomination Kit weights most heavily. Bruce's goal is letters from more than half the global DSE community. `[table in progress]`

*Table: [08-sponsorship.md](./08-sponsorship.md)*

---

## Open Items

- [ ] Finance: Microsoft Cisco 8000 WAN and SONiC frontend DC figures; SP segment bookings; out-of-territory account figures; product run-rate figures
- [ ] More component and platform revenue of the Silicon One kind — Bruce searching the internal database
- [ ] Early-period Web revenue figure, to quantify the segment-foundation claim
- [ ] Complete the sponsorship table and screen categories against the Nomination Kit requirements
- [ ] Brook and/or Matt: final Direct Leader Recommendation; 2HFY26 assessment when the cycle closes
- [ ] Confirm whether a formal executive coaching engagement occurred (PDP item recorded as in progress)
- [ ] Distribute remaining quotes from [12-quotes.md](./12-quotes.md)
- [ ] Formatting: CiscoSansTT, 10 pt minimum, cover photo, working hyperlinks
