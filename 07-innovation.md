## Innovation

> **Scope ([AGENTS.md](./AGENTS.md)):** **IPR and product/technology innovation** since **August 1, 2020**—often **downstream of Span of Influence** advocacy outside MIG.  
> **Include:** patents/CPOLs (post-2020 submissions + post-2020 *impact* of earlier work), architectural artifacts, labs/repos that drove **product or strategy**.  
> **Cross-ref:** Customer revenue from those products → **06-business-impact.md**. External blog/conference reach alone → **05-industry-impact.md**. Internal BU persuasion without IP artifact → **04-span-of-influence.md**.

**Suggested package length:** ~6 pages weighted. Third-person; flagship innovations ordered by weight, supporting work in tables. Voice and claim-strength rules: [voice-guide.md](./voice-guide.md).

---

## Innovation Philosophy

Bruce's innovation record follows a consistent method: identify an industry inflection three to five years before the market reaches it, build the working artifact that makes the idea testable, and then spend however long it takes persuading Cisco engineering to fund it. The artifacts matter as much as the ideas — a specification, a lab, an emulator, or an open-source repository turns an argument into something a skeptical business entity can evaluate and a customer can run.

This method produces a distinctive pattern in the record below. Bruce's inventions frequently appear first as a declined disclosure, an unfunded proposal, or a customer conversation Cisco was not ready to have — and then reappear years later as a shipping product, an acquisition, or an industry specification. The declined submissions are as much a part of the evidence as the granted patents.

---

## Innovation Summary

| Category | Evidence (Aug 2020 – present) |
| :--- | :--- |
| **Awards** | **2025 Pinnacle Award** — SRv6 uSID team; rare recognition for a member of the sales organization |
| **Invention disclosures** | **24 CPOL submissions since Aug 2020** (36 lifetime); **9 approved** for patent filing, defensive publication, or merge |
| **Patent filings** | **10 filings across 4 families**, including **5 continuations** on the SmartTOR / NIC-based segment routing family `[verify granted vs. pending]` |
| **Products shipped** | **SRv6 on SONiC, Cisco 8122** (Jun 2026); Cilium SRv6 CRD; SGT-in-uSID unified policy model |
| **Acquisition influence** | **Isovalent / Cilium** — early advocate from 2021; acquisition closed 2024 |
| **Bold Bets** | **Jalapeno** — the only field-submitted project to advance past the first evaluation round |
| **Open source** | [cisco-open/jalapeno](https://github.com/cisco-open/jalapeno); [segmentrouting](https://github.com/segmentrouting) org — srv6-msft, srv6-oci, srv6-mrc-emulator |
| **Architectural specs** | SRv6 uSID multi-tenancy for AI factories (Apr 2026); **WMP-PolarFly** flat-fabric paper contesting Amazon's RNG (Aug 2026); Policy Plane |
| **Hackathon** | Cisco EN Hackathon 2022 winner — SD-WAN + SRv6 (Team 6 / Group 14) |

---

## Flagship Innovations

---

### SRv6 on SONiC for the AI Backend, 2023 – 2026

**Customer Problem:** AI training fabrics need deterministic multipath and hard tenant isolation at GPU scale — requirements that standard ECMP and VXLAN overlays do not meet. Microsoft, Oracle, and the OpenAI compute supply chain were all converging on source-routed multipath, and all three preferred an open network operating system over a vendor NOS. Cisco had no SRv6 implementation on SONiC and no funded plan to build one. When Bruce first raised the requirement, MIG engineering disputed for weeks that customer urgency was real.

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

**Customer Problem:** Traditional SDN controllers were monolithic, vendor-specific, and did not compose. Hyperscalers had responded by building their own — Google's and Microsoft's homegrown systems — while everyone else was offered a controller product that could not be extended. What the market needed was a platform that treated network state as a queryable graph and let customers, application developers, and Cisco itself build services on top.

**Customer Solution:** Bruce is inventor and lead architect of **Jalapeno**, a cloud-native, database-driven network service broker providing programmable multi-domain services, graph-database reachability, and Kubernetes integration. He submitted it as a Bold Bet in November 2020 and carried it to the Validate phase. He subsequently open-sourced it through Cisco Legal as [cisco-open/jalapeno](https://github.com/cisco-open/jalapeno). He built the `srctl` command-line interface (2025) and extended Jalapeno with the API, UI, and initial implementation for the AI load-balancing use case. In parallel he drove SR-Apps field co-development, which influenced IPM, path tracing, NaaS, and host-based SRv6 extensibility without requiring a standalone application SKU, and produced the per-flow BSID steering concept (Dec 2020) that preceded the D-SDN direction.

**Business Impact:** Jalapeno was **the only Bold Bets submission from the sales organization to advance past the first evaluation round** and reach the funding ask before the program ended. Cisco's Segment Routing engineering team adopted Jalapeno as the SDN infrastructure platform for the SR-Apps initiative. The `srctl` demonstration ran at Akamai in May 2025. A Jalapeno RPO SDN application, built with Zafar Ali at the November 2024 AI hackathon and refined through the elephant-flows demonstration with Brook Crossman and Josh, reached a second version now used in the Verizon, AT&T, and Digital Realty engagements and feeding operator RPO/A3PO POC planning. Earlier field validation ran at Qwilt (Jan 2023) and Rackspace (Mar 2023).

---

### SRv6 uSID Hyperscale Market Entry — 2020 – 2025

**Customer Problem:** In 2020 SRv6 uSID was an engineering proposal without a hyperscale market. The operators who most needed native IPv6 summarization and scale-for-decades addressing were the least likely to take an architecture on a vendor's word, and Cisco had no field voice credible enough to open the conversation.

**Customer Solution:** Bruce built the argument as a thought experiment. His presentation *Scaling the Cloud to a Billion Servers*, delivered at an early internal SRv6 workshop in 2020, reframed uSID from a protocol optimization into the only addressing architecture that survives hyperscale growth. He then spent five years doing the unglamorous work: the first public NANOG presentation of uSID, the `segmentrouting` GitHub organization, customer workshops, and the sustained engineering partnership with Clarence Filsfils and the SR team. He drove internal confirmation of IOS-XR support for 256 uSID blocks per node (Oct 2023), the locator scale hyperscale designs require, and found and drove remediation of broken End.USD behavior in IOS-XR with Kamran Raza (Jan 2023).

**Business Impact:** The 2020 presentation led **Clarence Filsfils to task Bruce with leading SRv6 hyperscale market entry** — a mandate validated by the tier-1 and hyperscale wins documented in Business Impact. In **2025 Bruce received Cisco's Pinnacle Award** as part of the team recognized for SRv6 uSID's market impact, citing unified forwarding architecture, network-as-API programmability, and cross-domain automation readiness. Pinnacle recognition rarely reaches the sales organization; it confirms field-led SRv6 advocacy as company-level innovation rather than account support.

---

### SGT in uSID and the Policy Plane — 2023 – 2025

**Customer Problem:** Cisco carried identity in one architecture (Security Group Tags via ISE, TrustSec, and SD-WAN) and scale in another (SRv6 uSID for transport). The two never met. Enterprise customers could not extend policy identity across a service provider underlay, and hyperscale customers had no identity model at all. Each business entity optimized its own domain, and the gap between them was invisible in any single BU's roadmap.

**Customer Solution:** Bruce designed an architecture embedding 16-bit Security Group Tags within uSID function arguments, unifying enterprise identity with hyperscale transport in a single forwarding construct. Working with Josh Merrill from January 2024, he pursued SRv6 as an end-to-end solution spanning SASE, ISE, and transport, bringing in ISE Distinguished Engineer Darren Miller for identity services and Rupak Chandra for SRv6 in Cisco Secure Access. He generalized this into the **Policy Plane** concept — ThousandEyes topology visibility, ISE/SGT identity, and SRv6 transport as three composable glue layers — and served as technical wingman on the multi-BU Yukon++ effort with Josh Merrill.

**Business Impact:** The CPOL *SRv6 uSID Carrier with Embedded Security Group Tag to Identify AI Request* was merged with Clarence Filsfils, Pablo Camarillo, and Ahmed Abdelsalam. By **December 2025 the ISE team was fully committed** to SRv6 SGT and a unified policy model. The Policy Plane concept is gaining MIG traction, and the related Project Yukon and service-chain threads underpin the NaaS revenue framing at Verizon and AT&T documented in Business Impact. Two SD-WAN patent filings followed — *Core Network Support for Application-Requested Network Service Level Objectives* and *Underlay Network Traffic Steering* — along with the SD-WAN IPv6 traffic-marking filing with Saswat Praharaj and Alberto Rodriguez-Natal. `[verify PM attribution for Policy Plane; Carlos Pereira / OTel influence open in vault]`

---

### Flat Data Center Fabrics — WMP-PolarFly, 2024 – Present

**Customer Problem:** AI training clusters built on conventional Clos fat trees strand capacity structurally: hierarchy pins traffic between endpoint pairs to small link subsets that congest while the rest of the fabric idles. Flat topologies have promised an escape for a decade, but until 2026 no hyperscaler had deployed one in production. That changed when Amazon shipped **RNG (Resilient Network Graphs)** as the default fabric for new AWS builds — 69% fewer routers, up to 33% higher throughput, 9–45% lower cost. Amazon's published argument went further than its own design: it dismissed *structured* low-diameter topologies outright, on the grounds that the k-shortest-path routing they require cannot fit in commodity switch memory. That framing, if accepted, forecloses the architecture Cisco is best positioned to deliver.

**Customer Solution:** Bruce contested the framing directly, in a paper he authored: *Structured Optimality vs. Engineered Randomness — Weighted Multipath (WMP) Routing on PolarFly Topologies as an Alternative to Random-Graph Datacenter Fabrics* (v0.7, Aug 2026). Its central argument is that Amazon's dismissal assumes hop-by-hop path state and does not consider compressed source routing: **SRv6 uSID moves path state out of transit ASICs entirely**, so the forwarding-state objection disappears — and once it does, a Moore-bound-optimal structured graph holds per-bit efficiency and latency advantages no random topology can match, advantages that compound with every silicon generation. The paper proposes **WMP-PolarFly**, deriving SRv6 segment lists and their traffic weights algebraically from the polarity graph's projective-plane coordinates, and extends it with multi-slice partitioning of high-radix switches. At 51.2T radix a quad-slice configuration serves **~1M endpoints at diameter 2** with four edge-disjoint shortest paths per pair; a dual-slice configuration reaches **~4M endpoints at 99% of the Moore bound**. It further maps the MRC transport onto PolarFly's algebraically enumerable path sets, enabling per-packet spraying with path-aware congestion control.

The work began as Hoffman–Singleton graph-theory studies with OCI architect **Christian Martin** (Jun 2024), evaluating slimfly- and dragonfly-class topologies against GPU-scale requirements, and continued through late 2025. Martin has since **joined Cisco's MIG hyperscaler architecture team**, and the collaboration continues inside Cisco as SONiC and SRv6 topology and fabric modeling published at [github.com/segmentrouting/polarfly](https://github.com/segmentrouting/polarfly). Bruce also built the IOS-XR-based SRv6 uSID AI-backend demonstration for Oracle VP Jag Brar and his architecture team (Jan 2025).

**Business Impact:** The early studies documented **~50% savings on fabric nodes versus a comparable Clos design** (2HFY24 employee reflection) and anchored the Oracle AI-backend topology conversation. The WMP-PolarFly paper positions Cisco against a competitor architecture already in production at AWS, and does so on ground Cisco owns: unlike RNG — whose Spraypoint protocol is not open-sourced and whose ShuffleBox optics have no commercial source — **WMP-PolarFly builds entirely on FRR, SONiC, and standard SRv6 (RFC 8986, RFC 9256)**, meaning any operator can deploy it and Cisco can sell it. The research produced the *Virtualized Rail Architecture for AI/ML Ethernet Fabrics* and *AI Scale Up Pod Design for 1000 XPU* disclosures with Rob Murphy and Pirooz Tooyserkani; both were declined. Paper: `projects/wmp-polarfly-whitepaper-v07.md` `[confirm publication path — internal review, external whitepaper, or conference submission]`.

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
| **GitHub-first Cisco Live labs** | 2022–2026 | Bruce pioneered GitHub-based lab guides — configs, code, Containerlab — now common practice across instructor-led sessions. Same method as his customer co-development: open, reproducible, and available before the capability ships. `[SGM stats — how many ILTs now use the model]` |
| **CNRS / SR-Apps university partnership** | 2020–2026 | Field lead for university collaborations (OST Zurich and others) — HS-PCE, ACP tech fund, thesis projects; research-to-field-validation pipeline |
| **Adobe egress gateway POC rescue** | Oct 2024 | Bruce rebuilt the customer topology in his own lab after the engagement had failed, preserving the cloud-native egress-gateway proof point ahead of the Jun 2025 onsite workshop with Dan Stacks |
| **Innovation referral funnel** | 2026 | Colleagues with horizon-3 ideas are routed to Bruce for refinement — CHCN full-NG/SDN proposal (Riccardo, Jan 2026), advised scaling back to SRv6 uSID; SmartSwitch SDN brainstorm with Don Ewald (Jan 2026) |
| **BGP CURB controlled unicast replication** | 2023 | Two disclosures with Niall Masterson, Anbu Gunalan, and Anup Kumar Vasudevan; both declined |
| **Quantum-resistant SRv6 path spraying** | 2026 | *Spraying Encrypted Traffic Across Multiple Disjoint SRv6 Paths to Mitigate Future Quantum Decryption*, with Brook Crossman; declined |
| **BGP route-hijack prevention via NFTs** | 2025 | With Brian Shlisky, Jakob Heitz, and John Cuneo; declined |

---

## Intellectual Property

Bruce has submitted **36 invention disclosures** over his Cisco career, **24 of them since becoming a Principal Systems Engineer in August 2020**. Of the 24, **9 were approved** for patent filing, defensive publication, or merge into a related family; 14 were declined and 1 remains in draft. Those filings span four patent families and **10 individual filings**, including **5 continuations on the SmartTOR / NIC-based segment routing family** — a continuation pattern that signals Cisco building protection around the invention rather than filing once and moving on.

The declined disclosures are listed alongside the approved ones deliberately. Several describe architectures the industry adopted later: *SRv6 uSID Scheduled Fabric for AI/ML Clusters* (declined 2023) anticipates the SRv6-for-AI direction Microsoft, Oracle, and the MRC specification took up in 2025–2026, and *Latency Equalization to Enable Spraying and Reordering Elephant Flow in a Data Center Fat Tree* (declined 2020) describes the problem MRC now solves industry-wide.

> **`[verify before final PDF]`** — Candidate notes cite "6 issued, 6 pending, 18 total submissions." The tables below yield **36 lifetime disclosures / 24 since Aug 2020**, which is materially higher. The Talent Assessment snapshot (1HFY26) separately reports 1 patent pending USPTO approval, 3 approved patents in legal drafting, 2 submissions pending internal review, and 2 CPOL drafts imminent; Brook Crossman noted the innovation pace as **"on pace to break (ASP) records."** Reconcile the issued-versus-pending split against the CPOL portal and attach portal links. Per prior package guidance, do not describe a filing as an issued patent until confirmed.

### Patent Filings

*No issue dates recorded in the source extract — confirm granted versus pending per filing before final PDF.*

| Title | Innovators | Filing type | Filed |
| :--- | :--- | :--- | :--- |
| Underlay Network Traffic Steering | Bruce McDougall, Jeff Byzek, Alberto Rodriguez-Natal, Saswat Praharaj, Fabio Maino, Steve Wood | Continuation | 7/25/2024 |
| Authoritative Internet Protocol Version 6 (Ipv6) Traffic Marking In Software-Defined Wide-Area Networks (Sd-Wan) | Saswat Praharaj, Alberto Rodriguez-Natal, Bruce McDougall | Utility Original | 12/4/2025 |
| Smart-Tor Policy Orchestration Based On Nccl Topology | Clarence Filsfils, Pablo Camarillo, Ahmed Abdelsalam, Bruce McDougall, Carmine Scarpitta | Utility Non-Provisional | 11/11/2025 |
| Nic-Based Segment Routing In A Network Fabric | Clarence Filsfils, Pablo Camarillo, Ahmed Abdelsalam, Bruce McDougall, Carmine Scarpitta | Continuation | 2/5/2026 |
| Tor-Based Segment Routing In A Network Fabric | Clarence Filsfils, Pablo Camarillo, Ahmed Abdelsalam, Bruce McDougall, Carmine Scarpitta | Continuation | 2/5/2026 |
| Mechanism For Recovering Packet Policy From Telemetry Notifications In Ai Backends | Clarence Filsfils, Bruce McDougall, Pablo Camarillo, Joshua S Merrill, Ahmed Abdelsalam, Carmine Scarpitta | Utility Non-Provisional | 3/11/2026 |
| Nic-Based Segment Routing In A Network Fabric | Clarence Filsfils, Pablo Camarillo, Ahmed Abdelsalam, Bruce McDougall, Carmine Scarpitta | Continuation | 7/15/2026 |
| Nic-Based Segment Routing In A Network Fabric | Clarence Filsfils, Pablo Camarillo, Ahmed Abdelsalam, Bruce McDougall, Carmine Scarpitta | Continuation | 7/15/2026 |
| Mechanism For Recovering Packet Policy From Telemetry Notifications In Ai Backends | Clarence Filsfils, Bruce McDougall, Pablo Camarillo, Joshua S Merrill, Ahmed Abdelsalam, Carmine Scarpitta | Continuation | 7/15/2026 |

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
