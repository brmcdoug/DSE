## Span of Influence

> **Scope ([AGENTS.md](./AGENTS.md)):** Impact **internal to Cisco** since **August 1, 2020**—expanding beyond the **ASP + Web + MIG** orbit (IOS-XR, NCS 5k, Cisco 8000, SONiC-as-MIG-platform, Silicon One transport).  
> **This is not a customer/revenue section.** Account outcomes → **[06-business-impact.md](./06-business-impact.md)** / **[03-global-impact.md](./03-global-impact.md)**. External NANOG/GitHub reach → **[05-industry-impact.md](./05-industry-impact.md)**. Patent and product detail → **[07-innovation.md](./07-innovation.md)**.

**Suggested package length:** ~6 pages weighted. Organized by influence theme; third person, most recent activity first within each theme. Voice and claim-strength rules: [voice-guide.md](./voice-guide.md).

---

## How Bruce's Span Expanded

Bruce entered the Principal Systems Engineer role in August 2020 as a Segment Routing subject-matter expert serving Web and service provider accounts through MIG engineering. He now operates as a cross-business-entity architect whose positions shape product roadmaps in organizations that have no reporting relationship to his own, and whose technical judgment is solicited by corporate development, security, enterprise networking, and the office of the CTO.

| Dimension | Horizon 1 — early PSE (2020) | Horizon 2–3 — current (2026) |
| :--- | :--- | :--- |
| **Engineering orbit** | SRv6 feature SME within MIG and Web transport | Cross-BU advisor: **Cilium/Isovalent**, **SD-WAN**, **SSE / Cisco Secure Access**, **Nexus/DC**, **ISE**, **ThousandEyes**, **Future Enterprise Segmentation**, **Single OS (SOSIE)** |
| **Organizational level** | Theater SRv6 pilots; account-team consultant | **VP and executive** relationships (Knipp, Dorval, Morrissey, Gillies, Carnes); **corporate development** advisory; **PSE review subcommittee** voting member; DSE peer working groups |
| **Strategic framing** | "SR features for SP and Web" | **"The 2030 guy"** — host-networking air-gap, network-as-API, Linux NOS with hardware-accelerated applications, SRv6 uSID as unified programming model |
| **Innovation handoff** | Individual lab prototypes | Advocacy converted to outcomes: **Isovalent acquisition**, **SONiC SRv6 investment**, **SD-WAN/SSE roadmap commitments**, **ISE unified policy model** → **[07-innovation.md](./07-innovation.md)** |

**Technology domains (DSE requires ≥2):** (1) **Cloud-native and host networking** — eBPF, Cilium, Kubernetes CNI; (2) **Programmable transport** — SRv6 uSID end-to-end; (3) **Open network operating systems** — SONiC, SOSIE, Linux NOS strategy; (4) **Enterprise security and identity** — SGT, segmentation, Policy Plane.

---

## 1. Segment Routing Engineering Partnership

### Clarence Filsfils and the SR Brain Trust — 2020 – Present

Cisco's Segment Routing engineering organization under Fellow Clarence Filsfils sets the architecture direction for the company's transport portfolio and, increasingly, for how Cisco competes in AI infrastructure. The organization historically formed its market view from a small number of trusted field voices. Bruce has been one of them for nearly a decade, functioning as field lead, innovation partner, and the primary conduit between hyperscale customer reality and SR engineering priorities.

Bruce's involvement and influence include:

- Delivered *Scaling the Cloud to a Billion Servers* at an early internal SRv6 workshop (2020), after which **Clarence Filsfils tasked Bruce with leading Cisco's hyperscale SRv6 market entry** — a mandate validated by the 2025 Pinnacle Award and the tier-1 deployments documented in Business Impact
- Served as **SR-Apps field lead** (2020–2024), co-developing with SR and MIG engineering on path tracing into IPM, NaaS, and host-based SRv6 direction
- Acts as the **SRv6 engineering field broker**, introducing field SEs directly to Clarence's team (Gisiger, Olson, Vashisht, Sischo, Rockwell, Khanna, and others) rather than routing requests through account channels
- Briefed **MIG and Silicon leadership** (Mar 2026) on SRv6 use cases at Microsoft and Oracle, setting AI-backend and frontend data center priorities
- Drove product prioritization decisions including **256 uSID blocks per node in IOS-XR** (Oct 2023), which unblocked the hyperscale SRv6 designs Bruce had been advocating, and remediation of broken End.USD behavior with Kamran Raza (Jan 2023)
- Compiled the **Web encapsulations customer requirements document** with Bob Gisiger (2023), converting scattered hyperscaler host-networking requirements into an engineering backlog
- Edited four chapters of the **SRv6 book** with Clarence's team (2024)
- Consulted with Humberto La Roche of the IM&I CTO team on **L4S**
- Sustained a multi-year fabric-topology collaboration with **Christian Martin** that began when Martin was an OCI architect and continued after he **joined Cisco's MIG hyperscaler architecture team** — an external research partnership that converted into an internal one, now published as SONiC and SRv6 fabric modeling at [github.com/segmentrouting/polarfly](https://github.com/segmentrouting/polarfly)

A recurring pattern across the Web and hyperscale accounts is that Bruce's engagement is designed to be handed off: he builds the architecture, the lab, and the field capability, and then the account team runs the customer engagement without him. At **Meta he never presented to the customer at all** — he pioneered the SL-API technique at Microsoft, taught it to the account team, built the labs they validated it in, and they carried it to a $17M backbone re-entry themselves. The same shape appears at Microsoft (SONiC training that let the account team scale across expanding use cases), CoreWeave (self-service Containerlab environments), and Videotron (SE Philippe Vaillancourt self-training ahead of a customer workshop). Measuring Bruce's influence by the meetings he attends would understate it substantially.

Bruce's influence here operates at architecture-organization altitude rather than account-SE scope: he shapes what SR engineering builds, not merely which features his accounts receive. By 2025–2026 that influence extended into platform investment alignment across ISE, IOS-XE, Nexus, SONiC, SD-WAN, SASE, and Cilium.

*More details are located in the Innovation and Business Impact sections of this document.*

---

## 2. Cross-Business-Entity Expansion Beyond MIG

### Host Networking and the Isovalent Acquisition — 2021 – Present

Cisco's transport portfolio ended at the top-of-rack switch. Cloud operators had moved their overlays, policy enforcement, and forwarding decisions into Linux and Kubernetes on the host — a control point where Cisco had no product and no credible technical voice. Bruce named this the **host-networking air-gap** and spent years arguing that it represented an existential gap rather than an adjacent opportunity. The argument required persuading business entities outside MIG entirely, since no transport BU owned the problem.

Bruce's involvement and influence include:

- Identified Cilium and eBPF as the strategic inflection point and advocated for Cisco to acquire Isovalent from 2021, years before the acquisition closed in 2024
- Delivered the Isovalent presentation to the **Cisco AI tiger team** (Nov 2024) and built the **Isovalent SEVT lab** for field enablement
- Partnered with EMEA DSE **Virginia Teixeira** (Sep 2025) on SRv6 inside the data center with Cilium, SRv6 headend controller scale, and DCN business entity alignment
- Compiled worldwide account data into the **Cilium-SP feature investment case** — ~$34M Isovalent and ~$323M MIG pullthrough — used for product investment prioritization
- Authored the **multi-use-case Cilium customer requirements document** positioning Cilium as the host-networking policy execution engine for Kubernetes and non-Kubernetes workloads alike; **Cisco engineering has accepted it and is working to prioritize** the roadmap items it defines

Security, data center, and service provider teams now share a common host-networking vocabulary that did not exist inside Cisco in 2021, and the SD-WAN and SSE organizations cite SRv6 as a roadmap differentiator. Thomas Graf, Cilium co-creator and Isovalent founder, has provided a letter of recommendation covering the acquisition advocacy and subsequent enablement.

*More details are located in the Innovation section of this document.*

---

### SD-WAN, SSE, and Enterprise Platform Influence — 2020 – Present

SD-WAN, Cisco Secure Access, and the enterprise security portfolio sit entirely outside the MIG orbit and outside Bruce's assigned segment. Each was building its own transport and policy model, none of which interoperated with the SRv6 architecture Cisco was selling to service providers and hyperscalers. Bruce established himself as a standing technical advisor to these organizations without any organizational mandate to do so.

Bruce's involvement and influence include:

- Advised **Alberto Rodriguez-Natal** and the CNWAN team on SD-WAN product direction and the SRv6-SGT tie-in (from Sep 2020)
- Served as **SD-WAN SP-API advisor** (May 2021), proposing the direct binding-SID approach now reflected in business entity plans for 2026–2027
- Co-led the **SP Edge tiger team** (May 2021) with Vaughn Suazo, Jeff Byzek, Craig Hill, Errol Roberts, and David Jansen
- Reached architectural agreement with **Rupak Chandra** on SRv6 for Cisco Secure Access (Aug 2024)
- Serves as **cloud-native SME on demand to business entity leaders** including Steve Wood and Errol Roberts (from Jan 2025), providing Kubernetes, Cilium, and eBPF depth these organizations lack internally

The influence is documented in intellectual property rather than only in relationships: the SD-WAN patent family — *SP Underlay Services for SD-WAN*, *Core Network Support for Application-Requested Network Service Level Objectives*, *Underlay Network Traffic Steering*, and *Authoritative IPv6 Traffic Marking in SD-WAN* — carries Bruce as a named inventor alongside SD-WAN engineering staff.

*More details are located in the Innovation section of this document.*

---

### Future Enterprise Segmentation and Unified Policy — 2022 – Present

Cisco carried identity in the enterprise portfolio through Security Group Tags, ISE, and TrustSec, and carried scale in the service provider portfolio through SRv6 uSID. The two architectures had no meeting point, and protocol sprawl between VXLAN and SRv6 was accumulating across enterprise and SP domains. The **Future Enterprise Segmentation SWAT team** was convened in December 2022 under Tim Carnes and Matt Gillies to address it, and Bruce was selected as a member.

Bruce's involvement and influence include:

- Authored Sprint 3 recommendations on protocol sprawl and established **SGT as the normalized identity gate** for attribute-based access control, working with Marina Ferreira, Errol Roberts, Steven Chimes, Steven Moore, and Tjerk Bijlsma
- Developed the *Embedding Services in the Network* and Service SID concepts (Mar 2022) with Josh Merrill, John Mullooly, and Kamran Raza
- Presented **SRv6 with SGT to Matt Gillies** (Apr 2025) with Josh Merrill, establishing the unified policy model spanning ISE, SSE, and SD-WAN
- Carried the SRv6-with-SGT architecture into Verizon executive conversations, designing the majority of the architecture and intellectual property while Cisco PSE **Josh Merrill delivered the executive presentations** — deliberately putting a colleague in front of the customer's leadership
- Co-led the **SRv6 end-to-end DC/NX-OS tiger team** (Feb 2026) with Brenden Buresh, Marina Ferreira, and Varun, extending SRv6 from SP transport into enterprise data center switching, following the DC/campus end-to-end EVPN tiger team (Dec 2025)

By **December 2025 the ISE organization had committed** to SRv6 SGT and a unified policy model — the culmination of three years of multi-business-entity work connecting enterprise segmentation discourse to SRv6 uSID as a single programming construct.

*More details are located in the Innovation section of this document.*

---

## 3. Open Network Operating System Strategy

### Single OS (SOSIE) Working Group — 2024 – Present

Cisco had converged its hardware on Silicon One while its software remained fragmented across NX-OS, IOS-XR, and IOS-XE. That divergence carried a quantified commercial cost: an estimated **$500M of Edgecore leakage** identified in the October 2024 session, as customers who wanted disaggregated open-NOS platforms went elsewhere. No single business entity owned the problem, and no forum existed to raise it.

Bruce **co-founded the Single OS (SOSIE) working group** with DSE and PSE peers Brenden Buresh, Craig Hill, Virginia Teixeira, and Rob Murphy to create that forum.

Bruce's involvement and influence include:

- Framed the multi-year path toward a **Linux-based network operating system** with hardware-accelerated packet applications and a Cilium-class service control plane
- Quantified the fragmentation risk against competitive whitebox loss
- Extended the group's forward look to Mythos and AI-assisted security patching for vulnerability-surface reduction (2026)

The working group established a cross-business-entity venue for network operating system strategy that had not previously existed, and gave Cisco's field architect community a shared position on open NOS.

---

### SONiC Strategy Across Segments — 2023 – Present

Bruce **led the Americas PA/DA SONiC forum** (Dec 2023), building field architect consensus on open-NOS strategy across horizon 1, 2, and 3 for Cloud, SP, Enterprise, and Public Sector with Brenden Buresh, Cesar Obediente, Vaughn Suazo, David Jansen, Craig Hill, and Rob Murphy. He bridges Silicon One, Cisco 8000, SONiC, and AI backend engineering, translating hyperscaler co-development into an internal narrative MIG and IMI can execute against, and partners with Cisco SRv6 and SONiC engineering on frontend data center, AI backend, and multi-tenancy use cases.

The internal outcome was **SONiC SRv6 prioritization and the June 2026 8122 release**; the customer revenue that followed is documented in Business Impact. At IETF Vancouver 2024, Ianik Semko referred to Bruce and his collaborators as **"the 2030 guys"** — external confirmation of an internal reputation.

He also drove the **SONiC with Cisco Secure Workload POC** (Dec 2025 – Feb 2026) with Jason Maynard and Chris Crider, and maintains the Live Protect on SONiC thread with enterprise DSE Brian Shlisky — pulling a security business entity into a platform conversation MIG could not resolve alone.

*More details are located in the Innovation and Business Impact sections of this document.*

---

### Competitive and Portfolio Intelligence

| Initiative | Date | Bruce's role |
| :--- | :--- | :--- |
| **SL-OnDemand tiger team** | Sep 2023 – Mar 2024 | **Only member from the sales organization** (with CX, Subha Dhesikan); delivered executive readout Mar 2024 |
| **Arista tiger team SONiC intelligence** | Feb 2024 | Field-to-business-entity competitive feedback on open-NOS positioning |
| **Portfolio Innovation Areas** | Feb 2026 | Consultant to the Security business entity (Connors, Lake, Roberts) with Vaughn Suazo and Fierbaugh |
| **Combatting Disaggregation** | Sep–Oct 2025 | Authored and delivered *Combatting Disagg with Network Service Innovation (SRv6)* to the full ASP team; repeated at TMC Innovation Hour |

---

## 4. Corporate Strategy and Executive Altitude

### Executive Interlocks and Technical Roadmap Ownership — 2025 – Present

Bruce serves as the **Web and Hyperscale representative for executive business entity interlocks** and owned **FY26 Global Sales Technical Roadmap** and BE Interlock Process responsibilities across the August 2025 and April 2026 cycles. In that capacity he sets the technical asks for AI, SRv6, and SONiC at sales-organization altitude, ensuring hyperscale requirements enter global sales planning rather than surfacing account by account.

---

### Neo-Cloud Equity Investment Advisory — Jun 2024

Cisco corporate development engaged Bruce as technical consultant on **AI tier-2 and neo-cloud equity investments**, working with Vladimirs Sazonovs, Lauren Johnson, and Ryan Houska. This placed field architecture judgment inside corporate investment decisions — a function ordinarily served by strategy or engineering staff, not by a field systems engineer.

---

### NaaS, NetCo/ServCo, and Project Yukon — 2021 – 2024

Bruce originated and carried the internal argument that service providers should expose network capability for **cloud-like consumption** rather than selling circuits.

| Thread | Date | Bruce's influence |
| :--- | :--- | :--- |
| **Future of SP Networking** | Jul 2021 | Established "cloud-like consumption of network services" in Cisco's NaaS vocabulary; two SP360 blog publications |
| **MCNS / NetCo / ServCo** | Feb 2023 | Architecture work with Brian Meaney, Virginia Teixeira, Alessandro Breccia, Louis, and Donzelli |
| **Cross-Domain Broker** | Oct 2023 | Presented the Jalapeno/ExBroker lineage to Beesely, Mohit Lad, and Eric Knipp |
| **Project Yukon** | Jan 2024 | NaaS architecture extending SRv6 to CPE and service nodes for Verizon and AT&T |
| **SP NaaS EU advisor** | Q2–Q3 2023 | Extended NaaS planning into EMEA |

---

### Executive Recognition and Silicon Strategy — 2021 – 2023

Cisco vice presidents **Eric Knipp, John Dorval, and Patrick Morrissey** have cited Bruce's influence at **more than $1B**, including the foundational Amazon Silicon One engagement recognized at steering level in Q1 FY23. Bruce's generational TAM analysis for Silicon One (12.8T through 51.2T) informed steering-level investment discussion. The revenue consequences are documented in Business Impact; the significance here is that a field systems engineer's architecture position reached silicon investment planning.

---

## 5. Field Architect Multiplier and Peer Network

### PSE Review Subcommittee — 2021 – 2024

Bruce served **three years as a voting member of the Principal Systems Engineer review subcommittee**, shaping the promotion standard itself rather than only preparing candidates for it — including the March–May 2024 cycle with Mike McPhee. Individual mentee outcomes are documented in SE Community Leadership; the committee service is organizational influence over how Cisco defines senior technical leadership.

---

### Cross-Organization Peer Network

Bruce's standing collaborators outside the ASP+Web and MIG orbit — the practical measure of span:

| Peer | Role / organization | Shared work |
| :--- | :--- | :--- |
| **Brenden Buresh** | DA, GES Office of the CTO | Cloud-native SRv6, SOSIE co-founder, DC/NX-OS tiger team |
| **Craig Hill** | DSE, US Public Sector | Routing architecture, Future Enterprise Segmentation, SOSIE co-founder |
| **Virginia Teixeira** | DSE, EMEA | SOSIE co-founder, DCN and transport/AI convergence |
| **Rob Murphy** | PSE | SONiC labs, SOSIE co-founder, enablement assets, AI fabric disclosures |
| **David Jansen** | DSE | SP Edge tiger team, Americas SONiC forum |
| **Brian Meaney** | DA, EMEA CTO | MCNS, NetCo/ServCo, NaaS architecture |
| **Mike McPhee** | DSE | PSE review subcommittee |
| **Marina Ferreira** | PSE | Future Enterprise Segmentation, DC/NX-OS tiger team |
| **Josh Merrill** | — | SGT-in-uSID co-inventor, Policy Plane, Yukon++ |
| **Matt Gillies** | VP, Global Solutions Engineering | SRv6+SGT executive validation; Bruce's leader from Jun 2026 |

---

### Additional Span Threads

| Thread | Period | Note |
| :--- | :--- | :--- |
| **Hawkv6 / OST Zurich** | 2025 | Distributed controller application; cross-reference Industry Impact and Innovation |
| **ArangoDB / Jalapeno graph** | 2025 | Programmable services architecture with Josh Merrill |
| **Operator RPO / A3PO planning** | 2025 | POC architecture support for AT&T and Verizon |
| **NSM/NSE and ET&I** | Aug 2020 | Jalapeno-SDN and SRv6-TE work with Swanson, Joyce, and McFarland |
| **Experience Broker** | 2021 | Internal mindshare; direct lineage to Cross-Domain Broker |

---

## Signature Internal Influence Themes

These are the five positions Bruce is known for inside Cisco. Each began as a minority view and each has since become, or is becoming, company direction.

1. **The host-networking air-gap** — the control point moved to the host; Cisco must participate in Linux and eBPF. *Outcome: Isovalent acquisition, 2024.*
2. **SRv6 uSID as a network API** — one programming model across IOS-XR, IOS-XE, NX-OS, SONiC, SD-WAN, and host CNI. *Outcome: 2025 Pinnacle Award; platform alignment across six product lines.*
3. **Open NOS and SONiC** — open network operating systems are required for hyperscaler relevance. *Outcome: SRv6 on SONiC shipped for the Cisco 8122, June 2026.*
4. **The Policy Plane** — identity (SGT), transport (SRv6), and observability as composable glue across business entities. *Outcome: ISE committed to the unified policy model, December 2025.* `[verify PM attribution]`
5. **Linux as the future NOS** — routing as hardware-accelerated applications on a Cilium-class control plane. *Outcome: SOSIE working group; ongoing.*

---

## Open Items

- [ ] SD-WAN and SSE product management quotes confirming SRv6 roadmap commitment
- [ ] Will Etherton OS-convergence report outcome (if shareable)
- [ ] Policy Plane traction with MIG product management (Carlos Pereira / OTel)
- [ ] Confirm $500M Edgecore leakage figure is quotable in the package
- [ ] Confirm VP citations (Knipp, Dorval, Morrissey) are attributable by name

**Last body pass:** Aug 2026 — rewritten to [voice-guide.md](./voice-guide.md) register; thematic structure retained from Jun 2026 pass.
