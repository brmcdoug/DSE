## Span of Influence

## How Bruce's Span of Influence Expanded

| Period           | Altitude and scope                                             | Evidence                                                                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2020**         | Production routing and data centre SME for Web and SP accounts | Account and theater engagements through MIG engineering                                                                                                                                     |
| **2021–2022**    | Cross-BU advisor                                                | SD-WAN product direction with SP-services API spec and CNWAN; SP Edge tiger team co-lead; PSE review subcommittee                                                                          |
| **2023–2024**    | Architecture-organization altitude                             | SR brain trust field lead; SONiC investment case; Americas PA/DA SONiC forum; Future Enterprise Segmentation tiger team; corporate development advisory                                                |
| **2024–present** | Cross-platform engineering engagement                          | SRv6 feature development across **IOS-XR, IOS-XE, NX-OS, SONiC, SD-WAN, SASE, ThousandEyes** (Synthetic Path Tracing patent) **and Cilium** — eight platforms, five business entities       |
| **2025–2026**    | Company and executive altitude                                 | Co-founder, **SOSIE**, **UFA**, and **UPM** tiger teams; Web/Hyperscale representative for executive BU interlocks; FY26 Global Sales Technical Roadmap owner; EVPN Least Complexity issue reaches CPO Jeetu Patel via Brook Crossman; Cilium CRD accepted by engineering |

Bruce's influence inside Cisco comes from a specific vantage point: he has spent the better part of a decade deeply enmeshed in the architectures actually driving the industry — Hyperscale DC and WAN, open NOS, host networking, and now AI fabrics — and that proximity to where the industry is headed is why he has been right often enough, early enough, that people from across the company ask what he thinks.

### How he thinks about it

Bruce reasons about networks the way a hyperscale architect does: holistically, and independent of vendor org charts and product silos. A data centre platform and a backbone platform are fundamentally the same kind of thing. Linux is an operating system, routing and switching are apps. In some places the topology is highly symmetric and concentrated into a small physical space; in others it is asymmetric, with far lower available bandwidth per square kilometre. The difference is one of degree, not of kind.

Cisco's engineering organization, like every large vendor's, is divided into places in the network — Conway's Law in practice — and that division works against how hyperscalers and network operators actually think about their own infrastructure. Much of Bruce's internal-facing work has been a sustained effort to push Cisco past it, bringing the company into line with where the hyperscaler and AI-driven market had already gone: **unified SRv6 forwarding** end to end rather than per-domain encapsulations, **fixed-form-factor fabrics** in roles convention reserved for chassis, **flat low-diameter topologies** in place of hierarchy, and **the host as a first-class network participant**. He applies the same reduction to policy — a firewall, an access control list, and a Layer 3 VPN are all ways of forwarding data *intentionally* rather than blindly, one problem rather than several.
// from my perspective Conway's Law is a bad thing as it means Cisco is organized around a world that no longer exists. The trick shot here is how to say that without being insulting and still convey my DSE-level work to try and break Cisco out of it and into the hyperscale/AI world of today? Also, "like every large vendor's" is not accurate. In fact our competitors (Arista, Juniper, Nokia) purposefully exploit Cisco's siloed approach and sell a single/unified solution across campus, DC, and WAN

That thinking is now formalized in three tiger teams Bruce co-founded. **SOSIE** argues for a single Linux-based network operating system in place of NX-OS, IOS-XR, and IOS-XE. The **Unified Forwarding Architecture (UFA)** is the SRv6-end-to-end effort described above, carried as a named initiative. The **Unified Policy Model (UPM)** embeds identity into that same forwarding plane so enterprise segmentation (SGT) and hyperscale transport share one policy model rather than two. Bruce is also advocating — a position still in progress, not yet realized — that Cisco invest directly in AI host networking, developing SmartNICs and a scale-up Ethernet solution to compete directly with Nvidia, AMD, and Broadcom, and pushing each successive silicon generation to market on a competitive timeline so Cisco does not concede addressable market to those competitors by arriving late.
// let's rename SOSIE to Single-OS, or better yet Single-Secure-OS (SSOS)

### Technology domains (DSE requires ≥2)

1. **Mass Scale Infrastructure** - Hyperscale routing, data center, and AI network architecture
2. **Programmable transport** — Segment Routing and SRv6 uSID, end to end
3. **Cloud-native and host networking** — eBPF, Cilium, Kubernetes CNI
4. **Open network operating systems** — SONiC, Linux NOS strategy, disaggregation
5. **Enterprise identity and policy** — SGT, segmentation, the Unified Policy Model

---

## Internal Influence — Initiatives and Relationships

| Initiative and date                                                | Impact                                                                                                                                                                                                   |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **SR brain trust field lead** — 2020 – present                     | Cisco's Segment Routing engineering organization under Fellow **Clarence Filsfils** sets architecture direction for the transport portfolio and, increasingly, for how Cisco competes in AI infrastructure. Bruce has been one of a small number of trusted field voices in it for nearly a decade. After his *Scaling the Cloud to a Billion Servers* presentation an in internal workshop in 2020, Filsfils tasked him with leading Cisco's **hyperscale SRv6 market entry**. He acts as the field broker between SEs and Clarence's team, is credited in the contributor acknowledgements of three chapters of the SRv6 book, and has driven product decisions including uSID block scale and static uSIDs in IOS-XR and uSID support in SONiC. *More details are located in the Innovation section of this document.* |
| **Host networking and the Isovalent acquisition** — 2021 – present | Bruce named the **host-networking air-gap** and argued for years that Cisco needed a presence at the workload boundary — an argument that required persuading business entities outside MIG, since no transport BU owned the problem. He advocated acquiring Isovalent from 2021, recently built the Cilium-SP investment case (**~$34M Isovalent / ~$323M MIG pullthrough**), and authored the multi-use-case Cilium CRD that **Cisco engineering has accepted and is working to prioritize**. **Thomas Graf**, Cilium co-creator and Isovalent founder, can attest. *More details are located in the Innovation section of this document.* |
| **SD-WAN, SSE, and enterprise platforms** — 2020 – present         | Bruce developed relationships and influence with senior engineers in the SD-WAN, Cisco Secure Access, and the enterprise security portfolio. He established himself as a strategic advisor and SR/SRv6 SME to Alberto Rodriguez-Natal leading the CNWAN project, and proposed the SD-WAN Service-Provider-API use the SR Binding-SID apprach rather than legacy DSCP-mappings, collaborated with Rupak Chandra on SRv6 for Cisco Secure Access, and serving as cloud-native SME on demand to security and SDWAN Distinguished Engineers Steve Wood and Errol Roberts. **The influence is documented in issued IP: Bruce is first-named inventor on *Underlay Network Traffic Steering*, granted October 2024**, alongside SD-WAN engineering staff — first inventor position on a granted patent filed by a business entity he does not belong to. *More details are located in the Innovation section of this document.* |
// is the 'first inventor position' actually important, or is this a case of the agent rigidly following a rule about business entities i've not been traditionally aligned with?
| **SRv6 with SGT and the Unified Policy Model (UPM)** — 2022 – present | Cisco carried identity in one architecture and scale in another, and the two never met. Working the Future Enterprise Segmentation tiger team, Bruce recognized that an SGT and a uSID are both 16 bits, and designed the architecture that unifies them. He co-founded the **Unified Policy Model (UPM)** tiger team to carry the idea forward, presented SRv6+SGT to Matt Gillies with Josh Merrill, and brought in ISE Distinguished Engineer Darren Miller. **By December 2025 the ISE organization had committed** to SRv6 SGT and a unified policy model. At Verizon, Bruce designed the architecture and the intellectual property while Josh Merrill carried the executive presentations. *More details are located in the Innovation section of this document.* |
// I would characterize it as Cisco's identity architecture has been fragmented to date and UPM looks to unify it and `extra bonus` tie it to the scale, extensibility and power of SRv6!
| **Single OS (SOSIE) working group co-founder** — 2024 – present    | Cisco had converged its hardware on Silicon One while its software remained fragmented across NX-OS, IOS-XR, and IOS-XE, a fact that is ruthlessly exploited by competitors like Arista and Juniper with stories built around single-OS + single management platforms. No business entity owned the problem and no forum existed to raise it. Bruce co-founded SOSIE with DSE and PSE peers **Brenden Buresh, Craig Hill, Virginia Teixeira, and Rob Murphy**, framing the multi-year path toward a Linux-based NOS with containerized routing, switching, and policy applications driving NPUs and Cilium/Tetragon/eBPF to secure the OS. |
| **Open NOS and SONiC strategy** — 2023 – present                   | Bruce led the Americas PA/DA SONiC forum (Dec 2023), building field-architect consensus across Cloud, SP, Enterprise, and Public Sector, and bridges Silicon One, Cisco 8000, SONiC, and AI-backend engineering. Sustained relationships with **Vijay Tapaskar** and **Mani Veerachamy** (SONiC on Cisco 8000) and Cisco Fellow **Praveen Bhagwatula**. He also drove the SONiC with Cisco Secure Workload and SONiC with Cilium/Tetragon POCs, demonstrating to MIG engineering leadership a path to aligning SONiC with Cisco's Live Protect strategy on NXOS, IOS-XE, and IOS-XR. *More details are located in the Innovation section of this document.* |
| **SP Network-as-a-Service and Project Yukon** — 2021 – 2024        | Bruce originated the internal argument that service providers should expose network capability for **cloud-like consumption** rather than just selling (commodity) circuits, and carried it through the NetCo/ServCo work with EU DSEs Brian Meaney and Virginia Teixeira, the Cross-Domain Broker readout to Beesely, Mohit Lad, and Eric Knipp, and Project Yukon at Verizon and AT&T. *More details are located in the Business Impact section of this document.* |
// the readout with Beesely et al didn't produce much of anything so i think we can drop it
| **Executive interlocks and roadmap ownership** — 2025 – present    | Bruce is the **Web and Hyperscale representative for executive business entity interlocks** and owned **FY26 Global Sales Technical Roadmap** and BE Interlock Process responsibilities, setting the technical asks for AI, SRv6, and SONiC at sales-organization altitude. He also co-prepared the **EVPN Least Complexity readout** with an informal group of PSEs and DSEs; **Brook Crossman delivered it to Chief Product Officer Jeetu Patel**, who committed to fixing the underlying problem and scheduled regular check-ins with Brook to track it. |
// i think this is an overclaim: "and owned **FY26 Global Sales Technical Roadmap** and BE Interlock Process responsibilities"...co-owner/coordinator along with Web SE Director Tyler Nielson and Web PSEs Rob Murphy and Masi Mohammad
| **Corporate development advisory** — Jun 2024                      | Cisco corporate development engaged Bruce as technical consultant on **AI tier-2 and neo-cloud equity investments** (Vladimirs Sazonovs, and sales leaders Lauren Johnson, Ryan Houska). |
// todo - Bruce check with Ryan and Vladimirs on outcome
| **Competitive and portfolio intelligence** — 2023 – 2026           | **Only member from the sales organization** on Cisco CX's SL-OnDemand tiger team led by CX DE Subha Dhesikan. Bruce collaborated with CX architects on a proposal for a CX managed `cloud-like consumption of network services` solution and delivered the readout to CX executives in March 2024. Consultant to the Security business entity on Portfolio Innovation Areas (Feb 2026, with Craig Connors, Mike Lake, Errol Roberts). Authored and delivered *Combatting Disaggregation with Network Service Innovation (SRv6)* to the full ASP organization, repeated at TMC Innovation Hour by request. |
| **PSE review subcommittee** — 2021 – 2024                          | **Three years as a voting member**, shaping the promotion standard itself rather than only preparing candidates to meet it. *More details are located in the Leadership section of this document.*       |
// shaping the promotion standard is an oversell

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

The criteria ask for impact at higher levels externally as well as internally. These are sustained working relationships with senior architects at the account level — most have been carried across multiple engagements documented in Business and Global Impact.

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
| **Brenden Buresh**    | DA, GES Office of the CTO                           | SOSIE co-founder; DC/NX-OS tiger team; Adobe Cilium POC                                                   |
| **Craig Hill**        | DSE, US Public Sector                               | SOSIE co-founder; Future Enterprise Segmentation; co-recipient, 2025 Pinnacle Award                       |
| **Virginia Teixeira** | DSE, EMEA                                           | SOSIE co-founder; DCN and transport/AI convergence                                                        |
| **Rob Murphy**        | PSE                                                 | SOSIE co-founder; SONiC labs; AI fabric disclosures                                                       |
| **David Jansen**      | DSE                                                 | SP Edge tiger team; Americas SONiC forum                                                                  |
| **Brian Meaney**      | DA, EMEA CTO                                        | MCNS, NetCo/ServCo, NaaS architecture                                                                     |
| **Mike McPhee**       | DSE                                                 | PSE review subcommittee                                                                                   |
| **Marina Ferreira**   | PSE                                                 | Future Enterprise Segmentation; DC/NX-OS tiger team                                                       |
| **Brian Shlisky**     | DSE                                                 | Host-networking, Cilium/Tetragon on SONiC POC |
| **Jeffry Handel**     | DSE                                                 | UFA co-founder |
| **Josh Merrill**      | PSE                                                 | SGT-in-uSID co-inventor; UPM; Yukon++                                                                     |
| **Christian Martin**  | Cisco MIG hyperscaler architecture *(formerly OCI)* | Low-diameter fabric research; WMP-PolarFly — an external research partnership that became an internal one |
// Rob Murphy and Josh Merrill and I are all in ASP/Web so maybe they don't go on this list?
---

## Signature Internal Influence Themes

Five positions Bruce is known for inside Cisco. Each began as a minority view; each has since become, or is becoming, company direction.

1. **The host-networking air-gap** — the control point moved to the host; Cisco must participate in Linux and eBPF. *Outcome: Isovalent acquisition, 2024, MIG investigating investment in SmartNIC and Scale-Up.*
// I know I coined the term `air-gap`, but let's just mention that once (maybe in exec summary) and then just call it host-networking everywhere else
1. **Unified Forwarding Architecture (UFA) built on SRv6 uSID** — one forwarding architecture across IOS-XR, IOS-XE, NX-OS, SONiC, SD-WAN, and host (CNI, NIC). *Outcome: 2025 Pinnacle Award; platform alignment across six product lines.*
2. **Open NOS and SONiC** — required for hyperscaler relevance. *Outcome: SRv6 on SONiC shipped for the Cisco 8122, June 2026.*
3. **Identity and transport as one plane (UPM)** — identity, transport, and observability as composable layers rather than separate systems. *Outcome: ISE committed to the unified policy model, December 2025.* `[verify PM attribution]`
4. **Linux as the future NOS (SOSIE)** — routing as a containerized set of hardware-accelerated applications on an OS protected by Cilium/Tetragon. *Outcome: SOSIE working group; ongoing.*
5. **AI host networking and scale-up Ethernet** — Cisco should build SmartNICs and a scale-up Ethernet solution to compete directly with Nvidia, AMD, and Broadcom rather than concede the layer. *Outcome: advocacy in progress; not yet realized.*
