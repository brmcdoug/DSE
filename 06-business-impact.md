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
| **CoreWeave** | DC + WAN / AI | ~$20M FY26; ~$250M proj. FY27 | SONiC SME; lead SRv6-for-AI architect |
| **Applied Digital** | AI infrastructure | ~$30M `[verify]` | Rail diagrams + AI calculator; solution spec |
| **Salesforce** | NG DC / SR | `[verify]` | SR customer presentation (Oct 2023) |
| **Americas SP** | Bell, Verizon, Dish/Boost, Videotron, Riot | ~$90M+ partial | SR/SRv6, host-based Cilium, NaaS architecture |

**Aggregate placeholder (ASP+Web only):** Multiple **billions** in hyperscaler and tier-1 SP pipeline and booked revenue (Aug 2020–present). *Final figures require finance validation.*

---

## Business Impact — Draft Package Body

---

### Meta — Backbone Fabric (BBF) Production Win — Feb 2026

After a multi-year co-development effort, Meta booked a **$17M** first production order for P200 on the **Backbone Fabric (BBF)** architecture—Cisco beating Arista (and Broadcom Q4D) for strategic P200 insertion into Meta’s backbone. Account leadership cited rebuilding credibility after years outside Meta’s backbone environment. Bruce developed **VXR-based POC labs** for SE co-validation; Asoka: *“Thank you for helping us with the VXR setup. That was huge!!”* Wilson Le framed the win as a *“landmark win”* and landmark for re-entering Meta’s backbone.

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

Bruce supported a **Digital Realty** SRv6 POC thread exploring colo fabric options and potential **Arista displacement** with SRv6 `[verify $]`. *Primary narrative may also appear in **03-global-impact.md** if classified outside ASP+Web.*

---

### Microsoft — SRv6 AI Backend & SONiC 8122 — 2024–2026

Bruce evangelized inside Cisco that **SRv6 for AI backend** (MRC, multi-tenancy, static pinning) was production-real—culminating in **SRv6 on SONiC for Cisco 8122** (202511 codebase, **June 2026**). He authored the **SRv6 multi-tenant AI fabric** spec and POC repos ([srv6-msft](https://github.com/segmentrouting/srv6-msft), [srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator)) used by Microsoft engineers in executive presentations; planned **OCP Summit 2026** co-presentation.

**Customer context:** AI super-factory WAN (120k+ fiber miles), MRC on hosts, scale-up/scale-out segmentation—aligned with vault AI-backend notes.

**Bruce’s actions:**
- SONiC training for account SEs (2024–present)
- Convinced skeptical engineering to invest in SRv6-for-AI on SONiC
- Multi-tenant architecture, whitepaper, customer/SE labs
- **SRv6 DC-Frontend POC (1HFY26):** two key use cases; **Mohan** installed setup in personal lab and demoed internally
- **MIG commitment:** SRv6 on SONiC **G200** in **Q1 FY26** for Microsoft and Oracle testing paths (Talent Assessment 1HFY26)
- Disaggregated RH/T2 SRv6 tunnel mesh, Ti-LFA, anchor-route scale/convergence work (ongoing with Mohan/Joe)

**Vault:** `customers/Microsoft AI-Backend.md`, `customers/Microsoft  SRv6.md`, `customers/MSFT octans-drh.md`, `innovation/SRv6-MultiTenant-Design-rev3.md`

---

### Microsoft — PhyNet, dRH, Project Octans & DCIX — 2023–2026

Bruce is a primary SME on Microsoft’s **Regional Network Gateway / PhyNet** program: anchor routes, DCIX T2-to-T2 bypass, IPv4 containment, multi-million-route scale, and **disaggregated RH (dRH / Project Octans)**—SRv6 tunnel meshes between LRHs, Ti-LFA, micro-loop avoidance, selective FIB download. **Octans** flattens AI DC fabric (8-way NIC-to-T1 connectivity, &lt;10µs hardware FRR). Vault notes cite ~**120k** v4/v6 routes, convergence targets, and AZ/DCIX drivers.

**Bruce’s actions:**
- Architecture working sessions (Mohan dRH, Chris Whyte G400/MRC, Pan WAN lunch-and-learn)
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

**Placeholder revenue:** ~**$20M FY26**; ~**$250M projected FY27** `[verify]`.

**Vault:** `customers/Coreweave DC.md`, `customers/Coreweave backbone.md`, `customers/Coreweave lab.md`

---

### Oracle Cloud Infrastructure — SRv6 for AI (Acceleron / MRC) — 2023–2026

Bruce is **lead architect** for Cisco/OCI **SRv6 for AI**: aligned with Oracle **Acceleron** multiplanar networking (SRv6 source routing from NIC, N-diverse paths, MRC on Stargate/Abilene). Delivered SRv6 CRD, VXR lab, SRv6 SONiC image, SRv6 GRT work; **Hoffman–Singleton** low-diameter topology study. Oracle public blog (2026) cites SRv6 static routing for MRC—same industry pattern Bruce drove on Microsoft.

**Also:** Consultant/SW advisor on Oracle **ONOS / Cloud OS** strategy alignment.

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

Canadian cable operator (Quebec; Freedom Mobile integration): building **SRv6 backhaul** to interconnect four MPLS-LDP regions over IPv6 core with SRv6 gateways. Bruce supported SE Philippe Vaillancourt—reshaped a CX-driven agenda, coordinated Ianik/Jakub/Dan Voyer, onsite SRv6 update; customer wants management buy-in for brownfield migration. Interests: workload-to-cloud IPv6, **Cilium** policy/Hubble.

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

Americas HQ CDN/SP (assignment **`[confirm]`** in AGENTS checklist): Bruce engaged on **800G deployment**, RSVP→SR momentum on backbone, **SRv6-TE** honesty on Silicon One strengths/weaknesses, Linode/Prolexic SR path (John Leddy/Russ White). **Jul 2023:** **H.Insert.Preserve** thread with **J. Leddy**. **Oct 2023:** **FRR SRv6 L3VPN image and lab** for Russ White. **May 2025:** **`srctl`/Jalapeno** demo (Talent Assessment). Akamai SRv6 notes: SONiC + Silicon One for high-capacity probe generation.

**Vault:** `customers/Akamai.md`, `customers/Akamai SRv6.md`, `customers/Akamai-Prolexic SRv6.md`

---

### T-Mobile — Magenta Cloud Segmentation & Cilium — 2024–2025

Assigned SP: Bruce contributed to **macro/micro/nano segmentation** narrative (Cilium policy, ZBF, eBPF/Tetragon, ACI vs. Cilium positioning). **Dec 2024:** **Magenta Cloud RFP** support. Greenfield DC opportunities (Polaris, Tortugas timeline); Openshift-everywhere direction; v6-only underlay discussions; **Hypershield/Cilium** progress in MagentaCloud; slicing/Webex first-app use cases (historical CTO engagement).

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

Neo-cloud / AI infrastructure provider: Bruce’s **rail diagrams and AI calculator** helped the account team articulate and **size the solution** for the customer engagement.

**Placeholder revenue:** ~**$30M** `[verify]`

**Vault:** `[add customer note path]`

---

### Lambda Labs — Executive Briefing — Jul 2024

Bruce presented **host-based SRv6** and consulted on **DC design** at a **Lambda Labs EBC**—Web/neo-cloud GPU cloud engagement.

**Assignment `[confirm]`** — listed in AGENTS Web seed list.

**Vault:** `[add customer note path]`

---

### Google — GDC & B4 — 2021–2024

Bruce served as strategy consultant; developed **end-to-end SRv6 proposal** and training for **Google Distributed Cloud (GDC)**; interim **lead SE** on **B4 SR-MPLS** during account SE leave. **SL-API for Alphanet** noted in vault hub.

**Placeholder revenue:** ~**$20M** `[verify]`.

**Vault:** `customers/Google.md`

---

### Amazon Web Services — Silicon One — 2021–2024

Bruce supported **Silicon One** strategy: internal consultant; **12.8T→25.6T→51.2T** TAM modeling with customer/account team; project-managed feature development tracking between AWS and Cisco engineering. **Feb 2023:** **SRv6 for AWS telco customers** thread (Riggs, Chris Martin). Span-of-influence notes cite VP-level recognition of foundational silicon deals **Q1FY23** `[verify $]`.

**Placeholder revenue:** ~**$20M** Direct Connect / Silicon One `[verify]`.

**Vault:** `xarchive-2021-2022/AWS-may-2021.md`, `dse/04-Span-of-Influence-MOC.md`, `dse/DSE General MOC.md` (Feb 2023 AWS SRv6 telco thread)

---

### Salesforce — SR for NG DC — Oct 2023

Bruce delivered **SR customer presentation** for **Salesforce (SFDC)** NG DC positioning—Web/enterprise-adjacent account **`[confirm ASP assignment]`**.

**Vault:** `[add customer note path]`

---

### Equinix — NGN / Disaggregation / SRv6 — 2023–2026 `[confirm ASP assignment]`

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
| AWS | Web | 2021–2024 | Silicon One TAM/features | TAM model; PM tracking |

---

## Explicitly Excluded from This Section (re-filtered June 2026)

| Item | Route to |
| :--- | :--- |
| Geico, Fiserv, Adobe, Honeywell, TI, Disney, NYU, TTD, NSight | **03-global-impact.md** |
| Rakuten, Evroc, NTT East, MTN/DU | **03-global-impact.md** |
| James Munroe / Province of NB (CLEU lab outcome) | **Global Impact** or **Industry** `[confirm]` |
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

**Gaps / Bruce to complete:**
- [ ] Finance-validated $ for all rows; reconcile Meta $2B vs $17M booked vs BBF $300M estimate
- [ ] John Dorval / MSFT WAN validation for SWAN claims
- [ ] Confirm: Akamai, Equinix, Salesforce, Lambda Labs, Riot Games, Viasat, Comcast in ASP+Web list
- [ ] Verizon / AT&T / T-Mobile pipeline $ where available
- [ ] Remove duplicate MOC scratch content (done in this rewrite)

**Open validation (from MOC):** *“Would John Dorval agree with everything I write?”* — MSFT WAN/SWAN narrative needs stakeholder review before final package.
