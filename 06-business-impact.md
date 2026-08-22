## Business Impact

## Business Impact Model — Co-Development, Mindshare, and Relationships

Bruce's business impact follows a repeatable pattern: train SE teams and customer engineers on architectures and products before they need them, build the POC labs and simulations that make those architectures testable (SONiC, SRv6, SL-API, host networking), then co-develop with hyperscalers and tier-1 SPs until the pipeline matures. Account notes describe this as multiyear partnership rather than a transactional sales cycle.

Bruce works directly with customers throughout, and he multiplies: because account teams get the architecture, the education, and the working code up front, they can carry the engagement without needing him in the room. A significant share of the revenue below was closed that way. The pattern originates at Microsoft and repeats at Meta, Google, and CoreWeave.

**Web culture influence:** Bruce aligned Cisco's Web selling motion with hyperscaler-style thinking — open NOS, disaggregation, Linux tool-chains, and API-driven forwarding — which underpins the strategic investments in SONiC and Silicon One behind multiple accounts below.

---

## Revenue Context

Supporting materials for every engagement below are collected in the [DSE nomination SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).

Bruce's assigned Americas Web/Hyperscale theater booked **$10.9B from 2022 to 2026**, itemized by customer in the Business Impact Summary of the Executive Overview. Those are org-level figures. Each account entry below leads with the revenue that falls within Bruce's own engagement scope, which is the narrower and more meaningful number.

---

### Microsoft, 2021 – Present

**Revenue within Bruce's engagement scope, since 2021:** Cisco 8000 AI/DC revenue **$1.744B** `[Bruce to confirm attribution with account team]`; WAN revenue **$306.4M**. Segment bookings for the account over 2022–2026 were $3.97B.

Microsoft operates Azure, one of the two largest public cloud platforms in the world, and is Cisco's single largest Web/Hyperscale customer by bookings. Its AI infrastructure program spans a continent-scale super-factory WAN linking Fairwater DC sites in Wisconsin and Georgia, backbone growth from ~1,800 toward ~3,000 nodes, and a data center estate being re-architected around disaggregated hardware and open network operating systems. Bruce has served as architect and advisor across Microsoft's Frontend DC, WAN/Metro/DCI, SONiC, SRv6, and AI-backend programs since 2021, working directly with Microsoft's network engineering leadership while account SEs drive production engagements. This account carries the pattern that recurs across the rest of this section: Bruce equips the field and the customer with thought leadership, architecture, education, and labs, and the revenue is realized by others running with it.

**SRv6 for the AI Backend and SONiC on the Cisco 8122:** Beginning in 2024, Bruce argued inside Cisco that SRv6 for the AI backend was a production requirement rather than a research topic. Cisco engineering was skeptical, and the investment case for SRv6 on SONiC was not initially funded. Bruce built the technical and customer evidence that changed that position and led to Cisco support in 2026. Bruce's involvement and accomplishments include:

- Authored the SRv6 uSID multi-tenant AI fabric specification, which became the reference architecture for both the Microsoft and Oracle AI-backend engagements `[todo - upload a copy of the paper to Bruce's DSE onedrive folder and link here]`
- Built the `srv6-msft` POC repository, shared privately with Microsoft's architects, and the public [srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator); Microsoft engineers used both in their own internal executive presentations
- Built the first SRv6-for-AI elephant-flow path-pinning demonstration (Nov 2024) as an internal proof point ahead of customer-scale POCs, later developed further and used in the Cisco Live SRv6 lab
- Delivered SONiC training to Microsoft account SEs from 2024 forward, enabling the account team to scale its engagement across Microsoft's expanding SONiC use cases
- Secured MIG commitment for SRv6 on Cisco 8000 SONiC platforms in Q1 FY26, unblocking the Microsoft and Oracle testing paths and delivering **SRv6 on SONiC for Cisco 8000 platforms across G-series and P-series silicon** (June 2026, 202511 codebase) as the direct product outcome

The architecture was validated; unfortunately the timing was not. Cisco has been late to market across successive switch-silicon generations — 12.8T, 25.6T, and 51.2T — and considering the speed at which the hyperscale market is currently moving, it often removes Cisco from consideration entirely. Microsoft and Oracle had both begun SRv6-for-AI deployments on competitor hardware before Cisco shipped, on the architecture Bruce had specified. The recurring pattern is the strategic argument: articulating the superior architecture does not recover the opportunity if the silicon is not there to carry it. FY2027 TAM recovery projection on G300 102.4T silicon: `[pending finance validation]`.

**PhyNet, disaggregated T2 and Regional Hubs:** Bruce is a primary Cisco SME on Microsoft's Frontend DC (PhyNet) and DCI/Metro (Regional Network Gateway or RNG), and on Microsoft's initiatives to disaggregate their chassis-based T2/Spine and DCI fabric layers into upper and lower pizza-box Clos tiers. Bruce's involvement and accomplishments include:

- Designed SRv6 tunnel-mesh architecture between disaggregated Regional Hubs, covering Ti-LFA, micro-loop avoidance, and selective FIB download at ~120k v4/v6 route scale, letting Microsoft deploy lower-cost platforms with smaller FIB capacity
- Solved anchor-route, DCIX T2-to-T2 bypass, and IPv4 containment requirements against sub-second convergence targets
- Built both IOS-XR and SONiC/FRR prototypes for BGP GRT (Global Routing Table), BGP confederations, and SRv6-TE, on the disaggregated RH (dRH or disaggregated Regional Hub routing layer). This effort was highlighted on the **global PSE/DSE call** as the "nine POCs at once" project, recognizing Bruce's use of agent-assisted development to iterate rapidly through topologies and scenarios `[verify date — June 2026]`
- Developed and delivered the dRH SRv6-versus-VXLAN architecture comparison and a SONiC GRT lab POC to Microsoft lead architects Abhishek Dosi and Mohan Nanduri with Cisco engineering (Mar 2026)
- Ran the SRv6 DC-frontend POC (Aug 2025) across 4PE, DCIX, and a mixed IOS-XR/SONiC fabric, demonstrating prefix-hiding at scale and SRv6-TE for inter-DC traffic
- Generated lab scenarios — configurations, topologies, and documentation — using agent-assisted tooling, compressing POC development time and enabling MSFT architects to install the setup in their labs and demo internally

**1.6T WAN backbone and SWAN:** Cisco 8000 WAN revenue at Microsoft ran ~$65.9M in FY25 and ~$60M in FY26. The relationship behind it began before Bruce's PSE promotion with the IOS-XR **SL-API SWAN controller integration** — the technique that later transferred to Meta's backbone win and Google's Alphanet program, both detailed at their own entries below — and he has sustained it since in close partnership with **Senior SE Pan Chou**, delivering SR and SRv6 tutorials to the Microsoft WAN team and running a multi-planar architecture design session with them. Pan Chou owns the account relationship; Bruce supplies the architecture and the horizon-2 guidance behind it.

Bruce developed the POC labs and field training for Microsoft's 1.6T backbone redesign, modeling node growth from ~1,800 to ~3,000, prefix expansion, sub-3-second convergence targets, and ISIS planes versus geographic domains. He positioned SRv6 uSID as the option that scales for decades — native IPv6 summarization, flow-label entropy, and extension to hosts and SmartNICs — and delivered two SRv6 WAN lunch-and-learn sessions to the Microsoft WAN team (Apr–May 2025).

**Financial impact:** Within Bruce's engagement scope since 2021 — **$1.744B** Cisco 8000 AI/DC revenue `[Bruce to confirm attribution with account team]` and **$306.4M** WAN revenue, of which Cisco 8000 WAN specifically ran ~$65.9M (FY25) and ~$60M (FY26). Segment bookings for the account were $3.97B over 2022–2026. **Competitive impact:** Established SRv6-on-SONiC as a supported path on the Cisco 8000, closing the gap against competitor hardware already deployed in Microsoft's AI backend and Frontend DC, and positioned SRv6 uSID against VXLAN in the dRH frontend re-architecture. **Strategic impact:** The multi-tenant AI fabric specification became the reusable reference architecture for Oracle and CoreWeave; SRv6-on-SONiC productization opened the open-NOS AI-backend market across the entire hyperscale and neocloud segment. **Overall customer impact:** A repeatable disaggregated, open-NOS data center and backbone architecture that scales Microsoft's AI infrastructure without the route-scale and convergence ceilings of the prior design.

**Evidence:** [ASP Web FY20-26 Product Bookings](https://cisco.sharepoint.com/:x:/r/sites/GSPWEB-SalesandFinance/Shared%20Documents/ASP%20Web%20Finance/Adhoc/Q4%2726/ASP%20Web%20FY20-26%20Product%20Bookings.xlsx?d=wf735385979d541b6bdda11cfd8c7993f&csf=1&web=1&e=LUS3pf); GitHub `segmentrouting/srv6-msft`, `segmentrouting/srv6-mrc-emulator`; vault `customers/Microsoft AI-Backend.md`, `customers/Microsoft SRv6.md`, `customers/MSFT octans-drh.md`, `customers/Microsoft-WAN.md`, `innovation/SRv6-MultiTenant-Design-rev3.md`; Talent Assessment 1HFY26; published SWAN architecture reference — [ACM 10.1145/3603269.3604860](https://dl.acm.org/doi/pdf/10.1145/3603269.3604860) `[confirm this paper documents the SL-API/SDN forwarding technique Bruce pioneered]`.

The productization of SRv6-on-SONiC and the multi-tenant specification are detailed in the Innovation section of this document. The internal advocacy that funded them is detailed in Span of Influence.

---

### Meta, 2021 – Present

**Revenue within Bruce's engagement scope:** WAN franchise **~$300M delivered over two years**; **$17M** first 8223 production order into the new BBF, Feb 2026; **$178.3M** Silicon One since 2021, on the analysis and SDK work originated in the AWS engagement `[verify]`. Segment bookings for the account over 2022–2026 were $3.11B.

Meta operates one of the largest private backbones in the world, connecting a global data center estate that serves more than three billion daily users. Cisco had been displaced from Meta's backbone and was competing to re-enter against Arista and Broadcom Jericho silicon. Bruce has served the Meta account team as architecture and strategy consultant from 2021, equipping them with the architecture, the technique, and the labs. They carried it to the customer themselves — enormous revenue impact delivered entirely through other people.

Two distinct outcomes came out of that work.

**The WAN franchise.** Bruce transferred the SL-API technique from its Microsoft SWAN origin to Meta, where it became the key technical differentiator. He delivered SL-API, SDN, and Segment Routing enablement sessions to the Cisco account team (2022–2024), modeled on the Microsoft SWAN engagement, along with the reference material, repositories, and code they needed to run the customer conversation without him. He also built VXR-based POC labs that let the account SEs co-validate the EBB, BBF, and RBB architectures with Meta engineers before hardware was available. The franchise this secured has **delivered ~$300M over the past two years** `[verify]`. In February and March 2026 Meta committed RBB to SRv6, building on the same SL-API foundation; the RBB pipeline is cited at ~$350M/year `[verify]`.

**The 8223 platform insertion.** In April 2024 Meta opened what became a roughly two-year Express Backbone / Backbone Fabric evaluation cycle. Cisco needed to prove P200 silicon in an account where Arista was incumbent and where the customer validates independently rather than accepting vendor test results. Bruce obtained pre-release 8223 code through his engineering and VXR team relationships in March 2026, before the hardware was GA, and built the account SE team an **8223 simulation lab**. That gave Asoka DeSaram and Leif Berntsson a head start on driving Meta's certification of the platform for the BBF role, at a critical point in the evaluation. Meta booked a **$17M first production order** for the Cisco 8223-64EH (P200) 64×800G platform into the new BBF portion of the backbone in February 2026. Asoka on the lab support: *"Thank you for helping us with the VXR setup. That was huge!!"* Asoka and Leif went on to reuse the VXR lab pattern in the Web-wide AI hackathon (May 2026).

**Financial impact:** WAN franchise ~$300M delivered over two years; $17M first 8223 production order booked Feb 2026; RBB pipeline ~$350M/year `[verify]`; $3.11B in total segment bookings 2022–2026, including $1.91B in FY26. **Competitive impact:** Countered Arista's incumbency on the backbone and established Cisco as a credible second source in a multi-vendor global deployment — the re-entry point for a franchise Cisco had previously lost `[confirm framing with account team]`. **Strategic impact:** Proved that a technique developed at one hyperscaler transfers directly to another (see Microsoft, above, and Google, below, for the same transfer), and established the VXR co-validation lab as a repeatable pre-GA sales motion now reused across the Web segment. It also demonstrated the return on sustained internal architectural consultancy: five years of education and advocacy on SRv6 and SL-API, carrying no attributable revenue at the time, converted into a backbone franchise won by a team Bruce equipped rather than led. **Overall customer impact:** A validated backbone fabric architecture and a committed SRv6 path for RBB, with pre-GA access that let account SEs and Meta's engineers evaluate on their own terms rather than on vendor timelines.

**Evidence:** [ASP Web FY20-26 Product Bookings](https://cisco.sharepoint.com/:x:/r/sites/GSPWEB-SalesandFinance/Shared%20Documents/ASP%20Web%20Finance/Adhoc/Q4%2726/ASP%20Web%20FY20-26%20Product%20Bookings.xlsx?d=wf735385979d541b6bdda11cfd8c7993f&csf=1&web=1&e=LUS3pf); vault `customers/Meta.md`; DSE General MOC (Mar 2026 Asoka 8223 thread); SWAN architecture reference — [ACM 10.1145/3603269.3604860](https://dl.acm.org/doi/pdf/10.1145/3603269.3604860).

**Note:** Meta was the second customer after Microsoft to adopt the SL-API/SDN/SR technique Bruce pioneered — the transfer is the strategic point, and Google (Alphanet) is now the third.
The origination of the SL-API technique is detailed in the Innovation section of this document. The VXR lab enablement pattern is detailed in the Leadership section.

---

### Oracle Cloud Infrastructure, 2023 – Present

**Revenue within Bruce's engagement scope:** ~$20M `[verify]`, with a 2026–2028 projection `[verify]`. Segment bookings for the account over 2022–2026 were $446M.

Oracle Cloud Infrastructure is the fastest-growing of the major public clouds and has committed to one of the industry's largest AI training buildouts. Its Acceleron program re-architects the AI fabric around multiplanar fabrics with source routing originating at the NIC — an approach that requires exactly the host-based SRv6 model Bruce had been advocating inside Cisco since 2019, when SRv6 uSID first made it practical. Bruce is Cisco's lead architect for SRv6 for AI at OCI.

**SRv6 for AI — Acceleron and MRC:** Oracle needed N-diverse path selection with multipath reliable connection (MRC) running on GPU hosts in their Stargate and Abilene DCs, with source routing pushed to the NIC rather than computed in the fabric. Bruce's involvement and accomplishments include:

- Serves as SONiC-on-Cisco-8000 SME for the wider OCI account engagement, and as lead architect for the SRv6-for-AI program since December 2024 
- Opened the general Cisco-as-credible-vendor conversation for OCI AI backend fabrics at OCP in October 2024
- Delivered the SRv6 customer requirements document, the VXR lab, the SRv6 SONiC image, and the SRv6 GRT implementation that made the architecture testable
- Conducted low-diameter topology studies (Hoffman-Singleton, PolarFly) with OCI architect Christian Martin (Jun 2024 — late 2025), producing the lab and design document evaluating fabric diameter against GPU-scale requirements
- Built and demonstrated an IOS-XR based SRv6 uSID AI-backend demonstration for Oracle VP Jag Brar and his architecture team (Jan 2025)
- Delivered a three-hour onsite SRv6 tutorial to Oracle engineering (2025) and a three-part follow-on series (Mar, Apr, and Jun 2026) and supported the SE team on SONiC 8122 lab configurations (Jun 2025)
- Served as consultant and software advisor on Oracle's Solar-OS (SONiC on Oracle Secure Linux), including the April 2025 EBC with the Cisco SONiC and Solar-OS teams

OCI was running SRv6 in limited production by the end of 2025. Oracle's own 2026 public blog cites SRv6 static routing for MRC — the same architectural pattern Bruce drove at Microsoft, now published by the customer as their design of record.

**Financial impact:** $446M in segment bookings 2022–2026, with ~$20M attributed to Bruce's engagement scope and a 2026–2028 projection `[verify]`. **Competitive impact:** As at Microsoft, Oracle's current SRv6-for-AI deployments run on competitor hardware. Cisco's SRv6-on-SONiC path for the 8122 and future G300 platform — which Bruce secured — is the recovery vehicle, and OCI's published commitment to the architecture makes the market real rather than speculative. **Strategic impact:** Two independent hyperscalers converging on the same SRv6-for-AI architecture, one of them publishing it publicly, converted Bruce's internal position from a contested opinion into industry evidence — and directly supported the SONiC investment case detailed in the Innovation section. **Overall customer impact:** A source-routed multiplanar AI fabric that reaches limited production inside a single year of the first architecture workshop.

**Evidence:** [ASP Web FY20-26 Product Bookings](https://cisco.sharepoint.com/:x:/r/sites/GSPWEB-SalesandFinance/Shared%20Documents/ASP%20Web%20Finance/Adhoc/Q4%2726/ASP%20Web%20FY20-26%20Product%20Bookings.xlsx?d=wf735385979d541b6bdda11cfd8c7993f&csf=1&web=1&e=LUS3pf); Oracle public blog 2026 `[add URL]`; GitHub `segmentrouting/srv6-oci`; vault `customers/Oracle-SRv6.md`, `customers/Oracle-800g-roce.md`; `projects/wmp-polarfly-whitepaper-v07.md`.

The multi-tenant specification and the flat-topology studies are detailed in the Innovation section of this document.

---

### CoreWeave, 2025 – Present

**Revenue Impact:** ~$20M FY26. Projected FY27 — $150M DC switching, $245M optics. Projected FY28–29 — $400M/year DC switching, $600M+/year optics `[verify]`

CoreWeave is the largest of the neo-cloud AI providers and a primary compute partner to OpenAI, building GPU capacity at a pace that compresses normal infrastructure planning cycles into months. The account had no established Cisco data center or WAN franchise and CoreWeave's engineering team evaluates open-NOS options by default. Bruce serves as Cisco's SONiC SME and lead SRv6-for-AI architect on the account.

**AI backend and global WAN architecture:** CoreWeave needed a backend fabric design that handled adaptive routing and ECN at GPU scale, and a global WAN capable of stitching AI data center fabrics across regions. Bruce's involvement and accomplishments include:

- Led the backend fabric architecture covering adaptive routing, ECN behavior, and MRC/SRv6 path metrics, including Vera Rubin Ultra path analysis
- Advisor and reviewer of the WAN backbone architecture — DSE David Smith was assigned as lead architect (Apr 2026) — ~196 edge routers, 42 TLRs, DSR stitching for AI-DC fabrics, and 32 D-pops for data center interconnect
- Built Containerlab and VXR lab environments with documentation for CoreWeave's NetDev engineering team (Mar 2026), offering virtual Cisco 8000 routers running either IOS-XR or SONiC and giving the customer a self-service evaluation path
- Served as technical lead for backend data center, SONiC, and simulation environments (VXR, Containerlab) at the CoreWeave EBC (Feb 2026)
- Demonstrated his SRv6-MRC-Emulator tool to CoreWeave VP Shiv Patel, who encouraged his internal team to adopt it on the strength of it being open source

Following the lab enablement, EBCs, and mindshare-building, the opportunity scope expanded to ~10,000–12,000 switches.

**Financial impact:** ~$20M FY26, with FY27 projected at $150M DC switching and $245M optics, and FY28–29 at $400M/year DC switching and $600M+/year optics `[verify]`. **Competitive impact:** Established Cisco as a credible open-NOS supplier and alternative to Nvidia Spectrum-X. **Strategic impact:** Reused the SRv6 multi-tenant AI fabric specification authored for Microsoft, demonstrating that the reference architecture transfers to neo-cloud operators; the Containerlab/VXR enablement pattern is now standard across Web AI accounts. **Overall customer impact:** A backend and WAN architecture sized for hyperscale AI factory growth, an MRC design template CoreWeave can leverage with their largest customer (OpenAI), and a self-service lab setup that lets CoreWeave engineering validate on their own schedule.

**Evidence:** [CoreWeave DC Back-End Switching CRD v1](https://cisco-my.sharepoint.com/:w:/r/personal/bgisiger_cisco_com/Documents/Desktop/Old%20Desktop/Web%20Operation%20Accounts/Big%20Projects/AI%20start-ups/CoreWeave/DC%20Switching/Back-end/CRD/CoreWeave%20DC%20Back-End%20Switching%20-%20Customer%20Requirements%20Document%20(CRD)%20v1.docx?d=w302ef71e18cc47529beaeb9e213af6a1&csf=1&web=1&e=mO6m5O); vault `customers/Coreweave DC.md`, `customers/Coreweave backbone.md`, `customers/Coreweave lab.md`; PSE time log Mar 2026.

---

### Bell Canada, 2020 – Present

**Revenue Impact:** 400 CPE initial purchase plus $1.8M core revenue, May 2026. Cumulative SRv6 and host-networking engagement `[verify]`; Isovalent revenue `[verify]`; NCS5500 and Cisco 8000 revenue tied to SRv6 `[verify]`

Bell Canada is Canada's largest telecommunications operator, serving the country's national wireline, wireless, and media infrastructure. Bell has been one of Cisco's most technically advanced Segment Routing partners and one of the earliest tier-1 operators to commit to end-to-end SRv6 with host-based extension. Bruce led the multi-year architecture work behind that commitment.

**End-to-end SRv6, host networking, and NaaS:** Bruce's involvement and accomplishments include:

- Partnered with Dan Bernier, Bell Canada Senior Architect, on a multi-year vision and architecture to transform a traditional Tier-1 service provider into a Cloud-like Network-as-a-Service company that operates more like a Hyperscaler. The architecture was built around a truly end-to-end SRv6 design spanning core, edge, metro, DC, Kubernetes hosts, and customer premise equipment (CPE)
- Bruce's Jalapeno and host-based SR/SRv6 session at KubeCon (Nov 2019) led directly to the multi-year partnership with Bernier. Over the course of 2020 and 2021 (one onsite workshop in Montreal, bi-weekly sessions) the host-based SRv6 discussions led to Bell investing in Cilium and driving their SRv6 integration all prior to the Cisco Isovalent acquisition — Bruce's mindshare building meant Cilium arrived in Cisco's portfolio with SRv6 already built in
- Developed the network-as-a-service architecture framing that positioned SRv6 as a service-delivery platform rather than a transport upgrade

Bell placed an initial purchase of 400 CPE together with $1.8M in core revenue for their first NaaS deployment on May 4, 2026 (Helene Roy).

**Financial impact:** 400 CPE initial purchase plus $1.8M core revenue (May 2026); cumulative engagement `[verify]`. **Competitive impact:** Secured the platform franchise for Bell's SRv6 build-out at the point of first production commitment. **Strategic impact:** Produced a tier-1 operator reference for end-to-end SRv6 with host-based Cilium — the architecture Bruce advocated internally for a decade, validated in a production carrier network. **Overall customer impact:** A programmable, service-oriented network architecture that extends consistent forwarding and network policy from the core to the workload.

**Evidence:** Vault `technologies/Bell Canada.md`; OCP 2024 SRv6-for-AI cohort.

Bruce's host-networking and Isovalent/Cilium advocacy is detailed in the Span of Influence and Innovation sections of this document.

---

### Google, 2021 – Present

**Revenue within Bruce's engagement scope:** ~$20M `[verify]`. Segment bookings for the account over 2022–2026 were $1.95B.

Google operates one of the world's largest data center and AI footprints, and GCP is a rapidly growing competitor to AWS and Azure. Google's B4 transport network is one of the largest and most-studied private WANs in the world. Google Distributed Cloud extends their cloud services into customer and edge environments. Cisco holds a significant share of Google's backbone and GDC footprint, and the account requires engineers who can engage Google's network software teams as peers. Bruce served as strategy consultant, SRv6 architect, and — during a period of account SE leave — interim lead SE for WAN.

**GDC SRv6 and B4:** Bruce's involvement and accomplishments include:

- Developed the end-to-end SRv6 proposal and training program for Google Distributed Cloud, and led the GDCE onsite SRv6 design session (May 2024)
- Stepped in as interim lead SE on B4 SR-MPLS during account SE leave, maintaining continuity on Cisco's largest Google engagement
- Opened the SRv6 for Google AI Backend program (Mar 2026), running introductions and kickoff with Nick Sischo, Pablo Camarillo, and Clarence Filsfils
- Extended the SL-API technique to Alphanet — the third hyperscaler after Microsoft and Meta to adopt it

**Financial impact:** $1.95B in segment bookings 2022–2026, including $1.05B in FY26; ~$250M attributed to Bruce's engagement scope `[verify]`. **Competitive impact:** Maintained Cisco's backbone position through an account SE transition, and opened the SRv6 conversation in the AI backend — an account Cisco is still working into rather than one it has won. **Strategic impact:** A third independent hyperscaler engaged on SL-API, reinforcing that the technique transfers; the SRv6-for-AI thread is early and running with Cisco's SR engineering leadership directly involved. **Overall customer impact:** A defined SL-API path for Alphanet and an opening position on SRv6 for GDC and the AI backend.

**Evidence:** [ASP Web FY20-26 Product Bookings](https://cisco.sharepoint.com/:x:/r/sites/GSPWEB-SalesandFinance/Shared%20Documents/ASP%20Web%20Finance/Adhoc/Q4%2726/ASP%20Web%20FY20-26%20Product%20Bookings.xlsx?d=wf735385979d541b6bdda11cfd8c7993f&csf=1&web=1&e=LUS3pf); vault `customers/Google.md`.

---

### Amazon Web Services, 2021 – Present

**Revenue within Bruce's engagement scope:** ~$20M Direct Connect `[verify]`. AWS itself bought only a few hundred thousand dollars of Silicon One. The analysis, feature development, and SDK work this engagement produced was inherited by the Silicon One engagement at Meta, which has booked **$178.3M** since 2021 `[verify attribution]`. Segment bookings for the account over 2022–2026 were $1.41B.

AWS is the largest public cloud provider in the world and one of the few customers with the scale to justify merchant silicon partnerships. Silicon One is Cisco's entry into that market, and the AWS relationship was the proof point for whether Cisco could compete as a silicon supplier rather than only a systems vendor. Bruce served as internal consultant on Silicon One strategy for the account.

**Silicon One strategy and feature program:** Bruce's involvement and accomplishments include:

- Built the 12.8T → 25.6T → 51.2T TAM model with the account team and the customer, sizing the multi-generation silicon opportunity
- Project-managed feature development tracking between AWS and Cisco engineering, keeping roadmap commitments aligned to customer qualification timelines
- Opened the SRv6-for-AWS-telco-customers thread with Riggs and Christian Martin (Feb 2023), extending the silicon relationship into architecture. That thread did not convert

Cisco leadership recognized the foundational silicon deals at VP level in Q1 FY23 `[verify $]`.

**The return came from a different account.** AWS never became a material Silicon One customer — the purchases totaled a few hundred thousand dollars. But the requirements analysis, the feature development, and the SDK work done to qualify for AWS were not account-specific, and the Silicon One engagement at **Meta** inherited all of it, booking **$178.3M since 2021**. The AWS engagement is best read as the investment that made a second, larger one possible.

**Financial impact:** ~$20M Direct Connect within Bruce's scope `[verify]`; a few hundred thousand dollars of Silicon One at AWS itself; **$178.3M** of Silicon One at Meta since 2021, on the analysis, feature, and SDK work this engagement produced `[verify attribution]`. Segment bookings for the account were $1.41B over 2022–2026, including $717M in FY26. **Competitive impact:** Opened a merchant-silicon position at the largest cloud operator, in a category Broadcom had held uncontested. The position at AWS did not convert, and Silicon One has lost addressable market to the same late-to-market pattern seen across the AI accounts. **Strategic impact:** The engineering investment proved portable. Requirements analysis, feature development, and SDK work built to qualify at one hyperscaler transferred whole to another, which is the argument for making that investment at all — and the generational TAM model became the basis for Silicon One planning across the Web segment. **Overall customer impact:** A multi-generation silicon roadmap aligned to AWS's own qualification cadence, and a qualified silicon platform a second hyperscaler could buy.

**Evidence:** [ASP Web FY20-26 Product Bookings](https://cisco.sharepoint.com/:x:/r/sites/GSPWEB-SalesandFinance/Shared%20Documents/ASP%20Web%20Finance/Adhoc/Q4%2726/ASP%20Web%20FY20-26%20Product%20Bookings.xlsx?d=wf735385979d541b6bdda11cfd8c7993f&csf=1&web=1&e=LUS3pf); vault `xarchive-2021-2022/AWS-may-2021.md`, `dse/04-Span-of-Influence-MOC.md`, `dse/DSE General MOC.md`.

---

### Verizon, 2024 – Present

**Revenue Impact:** Strategic A3PO/CX engagement; Project Yukon (NaaS) and service-chain revenue `[verify]`

Verizon operates the largest wireless network in the United States alongside a national wireline and FIOS footprint, with 52 packet-core data centers. Verizon was evaluating whether to carry MPLS forward or commit to SRv6 across wireless switching centers, data centers, VCP, FIOS, and XRAN — a decision affecting the entire estate. Bruce led the architecture consulting behind that evaluation.

**Enterprise-wide SRv6 roadmap and Project Yukon:** Bruce's involvement and accomplishments include:

- Built the architecture decision matrices comparing NX-OS, IOS-XR, SONiC, and SRv6 across Verizon's domains, quantifying prefix-summarization value against stitching cost
- Produced the internal SRv6 business case quantification and the seamless MPLS-to-SRv6 transition path
- Developed the Project Yukon network-as-a-service revenue framing
- Drove 400G server fabric, SONiC/SRv6, and SRv6-in-host (FRR/Cilium) threads for converged 5G and AI data centers, including AI pod deployment in existing facilities
- Ran AI and LLM network-automation and host-based SRv6 workshops with VZ Fellow Luay Jalil, VZ Senior Architect Nicklous Morris, Cisco PSE Josh Merrill, and senior account SE Jasbir Sidhu

Verizon's April 2024 MPLS World Congress presentation was built on Bruce's `srv6-labs` material.

The relationship with Morris and Jalil has since deepened into a specific technical thread: Bruce and Morris first connected in person at an IETF meeting to discuss host-based SRv6, and the conversation has continued through multiple follow-on discussions, now including Jalil. The group is planning a **Cilium-SRv6 proof-of-concept/demo** in the coming months `[planned — not yet delivered; update with outcome, and check whether it produces a revenue or pipeline entry once complete]`.

The **SRv6-with-SGT** work has not yet produced revenue, but is generating substantial mindshare at Verizon executive level. Bruce designed the majority of the architecture and the underlying intellectual property; Cisco PSE Josh Merrill has carried most of the executive presentation — an intentional division that puts a colleague in front of the customer's leadership.

**Financial impact:** Strategic A3PO/CX engagement; Yukon NaaS revenue `[verify]`. **Competitive impact:** Positioned SRv6 and SONiC as the forward architecture ahead of a formal RFP cycle. **Strategic impact:** Extended the host-networking and SRv6-in-host model from hyperscale into a tier-1 mobile operator, and produced a NaaS revenue framing reusable across the SP segment. **Overall customer impact:** A quantified transition path from MPLS to SRv6 across a national estate, with the business case attached.

**Evidence:** Vault `customers/Verizon.md`; MPLS-WC Apr 2024.

The Nicklous Morris / IETF connection is also referenced in Industry Impact's Operator Community section — same relationship, two facets (standards-adjacent origin here; commercial/technical thread there).

---

## Additional ASP+Web Engagements

### Akamai — Backbone SR/SRv6 and the Prolexic Controller — 2023–2025

Akamai operates the world's largest content delivery network. Its engineering leadership — **John Leddy** and **Russ White** — are among the most technically rigorous evaluators in the industry, and Bruce led Cisco's SRv6 architecture engagement with them: driving the RSVP-to-SR backbone transition alongside the 800G deployment, building the FRR SRv6 L3VPN image and lab for White (Oct 2023), and running SRv6 use-case workshops with both (Feb 2024). He gave a direct assessment of Silicon One SRv6-TE strengths and limitations rather than a positioning pitch, which is what the rest of the engagement ran on. The work has not produced a purchase.

Its most significant output was a POC multi-use-case **SDN controller** built on Bruce's open-source Jalapeno backend, programming SRv6 L3VPN routes onto a custom Linux forwarder for Prolexic's redirect-to-scrubber use case (2025 PDP) — the clearest customer-facing proof of the host-networking thesis, and a direct antecedent to the Cilium SRv6 product path. *Detailed in the Innovation section of this document.*

---

### Videotron — SRv6 Regional Backhaul — Feb–Apr 2026

Videotron is Quebec's largest cable operator and, following its Freedom Mobile acquisition, a national wireless challenger. Bruce consulted as SRv6 subject-matter expert on the backhaul design interconnecting four MPLS-LDP regions over an IPv6 core with SRv6 gateways, and enabled SE Philippe Vaillancourt by giving him access to his Containerlab SRv6 lab to self-train ahead of the customer workshop. He coordinated Ianik, Jakub, and Dan Voyer for the onsite SRv6 update. **Revenue:** ~$25M `[verify]`.

---

### T-Mobile — Magenta Cloud Segmentation & Cilium — 2024–2025

T-Mobile is the second-largest US wireless operator. Bruce built the macro/micro/nano segmentation architecture narrative — Cilium policy, zone-based firewalling, eBPF/Tetragon, and ACI-versus-Cilium positioning — and supported the Overlay RFP (Nov 2024) and Magenta Cloud RFP (Dec 2024). He drove greenfield DC opportunities (Polaris, Tortugas), v6-only underlay design, and Hypershield/Cilium evaluation in MagentaCloud. `[verify which elements T-Mobile adopted versus deferred before this entry is final]`

**Vault:** `customers/T-Mobile.md`

---

### Dish / Boost Mobile — SRv6 L3VPN on AWS — 2025–2026

Boost Mobile runs the first US cloud-native 5G network, built on public cloud infrastructure. Bruce developed the SRv6 L3VPN over AWS architecture as a replacement for GRE tunnels — Cilium SRv6 uSID, cloud-native L3VPN at the pod level (Jan 2026) — the package's clearest example of end-to-end SRv6 and Cilium running entirely in public cloud. Recognizing that Cilium cannot address SR-IOV kernel-bypass networking, he authored the multi-use-case Cilium customer requirements document that Cisco engineering has accepted and is working to prioritize. No revenue to date. *The Cilium CRD, which also underpins the Verizon engagement, is detailed in the Innovation section.*

---

### Applied Digital — AI Infrastructure — Sept 2024

Bruce's Web AI Fabrics calculator and rail architecture diagrams (Jun 2024) became a two-year scoping tool for Web SEs across the segment; the same artifacts sized the Applied Digital engagement. **Revenue:** ~$30M `[verify]`.

---

### Digital Realty — SRv6 POC — Oct 2025–present

Digital Realty is one of the two largest global colocation providers. Bruce drove the host-based and Cilium SRv6 component of the POC, standing up the deployment in the DLR lab (PDP Dec 2025), and served as subject-matter expert and evangelist for true end-to-end SRv6 — including the proposal that Digital Realty construct federated SRv6 partnerships with third-party service providers and neo-clouds, extending programmable transport across organizational boundaries rather than only within its own footprint. He presented Jalapeno at the Denver EBC and workshop (Jun 2025), where the second-generation RPO SDN application was deployed. `[verify $]`

On seeing Jalapeno, the customer remarked that they *"would have paid millions of dollars for something like this a couple of years ago — and here it is, open source."* `[confirm wording with account team before quoting]`

---

---

### Comcast — Load Balancing Architecture — Feb 2026

Bruce consulted on the Comcast load-balancing architecture; ~$5M opportunity scope `[verify with Jenelle/account team]`.

---

### Groq — SR-TE POC — Sep 2025

Bruce ran the SR-TE POC for this AI inference silicon provider, demonstrating Flex-Algo and traffic steering for data-sovereignty. The POC succeeded, and the opportunity was worth $10s of millions; Groq was subsequently acquired by NVIDIA before it could make any purchases (Sep 2025).

---

### Lambda Labs — Host-Based SRv6 & DC Design — Jul 2024 – Jul 2025

Bruce presented host-based SRv6 and consulted on data center design at the Lambda Labs EBC (Jul 2024), and later developed the Isovalent Egress Transit Gateway concept and opportunity with the account (Jul 2025).

---

---

---

### Salesforce — A9K Displacement and NG DC — Sep 2020 – Oct 2023

Bruce co-led the SFDC A9K POC development and execution with Asoka (Sep 2020), leveraging prior relationship and mindshare. **2022:** $38M win displacing Juniper on A9K `[confirm ASP+Web classification]`. **Oct 2023:** Delivered the Segment Routing presentation positioning Salesforce's next-generation data center.

---

## Out-of-Territory Engagements

The engagements below sit outside Bruce's Americas Service Provider and Web assignment. Teams in other theaters requested him by name for SONiC, SRv6, Cilium, and hyperscale architecture when they needed depth their own organization did not carry — he is effectively the sole Cilium and Kubernetes SME across Americas SP and Web. That reach rests on two decades of working relationships with senior SEs, PSEs, and DSEs kept up across Cisco regardless of geography or vertical.

---

### Geico, 2024

**Revenue Impact:** ~$1.6M SONiC on Cisco 8000 `[verify finance]`

Geico is the second-largest auto insurer in the United States and a Berkshire Hathaway company, expanding on-premises data center capacity with a 32×100G top-of-rack leaf-spine design. Its infrastructure leadership intended the facility to serve as a shared resource across Berkshire Hathaway companies, which meant enterprise scale with hyperscale architectural and commercial expectations — and no Cisco architect in the enterprise theater had SONiC depth. Geico had made a strategic decision to go open-source wherever possible and planned to deploy SONiC greenfield. Cisco Nexus was the incumbent, but Geico had signaled a willingness to choose a competitor's SONiC platform and demanded commercial terms matched to cloud-scale buying rather than enterprise switching quotes. Bruce's involvement and accomplishments include:

- Bruce served as SONiC subject-matter expert for the engagement, leading the data center architecture sessions (Mar 2024)
- Advocated directly with the BU for a cloud and hyperscale-style pricing model to support Berkshire-wide infrastructure sharing

**Financial impact:** ~$1.6M Cisco 8000 win `[verify finance]`. **Competitive impact:** Established SONiC on Cisco 8000 as viable for enterprise data center at a customer evaluating white-box alternatives. **Strategic impact:** Proved the hyperscale consumption model transfers to enterprise, and created a Berkshire Hathaway shared-infrastructure reference. **Overall customer impact:** A credible open-NOS data center path for a major insurer, with commercial terms matched to how they actually buy.

**Evidence:** Vault `customers/Geico.md`; 2HFY24 talent assessment.

---

### Honeywell, 2024

**Revenue Impact:** ~$2M Segment Routing / Cisco 8000 `[verify finance]`

Honeywell is a Fortune 100 industrial conglomerate operating a global network spanning six colocation facilities and two private data centers on an NCS 5501 backbone, with SD-WAN headend integration and IoT transport segmentation requirements. Arista was positioning against Cisco in the backbone.

**Segment Routing backbone architecture:** Honeywell needed path preference from SD-WAN into the private backbone, an assessment of Flex-Algo for IGP-based path selection without a controller, and an SR/SRv6 roadmap. Bruce served as architecture subject-matter expert on the backbone design, SD-WAN integration options, and Flex-Algo use cases (Apr 2024), and consulted on future IoT transport segmentation and internal chargeback models.

**Financial impact:** ~$2M Segment Routing / Cisco 8000 win `[verify finance]`. **Competitive impact:** Held the backbone franchise against Arista. `[verify — confirm Arista was actively competing and displaced]` **Strategic impact:** Demonstrated that MIG transport expertise transfers directly to enterprise private backbones outside the SP segment. **Overall customer impact:** A controller-free path selection architecture aligned to Honeywell's global colocation footprint.

**Evidence:** Vault `customers/Honeywell.md`.

---

### Adobe, 2024 – 2025

**Revenue Impact:** Renewal expansion from $750K to $1.6M ACV, one year after the POC (per Adobe account SE) `[confirm figure and attribution with account team before final]`

Adobe is a global technology enterprise with a multi-cloud footprint, migrating to Kubernetes under its Adobe Ethos program. Adobe's infrastructure had grown rapidly through acquisitions and remained a patchwork of overlapping RFC1918 space, simply NAT'ing site-to-site traffic over the internet. They wanted to simplify their architecture and bring the traffic back onto their private WAN, and engaged Cisco's Isovalent team in a Cilium Egress Gateway POC. In April 2024 the Isovalent SE had left the company and the proof of concept was failing during its critical validation window. The account systems engineer, Dan Stacks, needed Isovalent technical depth that did not exist on his team.

**Cilium egress gateway rescue and cloud-native SRv6:** Bruce's involvement and accomplishments include:

- Simulated Adobe's POC topology in his own lab (Apr 2024) to diagnose the failing proof of concept, despite having no prior hands-on experience with Isovalent egress gateway or load balancing, and resolved the configuration and deployment faults
- Served as core technical SME on the Cilium POC with Brenden Buresh and Dan Stacks through 2024–2025, providing critical-path egress gateway validation support throughout
- Proved egress gateway and load balancer functionality against Adobe performance requirements at the June 2025 onsite workshop
- Developed and presented a Cloud-Native SRv6 architecture (Feb 2025) — SRv6 L3VPN CNI-to-CNI, elimination of VXLAN and MPLS stitching at both top-of-rack and DCI/PE, eBPF visibility, and transit gateway cost reduction

The proof of concept completed successfully in October 2025 — and Adobe did not adopt Isovalent for the egress use case itself. They judged the product not yet ready for their environment, specifically its lack of support for non-Kubernetes workloads, and elected to stay with their incumbent load balancer for that function. Adobe responded well to the SRv6 architecture and concepts but considered them premature for their roadmap; Cisco expects to re-engage within one to two years. The account's contract nonetheless expanded from $750K to $1.6M ACV at the next renewal, one year after the POC, per the Adobe account SE.

The gap Adobe identified is the one Bruce then wrote up: the multi-use-case Cilium customer requirements document — extending Cilium to carry networking and policy for non-Kubernetes workloads — which Cisco engineering has since accepted and is working to prioritize. A lost proof of concept produced the product requirement.

**Financial impact:** Contract renewal grew from $750K to $1.6M ACV a year after the POC, per the account SE `[confirm figure and whether it is attributable to this engagement rather than broader account growth]`. **Competitive impact:** Preserved a Cilium proof point that was failing and would otherwise have closed the opportunity outright, keeping Cisco positioned for re-engagement rather than displaced. **Strategic impact:** Validated the post-acquisition Isovalent product path in a live enterprise engagement. The Cloud-Native SRv6 concept reviewed here is the same architecture Bruce co-developed with Dan Bernier at Bell Canada and later evaluated and tested at Boost Mobile and Digital Realty. **Overall customer impact:** A working egress and load-balancing architecture that moves Adobe-to-Adobe traffic off the public internet.

**Evidence:** Vault `customers/Adobe Cilium.md`, `customers/Adobe CN-SRv6.md`. `[Adobe / Dan Stacks testimonial pending]`

The Cilium SRv6 product path is detailed in the Innovation section of this document. Bruce's mentoring of Dan Stacks is detailed in the Leadership section.

---

### Fiserv, Jan 2026

**Revenue Impact:** Pipeline `[verify finance]`

Fiserv is one of the largest financial technology providers in the world, operating payment and banking infrastructure for thousands of institutions. The account sits outside ASP+Web; Bruce was engaged because the Enterprise team needed a top-level SME for the effort.

**SRv6 WAN and data center architecture:** Fiserv runs a Juniper RSVP-TE WAN overlay with VXLAN EVPN in the data center, and needed a credible path to extend a Segment Routing overlay end to end, simplify WAN-to-DC stitching, and evaluate geo-fencing and data-sovereignty steering — the same patterns Bruce had developed and fostered in numerous hyperscaler engagements — without a rip-and-replace program. Bruce delivered the SRv6 transfer of information to Fiserv's infrastructure team (Jan 2026), framed the WAN-to-DC extension with SD-WAN-to-SR anchor points and slice/shard/pinning in the data center, assessed Isovalent and Cilium relevance for the wireless private access context, and positioned SRv6 for AI backends for roadmap alignment.

**Financial impact:** Pipeline `[verify finance]`. **Competitive impact:** Opened an SRv6 displacement conversation against an incumbent Juniper RSVP-TE overlay. `[early — verify whether Fiserv has committed to a direction]` **Strategic impact:** Demonstrated that hyperscaler WAN patterns transfer to tier-1 financial services infrastructure. **Overall customer impact:** A staged simplification path from RSVP-TE to end-to-end Segment Routing without a forklift program.

**Evidence:** Vault `customers/Fiserv SRv6.md`. `[open question for Bruce: was this a single Jan 2026 TOI session, or has engagement continued into 2026? If continued, this entry can state more than "pipeline."]`

---

### Texas Instruments, 2024

Texas Instruments operates a global manufacturing and design network spanning fabs, design centres, and points of presence on four continents. Bruce led an onsite architecture workshop covering the global Segment Routing network and the SRv6 roadmap, against Arista competitive framing. The workshop went well enough that TI attempted to recruit him. `[verify whether revenue followed]`

---

---

### Province of New Brunswick — Cisco Live Europe 2026

**Revenue Impact:** Migration underway; platform revenue `[verify]`

The Province of New Brunswick operates the provincial government network for Canada's eighth-largest province. Lead architect James Munroe attended Bruce's Cisco Live Europe 2026 session with a conventional SR-MPLS migration already planned — the safe, well-trodden path that most operators of that scale were taking.

Bruce spent a single architecture conversation with him at a Meet-the-Engineer session, working through the design tradeoffs of adopting SRv6 directly versus staging through SR-MPLS first. Bruce and Munroe have stayed in contact since.

**Financial impact:** Migration in progress; platform revenue `[verify]`. **Competitive impact:** Converted a planned legacy-transport deployment into a next-generation architecture at the design stage. **Strategic impact:** This is the clearest single measure of Bruce's reach as a field multiplier — no account assignment, no follow-on engagement, no proposal. One conversation. **Overall customer impact:** James Munroe abandoned the planned SR-MPLS migration, authored a complete SRv6 design document within approximately two weeks of the conference, and began the migration — an unusually fast operator decision from a single conference conversation.

The Cisco Live session itself is detailed in the Leadership section of this document, and its industry visibility in Industry Impact.

---

### NYU and Carnegie Mellon, 2024

New York University and Carnegie Mellon were considering deploying SONiC in their high speed research networks. Bruce delivered SONiC education sessions and architectural/operational advice to both (Aug 2024). Research and higher-education networks are early adopters of disaggregated platforms and function as a credibility channel into the operator community — the engineers running them frequently move into industry roles carrying their platform preferences with them. `[Bruce to follow up with both account teams on documented outcomes: deployment, paper, or alumni placements]`

---
