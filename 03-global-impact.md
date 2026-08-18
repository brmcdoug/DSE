## Global Impact

> **Official criteria (DSE nomination PPT):**
> - *Demonstrate global impact outside the immediate area*
> - *Examples include leading global accounts, creating and delivering global training, developing new architectures that are adopted globally*
>
> **Official guidance (DSE nomination Word guide):** *"Provide a high-level summary of how your impact moved from regional / theater to global, using a bulleted list or a table to show the transition. A detailed version of the global impact can be added to the appropriate section of the package (business impact, innovation, SE leadership etc.). Chronological format with most recent global impact first."*

**Structure:** per the guidance above and Brenden Buresh's package, this section is a **summary that points to detail elsewhere**, in two-column table form. Official suggested length is **2–3 pages**. Named customer engagements — including out-of-territory Americas enterprise accounts — are detailed in **[06-business-impact.md](./06-business-impact.md)**. Voice and claim-strength rules: [voice-guide.md](./voice-guide.md).

---

## How Bruce's Impact Moved from Regional to Global

| Period | Scope of impact | Evidence |
| :--- | :--- | :--- |
| **2008–2014** | Account, then Americas region | SP routing, Carrier Ethernet, and Unified MPLS across US service provider accounts |
| **2015–2020** | Americas Web / hyperscale segment | Hyperscale production networks; first public NANOG presentation of SRv6 uSID |
| **2020–2023** | Cross-theater technology lead | **Global field lead for SR-Apps**; `github.com/segmentrouting`; global SRv6 workshops; APJC and EMEA operator support |
| **2023–2025** | Global architecture and product direction | SONiC investment case; Isovalent acquisition advocacy; SRv6+SGT across business entities; IETF draft editor; four SRv6 book chapters |
| **2025–2026** | Global role | **Lead Cloud-SP architect, Global Solutions Engineering** (Matt Gillies, from Jun 2026); Pinnacle Award for SRv6 uSID market impact; WMP-PolarFly paper |

---

## Global Initiatives

| Initiative and date | Impact |
| :--- | :--- |
| **Global field lead, SR-Apps** — 2020 – present | Bruce is Cisco's global field lead for SR-Apps, co-developing with Clarence Filsfils' Segment Routing engineering organization. The work put an application layer on Segment Routing and shaped IPM, path tracing, the NaaS direction, and host-based SRv6 extensibility — deliberately landing in the platform rather than behind a licence. SR engineering subsequently adopted his open-source Jalapeno project as the SR-Apps platform. He also built and maintains the university research channel (CNRS; OST Zurich with Professor Laurent Metzger), which produced the Hawkv6 distributed controller. *More details are located in the Innovation section of this document.* |
| **End-to-end SRv6, including host-based and cloud-native** — 2015 – present | Bruce identified that hyperscale operators had moved the network control point into the host, named the resulting gap the **host-networking air-gap**, and spent a decade arguing that Cisco needed a credible presence there. The architecture he advocated — SRv6 extended past the last-hop router to the host, the endpoint, and the application — is now Cisco's direction across IOS-XR, IOS-XE, NX-OS, SONiC, SD-WAN, and Cilium, has been adopted by operators on four continents, and underpins the MRC-plus-SRv6 convergence in AI infrastructure. *More details are located in the Innovation and Industry Impact sections of this document.* |
| **Architectures adopted globally — open NOS and SONiC** — 2023 – present | Bruce published the first public description and demonstration of SRv6 uSID on SONiC (May 2023), drove the internal investment case against sustained engineering scepticism, secured MIG's commitment for SRv6-on-SONiC G200 in Q1 FY26, and led the Americas PA/DA SONiC forum that built field-architect consensus on open-NOS strategy. **SRv6 on SONiC shipped for the Cisco 8122 in June 2026.** Global SONiC run rate `[pending]`. Sustained engineering relationships with **Vijay Tapaskar** and **Mani Veerachamy** (SONiC on Cisco 8000) and Cisco Fellow **Praveen Bhagwatula**. *More details are located in the Innovation section of this document.* |
| **Architectures adopted globally — host networking and Cilium** — 2021 – present | Bruce identified Cilium and eBPF as a strategic control point and advocated that Cisco acquire Isovalent from 2021, three years before the acquisition closed. Post-acquisition he built the Cilium-SP feature investment case — **~$34M Isovalent and ~$323M MIG pullthrough** — and authored the multi-use-case Cilium customer requirements document, accepted by Cisco engineering, positioning Cilium as the host-networking policy execution engine for Kubernetes and non-Kubernetes workloads alike. Deployed or in POC at Bell Canada, Boost Mobile, Adobe, Digital Realty, NSight, and T-Mobile. **Thomas Graf**, Cilium co-creator and Isovalent founder, can attest. *More details are located in the Innovation and Span of Influence sections of this document.* |
| **SP Network-as-a-Service as an architectural solution** — 2021 – present | Bruce's May 2022 SP360 publication introduced **cloud-like consumption of network services**, framing that predated the industry NaaS movement of 2024–2025 by two to three years. He carried it into Project Yukon at Verizon and AT&T, the SRv6 SD-WAN underlay design at Rakuten, and the Bell Canada NaaS architecture that produced a 500-unit first order for Bell's initial NaaS deployment. *More details are located in the Business Impact section of this document.* |
| **SRv6 with SGT — unified identity and policy** — 2022 – present | Working the Future Enterprise Segmentation tiger team, Bruce recognized that a Security Group Tag and an SRv6 uSID are both 16 bits, so an SGT fits as a trailing argument after locator and function — extending the network programming model to *Locator : Function : SGT*. The architecture spans ISE, SASE, SD-WAN, and MIG transport; **by December 2025 the ISE organization had committed** to SRv6 SGT and a unified policy model. *More details are located in the Innovation and Span of Influence sections of this document.* |
| **Chassis to pizza-box fabrics** — 2017 – present | Bruce articulated the hyperscaler shift toward building fabrics from fixed-form-factor routers — the *Fabrics and Planes* framing — which fed SP Compass Designs and Cisco's decision to release the 8000 initially as a fixed-chassis platform. Tim Carnes, then VP Worldwide Systems Engineering: *"His 'fabric architectures' concepts helped jumpstart the Compass Design effort and led to BU prioritization of pizzabox platforms from both the Fretta and Spitfire product lines."* The same shift is now visible at Microsoft as Project Octans. Industry fixed-versus-modular crossover year `[pending — Dell'Oro / Omdia via MIG or Competitive Intelligence]`. *More details are located in the Business Impact section of this document.* |
| **Global training and enablement** — 2020 – present | Bruce delivers SRv6, SONiC, and cloud-native enablement across all three theaters: Tech Elevate sessions in NA, EMEA, and APJC; the December 2025 SRv6 operator roadshow and companion SE enablement workshop; SRv6 DC/AI workshops drawing ~80 attendees across Sales and BU; and the public `srv6-labs` and dCloud assets used by Cisco SEs and customer engineers worldwide. His Cilium dCloud lab prompted an EMEA systems engineer to build a demonstration that reached the Cisco booth at MPLS World Congress, after which that engineer contributed production code to the Cilium project. *More details are located in the SE Community Leadership section of this document.* |
| **Cross-theater operator engagements** — 2024 – present | Bruce serves as architecture consultant to operators outside the Americas where local SRv6 and cloud-native depth does not exist: **Evroc** (EMEA sovereign cloud — SONiC spine and leaf, Cilium, inter-site design without Layer 2 stretch), **Rakuten** (APJC — SRv6 SD-WAN underlay high-level design and the Unified SRv6 Fabric case), **NTT East** (APJC — SRv6 and Cilium consultation across two Cisco Live engagements), and **MTN Nigeria** and **DU UAE**, where topology and migration designs delivered through APJC systems engineer Sanjay Nanda produced approximately **$85,000 in avoided customer lab expenditure** and a **2,300-node SRv6 POC** — two national operators on two continents, for customers Bruce never met. `[verify figures with Sanjay Nanda]` *More details are located in the Business Impact section of this document.* |
| **Systems integrator enablement — WWT** — 2026 | Bruce delivers SRv6, SONiC, and Cilium enablement workshops to World Wide Technology with Dave Clough. Capability built at one of Cisco's largest integration partners propagates across that partner's entire customer base rather than a single account. `[verify scope; LoR candidate]` |

---

## Global Product and Technology Run Rate

> **Attribution discipline.** Bruce does not own these product lines and this section does not claim their revenue. Each initiative above states a specific dated intervention; the figures below establish **the scale at which that intervention operated**. Figures are `[pending]` until sourced from finance or the relevant product team.

| Technology area | Global run rate | Source |
| :--- | :--- | :--- |
| Segment Routing / SRv6 | `[pending]` | Finance or SR product team |
| Cisco 8000 | `[pending]` | MIG |
| SONiC | `[pending]` | SONiC product team |
| Cilium / Isovalent since acquisition | `[pending]` | Isovalent / Security BE |
| **Cilium-SP pullthrough** *(validated)* | **~$34M Isovalent / ~$323M MIG** | Bruce's business case |
| NaaS-attributed SP pipeline | `[pending]` | — |

**Cisco's own attribution.** Cisco awarded a **2025 Pinnacle Award to the SRv6 uSID team** for the technology's global market impact, presented at the ceremony in early 2026. The team numbered roughly 40 and was almost entirely Cisco engineering; **Bruce and DSE Craig Hill were the only two recipients from the sales organization.**

---

## Open Items

- [ ] Global run-rate figures per the table above — and confirm which product and engineering leaders will **attest in writing**. Filsfils, Wollenweber, Graf, Tapaskar, Veerachamy, and Bhagwatula are all sponsorship candidates; an attestation sentence in a letter is worth more than any figure
- [ ] **Fixed vs. modular market data** — Dell'Oro / Omdia, SP routing and DC switching, back to ~2017 so the crossover year is visible. Use it to date the inflection against Bruce's 2017–2018 framing, not to claim revenue share
- [ ] **MTN Nigeria ~$85K / DU 2,300-node** — confirm with Sanjay Nanda
- [ ] **Evroc** — revenue or committed pipeline
- [ ] **WWT** — scope and LoR
- [ ] Add the **DSE nomination PPT and Word guide** to `reference/` so scope questions are citable rather than remembered

**Restructured Aug 17, 2026** to the official criteria and the two-column summary format. Named customer engagements previously held here — Geico, Honeywell, Adobe, Fiserv, Texas Instruments, Province of New Brunswick, NYU and Carnegie Mellon, Disney, Visa, The Trade Desk, Morgan Stanley, NSight — moved to [06-business-impact.md](./06-business-impact.md) under out-of-territory engagements.
