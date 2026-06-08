## Innovation

> **Scope ([AGENTS.md](./AGENTS.md)):** **IPR and product/technology innovation** since **August 1, 2020**—often **downstream of Span of Influence** advocacy outside MIG.  
> **Include:** patents/CPOLs (post-2020 submissions + post-2020 *impact* of earlier work), architectural artifacts, labs/repos that drove **product or strategy**.  
> **Cross-ref:** Customer revenue from those products → **06-business-impact.md**. External blog/conference reach alone → **05-industry-impact.md**. Internal BU persuasion without IP artifact → **04-span-of-influence.md**.

**Suggested package length:** ~6 pages weighted. Third-person, most-recent-first.

---

## Innovation Summary Table

| Category | Evidence (Aug 2020–present) |
| :--- | :--- |
| **Awards** | **2026 Pinnacle Award** — SRv6 uSID team (sales-org recipient) `[verify year label: vault says 2025]` |
| **Patents / CPOLs** | **6 issued**, **6 pending**, **18 total submissions** `[verify counts]` — see table below |
| **Bold Bets** | **Jalapeno** — only field project to advance past first evaluation round |
| **Open source** | [cisco-open/jalapeno](https://github.com/cisco-open/jalapeno); [segmentrouting](https://github.com/segmentrouting) org; srv6-msft, srv6-oci, srv6-mrc-emulator |
| **Product direction** | SRv6 on SONiC (8122 ship Jun 2026); SRv6-for-AI; Cilium SRv6 CRD; SGT-in-uSID |
| **Architectural specs** | SRv6 multi-tenant AI fabric (Apr 2026); Hoffman–Singleton fabric study; Policy Plane / Yukon++ threads |
| **Hackathon** | EN Hackathon 2022 winner — SD-WAN/SRv6 demo (Team 6 / Group 14) |

---

## Innovation — Draft Package Body

---

### Pinnacle Award — SRv6 uSID — 2025/2026

Bruce received Cisco’s **Pinnacle Award** as part of the team recognized for **SRv6 uSID market impact**—a rare honor for sales organization members. The award cites unified forwarding architecture, network-as-API programmability, and cross-domain automation readiness (SDN/NFV/5G/hyperscale).

**Strategic impact:** Validates field-led SRv6 uSID advocacy as company-level innovation, not only account support.

**Vault:** `dse/Pinnacle-Award-2025-SRv6-uSID.md`, `01-exec-summary.md`

---

### SRv6 Multi-Tenant AI Fabric Specification — Apr 2026

Bruce authored *SRv6 uSID Multi-Tenancy and Security for AI Factory Network Fabrics*—confidential design spec covering encap/decap at leaf, NIC, or hybrid; uDT tenant-ID allocation in 16-bit uSID space; explicit uA path pinning; scale targets (**131k GPU** per cluster, multi-cluster topologies). Referenced SONiC implementation paths (e.g., SwSS PR #4404, Mar 2026).

**Product/strategy impact:** Became the reference architecture for Microsoft/OCI/CoreWeave AI engagements; instantiated in open POC repos for customer and SE validation.

**Artifacts:** `innovation/SRv6-MultiTenant-Design-rev3.md`, `innovation/srv6-design-spec.md`  
**Repos:** [srv6-msft](https://github.com/segmentrouting/srv6-msft), [srv6-oci](https://github.com/segmentrouting/srv6-oci)

---

### SRv6 on SONiC — AI Backend Productization — 2024–2026

Bruce drove the **internal investment case** for SONiC SRv6 (beyond Phoenix Wing DCI/metro)—culminating in **SRv6 on SONiC for Cisco 8122** (202511 codebase, **June 2026**). Includes BGP GRT, SRv6-TE, disaggregated RH fast-reroute prototypes documented with Microsoft engineering.

**Span → Innovation path:** Field advocacy → engineering priority → shippable feature → hyperscaler co-development revenue (Business Impact).

**Vault:** `customers/Microsoft  SRv6.md`, `customers/MSFT octans-drh.md`, `07-Innovation-MOC.md`

---

### MRC Emulator & SRv6-for-AI Teaching Tools — 2025–2026

Bruce built the **[srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator)** and related labs so SEs and customers could model **Multipath Reliable Connection** + SRv6 static routing—aligned with OpenAI/Microsoft/NVIDIA/Broadcom/AMD industry specification. Microsoft and Oracle engineers used artifacts in internal executive presentations.

**Innovation type:** Reference implementation + enablement accelerator for a net-new architecture class.

---

### Isovalent / Cilium SRv6 Integration — 2021–2026

Bruce was an **early advocate** for Cisco acquisition of **Isovalent** and **SRv6-in-Cilium**—technical validation of eBPF-based SRv6 L3VPN, egress gateway, and pod-level encap/decap (`Cilium-SRv6-CRD.docx`, Mar 2026). Post-acquisition, this defines a **product integration path** between cloud-native security and SP transport.

**Evidence:** Thomas Graf letter of recommendation (acquisition + SRv6 enablement); Bell Canada host-based SRv6 collaboration; Boost Mobile SRv6-on-AWS overlay design.

**Vault:** `customers/cilium-srv6.md`, `Isovalent-Cilium-Hub.md`, `07-Innovation-MOC.md`

---

### SGT in uSID — End-to-End Identity in SRv6 Program — Jan 2024–2025

Bruce developed architecture to embed **16-bit Security Group Tags** in uSID function arguments—unifying enterprise identity (ISE/SD-WAN SGT carry) with hyperscale SRv6 transport. Working sessions with Darren Miller, Pablo, Josh (ISE modernization). CPOL merged: *SRv6 uSID Carrier with Embedded Security Group Tag*.

**Impact:** Closes policy gap between enterprise segmentation and SP/hyperscale forwarding—FE Segmentation tiger team handoff.

**Vault:** `innovation/SGT, SRv6, NaaS Notes.md`, CPOL table below

---

### Policy Plane & Yukon++ — 2023–2025

Bruce’s **Policy Plane** concept—TEyes topology visibility + ISE/SGT identity + SRv6 transport as three “glue layers”—is gaining **MIG traction** per development-discussion notes. Related **Yukon++** / service-chain / NaaS threads document SP underlay exposing services to SD-WAN and cloud-like consumption.

**Status:** `[verify PM attribution]` — Carlos Pereira / OTel visibility platform influence noted as open question in vault.

**Vault:** `innovation/yukon-glue.md`, `innovation/SGT, SRv6, NaaS Notes.md`, `dse/06-Business-Impact-MOC.md`

---

### Jalapeno — Bold Bets & Open Source — 2021–2024

**Jalapeno Network Service Broker:** Bruce led the **only field-submitted Bold Bets** project to advance past the first evaluation round—programmable multi-domain network services, graph-DB reachability, K8s integration. Successfully open-sourced via Cisco Legal: **[cisco-open/jalapeno](https://github.com/cisco-open/jalapeno)**.

**`srctl` CLI (2025):** Bruce built the **`srctl`** command-line tool for Jalapeno—used in the **May 22, 2025 Akamai demo** (Talent Assessment 2HFY25). Extended Jalapeno with **API, UI, and initial code** for the **AI load-balancing** use case.

**Themes:** Network service brokerage, programmable underlays, cloud-native control plane—precursor to homegrown hyperscaler controllers and AI-backend TE.

**Vault:** `xarchive-2021-2022/BB-Jalapeno-Overview-20210820.md`, `labs/jalapeno-notes.md`

---

### Cilium-SP Feature Business Case — 1HFY26

Bruce **gathered and compiled account data worldwide** to build the business case for **Cilium-SP feature development**, estimating pullthrough revenue of **~$34M (Isovalent)** and **~$323M (MIG)** `[verify finance methodology]`. Span → Innovation: field evidence driving product investment prioritization for service-provider Cilium capabilities.

**Cross-ref:** End-to-end SRv6 + Cilium platform investments (ISE, IOS-XE, Nexus, SONiC, SD-WAN, SASE) noted in same assessment cycle → **04-span-of-influence.md**

---

### EN Hackathon — SD-WAN / SRv6 — 2022

**Winner:** Cisco EN Hackathon 2022 (Team 6 / Group 14) — SD-WAN + SRv6 demonstration.  
**Link:** [Hackathon winners page](https://cisco.sharepoint.com/sites/EN-Hackathon/SitePages/Hackathon2022-Winners.aspx) (internal)

---

### Hoffman–Singleton Fabric Study — 2024–2025

Low-diameter, high-radix fabric design applying **Hoffman–Singleton graph theory**—co-developed with Oracle engagement for AI backend topology options (slimfly/dragonfly class). Employee reflection (2HFY24) cites **~50% savings on fabric nodes vs. comparable CLOS** for hyperscale DC design. CPOL submissions include declined *Virtualized Rail Architecture for AIML Ethernet fabrics* and related AI scale-up pod designs.

**Vault:** `innovation/Hoffman-Singleton-Fabric-Design.md`, `customers/Oracle-SRv6.md`

---

### GitHub-First Cisco Live Labs — 2022–2026

Bruce **pioneered GitHub-based Cisco Live lab guides** (configs, code, Containerlab)—now common practice across ILT sessions. Ties to innovation methodology: open, reproducible co-development with hyperscalers before product exists.

**Vault:** `07-Innovation-MOC.md`, `dse/GithubJalapenoLinkedIn - stats.md` `[if exists]`

---

### CNRS / SR-Apps University Partnership — 2020–2026

Bruce serves as **field lead** for CNRS/SR-Apps university collaborations (OST Zurich and others)—HS-PCE, ACP tech fund, thesis projects. Innovation impact: pipeline of SR/SRv6 research → field validation → product feedback.

**Vault:** `07-innovation.md` (candidate notes), `mentor/Satoshi Yamashita – STLDP.md`

---

### SONiC CSW / Live Protect Thread — Jan–Feb 2026

Vault notes **SONiC CSW** sessions and question whether capabilities **productize as Live Protect** across route/switch portfolio—eBPF/runtime security intersection with Isovalent. `[verify product outcome]`

**Vault:** `dse/DSE General MOC.md`, `technologies/Isovalent Runtime Security.md`

---

## Patents & CPOL Submissions

*From vault `07-Innovation-MOC.md` — Bruce to verify issued vs. pending vs. declined and attach CPOL links.*

| Date | Status | Title |
| :--- | :--- | :--- |
| 2025-12-02 | Declined | Using Ethereum NonFungible Tokens to prevent BGP Route Hijacks |
| 2025-11-23 | Declined | AI Scale Up Pod Design for 1000 XPU |
| 2025-10-30 | Submitted | Segment Routing SID and SGT state preservation for traffic traversing a non-SR SRv6 service chain |
| 2025-10-02 | Declined | Virtualized Rail Architecture for AIML Ethernet fabrics |
| 2025-05-22 | Approved — Patent Application | System and Method for Authoritative IPv6 Traffic Marking in SDWAN Networks |
| 2025-03-21 | Approved — Patent Application | SmartTOR Policy Orchestration based on NCCL topology |
| 2025-03-21 | Approved — Defensive Publication | Avoiding Fabric Congestion Using an SRTE Agent for AI training using existing Data Centers |
| 2025-03-21 | Merged | SRv6 uSID Carrier with Embedded Security Group Tag (SGT) to Identify AI Request |
| 2023-01-31 | Approved — Patent Application | Synthetic Path Trace of Segment Routed Networks |
| 2022-10-12 | Approved — Patent Application | Network OS Scheduled FIB to account for intermittent connectivity due to orbital dynamics |
| 2022-02-04 | Approved — Patent Application | SP Underlay Services for SDWAN |
| 2021-12-30 | Approved — Patent Application | System and method for SDWAN tunnel provisioning via control plane based on application connectivity requirements |
| 2019-05-28 | Approved — Defensive Publication | Dataplane-based DDoS mitigation and spoofing prevention via SRv6 network programming |
| 2014-06-08 | Approved — Patent Application | Segment routing label switch paths in NFV communications networks |

**Post–Aug 2020 focus for package body:** 2021-12-30 onward rows; earlier filings summarized in exec thru-narrative only unless impact landed after PSE (e.g., defensive pubs cited in SRv6 product strategy).

**Aggregate `[verify]`:** 6 issued, 6 pending, 18 total CPOL submissions (per candidate notes).

**Talent Assessment snapshot (1HFY26, Jan 2026):** 1 patent pending USPTO approval; 3 approved patents in legal drafting; 2 submissions pending internal review; 2 CPOL drafts imminent. Brook noted innovation pace **“on pace to break (ASP) records.”** Reconcile with table above before final PDF.

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
- [ ] Confirm Pinnacle Award year label (2025 vs 2026)
- [ ] Policy Plane publication (noted “need to publish” in MOC)
- [ ] SGM stats: how many CL ILTs now use GitHub lab model
- [ ] Carlos Pereira / OTel platform influence confirmation
- [ ] Phoenix Wing blog link: `2023 sonic-blog-alibaba_msft` (wikilink broken in vault)
