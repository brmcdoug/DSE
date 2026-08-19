## Personal Development

> **Scope ([AGENTS.md](./AGENTS.md)):** Journey from **PSE (Aug 1, 2020) toward DSE**—growth that enabled broader span, global impact, innovation, and SE leadership.  
> **Not a cert list:** each item ties **learning → application → impact**, with detail in the linked sections.

**Suggested package length:** ~1 page body plus tables. Voice and claim-strength rules: [voice-guide.md](./voice-guide.md).

---

## Development Narrative — PSE to DSE

Bruce received direct feedback from the PSE review committee at promotion: expand beyond the Web and service provider comfort zone. He treated that as a work plan rather than a note.

Over the following six years he built capability and relationships deliberately outside the ASP+Web and MIG orbit — enterprise SD-WAN and Cisco Secure Access, the Future Enterprise Segmentation tiger team, co-founding the Single OS (SOSIE) working group with DSEs from Cisco Enterprise, Public Sector, Web/ASP, and EMEA, Isovalent and security engineering, ThousandEyes, the EMEA peer network, CX, the SL-OnDemand tiger team, and the OST Zurich university collaboration. Each is documented in Span of Influence; the point here is that none of it was assigned.

The second deliberate choice was technical rather than organizational. Rather than remaining a routing architect, Bruce invested in **production-grade builder skills** — Linux, Kubernetes, Cilium and eBPF, Containerlab, GitHub workflows, dCloud publishing, Python, Golang, and agent-assisted development. That is why the labs, emulators, and POC repositories in this package exist as running code that account teams and customer engineers reuse, rather than as slides. It is also why he can move at the speed the market does: the 8122 SRv6-on-SONiC work, the MRC emulator, and the Cilium POCs were all built without a dedicated engineering team.

That investment compounds in an unexpected place. Years of self-training in Python, Go, Kubernetes, DevOps practice, and Git have made Bruce markedly more effective with **agent-assisted development** — because he knows precisely what he is trying to build, he can describe it accurately and iterate with an agent as a development partner rather than hoping for a usable result. The engineers who get the most out of these tools are the ones who could have written the code themselves.

In **June 2026** Bruce transferred from Brook Crossman's ASP/Web organization, where he had spent roughly five years, to **Matt Gillies' Global Solutions Engineering team as lead Cloud-SP architect** — the same horizon-2 and horizon-3 mission at global scope.


**DSE mentor:** Vaughn Suazo, formally selected 2HFY25, meeting bi-weekly against defined deliverables. **Unofficial mentor:** David Jansen. **Managers:** Brook Crossman (ASP/Web through Jun 2026); Matt Gillies (Global, from Jun 2026).

---

## Development Areas and Actions Taken

Bruce's talent assessments identify two consistent development areas. Both are named here directly, with the actions taken against them.

**Executive communication.** Brook Crossman's 2HFY25 assessment called for stronger executive communications and more live SE engagements, and coached Bruce directly on upleveled messaging through 2HFY25 and 1HFY26. On Brook's recommendation Bruce worked through *Conversational Intelligence* (Jul 2025). He then applied it in volume: cross-BU workshops, the *Combatting Disaggregation* presentation to the full ASP organization, the April 2025 SRv6-for-AI workshop in front of MIG engineering leadership, and executive readouts including the EVPN Least Complexity presentation to Chief Product Officer Jeetu Patel. `[the PDP item "engage exec conversation coach/mentor" was recorded as in progress — confirm whether a formal external coach was engaged, or whether Brook's coaching and the DSE mentorship with Vaughn Suazo satisfied it]`

**Filtering demand and delegating for others' visibility.** The 1HFY26 assessment identified the consequence of being the person everyone calls: Bruce can work on filtering inbound requests and handing projects to others so they gain the exposure.

His response has taken a consistent shape — spot something good an engineer is already doing, then find them a stage for it:

- Saw **Dan Stacks'** AI tool and presented it to HQ Architecture Staff, giving Stacks the exposure rather than taking the slot himself
- Took **Santosh's** SONiC Nuggets idea, made it deliverable, and put Santosh's name on a visible programme — recruiting **John McCleod** as co-presenter, who was building SONiC skills for his own customer anyway
- Built the CLUS 2026 *Beyond the Switchport* breakout jointly with **Chris Lapp** so Lapp would have a Cisco Live breakout of his own
- Backed **Nico Michel's** interest in lab collaboration: handed him development of a Containerlab version of the SONiC Sales Edge training, and plans to have him extend `srv6-mrc-emulator` with a Containerlab UI and Edgeshark traffic-capture tooling. Michel won **Distinguished Speaker at CLEU 2026** co-presenting Bruce's lab

This remains active work rather than a closed item, but the mechanism is now deliberate rather than incidental.

---

## Talent Assessment Development Arc *(Brook Crossman, manager)*

| Period | Development highlights | Manager development notes |
| :--- | :--- | :--- |
| **2HFY24** | Geico first SONiC/C8000 order (~$1.6M); SRv6-SGT and Yukon++ with Josh Merrill; Isovalent overview to global PSE/DSE | Working toward next step; needs a **foundational DSE-linked project** with business metrics |
| **1HFY25** | Top 3–4 SONiC and Cilium SME; AI/ML fabric and K8s/CNI depth; Enterprise+SP SRv6+SGT; official PSE mentor to Nacho; extended-team support for Marina Ferreira and Masi Mohammed | **Adopt longer-term mentees** on the road to DSE |
| **2HFY25** | Vaughn Suazo engaged as DSE mentor; Adobe Cilium EGW POC rescue; owned the April BE/Sales SRv6 workshop; `srctl` and Jalapeno AI load-balancing tooling | **Executive communications**; more live SE engagements |
| **1HFY26** | 2025 Pinnacle Award; Cilium-SP business case ($34M Isovalent / $323M MIG); MIG G200 SRv6 Q1'26 commitment | Aligned on goals; **filter inbound requests**; delegate projects for others' visibility. Innovation pace **"on pace to break (ASP) records"** |
| **2HFY26** | — | `[Brook — manager section pending cycle close]` |

**Source:** `./talent-assessment/` PDFs.

---

## Education and Certifications

| Credential | Date | Relevance and application |
| :--- | :--- | :--- |
| **BA**, University of Washington | 1996 | Undergraduate foundation |
| **CCIE Service Provider #35169** | 2012 | Foundation for SR/SRv6 field leadership; peer credibility with SP and hyperscaler operators |
| **O'Reilly — *Open Source Labbing*** (co-developed with Russ White, Akamai) | 2024–2025 | Four-hour course delivered live twice; both sessions in the O'Reilly catalog; materials at [github.com/brmcdoug/open-source-labbing](https://github.com/brmcdoug/open-source-labbing). Co-authorship with one of the industry's most recognized networking authors → **Industry Impact** `[verify catalog link]` |
| **Executive communication development** | 2HFY25 – present | Direct coaching from Brook Crossman on upleveled messaging; applied in cross-BU workshops and executive readouts `[confirm formal coaching engagement]` |
| **Conversational Intelligence** | Completed Jul 2025 | Communication method for multi-BU persuasion work |

---

## Skill Development — Learning to Impact

| Period | Development | Application → impact |
| :--- | :--- | :--- |
| **2026** | Agent-assisted coding; **MRC** study, labs, and emulator (superseded the Ultra Ethernet plan when the industry moved) | MRC emulator and srv6-msft repos → **Innovation**, **Industry Impact** |
| **2025–2026** | Deep **Cilium and eBPF** hands-on | Adobe egress gateway POC rescue → **Global Impact**; host networking across BUs → **Span** |
| **2024–2025** | **SONiC** depth ahead of mainstream field adoption; dCloud lab publication | SONiC SME on Microsoft, CoreWeave, Geico → **Business** and **Global Impact** |
| **2023–2024** | **Containerlab** early adoption; GitHub-first lab guides | srv6-labs launch; CLEU 5.0 Distinguished Speaker → **Leadership** |
| **2021–2023** | **Kubernetes** and the cloud-native stack; Jalapeno open-source maintenance | Bold Bets; EN Hackathon win → **Innovation** |
| **2020–2022** | Cross-BU exposure: SD-WAN, SSE, FE Segmentation, PSE committee | SRv6 on enterprise platforms; promotion standards → **Span of Influence** |

---

## Personal Development Plan (Jul 2025) — Status

| Action | Due | Status |
| :--- | :--- | :--- |
| Engage executive conversation coach or mentor | Mar 2026 | **In progress** — Brook Crossman coached directly on upleveled messaging (2HFY25–1HFY26); *Conversational Intelligence* completed Jul 2025; DSE mentorship with Vaughn Suazo ongoing `[confirm whether a formal external coach was engaged]` |
| Fork Cilium; POC SRv6 feature | Oct 2025 | **Complete** — Adobe EGW/LB POC |
| MRC study and customer enablement *(replaced Ultra Ethernet)* | Aug 2025 | **Complete** — presentation, lab, emulator, SE and customer enablement |
| Read *Conversational Intelligence* | Jul 2025 | **Complete** |
| Deliver 2 Stay Ready Friday sessions | Sep 2025 | **Complete** — Cisco Live SRv6 lab, Jul and Nov 2025 |
| Mentor Ignacio ("Nacho") Sanchez to PSE | Jul 2026 | **Complete — promoted Jun 2026** |
| Cilium EGW/LB at Adobe | Oct 2025 | **Complete** — testimonial pending |
| Digital Realty Cilium/SRv6 and Akamai SRv6 controller POC | Dec 2025 | **Partial** — DLR POC lab stood up; Akamai redirect-to-scrubber controller built; production status open |
| Non–Cisco Live conference delivery | Jul 2026 | **In progress** — MPLS-WC and operator workshops delivered; OCP 2026 planned |
| Optimize Jalapeno codebase | Jul 2026 | **In progress** |
| SRv6 deployment at a hyperscaler | Jul 2026 | **In progress** — Microsoft and Oracle have initial deployments **on competitor hardware**, validating the architecture while Cisco was late to market. Cisco 8122 SONiC SRv6 shipped Jun 2026; FY2027 TAM recovery `[pending finance]` |

**Risk identified in the original plan:** Cisco execution on software and hardware roadmaps — mitigated by the open-source lab strategy and direct customer co-development, both of which proved out.

---

## Vibe-Labbing — The Builder Mindset

Bruce describes his current working model as **vibe-labbing**: agent-assisted tooling to compress lab and demo cycles while holding architectural rigor through Containerlab, GitHub Actions, and reproducible topologies. He characterized AI tooling as a "brain-extender" in the 1HFY26 assessment.

This is not adjacent to the impact in this package — it is the mechanism. It is how a field systems engineer with no engineering team ships POC repositories ahead of feature availability, and why grade-12 SEs and customer engineers can run the same environments in hours rather than quarters.

---

## How Development Enabled Each Criterion

| DSE criterion | Development enabler |
| :--- | :--- |
| **Business Impact** | SONiC and SRv6 builder skills applied at Microsoft, Meta, Oracle, CoreWeave |
| **Global Impact** | EMEA and APJC peer relationships; enterprise and SD-WAN depth for Geico, Adobe, and Fiserv-class accounts |
| **Span of Influence** | SOSIE, FE Segmentation, Isovalent engineering literacy, PSE committee service |
| **Industry Impact** | GitHub open-source curation; conference speaking; O'Reilly course with Russ White |
| **Innovation** | Cilium fork and POC path; Jalapeno; sustained CPOL pipeline |
| **Leadership** | dCloud and Cisco Live lab authorship; six PSE promotions mentored or advised |
| **Personal Development** | Executive communication program; continuous cross-domain learning |

---

## Open Items

- [ ] **Brook / Matt** — 2HFY26 talent assessment manager section when the cycle closes
- [ ] Akamai SRv6 controller POC — production status with account team
- [ ] Adobe / Dan Stacks testimonial
- [ ] O'Reilly catalog link and exact course title
- [ ] OCP 2026 delivery confirmation

**Vault:** `dse/09-Personal-Development-MOC.md`, `dse/DSE General MOC.md`. **Last body pass:** Aug 2026 — rewritten to [voice-guide.md](./voice-guide.md) register; development areas stated directly with actions taken.
