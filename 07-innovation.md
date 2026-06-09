## Innovation

> **Scope ([AGENTS.md](./AGENTS.md)):** **IPR and product/technology innovation** since **August 1, 2020**—often **downstream of Span of Influence** advocacy outside MIG.  
> **Include:** patents/CPOLs (post-2020 submissions + post-2020 *impact* of earlier work), architectural artifacts, labs/repos that drove **product or strategy**.  
> **Cross-ref:** Customer revenue from those products → **06-business-impact.md**. External blog/conference reach alone → **05-industry-impact.md**. Internal BU persuasion without IP artifact → **04-span-of-influence.md**.

**Suggested package length:** ~6 pages weighted. Third-person, most-recent-first.

---

## Innovation Summary Table

| Category | Evidence (Aug 2020–present) |
| :--- | :--- |
| **Awards** | **2025 Pinnacle Award** — SRv6 uSID team (sales-org recipient) |
| **Patents / CPOLs** | **6 issued**, **6 pending**, **18 total submissions** `[verify counts]` — see table below |
| **Bold Bets** | **Jalapeno** — only field project to advance past first evaluation round |
| **Open source** | [cisco-open/jalapeno](https://github.com/cisco-open/jalapeno); [segmentrouting](https://github.com/segmentrouting) org; srv6-msft, srv6-oci, srv6-mrc-emulator |
| **SR-Apps** | early development and prototyping effort which led to D-SDN and SRv6 auto-BW; leveraged Jalapeno a development platform | 
| **Product direction** | SRv6 on SONiC (8122 ship Jun 2026); SRv6-for-AI; Cilium SRv6 CRD; SGT-in-uSID |
| **Architectural specs** | SRv6 multi-tenant AI fabric (Apr 2026); Hoffman–Singleton fabric study; Policy Plane / Yukon++ threads |
| **Hackathon** | EN Hackathon 2022 winner — SD-WAN/SRv6 demo (Team 6 / Group 14) |

---

## Innovation — Draft Package Body

---

### End.USD XR Fix — Jan 2023

Bruce found **broken End.USD behavior in IOS-XR** and worked directly with **Kamran Raza** on the fix—field-discovered defect with engineering remediation (Innov + Span).

---

### First SRv6-for-AI / uSID Brainstorm — May 2023

**May 31, 2023:** First internal discussion of **SRv6 uSID testing for AI workloads** (Pablo, Praveen)—later validated by **Microsoft at OCP 2024/2025** and **MRC 2026** announcements.

---

### Convincing MIG on SONiC SRv6 for AI — Nov 2024

Close coordination with SRv6 engineering on **SONiC feature development** (uSID forwarding, static uSIDs, BGP GRT, sonic-vpp, sonic-vs). Bruce was **instrumental in convincing the BU** the AI-backend use case was real—that **OpenAI was driving Microsoft and OCI investment**—when MIG engineering initially disputed customer urgency for weeks/months.

---

### “Scaling the Cloud to a Billion Servers” — 2020

Thought-experiment presentation for early **internal SRv6 workshop**—audience impact led **Clarence Filsfils** to emphasize Bruce must lead **hyperscale SRv6** market entry (validated **2025** tier-1 wins).

---

### Bold Bets — Jalapeno — 2020–2021

**Nov 2020:** Bold Bet advanced to **Validate phase** (Innov, Global). **2021 summary:** Only **Bold Bet submission from sales org** promoted through process to **funding ask** before program ended—field-led open SDN controller lineage.

---

### SR-Apps & Per-Flow BSID — 2020–2021

**Jul 2020–2024:** SR-Apps field co-development influenced **IPM**, path tracing, **NaaS**, and host-based SRv6 extensibility without standalone app SKU. **Dec 2020:** Per-flow steering into **BSID** deck—precursor to **DSDN** direction.

---

### ThousandEyes & Synthetic Path Tracing — Mar 2022

ThousandEyes SRv6 architecture engagement → issued patent **US12289210** (*Synthetic Path Tracing of Segment Routed Networks*); **Jan 2025** CIPOL renewal with Hans Ashlock.

---

### AquarianSpace / Scheduled FIB — Feb 2022

Deep-space **Delay Tolerant Networking** research for Brook Crossman (AquarianSpace)—Cisco declined product investment; **patent pending US12494999** (*Scheduled FIB to Account for Intermittent Connectivity Due to Orbital Dynamics*); **Sep 2025** CIPOL filed.

---

### EN Hackathon Winner — Sep 2022

**EN Hackathon** winner—proof point for **SRv6-SDWAN** integration (see CIPOL; later **SRv6-SGT** work).

---

### SONiC CSW POC — Dec 2025

**SONiC Cisco Secure Workload POC** with Jason Maynard, Chris Crider—proved **CSW** as viable product to secure SONiC infrastructure (Innov + Span).

---

### Pinnacle Award — SRv6 uSID — 2025

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

Bruce drove the **internal investment case** for SONiC SRv6—culminating in **SRv6 on SONiC for Cisco 8122** (202511 codebase, **June 2026**). Includes BGP GRT, SRv6-TE, disaggregated RH fast-reroute prototypes documented with Microsoft engineering. Bruce partners with Cisco SRv6/SONiC engineering on scope and early validation *(industry Phoenix Wing is Alibaba-led; Bruce’s work is Cisco engineering + customer POC path)*.

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

Bruce developed architecture to embed **16-bit Security Group Tags** in uSID function arguments—unifying enterprise identity (ISE/SD-WAN SGT carry) with hyperscale SRv6 transport. **Jan 2024:** With **Josh Merrill**, Bruce began pursuing **SRv6 as end-to-end solution** spanning **SASE, ISE, and transport**—pulling in **Darren Miller (ISE DE)** for identity services. **First documented Jan 2024**; co-invented **SRv6-SGT** concept and served as wingman on multi-BU **Yukon++** (“Cisco Powered Part 2”) with Josh Merrill. Working sessions with Darren Miller, Pablo, Josh (ISE modernization). CPOL merged: *SRv6 uSID Carrier with Embedded Security Group Tag*. **Dec 2025:** **ISE fully on board** with SRv6 SGT and **unified policy model**.

**Vault:** `innovation/SGT, SRv6, NaaS Notes.md`, CPOL table below

---

### Policy Plane & Yukon++ — 2023–2025

Bruce’s **Policy Plane** concept—TEyes topology visibility + ISE/SGT identity + SRv6 transport as three “glue layers”—is gaining **MIG traction** per development-discussion notes. Related **Yukon++** / **Project Yukon** (Jan 2024) / service-chain / NaaS threads document SP underlay exposing services to SD-WAN and cloud-like consumption for **Verizon and AT&T**.

**Status:** `[verify PM attribution]` — Carlos Pereira / OTel visibility platform influence noted as open question in vault.

**Vault:** `innovation/yukon-glue.md`, `innovation/SGT, SRv6, NaaS Notes.md`, `dse/06-Business-Impact-MOC.md`

---

### Jalapeno — Bold Bets & Open Source — 2021–2024

**Jalapeno Network Service Broker:** Bruce led the **only field-submitted Bold Bets** project to advance past the first evaluation round—programmable multi-domain network services, graph-DB reachability, K8s integration. Successfully open-sourced via Cisco Legal: **[cisco-open/jalapeno](https://github.com/cisco-open/jalapeno)**.

**Early field validation (pre-OSS):** **ExBroker/Jalapeno** presented to **Qwilt** (CDN, Jan 2023) and **Rackspace** (Mar 2023); **Cross-Domain Broker** exec readout (Oct 2023) → **04-span-of-influence.md**.

**`srctl` CLI (2025):** Bruce built the **`srctl`** command-line tool for Jalapeno—used in the **May 22, 2025 Akamai demo** (Talent Assessment 2HFY25). Extended Jalapeno with **API, UI, and initial code** for the **AI load-balancing** use case. **Oct 2023:** **FRR SRv6 L3VPN image and lab** for Russ White (**Akamai**)—operator prototype path.

**Themes:** Network service brokerage, programmable underlays, cloud-native control plane—precursor to homegrown hyperscaler controllers and AI-backend TE.

**Vault:** `xarchive-2021-2022/BB-Jalapeno-Overview-20210820.md`, `labs/jalapeno-notes.md`

---

### Cilium-SP Feature Business Case — 1HFY26

Bruce **gathered and compiled account data worldwide** to build the business case for **Cilium-SP feature development**, estimating pullthrough revenue of **~$34M (Isovalent)** and **~$323M (MIG)**—validated estimates used for product investment prioritization. **Nov 2025:** Maintains **Cilium-SP opportunity/TAM tracker** capturing telco and SP use cases globally.

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

### IOS-XR Hyperscale uSID — 256 Blocks per Node — Oct 2023

Bruce drove internal confirmation of **IOS-XR support for 256 uSID blocks per node**—productizing hyperscale SRv6 locator scale required for Web/SP AI and WAN designs. Span handoff → **04-span-of-influence.md**.

---

### GitHub-First Cisco Live Labs — 2022–2026

Bruce **pioneered GitHub-based Cisco Live lab guides** (configs, code, Containerlab)—now common practice across ILT sessions. Ties to innovation methodology: open, reproducible co-development with hyperscalers before product exists.

**Vault:** `07-Innovation-MOC.md`, `dse/GithubJalapenoLinkedIn - stats.md` `[if exists]`

---

### CNRS / SR-Apps University Partnership — 2020–2026

Bruce serves as **field lead** for CNRS/SR-Apps university collaborations (OST Zurich and others)—HS-PCE, ACP tech fund, thesis projects. Innovation impact: pipeline of SR/SRv6 research → field validation → product feedback.

**Vault:** `07-innovation.md` (candidate notes), `mentor/Satoshi Yamashita – STLDP.md`

---

### Innovation Referrals & “Nutty Ideas” — 2026

Bruce is a known **innovation funnel** inside Cisco—colleagues with horizon-3 ideas are **referred to Bruce** for brainstorming and refinement:

- **Jan 2026 — CHCN (Riccardo):** Full-NG/SDN architecture proposal; Bruce advised scaling back to **SRv6 uSID**; Riccardo developing rich demo
- **Jan 2026 — Don Ewald (Microsoft SE):** SDN/SmartSwitch “Nutty Idea” brainstorm

---

### Jalapeno RPO / SDN App Lineage — Nov 2024–2025

**Nov 2024:** AI hackathon with **Zafar Ali** produced early **Jalapeno RPO SDN app**. **Nov 2024:** **Elephant-flows demo** (Brook, Josh, HQ)—**second RPO version** later used in **Verizon, AT&T, and Digital Realty** engagements. Feeds operator **RPO/A3PO POC planning** (Sep 2025).

---

### SRv6 Multi-Tenant AI Fabric & MRC — May 2026

**May 2026:** **SRv6 multi-tenant design** completed and reviewed with **Microsoft and Oracle** (Lokesh Khanna, John McLeod, Joe Rockwell). Same month: industry **MRC announcement**—Bruce developed **PPT + emulator project** shared with MSFT and Oracle (see **srv6-mrc-emulator**).

**Cross-ref:** **06-business-impact.md** (Microsoft/OCI AI backend).

---

### Cilium-SP CRD & Progressive Use Cases — Mar 2026

Bruce authored **Cilium-SP CRD** documentation with **progressive use cases** from **L3VPN → EGW → TGW**—product-facing artifact bridging SP transport and cloud-native service insertion (`Cilium-SRv6-CRD.docx` lineage).

---

### SD-WAN CPOL Threads — Feb–Jun 2024

- **Feb 2024:** **C/P/1035600** — *Core Network Support for Application-Requested Network Service Level Objectives* (SD-WAN engineering)
- **Jun 2024:** **C/P/1035601** — *Underlay Network Traffic Steering* (SD-WAN team)

Span handoff → **04-span-of-influence.md** (SD-WAN/SSE); patent table below.

---

### SRv6 for SSE — Aug 2024

Architectural agreement and **CPOL thread** with **Rupak Chandra** on **SRv6 for Cisco Secure Access (SSE)**—enterprise security plane integration with SRv6 transport.

---

### Adobe EGW POC Rescue — Oct 2024

Bruce **rescued Adobe EGW POC** during critical validation window—field intervention that preserved cloud-native egress-gateway proof point ahead of **Jun 2025** onsite workshop (Dan Stacks).

---

### Polarfly Topology Research — Jan 2025

**Polarfly** project with **Chris Martin (OCI)**—low-diameter fabric research adjacent to Hoffman–Singleton study.

---

### SONiC Cisco Secure Workload POC — Dec 2025–Feb 2026

With **Jason Maynard** and **Chris Crider**, Bruce developed **SONiC + Cisco Secure Workload (CSW)** POC—**successful POC** proving CSW as **Live Protect for SONiC** (collaboration with security SE specialist team). Follow-on sessions **Jan–Feb 2026** track productization `[verify]`. **Oct 2025+:** Ongoing **Live Protect on SONiC** thread with enterprise DSE **Brian Shlisky**.

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
- [ ] Policy Plane publication (noted “need to publish” in MOC)
- [ ] SGM stats: how many CL ILTs now use GitHub lab model
- [ ] Carlos Pereira / OTel platform influence confirmation
