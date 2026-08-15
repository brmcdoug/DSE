## Global Impact

> **Scope ([AGENTS.md](./AGENTS.md)):** Customer and revenue impact **outside the ASP + Web assignment** since **August 1, 2020**.  
> **Global Impact ≠ "outside Americas."** Geico, Fiserv, Adobe, and similar North American enterprise accounts belong here because they are **not** Web/hyperscale or assigned SP accounts.  
> **Route elsewhere:** Microsoft, Meta, OCI, CoreWeave, Verizon, Bell, Videotron, Digital Realty → **[06-business-impact.md](./06-business-impact.md)**; srv6-labs, NANOG, CLEU labs → **Industry / SE Leadership**; Isovalent acquisition advocacy → **Span / Innovation**.

**Suggested package length:** 7 pages per README weighting — see note at end of section. Third person; organized by expansion pattern. Voice and claim-strength rules: [voice-guide.md](./voice-guide.md).

---

## How Global Impact Expanded Beyond ASP + Web

Bruce's assignment through June 2026 was Americas Service Provider and Web — tier-1 hyperscalers and named SP accounts. Everything in this section happened outside that assignment, on customers where Bruce had no quota, no account responsibility, and no obligation to engage.

The pattern is consistent: field teams, APJC and EMEA peers, and enterprise theaters request him by name for SONiC, SRv6, Cilium/eBPF, and cloud-scale architecture, because the expertise does not exist in their own organizations. As in Business Impact, much of this work is delivered **through other engineers rather than in front of customers** — Bruce supplies the architecture, the designs, and the labs, and the local team runs the engagement. Two national operators on two continents advanced their SRv6 programs this way without Bruce ever meeting them. What he transfers is not product knowledge but the horizon-2 architecture patterns developed on hyperscale accounts — open network operating systems, host-based networking, stitching elimination, and cloud-style consumption models — applied to insurers, banks, manufacturers, universities, provincial governments, and operators in three theaters.

| Period | Expansion | Representative accounts |
| :--- | :--- | :--- |
| **2020–2023** | Enterprise cloud-native and education | Adobe Cilium threads; NYU HSRN SONiC; Morgan Stanley SRv6 |
| **2024** | Americas enterprise SONiC and SR depth | **Geico** (~$1.6M); **Honeywell** (~$2M); Texas Instruments; The Trade Desk; MTN/DU enablement |
| **2025** | APJC and EMEA operators; media and financial | **Rakuten** SRv6-SDWAN HLD; **Evroc** colo-2; Disney DGN; NTT East; Visa |
| **2025–2026** | Financial services, public sector, partner multiplier | **Fiserv** SRv6 TOI; **Adobe** POC complete; **Province of NB** migration; WWT enablement |

*Dollar figures marked `[verify]` pending finance validation.*

---

## 1. Americas Enterprise and Financial Services

### Geico, 2024

**Revenue Impact:** ~$1.6M Cisco 8000 `[verify finance]`

Geico is the second-largest auto insurer in the United States and a Berkshire Hathaway company, expanding on-premises data center capacity in Colorado at roughly 118 racks with 32×100G top-of-rack in a leaf-spine design. Geico's infrastructure leadership intended the facility to serve as a shared resource across Berkshire Hathaway companies, which meant enterprise scale with hyperscale architectural and commercial expectations — and no Cisco architect in the enterprise theater with SONiC depth.

**SONiC data center fabric:** Geico needed SONiC on Cisco 8000 for a greenfield colocation fabric, a migration path from cloud and a legacy Nexus 9000 footprint, and commercial terms that matched cloud-scale buying rather than traditional enterprise switching quotes. Bruce's involvement and accomplishments include:

- Served as SONiC subject-matter expert for the Colorado colocation architecture, leading the data center architecture sessions (Mar 2024)
- Advocated directly with the business entity for a **cloud and hyperscale-style pricing model** to support Berkshire-wide infrastructure sharing — a commercial argument, not a technical one, made on behalf of an account he did not own
- Enabled the account team on leaf-spine design, the Q2 production timeline, and workload migration framing

**Financial impact:** ~$1.6M Cisco 8000 win `[verify finance]`.
**Competitive impact:** Established SONiC on Cisco 8000 as viable for enterprise data center at a customer evaluating white-box alternatives.
**Strategic impact:** Proved the hyperscale consumption model transfers to enterprise, and created a Berkshire Hathaway shared-infrastructure reference.
**Overall customer impact:** A credible open-NOS data center path for a major insurer, with commercial terms matched to how they actually buy.

**Evidence:** Vault `customers/Geico.md`; 2HFY24 talent assessment.

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).

---

### Honeywell, 2024

**Revenue Impact:** ~$2M Segment Routing / Cisco 8000 `[verify finance]`

Honeywell is a Fortune 100 industrial conglomerate operating a global network spanning six colocation facilities and two private data centers on an NCS 5501 backbone, with SD-WAN headend integration and IoT transport segmentation requirements. Arista was positioning against Cisco in the backbone.

**Segment Routing backbone architecture:** Honeywell needed path preference from SD-WAN into the private backbone, an assessment of Flex-Algo for IGP-based path selection without a controller, and an SR/SRv6 roadmap. Bruce served as architecture subject-matter expert on the backbone design, SD-WAN integration options, and Flex-Algo use cases (Apr 2024), and consulted on future IoT transport segmentation and internal chargeback models.

**Financial impact:** ~$2M Segment Routing / Cisco 8000 win `[verify finance]`.
**Competitive impact:** Held the backbone franchise against Arista. `[verify — confirm Arista was actively competing and displaced]`
**Strategic impact:** Demonstrated that MIG transport expertise transfers directly to industrial enterprise backbones outside the SP segment.
**Overall customer impact:** A controller-free path selection architecture aligned to Honeywell's global colocation footprint.

**Evidence:** Vault `customers/Honeywell.md`.

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).

---

### Adobe, 2024 – 2025

**Revenue Impact:** Nexus and cloud-native pull-through `[verify finance]`

Adobe is a global technology enterprise with a multi-cloud footprint, migrating to vanilla Kubernetes under its Adobe Ethos program. Adobe wanted to move Adobe-to-Adobe traffic off the public internet using Cilium — egress gateway, load balancing, overlapping RFC1918 space, and multihop BGP. In 2024 the proof of concept was failing during its critical validation window, and the account systems engineer, Dan Stacks, needed Isovalent depth that did not exist on his team.

**Cilium egress gateway rescue and cloud-native SRv6:** Bruce's involvement and accomplishments include:

- **Rebuilt Adobe's entire topology in his own lab (Apr 2024)** to diagnose the failing proof of concept, despite having no prior hands-on experience with Isovalent egress gateway or load balancing, and resolved the configuration and deployment faults
- Provided critical-path egress gateway validation support during the October 2024 POC window
- Served as core technical SME on the Cilium POC with Brenden Buresh and Dan Stacks through 2024–2025
- Proved egress gateway and load balancer functionality against performance requirements at the June 2025 onsite workshop
- Reviewed and shaped the Cloud-Native SRv6 architecture (Feb 2025) — SRv6 L3VPN CNI-to-CNI, elimination of VXLAN and MPLS stitching at both top-of-rack and DCI/PE, eBPF visibility, and transit gateway cost reduction

The proof of concept completed in October 2025.

**Financial impact:** Nexus and cloud-native security pull-through `[verify finance]`.
**Competitive impact:** Preserved a Cilium proof point that was failing and would otherwise have closed the opportunity.
**Strategic impact:** Validated the post-acquisition Isovalent product path in a live enterprise engagement. The Cloud-Native SRv6 concept reviewed here is the same architecture later deployed at Boost Mobile and Digital Realty, and fed the multi-use-case Cilium customer requirements document Cisco engineering has since accepted — detailed in the Innovation section of this document.
**Overall customer impact:** A working egress and load-balancing architecture that moves Adobe-to-Adobe traffic off the public internet.

**Evidence:** Vault `customers/Adobe Cilium.md`, `customers/Adobe CN-SRv6.md`. `[Adobe / Dan Stacks testimonial pending]`

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).
The Cilium SRv6 product path is detailed in the Innovation section of this document. Bruce's mentoring of Dan Stacks is detailed in SE Community Leadership.

---

### Fiserv, Jan 2026

**Revenue Impact:** Pipeline `[verify finance]`

Fiserv is one of the largest financial technology providers in the world, operating payment and banking infrastructure for thousands of institutions. The account sits outside ASP+Web; Bruce was engaged because the field needed SRv6 depth that the enterprise financial theater could not supply.

**SRv6 WAN and data center architecture:** Fiserv runs a Juniper RSVP-TE WAN overlay with VXLAN EVPN in the data center, and needed a credible path to extend a Segment Routing overlay end to end, simplify WAN-to-DC stitching, and evaluate geo-fencing and data-sovereignty steering — the same patterns Bruce had developed in hyperscaler SWAN work — without a rip-and-replace program. Bruce delivered the SRv6 transfer of information to Fiserv's banking infrastructure team (Jan 2026), framed the WAN-to-DC extension with SD-WAN-to-SR anchor points and slice/shard/pinning in the data center, assessed Isovalent and Cilium relevance for the wireless private access context, and positioned SRv6 for AI backends for roadmap alignment.

**Financial impact:** Pipeline `[verify finance]`.
**Competitive impact:** Opened an SRv6 displacement conversation against an incumbent Juniper RSVP-TE overlay. `[early — verify whether Fiserv has committed to a direction]`
**Strategic impact:** Demonstrated that hyperscaler WAN patterns transfer to tier-1 financial services infrastructure.
**Overall customer impact:** A staged simplification path from RSVP-TE to end-to-end Segment Routing without a forklift program.

**Evidence:** Vault `customers/Fiserv SRv6.md`.
// Fiserv: was this a single TOI session, or has it continued into 2026? If it has continued, the entry can claim more than it currently does.

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).

---

### Additional Americas Enterprise Engagements

| Customer | Period | Bruce's contribution | Outcome |
| :--- | :--- | :--- | :--- |
| **Visa** | 2025 | Isovalent introduction; SR/SRv6 RPO demonstration | Financial services pipeline `[verify]` |
| **Disney** | 2025 | DGN and SR-MPLS architecture collaboration | Media enterprise; micro-segmentation and DPU considerations |
| **Texas Instruments** | 2024 | Global POP and SRv6 roadmap architecture | Manufacturing WAN; Arista competitive framing |
| **The Trade Desk** | 2024 | SONiC and IOS-XR platform diversity evaluation | Ad-tech data center at neo-cloud scale |
| **Morgan Stanley** | 2023 | SRv6 architecture presentation | Financial services enablement |
| **NSight** | 2025–2026 | Cilium, Kubernetes, and AI-services architecture for the packet core team; same host-networking policy model as the Cilium CRD | Regional service provider (Green Bay) |
| **Applied Digital** | 2024 | AI rail architecture diagrams and fabric calculator | ~$30M cited `[verify]` — *see Business Impact for account treatment* |

---

## 2. Public Sector and Education

### Province of New Brunswick — Cisco Live Europe 2026

**Revenue Impact:** Migration underway; platform revenue `[verify]`

The Province of New Brunswick operates the provincial government network for Canada's eighth-largest province. Lead architect **James Munroe** attended Bruce's Cisco Live Europe 2026 session with a conventional SR-MPLS migration already planned — the safe, well-trodden path that most operators of that scale were taking.

Bruce spent a single architecture conversation with him at a Meet-the-Expert session, working through the design tradeoffs of adopting SRv6 directly versus staging through SR-MPLS first.

**Financial impact:** Migration in progress; platform revenue `[verify]`.
**Competitive impact:** Converted a planned legacy-transport deployment into a next-generation architecture at the design stage.
**Strategic impact:** This is the clearest single measure of Bruce's reach as a field multiplier — no account assignment, no follow-on engagement, no proposal. One conversation.
**Overall customer impact:** **James Munroe abandoned the planned SR-MPLS migration, authored a complete SRv6 design document within approximately two weeks of the conference, and began the migration** — an unusually fast operator decision from a single conference conversation.

The Cisco Live session itself is detailed in the SE Community Leadership section of this document, and its industry visibility in Industry Impact.

---

### NYU and Carnegie Mellon, 2024

Bruce advised **New York University** on the HSRN SONiC research network (Aug 2024) and delivered a SONiC education session to **Carnegie Mellon**.
// NYU/CMU: is there any documented outcome — a deployment, a paper, students who went on to operator roles? Without one this stays a two-line entry. Research and higher-education networks are early adopters of disaggregated platforms and function as a credibility channel into the operator community — the engineers running them frequently move into industry roles carrying their platform preferences with them.

---

## 3. APJC and EMEA Operators

### Evroc, 2024 – 2026 *(ongoing)*

**Revenue Impact:** `[verify finance]`

Evroc is a European sovereign-cloud provider building hyperscale capacity in the EU, and is exactly the kind of operator Cisco needs as a reference in the EMEA neo-cloud market. Evroc faced a startup-scale engineering organization against production-grade multi-site fabric requirements, with no Cisco architect in theater carrying both SONiC and cloud-native depth.

Bruce serves as architecture advisor on colocation-2 readiness, covering SONiC spine and leaf design with 8201 border routers, host multi-homing, Kubernetes-centric segmentation across Cilium and Calico, and inter-site design without Layer 2 stretch. He framed the tradeoff between short-term EVPN-to-host and long-term pure IP with VPC-in-host, and drove WAN, frontend data center, SRv6, and host-overlay direction.

**Strategic impact:** Reuses the CoreWeave and Microsoft-class architecture patterns in the EMEA theater, on an account with no Americas relationship. Evroc engagement originated from Cisco Live Europe.
// Evroc: any revenue or committed pipeline yet? This is the one EMEA account that could carry a number.
**Overall customer impact:** A production-grade multi-site fabric design an early-stage engineering team can actually execute.

**Evidence:** Vault `customers/Evroc.md`.

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).

---

### Rakuten, Jul 2025

**Revenue Impact:** `[verify finance]`

Rakuten Mobile operates the world's first fully virtualized, cloud-native mobile network and is among the most architecturally aggressive operators in APJC. The APJC account team requested Bruce for high-level design work on extending the SD-WAN underlay with SRv6.

Bruce produced the SRv6 SD-WAN underlay high-level design, evaluating Cisco models for SRv6 CPE-to-CPE and private-cloud host integration through Cilium, documenting the customer's stated preference for traditional PE models, and building the **Unified SRv6 Fabric** value case for the APJC account team.

**Strategic impact:** Direct architecture influence on a tier-1 APJC operator's WAN evolution without account ownership, in a theater twelve time zones from his own.

**Evidence:** Vault `customers/Rakuten SRv6-SDWAN.md`.

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).

---

### NTT East, 2025

Bruce served as SRv6 and Cilium subject-matter expert for the APJC account team at **NTT East**, one of Japan's two incumbent regional carriers, delivering SRv6 and Cilium introductions that produced study-level SRv6 L3VPN interest.

---

## 4. Field Multiplier — Impact Without Customer Contact

The purest measure of global reach is impact on customers Bruce never met, achieved by making another theater's systems engineer more capable.

### MTN Nigeria and DU UAE — via APJC Field Enablement, 2024

**Revenue Impact:** ~$85K customer lab savings; 2,300-node POC topology `[verify]`

**MTN Nigeria** is the largest mobile operator in Africa, and **DU** is one of two national operators in the United Arab Emirates. Neither is an ASP+Web account and neither is in Bruce's theater. APJC systems engineer **Sanjay Nanda** engaged Bruce for SRv6 topology and migration expertise he could not source locally.

Bruce built the topology and migration designs Sanjay carried into both accounts, producing approximately **$85,000 in avoided customer lab expenditure at MTN Nigeria** and a **2,300-node SRv6 POC topology at DU** — POC scale that would not have been attempted without the design work `[verify]`.

**Strategic impact:** Two national operators on two continents advanced their SRv6 programs on architecture Bruce authored, through a systems engineer he enabled rather than an account he covered.

---

### WWT — Systems Integrator Enablement, 2026

Bruce delivers SRv6, SONiC, and Cilium enablement workshops to **World Wide Technology** with Dave Clough. WWT is one of Cisco's largest systems integration partners; capability built there propagates across the partner's entire customer base rather than a single account. `[verify scope; LoR candidate]`

---

## Summary Table — Global Impact Accounts

| Customer | Theater | Segment | Signature outcome | Revenue / status |
| :--- | :--- | :--- | :--- | :--- |
| **Geico** | Americas | Insurance | SONiC DC fabric; Berkshire-wide pricing model | **~$1.6M** `[verify]` |
| **Honeywell** | Global ent. | Industrial | SR backbone; Flex-Algo; held off Arista | **~$2M** `[verify]` |
| **Adobe** | Global ent. | Technology | Rescued failing Cilium POC; completed Oct 2025 | Pull-through `[verify]` |
| **Fiserv** | Americas | Financial | SRv6 TOI; RSVP-TE displacement path | Pipeline `[verify]` |
| **Province of NB** | Americas | Public sector | One conversation → SRv6 design + migration in ~2 weeks | Migration begun |
| **Evroc** | EMEA | Sovereign cloud | Colo-2 SONiC/Cilium architecture | Ongoing `[verify]` |
| **Rakuten** | APJC | Mobile/cloud SP | SRv6-SDWAN underlay HLD; Unified SRv6 Fabric case | HLD `[verify]` |
| **MTN Nigeria / DU** | EMEA/APJC | Mobile SP | ~$85K lab savings; 2,300-node POC | Enablement `[verify]` |
| **Visa** | Global | Financial | Isovalent introduction; RPO demo | Pipeline `[verify]` |
| **Disney** | Americas | Media | DGN / SR-MPLS architecture | Collaboration `[verify]` |
| **Texas Instruments** | Global ent. | Manufacturing | Global POP / SRv6 roadmap | Architecture `[verify]` |
| **NTT East** | APJC | Tier-1 SP | SRv6 / Cilium introductions | Study `[verify]` |
| **The Trade Desk** | Americas | Ad-tech | SONiC and XR evaluation | Mindshare `[verify]` |
| **Morgan Stanley** | Americas | Financial | SRv6 architecture presentation | Enablement |
| **NSight** | Americas | Regional SP | Cilium / K8s / AI services | Early `[verify]` |
| **NYU / CMU** | Americas | Education | SONiC advisory and education | Enablement |
| **WWT** | Americas | SI partner | SRv6/SONiC/Cilium workshops | `[verify]` |

**Pre-2020 / early-PSE mindshare only (exec thru-line):** Telstra, Indosat, Goldman and Wells Jalapeno threads, Brussels SR workshop (2022) — not expanded as body case studies per [AGENTS.md](./AGENTS.md) time scope.

---

## Note on Page Budget

README weighting allocates **7 pages** to Global Impact, equal to Business Impact. This draft runs closer to **4–5 pages**, and expanding it further would require padding engagements that are honestly summarized in the table above.

For reference, Brenden's package allocates **2 pages** to Global Impact against **17 pages** for Business Impact — the README weighting is generic guidance rather than an observed pattern in a successful package. **Recommendation:** hold Global Impact at its natural length and reallocate the surplus to Business Impact and SE Community Leadership, where the evidence supports the volume. `[Bruce decision]`

---

## Open Items

- [ ] Finance validate: Geico **~$1.6M**, Honeywell **~$2M**, Adobe pull-through, Fiserv pipeline
- [ ] Adobe / Dan Stacks testimonial on Cilium EGW/LB impact — strongest available customer quote for this section
- [ ] MTN Nigeria **~$85K** and DU **2,300-node** figures — confirm with Sanjay Nanda
- [ ] Province of NB — confirm migration status and whether James Munroe would provide a quote or LoR
- [x] Digital Realty assignment resolved — **ASP+Web**, drafted in [06-business-impact.md](./06-business-impact.md)
- [ ] Softbank, Telstra, Swisscom, Telia — confirm post-2020 outcomes or omit from lists
- [ ] WWT / Dave Clough — scope and LoR
- [ ] Evroc — confirm revenue or pipeline figure

**Vault harvest:** `dse/03-Global-Impact-MOC.md`, enterprise customer notes (Geico, Fiserv, Adobe, Honeywell, Rakuten, Evroc, NTT East). **Last body pass:** Aug 2026 — rewritten to [voice-guide.md](./voice-guide.md) register; restructured by expansion pattern.
