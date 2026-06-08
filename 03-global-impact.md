## Global Impact

> **Scope ([AGENTS.md](./AGENTS.md)):** Customer and revenue impact **outside the ASP + Web assignment** since **August 1, 2020**.  
> **Global Impact ≠ “outside Americas.”** Geico, Fiserv, Adobe, and similar North American enterprise accounts belong here because they are **not** Web/hyperscale or assigned SP accounts.  
> **Route elsewhere:** Microsoft, Meta, OCI, CoreWeave, Verizon, Bell, Videotron → **Business Impact**; srv6-labs, NANOG, CLEU → **Industry / SE Leadership**; Isovalent advocacy → **Span / Innovation**.

**Suggested package length:** 2–3 pages (body). Narratives below are third-person, most-recent-first, ready to trim for the final PDF.

---

## Transition Summary — Beyond ASP + Web

| Period | Expansion | Representative accounts |
| :--- | :--- | :--- |
| **2020–2023** | Enterprise cloud-native + education | Adobe Cilium threads; NYU HSRN SONiC advisory |
| **2024** | Americas enterprise SONiC/SR depth | Geico Colorado DC; Honeywell backbone; Texas Instruments global POP; The Trade Desk SONiC evaluation |
| **2025** | APJC/EMEA operators + media enterprise | Rakuten SRv6-SDWAN HLD; Evroc colo-2 architecture; Disney DGN/SR-MPLS; NTT East CLIVE/Cilium introductions |
| **2025–2026** | Financial services, colo, neo-cloud, field enablement | Fiserv SRv6 TOI; **Digital Realty** SRv6 POC; **Applied Digital**; NSight; MTN/DU enablement `[verify $]` |

**Through-line:** Bruce repeatedly applies the same horizon-2 patterns developed on ASP+Web accounts—SONiC, SRv6, Cilium/eBPF, cloud-native stitching removal—to **customers outside his assignment**, often with no dedicated account team in the Americas enterprise theater.

---

## Global Impact — Draft Package Body

*Dollar figures marked **[verify]** unless finance-approved.*

---

### Digital Realty — SRv6 POC — Oct 2025

Bruce engaged on a **Digital Realty** proof-of-concept exploring **SRv6** in colo/interconnect context—with potential to **displace Arista** in the design `[verify revenue and assignment: colo provider may be Global Impact]`.

**Impact:** Major colo operator; SRv6 positioning outside tier-1 ASP account list.

**Vault:** `[add customer note path]`

---

### Applied Digital — AI Fabric Architecture — Sept 2024

Bruce contributed **rail diagrams and AI calculator** artifacts that helped the account team **paint the solution picture and spec the design** for Applied Digital’s AI infrastructure engagement.

**Placeholder revenue:** ~**$30M** `[verify assignment and finance]`

**Vault:** `[add customer note path]`

---

### Morgan Stanley — SRv6 Presentation — Jun 2023

Bruce delivered an **SRv6 architecture presentation** to Morgan Stanley—financial-services operator audience outside ASP+Web assignment.

**Vault:** `[add customer note path]`

---

### Carnegie Mellon University — SONiC Education — Dec 2024

Bruce delivered a **SONiC education session** for Carnegie Mellon—extending open-NOS enablement into **higher education** (not ASP+Web).

**Cross-ref:** SE Leadership enablement pattern → **10-se-community-leadership.md**

---

### Hughes — SR/SRv6 Architecture — 2023

Bruce engaged on **SR/SRv6 architecture** for Hughes (satellite/SP operator)—architecture SME outside core Web assignment `[verify ongoing outcome]`.

**Vault:** `[add customer note path]`

---

### Rackspace — ExBroker / Jalapeno — Mar 2023

Bruce presented **ExBroker/Jalapeno** to Rackspace—early field validation of network-service-broker concept with a global hosting operator. Innovation artifact → **07-innovation.md**.

---

### Qwilt (CDN) — ExBroker / Jalapeno — Jan 2023

Bruce presented **ExBroker/Jalapeno** to **Qwilt** (CDN provider)—operator-facing programmable services narrative predating open-source Jalapeno release.

---

### Fiserv — SRv6 Architecture TOI — Jan 2026

Bruce delivered SRv6 transfer-of-information for Fiserv’s banking infrastructure team, focused on extending SR overlay from the Juniper RSVP-TE WAN into the data center (today VXLAN EVPN), geo-fencing/data-sovereignty steering (SWAN-style use cases), SD-WAN-to-SR anchor points, and slice/shard/pinning in the DC. The engagement included assessment of Isovalent for the WPA and a forward-looking SRv6 AI-backend slide for roadmap alignment—even though Fiserv is not building AI backends today.

**Impact:** Positions Cisco for SRv6-led WAN/DC simplification at a major financial-services operator in North America—outside ASP+Web assignment.

**Vault:** `customers/Fiserv SRv6.md`

---

### NSight (Green Bay) — Cilium / Container Security — 2025–2026

Bruce supported architecture discussions for NSight, a regional service provider with Cisco packet-core footprint, on container and Kubernetes security in the context of emerging AI services. Sessions covered container vs. VM models, K8s overview, Isovalent positioning, SR-IOV/packet-core context, and SRv6 relevance for future services—audience included network transport/optical/routing and mobile leadership.

**Impact:** Extends cloud-native security and SRv6 narrative into a **regional SP** outside the ASP+Web tier-1 SP list.

**Vault:** `customers/NSight cilium.md`

---

### Disney — DGN / SR-MPLS Architecture — 2025

Bruce participated in architecture collaboration on Disney’s Data Grid Network (DGN) for media workflows—foundation updates including SR-MPLS, Crosswork pilot alignment, micro-segmentation definitions across orgs, and DPU/elephant-flow considerations for NG data center designs.

**Impact:** Enterprise media operator in Americas; SR/MIG transport expertise applied outside assignment.

**Vault:** `customers/Disney SR.md`

---

### Rakuten — SRv6 SD-WAN Underlay HLD — Jul 2025

Bruce supported APJC on a high-level design for enhancing Rakuten’s SD-WAN underlay with SRv6—including Cisco-advocated models for SRv6 CPE-to-CPE and private-cloud host integration via Cilium—while documenting Rakuten’s preference for a traditional PE model and brainstorming a “Unified SRv6 Fabric” value case.

**Impact:** Direct APJC operator engagement outside Americas assignment; influences a major mobile/cloud operator’s WAN evolution.

**Vault:** `customers/Rakuten SRv6-SDWAN.md`

---

### Adobe — Cilium Egress/Ingress Gateway & Cloud-Native SRv6 — 2024–2025

Bruce was a core technical SME on Adobe’s **Cilium** POC (egress gateway, ingress VIP/HA, overlapping RFC1918, multihop BGP reachability) with Brenden Buresh and Dan Stacks—supporting Adobe Ethos (vanilla K8s) migration of Adobe-to-Adobe traffic off the public Internet. **July 2024** marked intensified **Adobe Cilium SRv6** thread. Separately, Bruce reviewed the **Cloud-Native SRv6** concept deck (Feb 2025): SRv6 L3VPN from CNI-to-CNI, elimination of VXLAN/MPLS stitching at ToR and DCI/PE boundaries, eBPF visibility, and TGW cost reduction.

**Impact:** Global enterprise with multi-cloud footprint; pull-through for Nexus and cloud-native security—**not** an ASP+Web account.

**Vault:** `customers/Adobe Cilium.md`, `customers/Adobe CN-SRv6.md`

---

### Evroc — EMEA Hyperscaler Colo-2 Architecture — 2024–2025

Bruce advised Evroc (Europe’s neo-cloud/hyperscaler ambition) on colo-2 production readiness: SONiC on spine/leaf, Cisco 8201 border, host multi-homing, Kubernetes-centric segmentation (Cilium/Calico direction), and inter-site architecture without L2 stretch—bridging startup resource constraints (EVPN to hosts short term) with pure IP fabric / VPC-in-host long term.

**Impact:** EMEA operator outside assignment; CLEU 2025 visibility `[cross-ref Industry/SE Leadership for session only]`.

**Vault:** `customers/Evroc.md`

---

### The Trade Desk — SONiC + XR Diversity — Oct–Nov 2024

Bruce supported a SONiC/XR positioning session for The Trade Desk (digital ad-tech, long-time Cumulus shop evaluating alternatives). Design context: 240-rack DC buildouts, 400G ToR, heavy open-source culture, BGP L3 fabric, IPv6 rollout plans—Cisco story centered on ASIC diversity, SONiC commitment, XR for heavy routing, and SRv6/uSID roadmap on SONiC. **Nov 2024:** follow-on **SONiC education session**.

**Impact:** Americas enterprise neo-cloud-scale DC; SONiC mindshare outside Web assignment.

**Vault:** `customers/The Trade Desk - sonic.md`

---

### Geico — SONiC Data Center Fabric — 2024

Bruce served as SONiC SME for Geico’s Colorado colo expansion: **~118 racks**, 32×100G ToR running SONiC, leaf/spine topology, production target end of Q2, migration of workloads from cloud toward on-prem Fredricksburg N9k footprint. Vault notes cite **~$1.6M** opportunity **[verify]**. Talent Assessment **2HFY24** records **first Geico SONiC/Cisco 8000 order at ~$1.6M** with follow-on potential.

**Impact:** Major U.S. insurer—**Americas geography, Global Impact segment** (not ASP+Web).

**Vault:** `customers/Geico.md`, `dse/DSE General MOC.md` `[verify revenue]`

---

### Texas Instruments — Global POP / SR Roadmap — May 2024

Bruce consulted on TI’s dual-plane, BGP-centric WAN architecture: 16×100G circuits in North Texas, metroplex mesh, manufacturing no-downtime constraints, traffic classification/prioritization, zero-trust segmentation, and planned extension to EMEA/APJC regions. Customer direction explicitly toward SRv6; competitive framing vs. Arista (BGP ODN, Flex-Algo, uLoop, link-delay TE).

**Impact:** Global manufacturing enterprise headquartered in Americas—outside assignment.

**Vault:** `customers/Texas Instruments.md`

---

### Honeywell — Backbone / Flex-Algo Architecture — Apr 2024

Bruce advised Honeywell on NCS5501 backbone across six colos and two private DCs, SD-WAN headend integration options, path preference from SD-WAN into the private backbone, and Flex-Algo interest (IGP-based path selection without controller)—plus future IoT transport segmentation and internal chargeback models.

**Impact:** Industrial enterprise global backbone design—non–ASP+Web.

**Vault:** `customers/Honeywell.md`

---

### NYU — High Speed Research Network (HSRN) SONiC — Aug 2024

Bruce advised NYU HSRN leadership on SONiC for research networking: cost, multi-vendor common management, telemetry/gNMI/Prometheus, leaf and routed-core roles, CI/CD/Containerlab integration, EVPN multi-homing, and custom P4/SDK research paths on the core ring.

**Impact:** Education/research sector enablement; SONiC adoption outside commercial SP/Web assignment.

**Vault:** `customers/NYU sonic.md`

---

### APJC Field Enablement — MTN Nigeria & DU UAE — Jul 2024 `[verify details]`

Bruce guided APJC engineer Sanjay Nanda on large-scale topology modeling for operators outside his assignment:

- **MTN Nigeria:** Docker-based topology cited to save ~**$85K** in lab costs; core migration LDP→SR-MPLS with Crosswork COE/SRTE implementation path.
- **DU UAE:** **2,300-node** SRv6 POC topology for operator evaluation.

**Impact:** Identifiable customer outcomes via field enablement on non-assigned accounts—classic Global Impact pattern.

**Sources:** Prior package notes / email analysis `[add vault customer notes]`; `email-analysis/circuit-web-sp-email-summary.md`

---

### NTT East — APJC SRv6 / Cilium — 2025 `[verify revenue]`

Bruce supported APJC account team (Asahi Kawabata, Hiroyuki Sugano) for NTT East interest in SRv6-for-research and Cilium/SRv6 introductions—including CLIVE meeting coordination, internal introductions to Isovalent APJC sales, and Cisco Live Melbourne engagement planning. Email thread indicates study-level interest in SRv6-L3VPN and service chaining.

**Impact:** Tier-1 APJC operator outside assignment; positions Cisco for long-cycle SRv6 + cloud-native security.

**Vault:** `customers/NTT East.md`; srv6-email corpus (CLIVE / Melbourne threads)

---

## Summary Table — Global Impact Accounts (draft)

| Customer | Theater | Segment | Bruce’s role (summary) | Revenue / outcome |
| :--- | :--- | :--- | :--- | :--- |
| Fiserv | Americas | Financial | SRv6 TOI; WAN→DC; Isovalent assessment | Pipeline `[verify]` |
| Applied Digital | Americas | Neo-cloud / AI | Rail diagrams; AI calculator; solution spec | ~$30M cited `[verify]` |
| Digital Realty | Global | Colo | SRv6 POC; Arista displacement thread | `[verify]` |
| Geico | Americas | Insurance | SONiC DC fabric SME | ~$1.6M cited `[verify]` |
| Adobe | Global ent. | Technology | Cilium POC; Cloud-Native SRv6 concept | Pull-through `[verify]` |
| Honeywell | Global ent. | Industrial | Backbone / Flex-Algo | Architecture `[verify]` |
| Texas Instruments | Global ent. | Manufacturing | POP/SRv6 roadmap | Architecture `[verify]` |
| Disney | Americas | Media | DGN / SR-MPLS | Collab `[verify]` |
| The Trade Desk | Americas | Ad-tech | SONiC + XR evaluation; Nov 2024 education | Mindshare `[verify]` |
| Morgan Stanley | Americas | Financial | SRv6 presentation (Jun 2023) | Architecture `[verify]` |
| Carnegie Mellon | Americas | Education | SONiC education session (Dec 2024) | Enablement |
| Hughes | Americas | SP/satellite | SR/SRv6 architecture (2023) | `[verify]` |
| NYU | Americas | Education | HSRN SONiC advisory | Research net `[verify]` |
| NSight | Americas | Regional SP | Cilium / K8s security | Early AI services `[verify]` |
| Rakuten | APJC | Mobile/cloud SP | SRv6-SDWAN HLD | HLD `[verify]` |
| Evroc | EMEA | Neo-cloud | Colo-2 SONiC/Cilium arch | Pre-prod customers `[verify]` |
| NTT East | APJC | Tier-1 SP | SRv6/Cilium SME for APJC team | Study / intro `[verify]` |
| MTN Nigeria | APJC | Mobile SP | Topology enablement (Sanjay) | ~$85K lab savings `[verify]` |
| DU UAE | EMEA | Mobile SP | 2300-node SRv6 POC topology | POC scale `[verify]` |

---

## Explicitly Excluded from This Section (re-filtered June 2026)

| Item | Route to |
| :--- | :--- |
| Microsoft, Meta, Oracle, CoreWeave, AWS, Google | **06-business-impact.md** |
| Verizon, Bell Canada, Videotron, Dish/Boost, AT&T, T-Mobile | **06-business-impact.md** |
| segmentrouting / srv6-labs / GitHub stats | **05-industry-impact.md** / **10-se-community-leadership.md** |
| CLEU/CLUS labs (generic) | **10-se-community-leadership.md** |
| Isovalent acquisition advocacy | **04-span-of-influence.md** / **07-innovation.md** |
| SRv6 multi-tenant AI spec used *primarily* on MSFT/OCI | **07-innovation.md** (+ Business Impact cross-ref) |
| Pre–Aug 2020 engagements | Exec overview thru-narrative only |

---

## Vault Harvest Log — June 7, 2026 (re-filter)

**Entry:** `dse/03-Global-Impact-MOC.md`  
**Hubs:** `Enterprise-Customers-Hub.md`, `03-Global-Impact-MOC`  
**Customer notes read:** Geico, Fiserv, Adobe CN-SRv6, Adobe Cilium, Honeywell, Texas Instruments, Disney SR, NYU sonic, The Trade Desk, NSight cilium, Rakuten SRv6-SDWAN, Evroc, NTT East  
**Cross-check:** `AGENTS.md` ASP+Web vs Global segment rule (Americas enterprise included)

**Gaps / Bruce to add:**
- [ ] Finance-validated $ for Geico, Adobe, Rakuten, Evroc
- [ ] Vault notes for MTN Nigeria, DU UAE
- [ ] Confirm Visa engagement classification
- [ ] Softbank, Telstra, Swisscom, Telia — confirm post-2020 non-assigned outcomes or drop
