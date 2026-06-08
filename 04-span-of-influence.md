## Span of Influence

> **Scope ([AGENTS.md](./AGENTS.md)):** Impact **internal to Cisco** since **August 1, 2020**—expanding beyond the **ASP + Web + MIG** orbit (IOS-XR, NCS 5k, Cisco 8000, SONiC-as-MIG-platform, Silicon One transport).  
> **This is not a customer/revenue section.** Account outcomes → **[06-business-impact.md](./06-business-impact.md)** / **[03-global-impact.md](./03-global-impact.md)**. External NANOG/GitHub reach → **[05-industry-impact.md](./05-industry-impact.md)**. Patent detail → **[07-innovation.md](./07-innovation.md)**.

**Suggested package length:** 2–3 pages (body). Third-person narratives below, most-recent-first.

---

## Span Expansion Summary

| Dimension | Horizon 1 (early PSE) | Horizon 2–3 (current) |
| :--- | :--- | :--- |
| **Engineering orbit** | SRv6 feature SME within MIG / Web transport | Cross-BU advisor: **Cilium/Isovalent**, **SD-WAN**, **SSE/Cisco Secure Access**, **Nexus/DC**, **Future Enterprise Segmentation**, **Single OS (SOSIE)** |
| **Organizational level** | Theater SRv6 pilots, account-team consultant | **VP/exec** relationships (Knipp, Dorval, Morrissey); **PSE committee**; DSE peer working groups (Buresh, Hill, Teixeira, Murphy) |
| **Strategic framing** | “SR features for SP/Web” | **“2030 guy”**—host networking air-gap, network-as-API, Linux NOS + hardware-accelerated apps, SRv6 uSID as unified programming model |
| **Innovation handoff** | Individual lab prototypes | Advocacy → **Isovalent acquisition**, **SONiC SRv6 investment**, **SD-WAN/SSE roadmap** commitments → see Innovation section |

**Technology domains (≥2):** (1) **Cloud-native / host networking** (eBPF, Cilium, K8s CNI); (2) **Programmable transport** (SRv6 uSID end-to-end); (3) **Open NOS strategy** (SONiC, SOSIE); (4) **Enterprise security integration** (SGT, segmentation, Policy Plane).

---

## Span of Influence — Draft Package Body

---

### Web / Hyperscale TAM — FY26 Global Sales Roadmap — Aug 2025 & Apr 2026

Bruce **owned Web/Hyperscale Technical Account Manager (TAM) responsibilities** for **FY26 Global Sales Technical Roadmap Requirements** and the **BE Interlock Process**—setting technical asks that flow into global sales planning (Aug 2025 and Apr 2026 cycles). Span outcome: field voice for AI/SRv6/SONiC priorities at **sales-org** altitude, not only account teams.

---

### Project Yukon — NaaS Architecture — Jan 2024

Bruce contributed to **Project Yukon** — **NaaS architecture** for **Verizon and AT&T** that heavily leverages **SRv6 extended to CPE/service nodes** (service-chain / underlay exposure to SD-WAN). Handoff to Business Impact for operator revenue threads; internal span = cross-BU NaaS framing beyond MIG transport.

**Vault:** `innovation/yukon-glue.md`, `customers/Verizon.md`

---

### SP NaaS Initiative — EU Advisor — Q2–Q3 2023

Bruce served as **EU advisor** on the **SP NaaS initiative**—extending network-as-a-service consumption models from Americas SP/Web context into EMEA planning.

---

### Cross-Domain Broker — Oct 2023

Bruce presented **Cross-Domain Broker** (Jalapeno / ExBroker lineage) to **Beesely, Mohit Lad, Eric Knipp**—executive-level internal advocacy for programmable multi-domain services.

**Cross-ref:** Innovation (Jalapeno); Industry (operator NaaS narrative).

---

### IOS-XR uSID Scale — 256 Blocks per Node — Oct 2023

Bruce confirmed **IOS-XR support for 256 uSID blocks per node**—unblocking hyperscale SRv6 designs he had been advocating internally. Product feedback loop (field → engineering), not a customer booking.

---

### Web Encapsulations CRD — Mid 2023

Bruce asked **Bob Gisiger** to compile **Web/encapsulations CRD** requirements—connecting hyperscaler host-networking needs to engineering backlog.

---

### AI Factory & Cross-BU Alignment — 2024–2026

Bruce bridges **Silicon One / Cisco 8000**, **SONiC**, and **AI backend** engineering—translating hyperscaler co-development (Microsoft, Oracle, CoreWeave) into an internal narrative MIG and IMI can execute. He drove the internal conviction case that **SRv6-for-AI** (MRC, multi-tenancy, static pinning) was production-real—culminating in product direction others implement; customer revenue is documented under Business Impact, but the **internal** outcome was cross-BU prioritization of SONiC SRv6 and AI-fabric specs.

**Internal influence:**
- Field lead with **Clarence Filsfils** SR organization on company-wide SRv6 strategy (“network as IPv6 header,” application-controlled paths)—not single-feature testing
- **Phoenix Wing:** aligned Cisco engineering with multi-vendor SONiC uSID narrative (Alibaba, Microsoft)—internal open-NOS strategy shift
- Referenced at **IETF Vancouver 2024** as *“the 2030 guys”* (Ianik Semko, re: Bruce and Dan B.)—internal/external validation of horizon-3 positioning

**Vault:** `dse/04-Span-of-Influence-MOC.md`, `AI-Factory-Hub.md`, `Silicon-Hardware-Hub.md`

---

### Single OS (SOSIE) Working Group — 2024–2026

Bruce **co-founded SOSIE** with DSE peers **Brenden Buresh**, **Craig Hill**, **Virginia Teixeira**, and PSE **Rob Murphy**. The group produced recommendations to senior leadership on **multi-OS fragmentation risk**—Silicon One hardware convergence vs. divergent NX/XR/IOS-XE software stacks—and advocated a multi-year path toward a **Linux-based NOS** with hardware-accelerated packet apps and Cilium-class service control plane.

**Oct 2024 session** (Brendan, Dave, Chuck, Bruce): documented $500M Edgecore leakage, Aviz/OEM gaps, Hyperfabric strategy questions, and actions to obtain **Will Etherton OS-convergence report** and clarify SONiC ownership with Amy Gerrie.

**Forward look:** SOSIE reform driven by **Mythos/AI security patching** and vulnerability-surface reduction—Span story continues into 2026.

**Vault:** `innovation/SOSIE.md`, `dse/DSE General MOC.md` (co-founder note)

---

### Isovalent / Cilium — Host-Networking Strategy — 2021–2026

Bruce put **host-based networking** and **host-based SRv6** on Cisco’s internal map—advocacy from 2014–2015 CIPOLs intensified post-PSE on K8s/eBPF. He identified **Cilium** as a strategic inflection (2021+) and advocated **Isovalent acquisition** before it closed (2023)—bridging cloud-native CNI with SP-grade SRv6 transport for engineering and security BUs.

**Internal outcomes:**
- Security, DC, and SP teams now share a **common host-networking** vocabulary (air-gap, egress gateway, SRv6-in-Cilium roadmap)
- **Nov 2024:** Presented Isovalent to **Cisco AI tiger team**; developed **Isovalent SEVT lab** — field enablement → **10-se-community-leadership.md**
- **SD-WAN** and **SSE** engineering teams cite SRv6 as a **development differentiator** when requesting resources *(field observation, 2024–2025)*

**Cross-ref:** Innovation (Cilium SRv6 CRD, Thomas Graf LoR); Business (Bell host-based); Global (Adobe POC).

**Vault:** `04-span-of-influence.md` (candidate notes), `Isovalent-Cilium-Hub.md`, `technologies/Isovalent Runtime Security.md`

---

### Future Enterprise Segmentation Tiger Team — 2023–2024

Bruce participated in **Carnes/Gillies-sponsored Future Enterprise Segmentation** working group—Sprint 3 recommendations on reducing segmentation protocol sprawl (VXLAN vs. SRv6) and using **SGT as a normalized identity gate** across enterprise and cloud attributes (ABAC alignment).

**Span outcome:** Connected enterprise segmentation discourse to **SRv6 uSID + SGT** unified programming (16-bit alignment)—handoff to Innovation (CPOL) and cross-domain NaaS/Policy Plane discussions in MIG.

**Vault:** `technologies/fe-segmentation.md`, `innovation/SGT, SRv6, NaaS Notes.md`

---

### SD-WAN & SSE — SRv6 Beyond MIG — 2022–2026

Bruce extended SRv6 advocacy from SP/hyperscale into **Enterprise BE platforms**: SD-WAN and **Cisco Secure Access (SSE)** teams treat SRv6 as a roadmap differentiator for multi-domain policy and service steering—extending his Web/SP architecture into **non-MIG product lines**.

**Vault:** `04-Span-of-Influence-MOC.md` (candidate notes); patent thread: *SP Underlay Services for SDWAN* → Innovation

---

### SR Brain Trust — Clarence Filsfils & SR Engineering — 2020–2026

Bruce operates as a **field lead and innovation partner** to the SR organization—company-wide SRv6 direction, uSID simplification, and “applications control network experience” framing (echoed in Clarence’s 2024–2025 MRC+SRv6 public narrative). This is **internal strategy influence**, distinct from any single account win.

**Thru-line (exec overview only):** Relationship deepened pre-2020; **post–Aug 2020 impact** is PSE-era field leadership and product feedback loops.

---

### End-to-End SRv6 Platform Momentum — 2025–2026

After years of internal evangelization, Bruce’s Talent Assessment reflection (1HFY26) documents **company-wide investment momentum** for end-to-end SRv6 (including SRv6 + SGT): Cisco is investing or near-investing across **ISE, IOS-XE/Catalyst, Nexus, SONiC, SD-WAN, SASE, and Cilium**. This is **Span of Influence** outcome—BU prioritization aligned to field architecture—not a single account booking.

**Cilium-SP business case:** Bruce compiled worldwide account data estimating **~$34M Isovalent** and **~$323M MIG pullthrough** for Cilium-SP feature development `[verify]` → detail in **07-innovation.md**.

---

### SRv6 Book & External Publications — 2024

Bruce served as **editor for four chapters** of the upcoming SRv6 book (Clarence Filsfils and team) — 2HFY24 employee reflection. Industry-facing publication thread → **05-industry-impact.md**.

---

### PSE Review Committee — 2021–2024

Bruce served **three years** as PSE review subcommittee / **voting member**— shaping promotion standards for the next generation of technical sellers. **Mar–May 2024** cycle with **Mike McPhee**. Detailed mentoring outcomes → **SE Community Leadership**; committee service is **organizational span** here.

**Vault:** `dse/DSE General MOC.md` (Mar–May 2024 PSE committee sessions)

---

### Executive & Silicon Strategy Relationships — 2021–2023

Documented **VP-level recognition** (Eric Knipp, John Dorval, Patrick Morrissey) citing **>$1B influence** and foundational **Amazon Silicon One** engagement (Q1FY23 steering-committee context)—internal credibility for field-led horizon-3 bets.

**AWS silicon strategy:** Tracked and influenced generational TAM shifts (12.8T ↔ 25.6T) at steering level—Span (internal), revenue detail in Business Impact.

**Vault:** `dse/04-Span-of-Influence-MOC.md`

---

### Cross-Org Peer Network

Regular collaborators outside ASP+Web assignment orbit:

| Peer | Domain |
| :--- | :--- |
| **Brenden Buresh** | Cloud-native SRv6, Adobe/Cilium, SOSIE |
| **Craig Hill** | Routing, FE Segmentation, SOSIE |
| **David Jansen** | `[extend]` |
| **Brian Meaney** | `[extend]` |
| **Virginia Teixeira** | SOSIE, enterprise |
| **Mike McPhee** | PSE committee, STLDP |
| **Rob Murphy** | SONiC labs, SRv6 enablement, SOSIE |
| **Dan B.** | Host-based SRv6, “2030” architecture |

---

## Signature Internal Influence Themes

1. **Host networking air-gap** — control point moved to host; Cisco must participate in Linux/eBPF or cede policy/overlay to competitors.
2. **SRv6 uSID as network API** — one programming model across IOS-XE, NX-OS, SONiC, SD-WAN, host CNI.
3. **Open NOS / SONiC** — internal investment case for hyperscaler relevance (distinct from Phoenix Wing industry story).
4. **Policy Plane** — identity (SGT) + transport (SRv6) + observability (TEyes/OTel) as glue across BUs; gaining MIG traction per candidate notes `[verify with PM]`.
5. **Linux future NOS** — routing as hardware-accelerated apps; Cilium-class service control plane (SOSIE vision).

---

## Explicitly Excluded from This Section

| Item | Route to |
| :--- | :--- |
| Revenue tables, $17M Meta booking, Bell 500-unit order | **06-business-impact.md** |
| Geico, Adobe, Rakuten customer narratives | **03-global-impact.md** |
| srv6-labs, NANOG uSID, MPLS-WC (external visibility) | **05-industry-impact.md** |
| CPOL titles, patent counts, MRC emulator repo detail | **07-innovation.md** |
| CLEU lab scores, Nacho mentoring | **10-se-community-leadership.md** |
| IMI/MIG feature testing without cross-BU angle | Omit or one-line only |

---

## Vault Harvest Log — June 7, 2026

**Entry:** `dse/04-Span-of-Influence-MOC.md`  
**Also read:** `innovation/SOSIE.md`, `technologies/fe-segmentation.md`, `Isovalent-Cilium-Hub.md`, `dse/DSE General MOC.md`, `dse/09-Personal-Development-MOC.md`, candidate notes in prior `04-span-of-influence.md`

**Gaps / Bruce to add:**
- [ ] Named quotes or emails from SD-WAN/SSE PMs on SRv6 roadmap commitment
- [ ] Will Etherton report outcome (if shareable)
- [ ] Extend peer table (Jansen, Meaney, Gillies/Carnes cadence)
- [ ] Confirm Policy Plane traction with MIG PM (Carlos Pereira / OTel platform)
