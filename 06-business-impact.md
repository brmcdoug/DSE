## Business Impact

> **Scope ([AGENTS.md](./AGENTS.md)):** Customer and revenue impact **within the ASP + Web assignment** since **August 1, 2020**.  
> **In-scope:** Americas Web/hyperscale/neo-cloud (Microsoft, Meta, AWS, Google, OCI, CoreWeave, etc.) and **assigned tier-1 SP** (Verizon, Bell Canada, Videotron, AT&T, T-Mobile, Dish/Boost, etc.).  
> **Route elsewhere:** Geico, Fiserv, Adobe, Rakuten, Evroc, MTN/DU, NTT East → **[03-global-impact.md](./03-global-impact.md)**. Pure open-source/NANOG/CLEU without account revenue → Industry / SE Leadership.

**Suggested package length:** ~7 pages weighted. Narratives below are third-person, most-recent-first, ready to trim for the final PDF.

---

## Business Impact Model — Co-Development, Not Transactional Sales

Bruce’s ASP+Web business impact follows a repeatable pattern: **train SE teams and customer engineers on architectures and products that do not yet exist**, build POC labs and emulators (SONiC, SRv6, SL-API, host-networking), then co-develop with hyperscalers and tier-1 SPs until the revenue pipeline matures. Account notes describe this as multiyear **partnership**, not a traditional sales cycle—Bruce often serves as internal strategy consultant, SONiC/SRv6 SME, and lead architect while grade-12 SEs run production engagements.

**Web culture influence:** Bruce contributed to aligning Cisco’s Web selling motion with hyperscaler-style thinking (open NOS, disaggregation, API-driven forwarding)—relevant to strategic investments in SONiC and Silicon One that underpin multiple accounts below.

*Cross-reference:* Productization outcomes (8122 SRv6-on-SONiC, Isovalent) → **Innovation** / **Span of Influence**. SE training mechanics → **SE Community Leadership**.

---

## Revenue Summary *(pending finance validation — June 7, 2026)*

| Customer / Segment | Scope | Placeholder $ | Bruce’s role (summary) |
| :--- | :--- | :--- | :--- |
| **Microsoft** | DC, DCI, Metro | ~$2.0B | Strategy consultant; SONiC training; SRv6 AI backend advocacy; POC labs; multi-tenant AI architecture |
| **Microsoft** | WAN / SWAN | ~$500M | SR/SRv6 training; SL-API/SDN WAN labs; 1.6T / multi-planar SRv6 modeling |
| **Meta** | WAN, EBB, RBB, BBF | ~$1.0B | SL-API technique pioneer (post-MSFT SWAN); VXR POC labs; AI hackathon enablement |
| **Meta** | BBF production win | **$17M booked** `[verify]` | VXR lab setup; backbone re-entry; P200/Thunderjet path |
| **Amazon** | Silicon One, Direct Connect | ~$20M | Silicon TAM modeling; feature development program management |
| **Google** | GDC, B4 SR-MPLS | ~$20M | SRv6 proposal and training; interim lead SE during account transition |
| **Oracle (OCI)** | Frontend + backend DC / AI | ~$20M | Lead architect SRv6 for AI; MRC and multi-tenancy; Hoffman-Singleton study |
| **CoreWeave** | DC + WAN / AI | ~$20M FY26; FY27 estimates $150M DC switching, $245M optics, FY28-29 estimates $400M/year DC switching, $600+/year optics [source](https://cisco-my.sharepoint.com/:w:/r/personal/bgisiger_cisco_com/Documents/Desktop/Old%20Desktop/Web%20Operation%20Accounts/Big%20Projects/AI%20start-ups/CoreWeave/DC%20Switching/Back-end/CRD/CoreWeave%20DC%20Back-End%20Switching%20-%20Customer%20Requirements%20Document%20(CRD)%20v1.docx?d=w302ef71e18cc47529beaeb9e213af6a1&csf=1&web=1&e=mO6m5O) | SONiC SME; lead SRv6-for-AI architect |
| **Applied Digital** | AI infrastructure | ~$30M `[verify]` | Rail diagrams + AI calculator; solution spec |
| **Salesforce** | NG DC / SR | `[verify]` | **Sep 2020:** A9K POC co-led w/ Asoka; SR/SRv6 mindshare (Oct 2023 exec preso) |
| **Comcast** | LB architecture | **~$5M** `[verify]` | Feb 2026 LB consultation |
| **Americas SP** | Bell, Verizon, Dish/Boost, Videotron, Riot | ~$90M+ partial | SR/SRv6, host-based Cilium, NaaS architecture |

**Aggregate placeholder (ASP+Web only):** Multiple **billions** in hyperscaler and tier-1 SP pipeline and booked revenue (Aug 2020–present). *Final figures require finance validation.*

---

## Business Impact — Draft Package Body

---

### Meta — Backbone Fabric (BBF) Production Win — Feb 2026

After a multi-year co-development effort, Meta booked a **$17M** first production order for P200 on the **Backbone Fabric (BBF)** architecture—Cisco beating Arista (and Broadcom Q4D) for strategic P200 insertion into Meta’s backbone. **Apr 2024:** Beginning of **~two-year EBB/BBF sales cycle**. Bruce developed **VXR-based POC labs** for SE co-validation; **Mar 2026:** Bruce leveraged **VXR team relationships** to obtain **8223 patch** when hardware was not yet GA—**key enabler** for Asoka/Leif and the production win (Asoka: *“Thank you for helping us with the VXR setup. That was huge!!”*).

**Strategic context:** BBF is part of EBB; estimate **~$300M over two years** for BBF; RBB pipeline cited at **~$350M/year** with **SL-API** as key to the win. Feb/Mar 2026: Meta **RBB moving to SRv6**, leveraging SL-API work Bruce pioneered in the Microsoft SWAN context.

**Bruce’s actions:**
- Internal consultant on strategy/positioning (2021–present)
- Delivered SL-API/SDN/SR sessions modeled on Microsoft SWAN (2022–2024)
- Built VXR POC labs for EBB/BBF/RBB; enabled Web-wide AI hackathon (May 2026)
- March 2026: Asoka 8223 test support tied to Meta BBF win (per DSE General MOC)

**Vault:** `customers/Meta.md`  
**Cross-ref:** Innovation (SL-API), SE Leadership (VXR lab pattern)

---

### Digital Realty — SRv6 POC — Oct 2025

Bruce supported a **Digital Realty** SRv6 POC thread exploring colo fabric options and potential **Arista displacement** with SRv6 `[verify $]`. Assisted **DLR team** in standing up **Cilium/SRv6 deployment** in their POC lab (PDP Dec 2025). *Primary narrative may also appear in **03-global-impact.md**.*

---

### Microsoft — SRv6 AI Backend & SONiC 8122 — 2024–2026

Bruce evangelized inside Cisco that **SRv6 for AI backend** (MRC, multi-tenancy, static pinning) was production-real—culminating in **SRv6 on SONiC for Cisco 8122** (202511 codebase, **June 2026**). **Microsoft and Oracle have initial SRv6-for-AI deployments on competitor hardware**—strong validation of the architecture Bruce championed, even where Cisco was late to market; **FY2027 TAM projection pending finance validation**. He authored the **SRv6 multi-tenant AI fabric** spec and POC repos ([srv6-msft](https://github.com/segmentrouting/srv6-msft), [srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator)) used by Microsoft engineers in executive presentations; planned **OCP Summit 2026** co-presentation.

**Customer context:** AI super-factory WAN (120k+ fiber miles), MRC on hosts, scale-up/scale-out segmentation—aligned with vault AI-backend notes.

**Bruce’s actions:**
- SONiC training for account SEs (2024–present)
- Convinced skeptical engineering to invest in SRv6-for-AI on SONiC
- Multi-tenant architecture, whitepaper, customer/SE labs
- **SRv6 DC-Frontend POC (1HFY26):** two key use cases; **Mohan** installed setup in personal lab and demoed internally
- **Mar 2025:** **SRv6 frontend DC** engagement begins (**Mohan**, **Joe Rockwell**); Bruce used **AI tools** to rapidly generate lab scenarios (configs, topologies, docs); **May 2025** onsite workshop—Bruce **led half** on technology and use cases
- **Jan 2026:** **dRH**—disaggregation of chassis T2 into upper/lower **pizza-box Clos** (MSFT frontend DC re-architecture with SRv6)
- **Aug 2025:** **SRv6 DC-frontend POC**—4PE, DCIX, mix of XR and SONiC; demonstrated **prefix-hiding/scale** and **SRv6-TE for inter-DC** traffic
- **Mar 2026:** **dRH SRv6 vs. VXLAN** presentation + **SONiC GRT** lab/POC for **Abhishek Dosi** and **Mohan** (with engineering)
- **MIG commitment:** SRv6 on SONiC **G200** in **Q1 FY26** for Microsoft and Oracle testing paths (Talent Assessment 1HFY26)
- Disaggregated RH/T2 SRv6 tunnel mesh, Ti-LFA, anchor-route scale/convergence work (ongoing with Mohan/Joe)
- **Nov 2024:** Built **first SRv6-for-AI elephant-flows demo** with Brook, Josh, HQ team—internal proof point before customer-scale POCs

**Vault:** `customers/Microsoft AI-Backend.md`, `customers/Microsoft  SRv6.md`, `customers/MSFT octans-drh.md`, `innovation/SRv6-MultiTenant-Design-rev3.md`

---

### Microsoft — PhyNet, dRH, Project Octans & DCIX — 2023–2026

Bruce is a primary SME on Microsoft’s **Regional Network Gateway / PhyNet** program: anchor routes, DCIX T2-to-T2 bypass, IPv4 containment, multi-million-route scale, and **disaggregated RH (dRH / Project Octans)**—SRv6 tunnel meshes between LRHs, Ti-LFA, micro-loop avoidance, selective FIB download. **Octans** flattens AI DC fabric (8-way NIC-to-T1 connectivity, &lt;10µs hardware FRR). Vault notes cite ~**120k** v4/v6 routes, convergence targets, and AZ/DCIX drivers.

**Bruce’s actions:**
- Architecture working sessions (Mohan dRH, Chris Whyte G400/MRC, Pan WAN lunch-and-learn)
- **Apr–May 2025:** Two **SRv6 WAN lunch-and-learn** sessions with Microsoft WAN team (PSE time log)
- SONiC/FRR prototypes: BGP GRT, SRv6-TE, BGP fast reroute on disagg RH
- Shared “Billion Servers” / scale framing with Microsoft engineering leadership

**Vault:** `customers/Microsoft  SRv6.md`, `customers/MSFT octans-drh.md`

---

### Microsoft — 1.6T WAN / SWAN / SRv6 uSID — 2024–2027 path

Bruce developed POC labs and training for **1.6T backbone** redesign: scaling from ~1,800 to ~3,000 nodes, prefix growth, convergence &lt;3s targets, ISIS planes vs. geo-domains, and **SRv6 uSID** as the “scale for decades” option (native IPv6 summarization, flow-label entropy, host/SmartNIC extension). SWAN/SL-API implications documented in WAN design analysis.

**Placeholder revenue:** ~**$500M** WAN/backbone (exec summary—**`[verify]`**, incl. John Dorval validation for SWAN claims).

**Vault:** `customers/Microsoft-WAN.md`, `customers/Microsoft  SRv6.md`

---

### CoreWeave — AI Backend & Global WAN — 2025–2026

Neo-cloud AI provider (OpenAI compute partner): Bruce serves as **SONiC SME** and **lead SRv6-for-AI architect**—backend adaptive routing/ECN, MRC/SRv6 metrics, Vera Rubin Ultra path analysis. **WAN backbone** design (Apr 2026 deck): ~196 edge routers, 42 TLRs, DSR stitching for AI-DC fabrics, 32 D-pops for DC interconnect.

**Mar 2026 (PSE time log):** Developed **Containerlab + VXR** lab setups and documentation for CoreWeave NetDev engineering; opportunity scope grew to **~10k–12k switches**. **Feb 2026:** CoreWeave EBC—VXR/Containerlab/SONiC technical lead.

**Placeholder revenue:** ~**$20M FY26**; ~**$250M projected FY27** `[verify]`.

**Vault:** `customers/Coreweave DC.md`, `customers/Coreweave backbone.md`, `customers/Coreweave lab.md`

---

### Comcast — Load Balancing Consultation — Feb 2026

Bruce consulted on **Comcast load-balancing** architecture engagement—**~$5M** opportunity scope per PSE time log `[verify with Jenelle/account team]`.

**Vault:** `[add customer note path]`

---

### Oracle Cloud Infrastructure — SRv6 for AI (Acceleron / MRC) — 2023–2026

Bruce is **lead architect** for Cisco/OCI **SRv6 for AI**: aligned with Oracle **Acceleron** multiplanar networking (SRv6 source routing from NIC, N-diverse paths, MRC on Stargate/Abilene). Delivered SRv6 CRD, VXR lab, SRv6 SONiC image, SRv6 GRT work; **Hoffman–Singleton** low-diameter topology study (**Jun 2024** lab and design doc with **Chris Martin**). Oracle public blog (2026) cites SRv6 static routing for MRC—same industry pattern Bruce drove on Microsoft.

**2024–2026 timeline (PSE time log):** **Oct 2024** SRv6-for-AI kickoff at **OCP** (first public customer discussions); **Nov 2024** onsite AI workshop; **Dec 2024** Bruce **led OCI SRv6 workshop**—**OCI running SRv6 in limited production by end of 2025**; **Aug 2025** **1,000-GPU POC** (SONiC advisory, later **SRv6 ownership**); **Jan 2025** **Polarfly** + **uA-on-XRd AI-backend demo** (Jag Brar); **Mar–Apr 2026** two-part **Oracle SRv6 tutorial** for Oracle engineering; **Jun 2025** assisted Asoka on **SONiC 8122** lab configs (`2026–2028` revenue projection `[verify]`).

**Also:** Consultant/SW advisor on Oracle **ONOS / Cloud OS** strategy alignment (**Apr 2025** EBC with sonic/solar-os team).

**Placeholder revenue:** ~**$20M** `[verify]`.

**Vault:** `customers/Oracle-SRv6.md`, `customers/Oracle-800g-roce.md`  
**Cross-ref:** Innovation (multi-tenant spec, srv6-oci repo)

---

### Bell Canada — C8231-G2 First Order — May 2026

**500 units** first order for **C8231-G2** routers received (Helene Roy, May 4, 2026)—culmination of end-to-end SRv6, host-based Cilium, and NaaS architecture work.

**Placeholder revenue:** ~**$20M** cumulative SRv6/host-networking engagement `[verify]`.

**Vault:** `technologies/Bell Canada.md`  
**Cross-ref:** Global Impact only if a *non-assigned* story—Bell is **ASP+Web SP**.

---

### Videotron — SRv6 Regional Backhaul — Feb–Apr 2026

Canadian cable operator (Quebec; Freedom Mobile integration): building **SRv6 backhaul** to interconnect four MPLS-LDP regions over IPv6 core with SRv6 gateways. Bruce supported SE **Philippe Vaillancourt**—gave him access to Bruce’s **Containerlab SRv6 lab** to self-train ahead of customer workshop; coordinated Ianik/Jakub/Dan Voyer for onsite SRv6 update.

**Placeholder revenue:** ~**$25M** `[verify]`.

**Vault:** `customers/Videotron SRv6.md`

---

### Verizon — SRv6 / SONiC / AI DC Strategy — 2024–2025

Tier-1 assigned SP: Bruce engaged on **enterprise-wide SRv6 roadmap** (wireless switching centers, DCs, VCP, FIOS, XRAN)—prefix summarization value, stitching cost, **Project Yukon / NaaS** revenue framing, seamless MPLS→SRv6 transition. Active threads: **400G server fabrics**, SONiC/SRv6 and **SRv6-in-host (FRR/Cilium)**, converged 5G/AI DCs, **Service Bus** stateful scaling (millions of flows, 52 packet-core DCs), AI pod deployment in existing DCs.

**Bruce’s actions:** Architecture decision matrices (NX/XR/SONiC/SRv6); internal SRv6 business case quantification; AI + LLM/network automation workshops with Luay/Josh/Jasbir. **Apr 2024 MPLS-WC:** Verizon presentation **leveraged srv6-labs** → **05-industry-impact.md**.

**Placeholder revenue:** Strategic A3PO/CX engagement; quantified Yukon/svc-chain TBD `[verify]`.

**Vault:** `customers/Verizon.md`

---

### Akamai — Backbone SR/SRv6 Transition — 2023–2025

Americas HQ CDN/SP (**ASP+Web**): Bruce engaged on **800G deployment**, RSVP→SR momentum on backbone, **SRv6-TE** honesty on Silicon One strengths/weaknesses, Linode/Prolexic SR path (John Leddy/Russ White). **Jul 2023:** **H.Insert.Preserve** thread with **J. Leddy**. **Oct 2023:** **FRR SRv6 L3VPN image and lab** for Russ White. **Feb 2024:** SRv6 use-case workshops with **Leddy** and **Russ White**. **Mar 2025:** **Static uSID POC** (Leddy). **May 2025:** **`srctl`/Jalapeno** demo (Talent Assessment). **Jun 2025:** **PLX over ADC** lab/demo/POC. **2025 PDP:** built demo **SDN controller** programming **SRv6 L3VPN** routes on custom Linux forwarder for **redirect-to-scrubber** use case — follow up on production status with account team.

**Vault:** `customers/Akamai.md`, `customers/Akamai SRv6.md`, `customers/Akamai-Prolexic SRv6.md`

---

### T-Mobile — Magenta Cloud Segmentation & Cilium — 2024–2025

Assigned SP: Bruce contributed to **macro/micro/nano segmentation** narrative (Cilium policy, ZBF, eBPF/Tetragon, ACI vs. Cilium positioning). **Nov 2024:** **Overlay RFP** support. **Dec 2024:** **Magenta Cloud RFP** support. Greenfield DC opportunities (Polaris, Tortugas timeline); Openshift-everywhere direction; v6-only underlay discussions; **Hypershield/Cilium** progress in MagentaCloud; slicing/Webex first-app use cases (historical CTO engagement).

**Vault:** `customers/T-Mobile.md`

---

### AT&T — NaaS / Inference Pods — Aug 2025

Bruce participated in **inference pod / private AI cloud** POC framing with Jim Durkin and Josh Fleishman—IPE cloud-connect routers, phased go-to-market leveraging AT&T network.

**Vault:** `customers/AT&T NaaS.md`

---

### Dish / Boost Mobile — SRv6 L3VPN on AWS — 2025–2026

Assigned SP (Boost): **SRv6 L3VPN overlays on AWS underlay** to replace GRE tunnels—Cilium SRv6 uSID, cloud-native L3VPN at pod level, “dark default” IPv6 fabric (`Boost-Cilium-SRv6.pptx`, Jan 2026). End-to-end SRv6 + Cilium in cloud per exec-summary notes.

**Vault:** `customers/Boost SRv6.md`, `customers/cilium-srv6.md`

---

### Applied Digital — AI Infrastructure — Sept 2024

Neo-cloud / AI infrastructure provider: Bruce’s **Web AI Fabrics calculator and rail architectures** (**Jun 2024**) became a **two-year scoping tool** for Web SEs; same artifacts helped size the **Applied Digital** engagement.

**Placeholder revenue:** ~**$30M** `[verify]`

**Vault:** `[add customer note path]`

---

### Voltage Park — SRv6 for DC — Jan 2024

Neo-cloud GPU provider: **EBC presentation**—lead architect **Drew Pletcher** interested in **DC frontend SRv6**; thread did not follow through to deployment `[verify with Drew]`. Appeared in **Oct 2024 OCP** SRv6-for-AI-backend cohort.

**Vault:** `[add customer note path]`

---

### Viasat — SRv6 Service Chaining & Slicing — 2024

Satellite/SP (**ASP+Web**): Bruce consulted on **SRv6 SFC design** (**May 2024**, Don Ewald); **Jul 2024** **slicing/service-chain SRv6 demo** with **Chris Olson**; **Oct 2024** **EBC** thread on **open-source controller** project.

**Vault:** `[add customer note path]`

---

### Groq — SR-TE POC — Sep 2025

AI inference silicon customer: Bruce supported **SR-TE POC** exploring **Flex-Algo** and **data-sovereignty** steering—**successful POC**; Groq subsequently **acquired by NVIDIA** (Sep 2025).

**Vault:** `[add customer note path]`

---

### eBay — SONiC EBC — Mar 2025

Bruce engaged on **SONiC EBC** with account team (**Ken Truong**)—Web-scale operator open-NOS evaluation.

**Vault:** `[add customer note path]`

---

### Voltage Park — SRv6 for DC — Jan 2024

Neo-cloud GPU provider: early **SRv6 for data center** architecture thread at **OCP 2024** kickoff cohort (with Microsoft, Oracle, Bell, Cloudflare). `[verify ongoing pipeline with Drew/account team]`

**Vault:** `[add customer note path]`

---

### Cloudflare — BMP Enhancements — Mar 2026

Bruce consulted on **BMP (BGP Monitoring Protocol)** enhancement path—features targeted for **26.4.x** release per engineering thread.

**Vault:** `[add customer note path]`

---

### Lambda Labs — Executive Briefing — Jul 2024

Bruce presented **host-based SRv6** and consulted on **DC design** at a **Lambda Labs EBC**—Web/neo-cloud GPU cloud engagement. **Jul 2025:** Consulted on **Isovalent Egress Transit Gateway** concept and opportunity.

**ASP+Web** account (confirmed Jun 2026).

**Vault:** `[add customer note path]`

---

### Google — GDC & B4 — 2021–2024

Bruce served as strategy consultant; developed **end-to-end SRv6 proposal** and training for **Google Distributed Cloud (GDC)**; interim **lead SE** on **B4 SR-MPLS** during account SE leave. **May 2024:** **GDCE onsite** SRv6 design. **Mar 2026:** **SRv6 for Google AI Backend**—intros and kickoff with **Nick Sischo**, **Pablo Camarillo**, **Clarence Filsfils**. **SL-API for Alphanet** noted in vault hub.

**Placeholder revenue:** ~**$20M** `[verify]`.

**Vault:** `customers/Google.md`

---

### Amazon Web Services — Silicon One — 2021–2024

Bruce supported **Silicon One** strategy: internal consultant; **12.8T→25.6T→51.2T** TAM modeling with customer/account team; project-managed feature development tracking between AWS and Cisco engineering. **Feb 2023:** **SRv6 for AWS telco customers** thread (Riggs, Chris Martin). Span-of-influence notes cite VP-level recognition of foundational silicon deals **Q1FY23** `[verify $]`.

**Placeholder revenue:** ~**$20M** Direct Connect / Silicon One `[verify]`.

**Vault:** `xarchive-2021-2022/AWS-may-2021.md`, `dse/04-Span-of-Influence-MOC.md`, `dse/DSE General MOC.md` (Feb 2023 AWS SRv6 telco thread)

---

### Salesforce — SR / A9K — Sep 2020 & Oct 2023

**Sep 2020 (PSE time log):** **SFDC A9K POC**—leveraged prior relationship and mindshare; **co-led POC development and execution** with Asoka (high Biz impact).

**Oct 2023:** SR customer presentation for **Salesforce (SFDC)** NG DC positioning.

**Vault:** `[add customer note path]`

---

### Equinix — NGN / Disaggregation / SRv6 — 2023–2026

Interconnect/hyperscale-adjacent: Bruce engaged on **universal packet fabric** evolution (SR→SRv6, disaggregation, SONiC/PINS POCs), AI/ML reference architecture with Nvidia, telemetry/SAI, Alibaba SRv6 interest. **Nov 2023 EBC:** **SL-API** as **bridge to disaggregation** narrative.

**Vault:** `customers/Equinix.md`

---

### Salesforce — A9K Displacement — 2022 `[confirm assignment]`

**$38M** win displacing Juniper on A9K (2022)—listed in candidate revenue notes; confirm ASP+Web classification.

---

## Summary Table — ASP+Web Engagements (draft)

| Customer | Segment | Period | Outcome / pipeline | Bruce role |
| :--- | :--- | :--- | :--- | :--- |
| Meta | Web | 2022–2026 | $17M BBF booked; BBF/RBB/SRv6 pipeline | SL-API pioneer; VXR labs |
| Microsoft | Web | 2021–2026 | AI backend SONiC ship; PhyNet/dRH; 1.6T WAN | Lead SME; labs; internal advocacy |
| CoreWeave | Neo-cloud | 2025–2026 | AI + WAN architecture | SONiC SME; SRv6 AI architect |
| Oracle | Web | 2023–2026 | Acceleron/MRC SRv6 AI | Lead architect; topology study |
| Bell Canada | SP | 2020–2026 | 500× C8231-G2 order May 2026 | SRv6/Cilium/NaaS architecture |
| Videotron | SP | 2026 | SRv6 regional backhaul | SME; SE enablement |
| Verizon | SP | 2024–2025 | SRv6 roadmap; AI DC; Service Bus | Architecture consulting |
| Akamai | SP/CDN | 2023–2025 | SR/SRv6 backbone transition | SRv6 SME; FRR labs |
| T-Mobile | SP | 2023–2025 | Cilium/segmentation; greenfield DC | Architecture workshops |
| AT&T | SP | 2025 | Inference pod POC | NaaS/AI pod framing |
| Boost/Dish | SP | 2025–2026 | SRv6 on AWS + Cilium | SRv6 L3VPN overlay design |
| Google | Web | 2021–2024 | GDC SRv6; B4 SR-MPLS | Strategy; interim lead SE |
| Viasat | SP | 2024 | SRv6 SFC/slicing | Design + demo consulting |
| Groq | Web/AI | 2025 | SR-TE POC | Flex-Algo / data sovereignty |
| eBay | Web | 2025 | SONiC EBC | SONiC evaluation |
| Cloudflare | Web | 2026 | BMP enhancements | Engineering consultation |
| AWS | Web | 2021–2024 | Silicon One TAM/features | TAM model; PM tracking |

---

## Explicitly Excluded from This Section (re-filtered June 2026)

| Item | Route to |
| :--- | :--- |
| Geico, Fiserv, Adobe, Honeywell, TI, Disney, NYU, TTD, NSight | **03-global-impact.md** |
| Rakuten, Evroc, NTT East, MTN/DU | **03-global-impact.md** |
| James Munroe / Province of NB (CLEU lab outcome) | **03-global-impact.md** |
| Patents, Bold Bets, srv6-labs LinkedIn stats | **07-innovation.md** / **05-industry-impact.md** |
| CLEU/Stay Ready Friday (generic SE training) | **10-se-community-leadership.md** |
| Isovalent acquisition advocacy | **04-span-of-influence.md** / **07-innovation.md** |
| Pre–Aug 2020-only engagements | Exec overview thru-narrative only |

---

## Vault Harvest Log — June 7, 2026

**Entry:** `dse/06-Business-Impact-MOC.md`  
**Hubs:** `Hyperscale-Customers-Hub.md`, `SP-Customers-Hub.md`, `AI-Factory-Hub.md`, `SONiC-Hub.md`, `SRv6-Master-Hub.md`  
**Customer notes read:** Microsoft (SRv6, AI-Backend, WAN, octans-drh), Meta, Oracle-SRv6, Coreweave (DC, backbone, lab), Bell Canada, Videotron SRv6, Verizon, Akamai (+ SRv6, Prolexic), T-Mobile, AT&T NaaS, Boost SRv6, Google, Equinix, cilium-srv6  
**Revenue placeholders:** `01-exec-summary.md`, `01-exec-summary-draft.md` (all **`[verify]`**)

**Vault harvest log — PSE time log (2024–2026, full Notes):** Third pass Jun 7 2026 — Adobe rescue story, Geico Berkshire pricing, Meta 8223/VXR, MSFT AI-lab generation + dRH, OCI production by end-2025, Jalapeno RPO lineage, May–Jun 2026 MRC/multi-tenant/global transition.

**Gaps / Bruce to complete:**
- [ ] Finance-validated $ for all rows; reconcile Meta $2B vs $17M booked vs BBF $300M estimate
- [ ] John Dorval / MSFT WAN validation for SWAN claims
- [ ] Confirm: Akamai, Equinix, Salesforce, Lambda Labs, Riot Games, Viasat, Comcast in ASP+Web list
- [ ] Verizon / AT&T / T-Mobile pipeline $ where available
- [ ] Remove duplicate MOC scratch content (done in this rewrite)

**Open validation (from MOC):** *“Would John Dorval agree with everything I write?”* — MSFT WAN/SWAN narrative needs stakeholder review before final package.
