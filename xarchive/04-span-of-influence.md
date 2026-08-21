## Span of Influence

## How Bruce's Span of Influence Expanded

| Period           | Altitude and scope                                             | Evidence                                                                                                                                                                                    |
| ------------------ | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2020**         | Production routing and data centre SME for Web and SP accounts | Account and theater engagements through MIG engineering                                                                                                                                     |
| **2021–2022**    | Cross-BU advisor without mandate                               | SD-WAN product direction with CNWAN; SP Edge tiger team co-lead; PSE review subcommittee                                                                                                    |
| **2023–2024**    | Architecture-organization altitude                             | SR brain trust field lead; SONiC investment case; Americas PA/DA SONiC forum; Future Enterprise Segmentation; corporate development advisory                                                |
| **2024–present** | Cross-platform engineering engagement                          | SRv6 feature development across **IOS-XR, IOS-XE, NX-OS, SONiC, SD-WAN, SASE, ThousandEyes** (Synthetic Path Tracing patent) **and Cilium** — eight platforms, five business entities       |
| **2025–2026**    | Company and executive altitude                                 | SOSIE co-founder; Web/Hyperscale representative for executive BU interlocks; FY26 Global Sales Technical Roadmap owner; EVPN readout to CPO Jeetu Patel; Cilium CRD accepted by engineering |

None of this influence came with authority attached. Business entities outside Bruce's own engage him because he settles an architecture on its merits first, and works out Cisco's position from there.

### How he thinks about it

Bruce reasons about networks the way a hyperscale architect does: **topologically, rather than by product category.** A data centre platform and a backbone platform are not different kinds of thing — both move data. In some places the topology is highly symmetric and concentrated into a small physical space; in others it is asymmetric, with far lower available bandwidth per square kilometre. The difference is one of degree, not of kind.

Cisco's portfolio, like every large vendor's, is organized into places in the network, and its engineering organizations mirror that division — Conway's law at work. Operating outside that framing is what lets Bruce see the seams: **unified SRv6 forwarding** end to end rather than per-domain encapsulations, **fixed-form-factor fabrics** in roles that convention reserved for chassis, **flat low-diameter topologies** in place of hierarchy, and **the host as a first-class network participant**.

He applies the same reduction to policy. There is nothing categorically distinct about a firewall, an access control list, or a Layer 3 VPN — each is a way of forwarding data *intentionally* rather than blindly. Recognizing them as one problem is what produced the **Policy Plane** and the SRv6-with-SGT architecture.

### Technology domains (DSE requires ≥2)

1. **Programmable transport** — Segment Routing and SRv6 uSID, end to end
2. **Cloud-native and host networking** — eBPF, Cilium, Kubernetes CNI
3. **Open network operating systems** — SONiC, Linux NOS strategy, disaggregation
4. **Enterprise identity and policy** — SGT, segmentation, the Policy Plane

---

## Internal Influence — Initiatives and Relationships

| Initiative and date                                                | Impact                                                                                                                                                                                                   |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **SR brain trust field lead** — 2020 – present                     | Cisco's Segment Routing engineering organization under Fellow **Clarence Filsfils** sets architecture direction for the transport portfolio and, increasingly, for how Cisco competes in AI infrastructure. Bruce has been one of a small number of trusted field voices in it for nearly a decade. After his *Scaling the Cloud to a Billion Servers* workshop in 2020, Filsfils tasked him with leading Cisco's **hyperscale SRv6 market entry**. He acts as the field broker between SEs and Clarence's team, is credited in the contributor acknowledgements of three chapters of the SRv6 book, and has driven product decisions including uSID block scale and static uSIDs in IOS-XR and uSID support in SONiC. *More details are located in the Innovation section of this document.* |
| **Global field lead, SR-Apps** — 2020 – present                    | Bruce co-develops SR-Apps with SR and MIG engineering, and SR engineering adopted his open-source Jalapeno project as its development platform for SR-Apps R&D — a field-built project becoming the foundation of an engineering initiative. He also runs the CNRS and OST Zurich university research channel. *More details are located in the Innovation section of this document.* |
| **Host networking and the Isovalent acquisition** — 2021 – present | Bruce named the **host-networking air-gap** and argued for years that Cisco needed a presence at the workload boundary — an argument that required persuading business entities outside MIG entirely, since no transport BU owned the problem. He advocated acquiring Isovalent from 2021, built the Cilium-SP investment case (**~$34M Isovalent / ~$323M MIG pullthrough**), and authored the multi-use-case Cilium CRD that **Cisco engineering has accepted and is working to prioritize**. **Thomas Graf**, Cilium co-creator and Isovalent founder, can attest. *More details are located in the Innovation section of this document.* |
| **SD-WAN, SSE, and enterprise platforms** — 2020 – present         | SD-WAN, Cisco Secure Access, and the enterprise security portfolio sit outside Bruce's segment, and each was building its own transport and policy model. He established himself as a standing advisor without mandate — advising Alberto Rodriguez-Natal and the CNWAN team, proposing the direct binding-SID approach as SD-WAN SP-API advisor, reaching architectural agreement with Rupak Chandra on SRv6 for Cisco Secure Access, and serving as cloud-native SME on demand to BE leaders including Steve Wood and Errol Roberts. **The influence is documented in issued IP: Bruce is first-named inventor on *Underlay Network Traffic Steering*, granted October 2024**, alongside SD-WAN engineering staff — first inventor position on a granted patent filed by a business entity he does not belong to. *More details are located in the Innovation section of this document.* |
| **SRv6 with SGT and the Policy Plane** — 2022 – present            | Cisco carried identity in one architecture and scale in another, and the two never met. Working the Future Enterprise Segmentation tiger team, Bruce recognized that an SGT and a uSID are both 16 bits, and designed the architecture that unifies them. He presented SRv6+SGT to Matt Gillies with Josh Merrill, brought in ISE Distinguished Engineer Darren Miller, and generalized the work into the **Policy Plane**. **By December 2025 the ISE organization had committed** to SRv6 SGT and a Secure Network Policy Framework. At Verizon, Bruce designed the architecture and the intellectual property while Josh Merrill carried the executive presentations. *More details are located in the Innovation section of this document.* |
| **Single OS (SOSIE) working group co-founder** — 2024 – present    | Cisco had converged its hardware on Silicon One while its software remained fragmented across NX-OS, IOS-XR, and IOS-XE, at an estimated **$500M of Edgecore leakage** `[verify quotable]`. No business entity owned the problem and no forum existed to raise it. Bruce co-founded SOSIE with DSE and PSE peers **Brenden Buresh, Craig Hill, Virginia Teixeira, and Rob Murphy**, framing the multi-year path toward a Linux-based NOS with hardware-accelerated packet applications and a Cilium-class service control plane. |
| **Open NOS and SONiC strategy** — 2023 – present                   | Bruce led the Americas PA/DA SONiC forum (Dec 2023), building field-architect consensus across Cloud, SP, Enterprise, and Public Sector, and bridges Silicon One, Cisco 8000, SONiC, and AI-backend engineering. Sustained relationships with **Vijay Tapaskar** and **Mani Veerachamy** (SONiC on Cisco 8000) and Cisco Fellow **Praveen Bhagwatula**. At IETF Vancouver 2024, Ianik Semko referred to Bruce and his collaborators as *"the 2030 guys."* He also drove the SONiC with Cisco Secure Workload POC, pulling a security business entity into a platform conversation MIG could not resolve alone. *More details are located in the Innovation section of this document.* |
| **SP Network-as-a-Service and Project Yukon** — 2021 – 2024        | Bruce originated the internal argument that service providers should expose network capability for **cloud-like consumption** rather than selling circuits, and carried it through MCNS and NetCo/ServCo work with Brian Meaney and Virginia Teixeira, the Cross-Domain Broker readout to Beesely, Mohit Lad, and Eric Knipp, and Project Yukon at Verizon and AT&T. *More details are located in the Business Impact section of this document.* |
| **Executive interlocks and roadmap ownership** — 2025 – present    | Bruce is the **Web and Hyperscale representative for executive business entity interlocks** and owned **FY26 Global Sales Technical Roadmap** and BE Interlock Process responsibilities, setting the technical asks for AI, SRv6, and SONiC at sales-organization altitude. He delivered the EVPN Least Complexity tiger team readout to executives including Chief Product Officer **Jeetu Patel**. |
| **Corporate development advisory** — Jun 2024                      | Cisco corporate development engaged Bruce as technical consultant on **AI tier-2 and neo-cloud equity investments** (Vladimirs Sazonovs, Lauren Johnson, Ryan Houska) — field architecture judgment inside corporate investment decisions, a function ordinarily served by strategy or engineering staff rather than by a field systems engineer. |
| **Competitive and portfolio intelligence** — 2023 – 2026           | **Only member from the sales organization** on the SL-OnDemand tiger team (with CX, Subha Dhesikan), delivering the executive readout in March 2024. Consultant to the Security business entity on Portfolio Innovation Areas (Feb 2026, with Connors, Lake, Roberts). Authored and delivered *Combatting Disaggregation with Network Service Innovation (SRv6)* to the full ASP organization, repeated at TMC Innovation Hour by request. |
| **PSE review subcommittee** — 2021 – 2024                          | **Three years as a voting member**, shaping the promotion standard itself rather than only preparing candidates to meet it. *More details are located in the Leadership section of this document.*       |

---

## Executive and Fellow Relationships

| Name                                                   | Role                                    | Domain                                                              |
| --------------------------------------------------------- | ------------------------------------------ | ---------------------------------------------------------------------- |
| **Clarence Filsfils**                                  | Cisco Fellow                            | Segment Routing and SRv6                                            |
| **Praveen Bhagwatula**                                 | Cisco Fellow                            | SONiC                                                               |
| **Thomas Graf**                                        | Cilium co-creator; Isovalent founder    | Host networking, eBPF                                               |
| **Vijay Tapaskar**, **Mani Veerachamy**                | SONiC on Cisco 8000 engineering         | Open NOS                                                            |
| **Kevin Wollenweber**                                  | BE leadership, MIG                      | SONiC and SRv6 investment                                           |
| **Matt Gillies**, **Tim Carnes**                       | Global Solutions Engineering leadership | SRv6+SGT validation; Bruce's leadership from Jun 2026               |
| **Eric Knipp**, **John Dorval**, **Patrick Morrissey** | Sales vice presidents                   | Cited Bruce's influence at **>$1B** `[verify attributable by name]` |
| **Jeetu Patel**                                        | Chief Product Officer                   | EVPN Least Complexity readout                                       |

## Cross-Organization Peer Network

Bruce's span rests on a habit rather than an assignment: over two decades he has built and maintained working relationships with senior SEs, PSEs, and DSEs across Cisco without regard to geography or vertical alignment, sustaining them for the learning and idea exchange as much as for any engagement. Most of the Global Impact section is downstream of this.

| Peer                  | Role                                                | Shared work                                                                                               |
| ------------------------ | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| **Brenden Buresh**    | DA, GES Office of the CTO                           | SOSIE co-founder; DC/NX-OS tiger team; Adobe Cilium POC                                                   |
| **Craig Hill**        | DSE, US Public Sector                               | SOSIE co-founder; Future Enterprise Segmentation; co-recipient, 2025 Pinnacle Award                       |
| **Virginia Teixeira** | DSE, EMEA                                           | SOSIE co-founder; DCN and transport/AI convergence                                                        |
| **Rob Murphy**        | PSE                                                 | SOSIE co-founder; SONiC labs; AI fabric disclosures                                                       |
| **David Jansen**      | DSE                                                 | SP Edge tiger team; Americas SONiC forum                                                                  |
| **Brian Meaney**      | DA, EMEA CTO                                        | MCNS, NetCo/ServCo, NaaS architecture                                                                     |
| **Mike McPhee**       | DSE                                                 | PSE review subcommittee                                                                                   |
| **Marina Ferreira**   | PSE                                                 | Future Enterprise Segmentation; DC/NX-OS tiger team                                                       |
| **Josh Merrill**      | PSE                                                 | SGT-in-uSID co-inventor; Policy Plane; Yukon++                                                            |
| **Christian Martin**  | Cisco MIG hyperscaler architecture *(formerly OCI)* | Low-diameter fabric research; WMP-PolarFly — an external research partnership that became an internal one |

---

## Signature Internal Influence Themes

Five positions Bruce is known for inside Cisco. Each began as a minority view; each has since become, or is becoming, company direction.

1. **The host-networking air-gap** — the control point moved to the host; Cisco must participate in Linux and eBPF. *Outcome: Isovalent acquisition, 2024.*
2. **SRv6 uSID as a network API** — one programming model across IOS-XR, IOS-XE, NX-OS, SONiC, SD-WAN, and host CNI. *Outcome: 2025 Pinnacle Award; platform alignment across six product lines.*
3. **Open NOS and SONiC** — required for hyperscaler relevance. *Outcome: SRv6 on SONiC shipped for the Cisco 8122, June 2026.*
4. **The Policy Plane** — identity, transport, and observability as composable layers. *Outcome: ISE committed to the Secure Network Policy Framework, December 2025.* `[verify PM attribution]`
5. **Linux as the future NOS** — routing as hardware-accelerated applications on a Cilium-class control plane. *Outcome: SOSIE working group; ongoing.*
