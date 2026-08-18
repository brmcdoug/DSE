## Innovation

> **Scope ([AGENTS.md](./AGENTS.md)):** **IPR and product/technology innovation** since **August 1, 2020**—often **downstream of Span of Influence** advocacy outside MIG.  
> **Include:** patents/CPOLs (post-2020 submissions + post-2020 *impact* of earlier work), architectural artifacts, labs/repos that drove **product or strategy**.  
> **Cross-ref:** Customer revenue from those products → **06-business-impact.md**. External blog/conference reach alone → **05-industry-impact.md**. Internal BU persuasion without IP artifact → **04-span-of-influence.md**.

**Suggested package length:** ~6 pages weighted. Third-person; flagship innovations ordered by weight, supporting work in tables. Voice and claim-strength rules: [voice-guide.md](./voice-guide.md).

---

## Innovation Philosophy

Bruce's innovation record starts from an unusual place for a vendor architect: **he was the operator first.** As a network engineer at the Expedia Group (2004–2007) he was hunting for scaling methods beyond the enterprise tooling of the era — which is why he was evaluating MPLS in the data centre in 2006, years before that was a normal thing to consider.

That origin still governs how he chooses what to work on. The question he asks is not how Cisco sells more. It is what he would want if he were still the operator: the simplest, most cost-effective, most agile and extensible, and longest-lasting architecture available. And past the individual operator, the ecosystem — because a healthy ecosystem is what produces durable growth for everyone in it. As he puts it, Cisco's customers do not think of themselves as customers; they think of themselves as network operators, and operators choose the technologies that make their own organizations successful. Roads have no value unless they are used, and they should be easy to use.

**Then he asks the second question: how does Cisco get to the centre of that future?** The order is the discipline. The architecture is settled on its merits first, and Cisco's position is worked out from there — which is why the positions hold up when customers pressure-test them, and why operators take his read of the industry seriously enough to present it themselves.

The consequence is that he is frequently ahead of Cisco, ahead of mainstream customers, and occasionally ahead of the hyperscalers. He is then persistent about it — evangelizing internally and with operators for as long as it takes, and building the labs, prototypes, whitepapers, blogs, and specifications that turn an argument into something a skeptical business entity can evaluate and a customer can run.

Most of these ideas begin as a brainstorm, his own or with a peer, and become an approved patent disclosure, a well-received paper, or a working demonstration. Some begin as a declined disclosure or an unfunded proposal and reappear years later as a shipping product, an acquisition, or an industry specification. Both paths appear in the record below.

### How the thinking developed

Four inflection points shaped the record.

**SDN and NFV (2012–2013)** opened an entirely new way of thinking about network architecture, and **Segment Routing (2013–2016)** opened it again. Bruce began combining the two, producing his first two patents — US9503363 (issued 2016) and US10250494 (issued 2019).

**Cloud/Hyperscale and host networking (2015–present)** produced the insight that has organized everything since. Moving to the Web sales team, Bruce dug into hyperscaler architectures at a time when Cisco was barely selling into cloud data centres at all. What he found was that these operators had **moved the network control point — the overlay, the PE function, the policy enforcement — into the host**, and had done so deliberately: a top-of-rack or leaf switch could never provide the service scale that VMs and Kubernetes demanded, and the host stack was not subject to the silicon limitations that constrain policy and flexibility in hardware. That changed his entire outlook. He spent the following decade evangelizing internally that Cisco needed a genuine technology presence at that control point, naming the gap **Cisco's host-networking air-gap** — an argument that culminated in the Isovalent acquisition. NVIDIA's architecture, combining scale-up, scale-out, and DPUs alongside its GPU/NIC partnership with Silicon One, has since validated the same thesis independently.

**SRv6** then produced an explosion of applied invention: almost all of Bruce's patents are built on it. The generative step was recognizing hosts and endpoints as direct consumers of SRv6 services — after which it is a short leap to treating other non-service-provider devices the same way, and the SD-WAN, SASE, and ThousandEyes work in this package follows from it. A parallel example is the **SGT insight of 2024**: working the Future Enterprise Segmentation tiger team, which had recommended Cisco standardize on a single end-to-end segmentation technology, Bruce noticed that a 16-bit Security Group Tag fits exactly into a 16-bit SRv6 uSID as a trailing argument after locator and function — extending the network programming model to *Locator : Function : SGT*.

**The AI era** has produced another wave, and one vindication: the elephant-flow balancer Bruce designed in 2017 describes the problem the industry took up in 2024 as SRv6 for AI.

The through-line is a single conviction, formed while writing his Principal Architect package: that the work he was drawn to could alter the trajectory of the company and possibly the industry — and that what he wanted was for networks to become a delight to operators, to end users, and to the applications that consume them.

---

## Innovation Summary

| Category | Evidence (Aug 2020 – present) |
| :--- | :--- |
| **Awards** | **2025 Pinnacle Award** — SRv6 uSID team of ~40, almost entirely Cisco engineering; Bruce and DSE Craig Hill were the only two recipients from sales |
| **Patents** | **6 patents, 9 patents pending, 1 defensive publication** |
| **Invention disclosures** | **24 CPOL submissions since Aug 2020** (36 lifetime) |
| **Platform and product innovation** | **SRv6 on SONiC, Cisco 8122** (Jun 2026); **SRv6 uSID on Nexus**; **SRv6 on Cisco SD-WAN** (forthcoming) |
| **Architecture and policy** | Cilium SRv6 CRD — host-networking policy execution engine; **SRv6 + SGT** unified policy model (*Locator : Function : SGT*), adopted by ISE Dec 2025 |
| **Acquisition influence** | **Isovalent / Cilium** — early advocate from 2021; acquisition closed 2024 |
| **Bold Bets** | **Jalapeno** — the only field-submitted project to advance past the first evaluation round |
| **Open source** | [cisco-open/jalapeno](https://github.com/cisco-open/jalapeno) — **78 stars, 15 forks**; [segmentrouting/srv6-labs](https://github.com/segmentrouting/srv6-labs) — **74 stars, 15 forks**; [srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator) — **5 stars** *(published 2026)*; plus srv6-msft, srv6-oci, polarfly |
| **Architectural specs** | SRv6 uSID multi-tenancy for AI factories (Apr 2026); **WMP-PolarFly** flat-fabric paper contesting Amazon's RNG (Aug 2026); Policy Plane |
| **Cross-company strategy** | **Single OS (SOSIE)** working group — co-founded with DSE/PSE peers to address NOS fragmentation and argue the Linux-NOS case |
| **Hackathon** | Cisco EN Hackathon 2022 winner — SD-WAN + SRv6 (Team 6 / Group 14) |

---

## Flagship Innovations

---

### SRv6 on SONiC for the AI Backend, 2023 – 2026

**Customer Problem:** AI training fabrics need deterministic multipath and hard tenant isolation at GPU scale — requirements that standard ECMP and VXLAN overlays do not meet. Microsoft, Oracle, and OpenAI were all converging on source-routed multipath, and all three preferred an open network operating system over a vendor NOS. Cisco had no SRv6 implementation on SONiC and no funded plan to build one. When Bruce first raised the requirement, MIG engineering disputed for weeks that customer urgency was real.

**Customer Solution:** Bruce built the evidence rather than repeating the argument. He authored *SRv6 uSID Multi-Tenancy and Security for AI Factory Network Fabrics* (Apr 2026), specifying encapsulation and decapsulation at leaf, NIC, or hybrid; uDT tenant-ID allocation within the 16-bit uSID space; explicit uA path pinning; and scale targets of 131,000 GPUs per cluster across multi-cluster topologies, with referenced SONiC implementation paths (SwSS PR #4404). Within a week of OpenAI's public MRC announcement he built and published the [srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator), giving SEs and customer engineers a way to model Multipath Reliable Connection with SRv6 static routing while the industry was still reading the specification, and published the [srv6-msft](https://github.com/segmentrouting/srv6-msft) and [srv6-oci](https://github.com/segmentrouting/srv6-oci) POC repositories. He worked directly with SRv6 engineering on SONiC feature scope — uSID forwarding, static uSIDs, BGP GRT, sonic-vpp, sonic-vs — and drove the argument that OpenAI demand was pulling Microsoft and OCI investment. The lineage traces to a May 2023 brainstorm with Pablo Camarillo and Praveen Bhagwatula on SRv6 uSID for AI workloads, and to a disclosure Bruce filed in August 2023, *SRv6 uSID Scheduled Fabric for Artificial Intelligence and Machine Learning Clusters*, which was declined.

**Business Impact:** **SRv6 on SONiC shipped for the Cisco 8122** on the 202511 codebase in **June 2026**, with MIG committing SRv6-on-SONiC G200 in Q1 FY26 to unblock Microsoft and Oracle qualification. The specification became the reference architecture for the Microsoft, Oracle, and CoreWeave AI engagements documented in Business Impact. Microsoft and Oracle engineers used Bruce's repositories in their own internal executive presentations, and OCI reached limited SRv6 production by the end of 2025. The work generated the SmartTOR / NIC-based segment routing patent family with Clarence Filsfils, Pablo Camarillo, Ahmed Abdelsalam, and Carmine Scarpitta — now at five filings — plus *Mechanism for Recovering Packet Policy from Telemetry Notifications in AI Backends*. Both Microsoft and Oracle deployed initial SRv6-for-AI on competitor hardware before Cisco shipped; the architecture was validated, and the delay Bruce spent two years arguing against is the measurable cost. FY2027 TAM recovery projection `[pending finance validation]`.

---

### Isovalent / Cilium — Closing the Host-Networking Air-Gap, 2021 – 2026

**Customer Problem:** For every device running a traditional network operating system, a hyperscale environment runs hundreds or thousands of Linux hosts. That is where cloud operators terminate their overlays, enforce policy, and make forwarding decisions — and Cisco had no credible technology presence there. Bruce named this the **host-networking air-gap**. Without a position at the workload boundary, Cisco's transport products could not participate in the policy and segmentation decisions that increasingly determine network architecture.

**Customer Solution:** Beginning in 2021, Bruce advocated internally that Cisco acquire Isovalent, the company behind Cilium and eBPF, identifying it as the strategic control point rather than an adjacent tooling purchase. He performed the technical validation that made the case concrete: eBPF-based SRv6 L3VPN, egress gateway, and pod-level encapsulation and decapsulation. After the acquisition closed in 2024, he authored the Cilium-SP customer requirements document with progressive use cases from L3VPN through egress gateway to transit gateway (Mar 2026), defining the product integration path between cloud-native security and service provider transport. He then compiled account data worldwide to build the Cilium-SP feature investment case, and maintains the Cilium-SP opportunity and TAM tracker covering telco and SP use cases globally (Nov 2025).

Most recently he authored the **multi-use-case Cilium customer requirements document** (`projects/Cilium-SRv6-Investment.docx`) — a strategic proposal to position Cilium as *the* host-networking policy execution engine across Cisco's portfolio. It addresses a real gap: Cilium cannot directly serve SR-IOV kernel-bypass workloads, so the proposal extends it to carry networking and policy for **both Kubernetes and non-Kubernetes workloads**, including transit gateway and service-chain functions. Cisco engineering has accepted the document and is working to prioritize it. The same proposal underpins the Boost Mobile, Verizon, and Viasat engagements documented in Business Impact.

**Business Impact:** Cisco acquired Isovalent in 2024. Bruce's business case estimated pullthrough revenue of **~$34M (Isovalent)** and **~$323M (MIG)** — validated figures used for product investment prioritization. The resulting product path is deployed or in POC at Bell Canada (host-based SRv6), Boost Mobile (SRv6 L3VPN over AWS underlay), Adobe (egress gateway), Digital Realty, and NSight. Thomas Graf, Cilium co-creator and Isovalent founder, has provided a letter of recommendation covering both the acquisition advocacy and the subsequent SRv6 enablement. The host-networking thesis Bruce had argued since 2013 became Cisco product strategy.

---

### Jalapeno and SR-Apps — Field-Led SDN, 2020 – 2025

**Customer Problem:** Traditional SDN controllers were monolithic, vendor-specific, and not extensible — a customer could not build on top of one. Hyperscalers had responded by building their own (Google Andromeda, Microsoft SWAN, Meta Express Backbone), and the rest of the market was offered dozens of use-case-specific controller products that could not be extended. What the market needed was a platform that treated network state as a queryable graph and let customers, application developers, and Cisco itself build services on top.

**Customer Solution:** Bruce is inventor and lead architect of **Jalapeno**, a cloud-native, database-driven network service broker providing programmable multi-domain services, graph-database reachability, and Kubernetes integration. He submitted it as a Bold Bet in November 2020 and carried it to the Validate phase. He subsequently open-sourced it through Cisco Legal as [cisco-open/jalapeno](https://github.com/cisco-open/jalapeno). He built the `srctl` command-line interface (2025) and extended Jalapeno with the API, UI, and initial implementation for the AI load-balancing use case. In parallel he was field and co-development lead for Clarence Filsfils "SR-Apps" initiative (2020 - 2023), which influenced IPM, path tracing, NaaS, and host-based SRv6 extensibility without requiring a standalone application SKU, that preceded the current D-SDN (Distributed SDN) direction.

**Business Impact:** Jalapeno was **the only Bold Bets submission from the sales organization to advance past the first evaluation round** and reach the funding ask. Unfortunately the Bold Bets program was discontinued and Jalapeno was not funded. Cisco's Segment Routing engineering team adopted Jalapeno as the development platform for the SR-Apps initiative. The `srctl` demonstration ran at Akamai in May 2025. A Jalapeno RPO SDN application, built with Zafar Ali at the November 2024 AI hackathon and, reached a second version now used in the Verizon, AT&T, and Digital Realty engagements and feeding operator POC planning. Earlier field validation ran at Qwilt (Jan 2023) and Rackspace (Mar 2023). **Bell Canada installed Jalapeno in their own lab** and worked with its topology-modelling capability.

---

### SRv6 uSID Hyperscale Market Entry — 2020 – 2025

**Customer Problem:** In 2020 SRv6 uSID was an engineering proposal without a hyperscale market. The operators who most needed native IPv6 summarization and scale-for-decades addressing were the least likely to take an architecture on a vendor's word, and Cisco had no field voice credible enough to open the conversation.

**Customer Solution:** Bruce built the argument as a thought experiment. His presentation *Scaling the Cloud to a Billion Servers*, delivered at an early internal SRv6 workshop in 2020, reframed uSID from a protocol optimization into the only addressing architecture that survives hyperscale growth. He then spent five years doing the unglamorous work: the first public NANOG presentation of uSID, the `segmentrouting` GitHub organization, customer workshops, and the sustained engineering partnership with Clarence Filsfils and the SR team. He drove internal confirmation of IOS-XR support for 256 uSID blocks per node (Oct 2023), the locator scale hyperscale designs require, and found and drove remediation of broken End.USD behavior in IOS-XR with Kamran Raza (Jan 2023).

**Business Impact:** The 2020 presentation led **Clarence Filsfils to task Bruce with leading SRv6 hyperscale market entry** — a mandate validated by the tier-1 and hyperscale wins documented in Business Impact. Cisco awarded a **2025 Pinnacle Award to the SRv6 uSID team** (presented at the ceremony in early 2026) for the technology's market impact, citing unified forwarding architecture, network-as-API programmability, and cross-domain automation readiness. The team numbered roughly 40 and was almost entirely Cisco engineering; **Bruce and DSE Craig Hill were the only two recipients from the sales organization**. That composition is the point — Cisco recognized field-led SRv6 advocacy as company-level innovation alongside the engineers who built it.

---

### SGT in uSID and the Policy Plane — 2023 – 2025

**Customer Problem:** Cisco carried identity in one architecture (Security Group Tags via ISE, TrustSec, and SD-WAN) and scale in another (SRv6 uSID for transport). The two never met. Enterprise customers could not extend policy identity across a service provider underlay, and hyperscale customers had no identity model at all. Each business entity optimized its own domain, and the gap between them was invisible in any single BU's roadmap.

**Customer Solution:** The insight came out of the Future Enterprise Segmentation tiger team, which had recommended that Cisco standardize on a single segmentation technology end to end. Investigating SGT for that work, Bruce noticed that **a Security Group Tag and an SRv6 uSID are both 16 bits** — so an SGT fits exactly as a trailing argument after locator and function, extending the network programming model to *Locator : Function : SGT*. He designed the architecture embedding 16-bit Security Group Tags within uSID function arguments, unifying enterprise identity with hyperscale transport in a single forwarding construct. Working with Josh Merrill from January 2024, he pursued SRv6 as an end-to-end solution spanning SASE, ISE, and transport, bringing in ISE Distinguished Engineer Darren Miller for identity services and Rupak Chandra for SRv6 in Cisco Secure Access. He generalized this into the **Policy Plane** concept — ThousandEyes topology visibility, ISE/SGT identity, and SRv6 transport as three composable glue layers — and served as technical wingman on the multi-BU Yukon++ effort with Josh Merrill.

**Business Impact:** The CPOL *SRv6 uSID Carrier with Embedded Security Group Tag to Identify AI Request* was merged with Clarence Filsfils, Pablo Camarillo, and Ahmed Abdelsalam. By **December 2025 the ISE team was fully committed** to SRv6 SGT and a unified policy model. The Policy Plane concept is gaining MIG traction, and the related Project Yukon and service-chain threads underpin the NaaS revenue framing at Verizon and AT&T documented in Business Impact. Two SD-WAN patent filings followed — *Core Network Support for Application-Requested Network Service Level Objectives* and *Underlay Network Traffic Steering* — along with the SD-WAN IPv6 traffic-marking filing with Saswat Praharaj and Alberto Rodriguez-Natal. `[verify PM attribution for Policy Plane; Carlos Pereira / OTel influence open in vault]`

---

### Flat Data Center Fabrics — WMP-PolarFly, 2024 – Present

**Customer Problem:** AI training clusters built on conventional Clos fat trees strand capacity structurally: hierarchy pins traffic between endpoint pairs to small link subsets that congest while the rest of the fabric idles. Flat topologies have promised an escape for a decade, but until 2026 no hyperscaler had deployed one in production. That changed when Amazon shipped **RNG (Resilient Network Graphs)** as the default fabric for new AWS builds — 69% fewer routers, up to 33% higher throughput, 9–45% lower cost. Amazon's published argument went further than its own design: it dismissed *structured* low-diameter topologies outright, on the grounds that the k-shortest-path routing they require cannot fit in commodity switch memory. That framing, if accepted, forecloses the architecture Cisco is best positioned to deliver.

**Customer Solution:** Bruce contested the framing directly, in a paper he authored: *Structured Optimality vs. Engineered Randomness — Weighted Multipath (WMP) Routing on PolarFly Topologies as an Alternative to Random-Graph Datacenter Fabrics* (v0.7, Aug 2026). Its central argument is that Amazon's dismissal assumes hop-by-hop path state and does not consider compressed source routing: **SRv6 uSID moves path state out of transit ASICs entirely**, so the forwarding-state objection disappears — and once it does, a Moore-bound-optimal structured graph holds per-bit efficiency and latency advantages no random topology can match, advantages that compound with every silicon generation. The paper proposes **WMP-PolarFly**, deriving SRv6 segment lists and their traffic weights algebraically from the polarity graph's projective-plane coordinates, and extends it with multi-slice partitioning of high-radix switches. At 51.2T radix a quad-slice configuration serves **~1M endpoints at diameter 2** with four edge-disjoint shortest paths per pair; a dual-slice configuration reaches **~4M endpoints at 99% of the Moore bound**. It further maps the MRC transport onto PolarFly's algebraically enumerable path sets, enabling per-packet spraying with path-aware congestion control.

The work began as Hoffman–Singleton graph-theory studies with OCI architect **Christian Martin** (Jun 2024), evaluating slimfly- and dragonfly-class topologies against GPU-scale requirements, and continued through late 2025. Martin has since **joined Cisco's MIG hyperscaler architecture team**, and the collaboration continues inside Cisco as SONiC and SRv6 topology and fabric modeling published at [github.com/segmentrouting/polarfly](https://github.com/segmentrouting/polarfly). Bruce also built the IOS-XR-based SRv6 uSID AI-backend demonstration for Oracle VP Jag Brar and his architecture team (Jan 2025).

**Business Impact:** The early studies documented **~50% savings on fabric nodes versus a comparable Clos design** (2HFY24 employee reflection) and anchored the Oracle AI-backend topology conversation. The WMP-PolarFly paper positions Cisco against a competitor architecture already in production at AWS, and does so on ground Cisco owns: unlike RNG — whose Spraypoint protocol is not open-sourced and whose ShuffleBox optics have no commercial source — **WMP-PolarFly builds entirely on FRR, SONiC, and standard SRv6 (RFC 8986, RFC 9256)**, meaning any operator can deploy it and Cisco can sell it. The research produced the *Virtualized Rail Architecture for AI/ML Ethernet Fabrics* and *AI Scale Up Pod Design for 1000 XPU* disclosures with Rob Murphy and Pirooz Tooyserkani; both were declined. Paper: `projects/wmp-polarfly-whitepaper-v07.md` `[confirm publication path — internal review, external whitepaper, or conference submission]`.

---

### SR-Apps and the University Research Pipeline — 2020 – Present

**Customer Problem:** Segment Routing's programmability was, in practice, only reachable by people who could write to a controller's internal model. There was no application layer — no way for a customer, a researcher, or a Cisco engineer to build a service on top of SR without a vendor building it for them. Separately, Cisco had no durable channel for turning academic routing research into field-validated architecture.

**Customer Solution:** Bruce served as **field lead for SR-Apps** (2020–2024), co-developing with SR and MIG engineering. The work influenced IPM and path tracing, the NaaS direction, and host-based SRv6 extensibility — deliberately without a standalone application SKU, so the capability landed in the platform rather than behind a licence. His per-flow binding-SID steering concept (Dec 2020) preceded the D-SDN direction. Cisco's SR engineering team subsequently adopted **Jalapeno as the SDN infrastructure platform for SR-Apps**, making a field-built open-source project the foundation of an engineering initiative.

He also built and maintains the university research channel, serving as field lead for the **CNRS / SR-Apps university collaborations** — HS-PCE, ACP technology fund work, and thesis supervision. The anchor relationship is **OST Zurich** with Professor Laurent Metzger: Bruce open-sourced the Jalapeno API gateway there in 2021, the partnership produced an SRv6 service-chaining demonstration in 2022, and master's student **Severin Dellsperger** went on to build **Hawkv6**, a distributed controller application, with Bart Van De Velde and Andreas Enotiadis.

**Business Impact:** SR-Apps put an application layer on Segment Routing and did it in the platform rather than as a licensed add-on. The university channel operates as a standing pipeline from operator-relevant research into field-validated architecture, and has produced at least one working controller application and a contributor who has since presented at industry venues. `[Bruce to add detail — CNRS scope and named collaborators, HS-PCE and ACP outcomes, and any SR-Apps features that shipped]`

---

### Synthetic Path Tracing and Scheduled FIB — Adjacent-Domain Invention, 2022 – 2025

**Customer Problem:** Two problems outside Bruce's assigned territory. First, ThousandEyes could measure path performance but could not synthesize the segment-routed path a packet would actually take, leaving a visibility gap between overlay measurement and underlay reality. Second, deep-space networking has no continuous connectivity: orbital dynamics make link availability a scheduling problem, and no network operating system has a forwarding table that understands time.

**Customer Solution:** For the first, Bruce engaged the ThousandEyes SRv6 architecture effort and co-invented *Synthetic Path Trace of Segment Routed Networks* with Hans Ashlock and Ben Haddox (filed Jan 2023, renewed Jan 2025). For the second, he conducted delay-tolerant networking research for Brook Crossman's AquarianSpace engagement and co-invented *Network OS Scheduled FIB to Account for Intermittent Connectivity Due to Orbital Dynamics* with Plamen Nedeltchev, alongside *Methods for Secure DTN Full and Partial Mesh Design in Interplanetary Networks*.

**Business Impact:** Synthetic Path Trace was approved as a patent application (US12289210). Scheduled FIB was approved as a patent application (US12494999); **Cisco declined to invest in the deep-space product opportunity**, and the DTN mesh disclosure was declined. Both entries demonstrate the breadth requirement for DSE — inventive contribution in observability and in space networking, well outside the SRv6 and hyperscale domains where Bruce's account work sits.

---

### SONiC with Cisco Secure Workload — Dec 2025 – Feb 2026

**Customer Problem:** As Cisco pushed SONiC into hyperscale and enterprise data centers, it had no runtime security story for the platform. Customers evaluating open NOS were being asked to accept a security posture worse than the one they had with a vendor NOS.

**Customer Solution:** Bruce built the SONiC plus Cisco Secure Workload POC with Jason Maynard and Chris Crider, collaborating with the security SE specialist team, and has run the ongoing Live Protect on SONiC thread with enterprise DSE Brian Shlisky since October 2025.

**Business Impact:** The POC succeeded, proving CSW viable as Live Protect for SONiC infrastructure and giving account teams a security answer for open-NOS deployments. Follow-on sessions through Jan–Feb 2026 track productization `[verify status]`. The work is a further instance of the Span-to-Innovation pattern: a gap identified from field engagement, closed by pulling a non-MIG business entity into a MIG platform conversation.

---

## Additional Innovation Contributions

| Innovation | Date | Contribution and outcome |
| :--- | :--- | :--- |
| **`srv6-mrc-emulator`** | 2026 | Built and published within a week of OpenAI's public MRC announcement. Bruce has demonstrated it internally to Web account teams and to Cisco product engineering, who use it to learn MRC architecture, multi-planar fabric design, host-encapsulation options, and SRv6 numbering schemes. Demonstrated to **CoreWeave VP Shiv Patel**, who directed his own team to use it — the tool being open source was central to that. [Repository](https://github.com/segmentrouting/srv6-mrc-emulator) |
| **EN Hackathon winner** | 2022 | Cisco EN Hackathon winner (Team 6 / Group 14) — SD-WAN + SRv6 demonstration; preceded the SRv6-SGT work. [Winners page](https://cisco.sharepoint.com/sites/EN-Hackathon/SitePages/Hackathon2022-Winners.aspx) (internal) |
| **GitHub-first Cisco Live labs** | 2022–2026 | Bruce pioneered GitHub-based lab guides — configs, code, Containerlab — now common practice across instructor-led sessions. Same method as his customer co-development: open, agile, and reproducible. `[SGM stats — how many ILTs now use the model]` |
| **Adobe egress gateway POC rescue** | Oct 2024 | Bruce rebuilt the customer topology in his own lab after the engagement had failed, preserving the cloud-native egress-gateway proof point ahead of the Jun 2025 onsite workshop with Dan Stacks |
| **Innovation referral funnel** | 2026 | Colleagues with horizon-3 ideas are routed to Bruce for refinement — CHCN full-NG/SDN proposal (Riccardo, Jan 2026), advised scaling back to SRv6 uSID; SmartSwitch SDN brainstorm with Don Ewald (Jan 2026) |
| **BGP CURB controlled unicast replication** | 2023 | Two disclosures with Niall Masterson, Anbu Gunalan, and Anup Kumar Vasudevan; both declined |
| **Quantum-resistant SRv6 path spraying** | 2026 | *Spraying Encrypted Traffic Across Multiple Disjoint SRv6 Paths to Mitigate Future Quantum Decryption*, with Brook Crossman; declined |
| **BGP route-hijack prevention via NFTs** | 2025 | With Brian Shlisky, Jakob Heitz, and John Cuneo; declined |

---

## Intellectual Property

Bruce holds **6 issued US patents**, with **9 patents pending** and **1 defensive publication**. Almost all are applied SRv6. **Four of the six issued during the PSE period** — two in 2024, one in 2025, one in December 2025 — and he is first-named inventor on one of them.

Those grants come out of **36 invention disclosures** submitted over his Cisco career, **24 of them since becoming a Principal Systems Engineer in August 2020** — a submission rate Brook Crossman characterized in the 1HFY26 assessment as **"on pace to break (ASP) records."** The pending filings include **5 continuations on the SmartTOR / NIC-based segment routing family** with Clarence Filsfils, Pablo Camarillo, Ahmed Abdelsalam, and Carmine Scarpitta — a pattern that signals Cisco building protection around the invention rather than filing once and moving on.

The declined disclosures are listed alongside the approved ones deliberately. Several describe architectures the industry adopted later: *SRv6 uSID Scheduled Fabric for AI/ML Clusters* (declined 2023) anticipates the SRv6-for-AI direction Microsoft, Oracle, and the MRC specification took up in 2025–2026, and *Latency Equalization to Enable Spraying and Reordering Elephant Flow in a Data Center Fat Tree* (declined 2020) describes the problem MRC now solves industry-wide.

> **Source note.** The six issued patents are confirmed against the Cisco Inventor Portfolio report of 17 Aug 2026 (US, excluding defensive publications). The pending count and the defensive publication are from the CPOL disclosure record below. `[optional — attach CPOL portal links per asset for the final package]`

### Issued Patents

*Source: Cisco Inventor Portfolio Stats, US, 17 Aug 2026 (`projects/Inventor Portfolio Stats - US-2026-08-17-20-21-52.xlsx`). Six issued US patents; **four issued during the PSE period**.*

| Title | Patent Number | Co-inventors | Filed | **Issued** |
| :--- | :--- | :--- | :--- | :--- |
| **Scheduled FIB to Account for Intermittent Connectivity Due to Orbital Dynamics** | 12,494,999 | Plamen Nedeltchev | Jan 2023 | **Dec 2025** |
| **Synthetic Path Tracing of Segment Routed Networks** | 12,289,210 | Hans Ashlock, Ben Haddox | Jul 2023 | **Apr 2025** |
| **Underlay Network Traffic Steering** | 12,120,027 | Saswat Praharaj, Fabio Maino, Alberto Rodriguez-Natal, Jeff Byzek, Steve Wood | Nov 2022 | **Oct 2024** |
| **Core Network Support for Application-Requested Network Service Level Objectives** | 12,009,998 | Saswat Praharaj, Fabio Maino, Alberto Rodriguez-Natal, Pradeep Kathail | May 2023 | **Jun 2024** |
| **Segment Routing Label Switch Paths in NFV Communications Networks** *(continuation)* | 10,250,494 | Clarence Filsfils, Sami Boutros, Rex Fernando, Siva Sivabalan, Lakshmi Sharma, Santiago Freitas, Rob Fielding | Oct 2016 | **Apr 2019** |
| **Segment Routing Label Switch Paths in NFV Communications Networks** *(original)* | 9,503,363 | *as above* | Mar 2015 | **Nov 2016** |

Three things are worth drawing out of that table. **Underlay Network Traffic Steering** (12,120,027) was filed by SD-WAN engineering — a business entity outside Bruce's own — alongside Praharaj, Maino, Rodriguez-Natal, Byzek, and Wood; granted IP in another BU's portfolio is the least arguable evidence of cross-organizational influence in this package. The **Scheduled FIB** grant (12,494,999) covers delay-tolerant networking for orbital dynamics, a domain unrelated to Bruce's day work and evidence of the breadth DSE requires. And the oldest family, **Segment Routing in NFV** (9,503,363 and 10,250,494), was filed in 2015 with **Clarence Filsfils** and the SR engineering leadership — the earliest documentary record of the partnership that runs through this package.

### All CIPOL Innovation Disclosures

| Submitted | Status | Title | Innovators |
| :--- | :--- | :--- | :--- |
| 2026-05-06 | Declined | Spraying encrypted traffic across multiple disjoint SRv6 paths to mitigate the impact of future quantum decryption techniques | Bruce McDougall, Brook Crossman |
| 2025-12-02 | Declined | Using Ethereum NonFungible Tokens to prevent BGP Route Hijacks | Brian S Shlisky, Bruce McDougall, Jakob Heitz, John N Cuneo |
| 2025-11-23 | Declined | AI Scale Up Pod Design for 1000 XPU | Rob Murphy, Bruce McDougall, Pirooz Tooyserkani |
| 2025-10-30 | Declined | Segment Routing SID and SGT state preservation for traffic traversing a nonSRSRv6 service chain | Bruce McDougall, Rupak Chandra, Joshua S Merrill |
| 2025-10-02 | Declined | Virtualized Rail Architecture for AIML Ethernet fabrics | Bruce McDougall, Rob Murphy |
| 2025-05-22 | Approved - Patent Application | System and Method for Authoritative IPv6 Traffic Marking in SDWAN Networks | Saswat Praharaj, Alberto Rodriguez-Natal, Bruce McDougall |
| 2025-03-21 | Approved - Patent Application | SmartTOR Policy Orchestration based on NCCL topology | Clarence Filsfils, Pablo Camarillo, Ahmed Abdelsalam, Bruce McDougall |
| 2025-03-21 | Approved - Defensive Publication | Avoiding Fabric Congestion Using an SRTE Agent for AI training using existing Data Centers | Zafar Ali, Clarence Filsfils, Francois Clad, Pablo Camarillo, Bruce McDougall |
| 2025-03-21 | Merged | Optimizing an AI training cluster without GPU topology awareness | Pablo Camarillo, Clarence Filsfils, Ahmed Abdelsalam, Bruce McDougall |
| 2025-03-21 | Merged | SRv6 uSID Carrier with Embedded Security Group Tag SGT to Identify AI Request | Bruce McDougall, Joshua S Merrill, Pablo Camarillo, Clarence Filsfils, Ahmed Abdelsalam |
| 2023-09-11 | Declined | Network OS Elastic Network Policy Plane | Bruce McDougall, Joshua S Merrill |
| 2023-08-25 | Declined | SRv6 uSID Scheduled Fabric for Artificial Intelligence and Machine Learning Clusters | Bruce McDougall, Pablo Camarillo, Clarence Filsfils, Praveen Bhagwatula |
| 2023-07-18 | Declined | Controlled Unicast Replication using BGP CURB Large Community Bit Index | Niall C Masterson, Anbu Gunalan, Bruce McDougall, Anup Kumar Vasudevan |
| 2023-07-06 | Declined | Controlled Unicast Replication using BGP CURB | Niall C Masterson, Anbu Gunalan, Anup Kumar Vasudevan, Bruce McDougall |
| 2023-01-31 | Approved - Patent Application | Synthetic Path Trace of Segment Routed Networks | Hans Ashlock, Bruce McDougall, Ben Haddox |
| 2022-10-12 | Approved - Patent Application | Network OS Scheduled FIB to account for intermittent connectivity due to orbital dynamics | PLAMEN Nedeltchev, Bruce McDougall |
| 2022-08-23 | Declined | Methods for secure DTN full and partial mesh design in interplanetary networks | PLAMEN Nedeltchev, Bruce McDougall, Brian A Christensen, Jag Kahlon, Jason H Hsieh |
| 2022-02-04 | Declined | A Generalized Software Defined Networking Infrastructure Platform | Bruce McDougall, Jeff Byzek |
| 2022-02-04 | Approved - Patent Application | SP Underlay Services for SDWAN | Bruce McDougall, Jeff Byzek, Alberto Rodriguez-Natal, Saswat Praharaj, Fabio Maino, Steve Wood |
| 2022-02-04 | Declined | Programmatic authenticated access control in a controllermediated SRv6 network | Jeff Byzek, Bruce McDougall |
| 2022-02-01 | Draft | Customized Topology Modeling in a Generalized Software Defined Networking Infrastructure Platform | Jeff Byzek, Bruce McDougall |
| 2021-12-30 | Approved - Patent Application | System and method for SDWAN tunnel provisioning via control plane based on application connectivity requirements | Saswat Praharaj, Fabio Maino, Alberto Rodriguez-Natal, Pradeep K Kathail, Bruce McDougall |
| 2021-03-01 | Declined | Wireless Client experience optimization SDN Subscription Model for Application Aware Networking | Bruce McDougall, Zafar Ali |
| 2020-12-14 | Declined | Latency Equalization to enable spraying and reordering elephant flow in a Data Center Fat Tree | Pascal Thubert, Francois Clad, Clarence Filsfils, Bruce McDougall |

*24 disclosures submitted on or after Aug 1, 2020 (the DSE package window). A further 12 were submitted earlier in Bruce's career; full lifetime export retained in the repository source file.*


| Date | Status | Title |
| :--- | :--- | :--- |
| 2025-12-02 | Declined | Using Ethereum NonFungible Tokens to prevent BGP Route Hijacks |
| 2025-11-23 | Declined | AI Scale Up Pod Design for 1000 XPU |
| 2025-10-30 | Submitted | Segment Routing SID and SGT state preservation for traffic traversing a non-SR SRv6 service chain |
| 2025-10-02 | Declined | Virtualized Rail Architecture for AIML Ethernet fabrics |
| 2025-05-22 | Approved — Patent | System and Method for Authoritative IPv6 Traffic Marking in SDWAN Networks |
| 2025-03-21 | Approved — Patent | SmartTOR Policy Orchestration based on NCCL topology |
| 2025-03-21 | Approved — Defensive Publication | Avoiding Fabric Congestion Using an SRTE Agent for AI training using existing Data Centers |
| 2025-03-21 | Merged | SRv6 uSID Carrier with Embedded Security Group Tag (SGT) to Identify AI Request |
| 2023-01-31 | Approved — Patent | Synthetic Path Trace of Segment Routed Networks |
| 2022-10-12 | Approved — Patent | Network OS Scheduled FIB to account for intermittent connectivity due to orbital dynamics |
| 2022-02-04 | Approved — Patent | SP Underlay Services for SDWAN |
| 2021-12-30 | Approved — Patent | System and method for SDWAN tunnel provisioning via control plane based on application connectivity requirements |
| 2019-05-28 | Approved — Defensive Publication | Dataplane-based DDoS mitigation and spoofing prevention via SRv6 network programming |
| 2014-06-08 | Approved — Patent | Segment routing label switch paths in NFV communications networks |

**Post–Aug 2020 focus for package body:** 2020-08-01 onward rows. Earlier filings appear in the executive thru-narrative only, unless impact landed after PSE promotion (e.g., defensive publications cited in SRv6 product strategy).

---

## Pre-PSE Origins (exec thru-narrative only — not body case studies)

| Year | Milestone | Package use |
| :--- | :--- | :--- |
| 2013–2015 | Host-networking CIPOLs; SR-to-host vision | Exec overview arc only |
| 2014–2019 | Early SR/NFV patents (e.g., US9503363, US10250494) | Cite impact post-2020 where realized |
| 2017 | Elephant flow balancer (precursor AI fabric LB) | Exec timeline / Industry alignment |

---

## Explicitly Excluded from This Section

| Item | Route to |
| :--- | :--- |
| Raw account $ / bookings | **06-business-impact.md** |
| NANOG/MPLS-WC talks without product/IP thread | **05-industry-impact.md** |
| PSE committee service | **04-span-of-influence.md** / **10-se-community-leadership.md** |
| Pure mentoring / CLEU scores | **10-se-community-leadership.md** |
| Geico/Adobe customer wins without distinct invention | **03-global-impact.md** |

---

## Vault Harvest Log — June 7, 2026

**Entry:** `dse/07-Innovation-MOC.md`  
**Also read:** `dse/Pinnacle-Award-2025-SRv6-uSID.md`, `innovation/SRv6-MultiTenant-Design-rev3.md`, `innovation/SOSIE.md`, `innovation/SGT, SRv6, NaaS Notes.md`, `innovation/yukon-glue.md`, `innovation/Hoffman-Singleton-Fabric-Design.md`, `customers/cilium-srv6.md`, `xarchive-2021-2022/BB-Jalapeno-Overview-20210820.md`, `dse/Pioneer Provider, Brag Book.md`

**Gaps / Bruce to complete:**
- [ ] CPOL portal links and correct issued/pending counts
- [ ] Policy Plane publication (noted “need to publish” in MOC)
- [ ] SGM stats: how many CL ILTs now use GitHub lab model
- [ ] Carlos Pereira / OTel platform influence confirmation
