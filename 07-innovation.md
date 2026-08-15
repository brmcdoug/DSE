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
| **Architectural specs** | SRv6 uSID multi-tenancy for AI factories (Apr 2026); Hoffman–Singleton fabric study; Policy Plane |
| **Hackathon** | Cisco EN Hackathon 2022 winner — SD-WAN + SRv6 (Team 6 / Group 14) |

---

## Flagship Innovations

---

### SRv6 on SONiC for the AI Backend, 2023 – 2026

**Customer Problem:** AI training fabrics need deterministic multipath and hard tenant isolation at GPU scale — requirements that standard ECMP and VXLAN overlays do not meet. Microsoft, Oracle, and the OpenAI compute supply chain were all converging on source-routed multipath, and all three preferred an open network operating system over a vendor NOS. Cisco had no SRv6 implementation on SONiC and no funded plan to build one. When Bruce first raised the requirement, MIG engineering disputed for weeks that customer urgency was real.

**Customer Solution:** Bruce built the evidence rather than repeating the argument. He authored *SRv6 uSID Multi-Tenancy and Security for AI Factory Network Fabrics* (Apr 2026), specifying encapsulation and decapsulation at leaf, NIC, or hybrid; uDT tenant-ID allocation within the 16-bit uSID space; explicit uA path pinning; and scale targets of 131,000 GPUs per cluster across multi-cluster topologies, with referenced SONiC implementation paths (SwSS PR #4404). He built the [srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator) so SEs and customer engineers could model Multipath Reliable Connection with SRv6 static routing before any product existed, and published the [srv6-msft](https://github.com/segmentrouting/srv6-msft) and [srv6-oci](https://github.com/segmentrouting/srv6-oci) POC repositories. He worked directly with SRv6 engineering on SONiC feature scope — uSID forwarding, static uSIDs, BGP GRT, sonic-vpp, sonic-vs — and drove the argument that OpenAI demand was pulling Microsoft and OCI investment. The lineage traces to a May 2023 brainstorm with Pablo Camarillo and Praveen Bhagwatula on SRv6 uSID for AI workloads, and to a disclosure Bruce filed in August 2023, *SRv6 uSID Scheduled Fabric for Artificial Intelligence and Machine Learning Clusters*, which was declined.

**Business Impact:** **SRv6 on SONiC shipped for the Cisco 8122** on the 202511 codebase in **June 2026**, with MIG committing SRv6-on-SONiC G200 in Q1 FY26 to unblock Microsoft and Oracle qualification. The specification became the reference architecture for the Microsoft, Oracle, and CoreWeave AI engagements documented in Business Impact. Microsoft and Oracle engineers used Bruce's repositories in their own internal executive presentations, and OCI reached limited SRv6 production by the end of 2025. The work generated the SmartTOR / NIC-based segment routing patent family with Clarence Filsfils, Pablo Camarillo, Ahmed Abdelsalam, and Carmine Scarpitta — now at five filings — plus *Mechanism for Recovering Packet Policy from Telemetry Notifications in AI Backends*. Both Microsoft and Oracle deployed initial SRv6-for-AI on competitor hardware before Cisco shipped; the architecture was validated, and the delay Bruce spent two years arguing against is the measurable cost. FY2027 TAM recovery projection `[pending finance validation]`.

---

### Isovalent / Cilium — Closing the Host-Networking Air-Gap, 2021 – 2026

**Customer Problem:** For every device running a traditional network operating system, a hyperscale environment runs hundreds or thousands of Linux hosts. That is where cloud operators terminate their overlays, enforce policy, and make forwarding decisions — and Cisco had no credible technology presence there. Bruce named this the **host-networking air-gap**. Without a position at the workload boundary, Cisco's transport products could not participate in the policy and segmentation decisions that increasingly determine network architecture.

**Customer Solution:** Beginning in 2021, Bruce advocated internally that Cisco acquire Isovalent, the company behind Cilium and eBPF, identifying it as the strategic control point rather than an adjacent tooling purchase. He performed the technical validation that made the case concrete: eBPF-based SRv6 L3VPN, egress gateway, and pod-level encapsulation and decapsulation. After the acquisition closed in 2024, he authored the Cilium-SP customer requirements document with progressive use cases from L3VPN through egress gateway to transit gateway (Mar 2026), defining the product integration path between cloud-native security and service provider transport. He then compiled account data worldwide to build the Cilium-SP feature investment case, and maintains the Cilium-SP opportunity and TAM tracker covering telco and SP use cases globally (Nov 2025).

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

### Low-Diameter AI Fabrics — Hoffman–Singleton and Polarfly, 2024 – 2025

**Customer Problem:** AI training clusters built on conventional Clos fabrics pay a node-count penalty that scales badly with GPU count. Oracle needed to know whether a fundamentally different topology could cut that cost without sacrificing bisection bandwidth or fault tolerance — a question requiring graph theory rather than product selection.

**Customer Solution:** Bruce applied Hoffman–Singleton graph theory to low-diameter, high-radix fabric design, producing the lab and design document with Chris Martin (Jun 2024) that evaluated slimfly- and dragonfly-class topologies against GPU-scale requirements. He extended the work through the Polarfly project with Chris Martin at OCI (Jan 2025), including the uSID-on-XRd AI-backend demonstration with Jag Brar.

**Business Impact:** The study documented **~50% savings on fabric nodes versus a comparable Clos design** for hyperscale data center fabrics (2HFY24 employee reflection). It anchored the Oracle AI-backend topology conversation and produced the *Virtualized Rail Architecture for AI/ML Ethernet Fabrics* and *AI Scale Up Pod Design for 1000 XPU* disclosures with Rob Murphy and Pirooz Tooyserkani. Both were declined. The underlying research remains the basis for Cisco's low-diameter fabric position with AI operators, and is documented in `projects/wmp-polarfly-whitepaper-v07.md`.

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
| **EN Hackathon winner** | 2022 | Cisco EN Hackathon winner (Team 6 / Group 14) — SD-WAN + SRv6 demonstration; preceded the SRv6-SGT work. [Winners page](https://cisco.sharepoint.com/sites/EN-Hackathon/SitePages/Hackathon2022-Winners.aspx) (internal) |
| **GitHub-first Cisco Live labs** | 2022–2026 | Bruce pioneered GitHub-based lab guides — configs, code, Containerlab — now common practice across instructor-led sessions. Same method as his customer co-development: open, reproducible, available before the product. `[SGM stats — how many ILTs now use the model]` |
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

| Asset Name | Title | Innovators | Asset Type | Case Type | Country Code | Sub Status Code | Filing Date | Issue Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C/P/1035601/US/CON/1 | UNDERLAY NETWORK TRAFFIC STEERING | Bruce McDougall, Jeff Byzek, Alberto Rodriguez-Natal, Saswat Praharaj, Fabio Maino, Steve Wood | Patent | Continuation | US | - | 7/25/2024 | - |
| C/P/1064834/US/ORG/1 | AUTHORITATIVE INTERNET PROTOCOL VERSION 6 (IPV6) TRAFFIC MARKING IN SOFTWARE-DEFINED WIDE-AREA NETWORKS (SD-WAN) | Saswat Praharaj, Alberto Rodriguez-Natal, Bruce McDougall | Patent | Utility Original | US | - | 12/4/2025 | - |
| C/P/1065283/US/UTL/1 | SMART-TOR POLICY ORCHESTRATION BASED ON NCCL TOPOLOGY | Clarence Filsfils, Pablo Camarillo, Ahmed Abdelsalam, Bruce McDougall, Carmine Scarpitta | Patent | Utility Non-Provisional | US | - | 11/11/2025 | - |
| C/P/1065283/US/CON/2 | NIC-BASED SEGMENT ROUTING IN A NETWORK FABRIC | Clarence Filsfils, Pablo Camarillo, Ahmed Abdelsalam, Bruce McDougall, Carmine Scarpitta | Patent | Continuation | US | - | 2/5/2026 | - |
| C/P/1065283/US/CON/1 | TOR-BASED SEGMENT ROUTING IN A NETWORK FABRIC | Clarence Filsfils, Pablo Camarillo, Ahmed Abdelsalam, Bruce McDougall, Carmine Scarpitta | Patent | Continuation | US | - | 2/5/2026 | - |
| C/P/1065287/US/UTL/1 | MECHANISM FOR RECOVERING PACKET POLICY FROM TELEMETRY NOTIFICATIONS IN AI BACKENDS | Clarence Filsfils, Bruce McDougall, Pablo Camarillo, Joshua S Merrill, Ahmed Abdelsalam, Carmine Scarpitta | Patent | Utility Non-Provisional | US | - | 3/11/2026 | - |
| C/P/1065283/US/CON/3 | NIC-BASED SEGMENT ROUTING IN A NETWORK FABRIC | Clarence Filsfils, Pablo Camarillo, Ahmed Abdelsalam, Bruce McDougall, Carmine Scarpitta | Patent | Continuation | US | - | 7/15/2026 | - |
| C/P/1065283/US/CON/4 | NIC-BASED SEGMENT ROUTING IN A NETWORK FABRIC | Clarence Filsfils, Pablo Camarillo, Ahmed Abdelsalam, Bruce McDougall, Carmine Scarpitta | Patent | Continuation | US | - | 7/15/2026 | - |
| C/P/1065287/US/CON/1 | MECHANISM FOR RECOVERING PACKET POLICY FROM TELEMETRY NOTIFICATIONS IN AI BACKENDS | Clarence Filsfils, Bruce McDougall, Pablo Camarillo, Joshua S Merrill, Ahmed Abdelsalam, Carmine Scarpitta | Patent | Continuation | US | - | 7/15/2026 | - |

### All CIPOL Innovation Disclosures

| DocketNo | Status | Title | Innovators | SubmittedDate | SubmissionType | PPM | CommitteeTitle | CreatedDate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C/I/1005976/ | Declined | Container networking via BGP and BMP | Tim Evens, Tim Laberge, Bruce McDougall, Karam Sivia | 2016-08-29 | Utility | Urmil Dave | X - Software Defined Networking | 2022-03-30T14:44:16.000Z |
| C/I/1015328/ | Declined | Advanced DDOS mitigation via the application of tagged packet headers to authenticated sessions | Dave Clough, Steve Braaten, Bruce McDougall, Karthik Kumaravel, Meghan McGinn | 2019-05-23 | Utility | Yandie Fashu-Kanu | Cisco Security | 2022-03-30T15:02:58.000Z |
| C/I/1020991/ | Declined | UntitledMapping network topology and performance data and executing traffic engineering policies via a graph database control plane and segment routing data plane | Bruce McDougall | 2018-10-28 | Utility | Rob Hamilton | Customer Experience | 2022-03-30T15:41:21.000Z |
| C/I/1024332/ | Approved - Defensive Publication | Dataplanebased DDOS mitigation and spoofing prevention via Segment Routing v6 SRv6 network programming | Bruce McDougall, Karthik Kumaravel, Dave Clough, Meghan McGinn | 2019-05-28 | Utility | Yandie Fashu-Kanu | Cisco Security | 2022-03-30T15:57:01.000Z |
| C/I/1024741/ | Declined | | Bruce McDougall | 2019-05-28 | Utility | Rob Hamilton | Customer Experience | 2022-03-30T15:39:21.000Z |
| C/I/1028300/ | Declined | SRv6 DNS Proxy for Improved Network Quality of Experience | Bruce McDougall, Karthik Kumaravel, Dave Clough, Zia Syed, Jeff Byzek | 2020-06-30 | Utility | Jurg Domenig | Routing, Switching, and Network OS | 2022-03-30T16:34:30.000Z |
| C/I/1029102/ | Declined | A Generalized Software Defined Networking Infrastructure Platform | Bruce McDougall, Jeff Byzek | 2022-02-04 | Utility | Rob Hamilton | Customer Experience | 2022-03-30T16:37:39.000Z |
| C/I/1029257/ | Draft | Multi Domain SRv6 Proxy for Improved Network Quality of Experience | Dave Clough, Karthik Kumaravel, Bruce McDougall, Jeff Byzek | 2020-06-25 | Utility | TBD | To Be Decided | 2022-03-30T16:41:48.000Z |
| C/I/1029329/ | Declined | Simplified 5G Core for enterprise use cases Cloudnative solution for integrating cloudnative applications into service provider 5G networks | Clarence Filsfils, Ahmed Abdelsalam, Serguei Bezverkhi, Bruce McDougall | 2020-07-03 | Utility | Jurg Domenig | Routing, Switching, and Network OS | 2022-03-30T16:43:47.000Z |
| C/I/1029638/ | Draft | DDOS mitigation via the application of tagged packet headers to authenticated sessions | Bruce McDougall, Karthik Kumaravel, Dave Clough, Jeff Byzek | 2020-07-09 | Utility | TBD | To Be Decided | 2022-03-30T16:42:59.000Z |
| C/I/1030123/ | Declined | Latency Equalization to enable spraying and reordering elephant flow in a Data Center Fat Tree | Pascal Thubert, Francois Clad, Clarence Filsfils, Bruce McDougall | 2020-12-14 | Utility | Jurg Domenig | Routing, Switching, and Network OS | 2022-03-30T16:48:41.000Z |
| C/I/1032284/ | Declined | Wireless Client experience optimization SDN Subscription Model for Application Aware Networking | Bruce McDougall, Zafar Ali | 2021-03-01 | Utility | Henal Babariya | [deprecated-do not use]Patentathon-BID | 2022-03-30T17:05:17.000Z |
| C/I/1035600/ | Approved - Patent Application | System and method for SDWAN tunnel provisioning via control plane based on application connectivity requirements | Saswat Praharaj, Fabio Maino, Alberto Rodriguez-Natal, Pradeep K Kathail, Bruce McDougall | 2021-12-30 | Utility | Clifford Chang | SD-WAN | 2022-03-30T17:27:03.000Z |
| C/I/1035601/ | Approved - Patent Application | SP Underlay Services for SDWAN | Bruce McDougall, Jeff Byzek, Alberto Rodriguez-Natal, Saswat Praharaj, Fabio Maino, Steve Wood | 2022-02-04 | Utility | Clifford Chang | SD-WAN | 2022-03-31T08:40:08.000Z |
| C/I/1035941/ | Declined | Programmatic authenticated access control in a controllermediated SRv6 network | Jeff Byzek, Bruce McDougall | 2022-02-04 | Utility | Jurg Domenig | Routing, Switching, and Network OS | 2022-03-31T08:40:13.000Z |
| C/I/1035965/ | Draft | Customized Topology Modeling in a Generalized Software Defined Networking Infrastructure Platform | Jeff Byzek, Bruce McDougall | 2022-02-01 | Utility | TBD | To Be Decided | 2022-03-30T17:29:18.000Z |
| C/I/1038384/ | Declined | Methods for secure DTN full and partial mesh design in interplanetary networks | PLAMEN Nedeltchev, Bruce McDougall, Brian A Christensen, Jag Kahlon, Jason H Hsieh | 2022-08-23 | Utility | Jan Lucas | Cisco Observability, Performance & Monitoring | 2022-09-20T05:25:12.000Z |
| C/I/1038927/ | Approved - Patent Application | Network OS Scheduled FIB to account for intermittent connectivity due to orbital dynamics | PLAMEN Nedeltchev, Bruce McDougall | 2022-10-12 | Utility | Jurg Domenig | Routing, Switching, and Network OS | 2022-10-10T19:11:46.000Z |
| C/I/1039921/ | Approved - Patent Application | Synthetic Path Trace of Segment Routed Networks | Hans Ashlock, Bruce McDougall, Ben Haddox | 2023-01-31 | Utility | Jan Lucas | Cisco Observability, Performance & Monitoring | 2023-01-31T03:34:30.000Z |
| C/I/1041019/ | Declined | Controlled Unicast Replication using BGP CURB | Niall C Masterson, Anbu Gunalan, Anup Kumar Vasudevan, Bruce McDougall | 2023-07-06 | Utility | Jurg Domenig | Routing, Switching, and Network OS | 2023-04-04T09:02:45.000Z |
| C/I/1042462/ | Declined | Controlled Unicast Replication using BGP CURB Large Community Bit Index | Niall C Masterson, Anbu Gunalan, Bruce McDougall, Anup Kumar Vasudevan | 2023-07-18 | Utility | Jurg Domenig | Routing, Switching, and Network OS | 2023-07-14T05:44:11.000Z |
| C/I/1042877/ | Declined | SRv6 uSID Scheduled Fabric for Artificial Intelligence and Machine Learning Clusters | Bruce McDougall, Pablo Camarillo, Clarence Filsfils, Praveen Bhagwatula | 2023-08-25 | Utility | Urmil Dave | Network Controller and Management | 2023-08-23T14:12:16.000Z |
| C/I/1043145/ | Declined | Network OS Elastic Network Policy Plane | Bruce McDougall, Joshua S Merrill | 2023-09-11 | Utility | Jurg Domenig | Routing, Switching, and Network OS | 2023-09-12T01:09:08.000Z |
| C/I/1062880/ | Declined | Segment Routing SID and SGT state preservation for traffic traversing a nonSRSRv6 service chain | Bruce McDougall, Rupak Chandra, Joshua S Merrill | 2025-10-30 | Utility | Yandie Fashu-Kanu | Cisco Security | 2024-10-13T19:43:55.000Z |
| C/I/1062903/ | Draft | Network enabled AI pipelines | | | Utility | | To Be Decided | 2024-10-16T18:00:21.000Z |
| C/I/1064834/ | Approved - Patent Application | System and Method for Authoritative IPv6 Traffic Marking in SDWAN Networks | Saswat Praharaj, Alberto Rodriguez-Natal, Bruce McDougall | 2025-05-22 | Utility | Clifford Chang | SD-WAN | 2025-01-04T19:50:33.000Z |
| C/I/1065283/ | Approved - Patent Application | SmartTOR Policy Orchestration based on NCCL topology | Clarence Filsfils, Pablo Camarillo, Ahmed Abdelsalam, Bruce McDougall | 2025-03-21 | Utility | Jurg Domenig | Routing, Switching, and Network OS | 2025-03-20T18:46:19.000Z |
| C/I/1065285/ | Approved - Defensive Publication | Avoiding Fabric Congestion Using an SRTE Agent for AI training using existing Data Centers | Zafar Ali, Clarence Filsfils, Francois Clad, Pablo Camarillo, Bruce McDougall | 2025-03-21 | Utility | Jurg Domenig | Outshift & Emerging Technology | 2025-03-20T19:09:57.000Z |
| C/I/1065286/ | Merged | Optimizing an AI training cluster without GPU topology awareness | Pablo Camarillo, Clarence Filsfils, Ahmed Abdelsalam, Bruce McDougall | 2025-03-21 | Utility | Jurg Domenig | Outshift & Emerging Technology | 2025-03-20T19:28:49.000Z |
| C/I/1065313/ | Merged | SRv6 uSID Carrier with Embedded Security Group Tag SGT to Identify AI Request | Bruce McDougall, Joshua S Merrill, Pablo Camarillo, Clarence Filsfils, Ahmed Abdelsalam | 2025-03-21 | Utility | Jurg Domenig | Routing, Switching, and Network OS | 2025-03-20T22:16:34.000Z |
| C/I/1066656/ | Declined | Virtualized Rail Architecture for AIML Ethernet fabrics | Bruce McDougall, Rob Murphy | 2025-10-02 | Utility | Jurg Domenig | Outshift & Emerging Technology | 2025-08-29T20:10:26.000Z |
| C/I/1067161/ | Declined | AI Scale Up Pod Design for 1000 XPU | Rob Murphy, Bruce McDougall, Pirooz Tooyserkani | 2025-11-23 | Design | Cato Nyberg | Hardware Design | 2025-10-23T23:33:36.000Z |
| C/I/1067244/ | Declined | Using Ethereum NonFungible Tokens to prevent BGP Route Hijacks | Brian S Shlisky, Bruce McDougall, Jakob Heitz, John N Cuneo | 2025-12-02 | Utility | Jurg Domenig | Routing, Switching, and Network OS | 2025-11-01T21:25:07.000Z |
| C/I/1067996/ | Declined | Spraying encrypted traffic across multiple disjoint SRv6 paths to mitigate the impact of future quantum decryption techniques | Bruce McDougall, Brook Crossman | 2026-05-06 | Utility | Jurg Domenig | Routing, Switching, and Network OS | 2026-01-27T04:28:48.000Z |
| C/I/1068842/ | Draft | Temporal Optimization of AI Network Paths | | | Utility | | To Be Decided | 2026-03-30T16:27:08.000Z |
| C/I/994875/ | Approved - Patent Application | Segment routing label switch paths in network functions virtualization communications networks | Siva Sivabalan, Sami Boutros, Clarence Filsfils, Rex Fernando, Lakshmi Sharma, Santiago Freitas, Bruce McDougall, Rob Fielding | 2014-06-08 | Utility | Urmil Dave | X - Software Defined Networking | 2022-03-30T11:59:38.000Z |


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
