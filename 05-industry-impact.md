## Industry Impact

> **Scope ([AGENTS.md](./AGENTS.md)):** Leadership and visibility **outside Cisco** among operators, architects, open-source communities, and standards-adjacent forums since **August 1, 2020**. **Direct revenue not required.**  
> **Cross-ref:** Same artifact drove account $ → **06-business-impact.md** / **03-global-impact.md**. Internal BU persuasion (SONiC investment inside Cisco) → **04-span-of-influence.md**. Patents/CPOL detail → **07-innovation.md**. CL **ILT scores and SE training delivery** → **10-se-community-leadership.md**.

**Suggested package length:** 2–3 pages (body). Third-person, most-recent-first.

---

## Industry Impact — Thematic Arc

Bruce’s industry impact is less a single deliverable than a ** sustained advocacy arc** (post–Aug 2020): host-based and hyper-distributed SRv6, cloud-like consumption of network services, open NOS (SONiC), and endpoint-directed paths—now converging with **MRC+SRv6** in tier-1 AI infrastructure. Public artifacts (GitHub, blogs, conferences) give operators and vendors reusable models independent of any one Cisco account team.

| Era | Industry-facing theme | Representative artifacts |
| :--- | :--- | :--- |
| **2020–2022** | SRv6 uSID simplification; programmability as API | IETF/community recognition; SR-Apps field lead |
| **2023** | Open, reproducible SRv6 labs; SONiC uSID narrative | **srv6-labs** launch; segment-routing.net; MPLS-WC |
| **2024–2025** | Host networking + eBPF; multi-vendor SONiC | Phoenix Wing alignment; CLEU/CLUS breakouts & panels |
| **2025–2026** | SRv6 for AI; MRC; multi-tenant fabrics | OCP abstract; operator roadshow; MRC industry papers |

*Optional package graphic:* timeline from “host-networking CIPOL (2015, exec thru-line only)” → MRC whitepaper (2024–2026 industry validation).

---

## Industry Impact — Draft Package Body

---

### OCP Summit — SRv6 Multi-Tenant AI Fabric — 2026 (planned)

Bruce prepared session abstract for **OCP Summit 2026** (co-present with Microsoft, per account notes)—public industry forum for **SRv6 uSID multi-tenancy** (network-, host-, hybrid encap/decap), two-dimensional ACL enforcement, and extension to multi-planar **MRC** workloads.

**Artifact:** `conferences/OCP 2026.md`; design spec → Innovation cross-ref.

---

### MRC + SRv6 — Industry Specification Alignment — 2024–2026

Industry titans (OpenAI, Microsoft, NVIDIA, AMD, Broadcom) published **Multipath Reliable Connection (MRC)** using **SRv6 static routing**—validating Bruce’s long-running host-networking and elephant-flow / AI-fabric framing. Oracle Acceleron public materials (2026) cite the same pattern. Bruce’s **[srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator)** gives operators and architects a teaching implementation.

**Industry quote (internal validation of external direction):** Ianik Semko, IETF Vancouver 2024 — *“I call you the 2030 guys”* (Bruce and Dan B.).

**Links:** [OpenAI MRC+SRv6 PDF](https://cdn.openai.com/pdf/resilient-ai-supercomputer-networking-using-mrc-and-srv6.pdf); [Cisco MRC+SRv6 blog](https://blogs.cisco.com/datacenter/mrc-and-srv6-how-foundational-networking-innovations-are-enabling-the-next-generation-of-ai-supercomputers)

---

### SRv6 Operator Roadshow & Pinnacle SE Workshop — Dec 2025

Bruce supported **SRv6 operator workshop** planning (Austin, late Feb–early Mar style)—50% customer / 50% Cisco content across hyperscale, enterprise, public sector, SP segments; plus **Pinnacle-aligned SE enablement workshop** (platforms, gaps, objections, competition). Industry impact: scales SRv6 adoption narrative to **multi-segment operators**, not ASP accounts alone.

**Vault:** `customers/SRv6 Roadshow Dec 2025.md`

---

### Cisco Live — Industry-Facing Thought Leadership — 2023–2026

Bruce delivers breakouts, panels, and labs consumed by **global practitioners** (not only Cisco SEs):

| Event | Session / role | Scores / notes |
| :--- | :--- | :--- |
| **CLEU 2026** | LTRSPG-2212 ILT; MTE NB SRv6 | 4.94 session / personal; MTE inspired operator SRv6 migration |
| **CLEU 2025** | LTRSPG-2212 ILT; MTE w/ Tejas Lad | 4.72 / 4.94; overflow lab; Iliad/Bechtel Cilium-SRv6 interest |
| **CLEU 2024** | LTRSPG-2212 | 4.88 / 4.94 |
| **CLEU 2023** | LTRSPG-2212 | **5.00 / 5.00 — Distinguished Speaker** |
| **CLUS 2026** | BTSP panel; lab; panel w/ Vaughn, Rob, Nico, Masi, Chris Lapp | Panel **5.0** session/presentation/SME |
| **CLUS 2025** | IBOSPG-2013 panel; LTRMSI-3000 | Panel **5.00 / 5.00** |
| **CLUS 2026** | “Beyond the Switchport” (w/ Chris Lapp) | Host-networking industry narrative |

**Split:** Detailed ILT enablement metrics → **SE Community Leadership**; **industry visibility** and operator attendance documented here.

**Vault:** `conferences/CLEU 2023.md` through `CLEU 2026.md`, `CLUS 2025.md`, `CLUS 2026.md`, `CLUS 2026 Beyond the Switchport.md`

---

### segmentrouting / srv6-labs — Open Source Community — Dec 2023–present

Bruce is **admin/curator** of [github.com/segmentrouting](https://github.com/segmentrouting) and launched **[srv6-labs](https://github.com/segmentrouting/srv6-labs)** (Dec 2023)—Containerlab topologies, starter and use-case labs adopted globally.

**Reach metrics `[verify current]`:**
- LinkedIn announcement: ~**40K** views in first week; **37,822** views, 267 reactions, 13 reposts (as of Jan 2024, per vault)
- **ipspace.net** “worth reading” mention: [blog.ipspace.net/2023/12/worth-reading-srv6-labs.html](https://blog.ipspace.net/2023/12/worth-reading-srv6-labs.html)
- Engineers at **Verizon**, **Oracle**, and others extended/contributed (vault notes)
- GitHub traffic snapshot (Feb 2025): 333 views / 46 unique visitors on srv6-labs repo; referrers include segment-routing.net, Google, ipspace

**Related repos (industry + customer co-dev):** [srv6-msft](https://github.com/segmentrouting/srv6-msft), [srv6-oci](https://github.com/segmentrouting/srv6-oci), [srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator), [polarfly](https://github.com/segmentrouting/polarfly)

**Vault:** `GitHub-MOC.md`, `dse/GithubJalapenoLinkedIn - stats.md`, `05-industry-impact.md` (candidate notes)

---

### Phoenix Wing & SRv6 uSID on SONiC — 2023–2025

Bruce contributed to industry narrative for **multi-vendor SRv6 uSID on SONiC** (Cisco, Alibaba, Microsoft—**Phoenix Wing**). Public write-up:

- [segment-routing.net — SRv6 uSID on SONiC](https://www.segment-routing.net/blogs/srv6-usid-on-sonic/)
- Pablo Camarillo LinkedIn amplification (vault reference)

**Industry impact:** Positions open NOS + uSID as cross-vendor pattern—not Cisco-proprietary MPLS/SR-MPLS alone.

**Vault:** `dse/05-Industry-Impact-MOC.md` (wikilink `2023 sonic-blog-alibaba_msft` — **broken in vault; restore link**)

---

### MPLS World Congress — Operator Community — 2023

Bruce participated in **MPLS World Congress 2023**—keynote/operator-track visibility; background collaborator on **customer presentations** (Verizon, Bell, Rakuten cited in development notes). CLEU 2025 diary: SR engineering encouraged Bruce to join **lead operators workshop** at MPLS-WC with Microsoft/OCI peers.

**Vault:** `dse/05-Industry-Impact-MOC.md`, `dse/DSE General MOC.md` (Apr 2023 MPLS-WC; Apr 2024 VZ presentation)

---

### Publications & Blogs — 2020–2026

| Channel | Examples | Audience |
| :--- | :--- | :--- |
| **segment-routing.net** | SRv6 uSID on SONiC; SRv6 lab content | Global SR/SRv6 practitioners |
| **SP360 / Cisco SP blogs** | Evolved connectivity; ML/AI in SP networking (SEVT-era) | SP architects |
| **LinkedIn** | srv6-labs launch; technical architecture posts | Global neteng community |
| **ipspace / automation community** | srv6-labs citation; Jalapeno on [Steinzi automation landscape](https://steinzi.com/network-automation-landscape/) | Net automation engineers |

**Vault:** `dse/06-Business-Impact-MOC.md` (two SP360 + one segment-routing.net blog, Jan 2024 dev discussion); `10-se-community-leadership.md` (SEVT blog URLs)

---

### Jalapeno — Open Source Network Automation — 2021–present

**[cisco-open/jalapeno](https://github.com/cisco-open/jalapeno)** — field-initiated project, legally open-sourced; listed on industry automation landscape maps; **jalapeno-bmp-demo** referenced for MPLS-WC 2026 community (Fred C / Severin Dellsperger thread).

**Industry role:** Reference architecture for programmable multi-domain services—used in teaching and community demos, not only Cisco internal labs.

**Vault:** `GitHub-MOC.md`, `dse/GithubJalapenoLinkedIn - stats.md`

---

### IETF & Standards-Adjacent Participation — 2020–2026

- **IETF Vancouver 2024:** “2030 guys” recognition (Semko)—host-based SRv6, endpoint service consumption
- **IETF SRv6-Ops:** Verizon Nick presenting host-based SRv6 requirements (Bruce collaboration thread, Oct 2025 vault)
- **Editor/contributor:** SRv6 book — **four chapters edited** (Clarence Filsfils and team; 2HFY24 Talent Assessment); topics include Service Programming, SR-Aware/Unaware Services (Dec 2023 notes)—industry education artifact
- **CNRS / SR-Apps:** Field lead for university partnerships (OST Zurich, etc.)—pipeline of operator-relevant research

**Pre–Aug 2020 (exec thru-line only):** NANOG first public **uSID** presentation (2020)—do not expand as body case study.

**Vault:** `07-innovation.md`, `customers/Verizon.md`, `dse/DSE General MOC.md`

---

### Host-Based Networking — Industry Narrative — 2020–present

Bruce coined and evangelized **“host networking air-gap”** and **host-based SRv6** externally and with operators—now reflected in:
- MRC+SRv6 industry specs (NIC-controlled paths)
- Cilium/eBPF SRv6 community work (Boost, Bell direction, Adobe POC—customer detail elsewhere)
- CL session **“Beyond the Switchport”** (kernel → CNI → eBPF → smartNIC horizon)

**Quote (Bob Gisiger, May 2026):** *“this is super cool, it's your vision for years of host based SRv6 coming to life in a big way…”* — internal echo of industry direction.

**Vault:** `evidence-summaries/quotes.md`, `04-span-of-influence.md` themes

---

## Summary Table — External Artifacts

| Artifact | Type | Industry reach |
| :--- | :--- | :--- |
| [segmentrouting/srv6-labs](https://github.com/segmentrouting/srv6-labs) | Open source | Global neteng; ipspace citation |
| [segment-routing.net SONiC uSID blog](https://www.segment-routing.net/blogs/srv6-usid-on-sonic/) | Publication | Multi-vendor SONiC narrative |
| [cisco-open/jalapeno](https://github.com/cisco-open/jalapeno) | Open source | Automation landscape listings |
| [srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator) | Open source | MRC+SRv6 teaching |
| MPLS-WC 2023 | Conference | Operator + SP community |
| OCP 2026 (planned) | Conference | Hyperscale AI fabric audience |
| CLEU/CLUS panels & breakouts | Conference | Practitioner scores 4.64–5.0 |
| MRC / Acceleron public docs | Industry spec | Tier-1 AI infrastructure |

---

## Explicitly Excluded from This Section

| Item | Route to |
| :--- | :--- |
| Meta $17M, Microsoft pipeline $ | **06-business-impact.md** |
| Geico, Adobe customer wins | **03-global-impact.md** |
| Isovalent acquisition internal advocacy | **04-span-of-influence.md** |
| CPOL patent table | **07-innovation.md** |
| ILT prep, Stay Ready Friday, Nacho mentoring | **10-se-community-leadership.md** |
| PSE committee service | **04-span-of-influence.md** (primary) |

---

## Vault Harvest Log — June 7, 2026

**Entry:** `dse/05-Industry-Impact-MOC.md`  
**Also read:** `GitHub-MOC.md`, `dse/GithubJalapenoLinkedIn - stats.md`, `conferences/CLEU 2023–2026`, `CLUS 2025–2026`, `OCP 2026.md`, `customers/SRv6 Roadshow Dec 2025.md`, `evidence-summaries/quotes.md`

**Gaps / Bruce to add:**
- [ ] Refresh srv6-labs LinkedIn/GitHub metrics for 2026
- [ ] NANOG/OCP confirmed acceptance dates and URLs
- [ ] Restore/fix `2023 sonic-blog-alibaba_msft` wikilink in vault
- [ ] MPLS-WC 2023 session titles / keynote confirmation
- [ ] Optional timeline graphic for final PDF
