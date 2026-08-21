## Business Impact

### Source data

- [Original XLS — Web Bookings 2022–2026](https://cisco.sharepoint.com/:x:/r/sites/GSPWEB-SalesandFinance/Shared%20Documents/ASP%20Web%20Finance/Adhoc/Q4%2726/ASP%20Web%20FY20-26%20Product%20Bookings.xlsx?d=wf735385979d541b6bdda11cfd8c7993f&csf=1&web=1&e=LUS3pf)
- [Updated XLS — Web Bookings 2021–2026](https://cisco.sharepoint.com/:x:/r/sites/GSPWEB-SalesandFinance/Shared%20Documents/ASP%20Web%20Finance/Adhoc/Q4%2726/ASP%20Web%20FY20-26%20Product%20Bookings.xlsx?d=wf735385979d541b6bdda11cfd8c7993f&csf=1&web=1&e=RNbkFw)

## Business Impact Model — Co-Development, Mindshare, and Relationships

Bruce's ASP+Web business impact follows a repeatable pattern: train SE teams and customer engineers on architectures and products before they need them, build POC labs and simulations (SONiC, SRv6, SL-API, host-networking), then co-develop with hyperscalers and tier-1 SPs until the revenue pipeline matures. Account notes describe this as multiyear partnership, not a traditional or transactional sales cycle — Bruce often serves as internal strategy consultant, the SONiC, SRv6, Linux, or scaled-routing SME, and lead architect while grade-12 SEs run production engagements.

A significant share of the revenue below was earned without Bruce in the room. His most common mode is not customer-facing: he consults with account SEs and account managers on technical strategy, gives them the architectural background and education, hands over resources — repositories, code, labs, reference designs — and they carry it to their customers themselves. The pattern originates at Microsoft and repeats at Meta, Google, and CoreWeave.
// I asked the agent to not characterize me as 'not customer facing'. I'm absolutley customer facing, however, I'm also a force multiplier in that my training and prep work with account teams allows them to go and sell without needing me in the room

**Web culture influence:** Bruce aligned Cisco's Web selling motion with hyperscaler-style thinking — open NOS, disaggregation, Linux tool-chains, and API-driven forwarding — which underpins the strategic investments in SONiC and Silicon One behind multiple accounts below.

---

## Revenue Summary *(finance segment data — Web/Hyperscale, 2022–2026)*

Finance-provided **Americas Web/Hyperscale segment bookings** by customer (USD). These are org-level figures, not individual attribution; they validate scale of Bruce's assigned theater and anchor account narratives below.

| Customer         | 2022               | 2023               | 2024             | 2025               | 2026               | Total               |
| ---------------- | ------------------ | ------------------ | ---------------- | ------------------ | ------------------ | ------------------- |
| Microsoft        | $603,378,443       | $713,506,622       | $225,591,710     | $861,488,473       | $1,571,150,100     | $3,974,611,348      |
| Google            | $403,924,231       | $102,597,166       | $108,203,941     | $286,867,842       | $1,049,281,606     | $1,949,286,786      |
| Meta              | $276,624,163       | $366,605,459       | $53,738,157      | $509,680,939       | $1,908,504,682     | $3,111,015,400      |
| Amazon           | $127,242,440       | $69,085,644        | $195,597,129     | $296,405,003       | $717,319,516       | $1,405,649,732      |
| Oracle           | $4,387,003         | $45,316,394        | $229,994,844     | $145,651,328       | $20,552,878        | $445,856,447        |
| Apple            | $726,231           | $7,542,020         | $10,246,872      | $6,812,501         | $11,249,631        | $36,557,255         |
| Web Platforms    | $29,484            | $2,381             | $1,070,267       | $2,382,671         | $2,290,663         | $5,775,466          |
| **Yearly total** | **$1,416,311,995** | **$1,304,655,686** | **$824,442,920** | **$2,109,288,757** | **$5,280,349,077** | **$10,935,048,436** |

**Segment aggregate (2022–2026):** $10.9B booked across listed Web/Hyperscale customers. 2026 YTD alone is $5.3B (Meta $1.9B, Microsoft $1.6B, Google $1.0B lead the year).

*Account-level placeholders below remain for scope narrative and Bruce's role; reconcile with finance on SP (Bell, Verizon, etc.) and Global Impact segments separately.*

| Customer / Segment  | Scope                                                                        | Placeholder $                                                                                                                                                                                            | Bruce's role (summary)                                                                                                           |
| ------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Microsoft**       | DC, DCI, Metro                                                               | ~$2.0B                                                                                                                                                                                                   | Strategy consultant; SONiC training; SRv6 AI backend advocacy; POC labs; multi-tenant AI architecture; SRv6 in DC Frontend (dRH) |
| **Microsoft**       | WAN / SWAN                                                                   | ~$500M                                                                                                                                                                                                   | SR/SRv6 customer training; SL-API/SDN SWAN labs; 1.6T / multi-planar SRv6 modeling                                               |
| **Meta**            | WAN, EBB, RBB, BBF                                                           | ~$1.0B                                                                                                                                                                                                   | SL-API technique pioneer (post-MSFT SWAN); VXR POC labs; AI hackathon enablement                                                 |
| **Meta**            | BBF production win                                                           | **$17M booked** `[verify]`                                                                                                                                                                               | VXR lab setup; backbone re-entry; P200/Thunderjet path                                                                           |
| **Amazon**          | Silicon One, Direct Connect                                                  | ~$20M                                                                                                                                                                                                    | Switch silicon TAM modeling; feature development program management                                                              |
| **Google**          | GDC, B4 SR-MPLS                                                              | ~$20M `[verify]`                                                                                                                                                                                         | SRv6 proposal and training; interim lead SE during account transition                                                            |
| **Oracle (OCI)**    | Frontend + backend DC / AI                                                   | ~$20M                                                                                                                                                                                                    | Lead architect SRv6 for AI; MRC and multi-tenancy                          |
| **CoreWeave**       | DC + WAN / AI                                                                | ~$20M FY26; FY27 estimates $150M DC switching, $245M optics, FY28-29 estimates $400M/year DC switching, $600+/year optics [source](https://cisco-my.sharepoint.com/:w:/r/personal/bgisiger_cisco_com/Documents/Desktop/Old%20Desktop/Web%20Operation%20Accounts/Big%20Projects/AI%20start-ups/CoreWeave/DC%20Switching/Back-end/CRD/CoreWeave%20DC%20Back-End%20Switching%20-%20Customer%20Requirements%20Document%20(CRD)%20v1.docx?d=w302ef71e18cc47529beaeb9e213af6a1&csf=1&web=1&e=mO6m5O) | SONiC SME; lead SRv6-for-AI architect                                                                                            |
| **Apple**           | Frontend DC                                                                  | ~$30M `[verify]`                                                                                                                                                                                         | SONiC on Cisco 8000, account strategy consultant                                                                                 |
| **Nvidia**          | Scale-Across WAN                                                             | ~$30M `[verify]`                                                                                                                                                                                         | Cisco 8223 , account strategy consultant                                                                                         |
| **Netflix**         | WAN                                                                          | ~$30M `[verify]`                                                                                                                                                                                         | CPOC architect, account strategy consultant                                                                                      |
| **Applied Digital** | AI infrastructure                                                            | ~$30M `[verify]`                                                                                                                                                                                         | Rail architecture and diagrams + AI calculator; solution spec                                                                    |
| **Salesforce**      | NG DC / SR                                                                   | `[verify]`                                                                                                                                                                                               | **Sep 2020:** A9K POC co-led w/ Asoka; SR/SRv6 mindshare (Oct 2023 exec preso)                                                   |
| **Americas SP**     | Bell, Verizon, AT&T, T-Mobile, Dish/Boost, Comcast, Equinix, Videotron, Riot | ~$100M+ partial                                                                                                                                                                                          | SR/SRv6, SP Cloud, K8s+Cilium, NaaS architecture, DC architecture, host-networking                                               |

**Aggregate (ASP+Web Web/Hyperscale segment, finance):** $10.9B booked 2022–2026 (table above). Tier-1 SP and Global Impact revenue tracked separately.

// Total Meta Silicon-1 revenue since 2021:  $178,275,649.89 
// Total Meta Cisco 8000 revenue since 2021:  $579,891,328.84  - I'm working to separate DC and WAN/Metro as I won't take credit for DC

// Total Microsoft WAN revenue since 2021:  $306,442,256.97 
// Total Microsoft AI/DC Cisco 8000 revenue since 2021:  $1,743,557,527.06  - I will speak with the account team to get their take on my contribution

// more to come

---

### Microsoft, 2021 – Present

| FY22  | FY23  | FY24  | FY25  | FY26   | **Total**  |
| ----- | ----- | ----- | ----- | ------ | ---------- |
| $603M | $714M | $226M | $861M | $1.57B | **$3.97B** |

*Americas Web/Hyperscale segment bookings. Bruce-attributed scope: ~$2.0B DC/DCI/Metro and ~$500M WAN `[verify]`. Cisco 8000 WAN revenue specifically: ~$65.9M (FY25) and ~$60M (FY26).*

Microsoft operates Azure, one of the two largest public cloud platforms in the world, and is Cisco's single largest Web/Hyperscale customer by bookings. Its AI infrastructure program spans a continent-scale super-factory WAN linking Fairwater DC sites in Wisconsin and Georgia, backbone growth from ~1,800 toward ~3,000 nodes, and a data center estate being re-architected around disaggregated hardware and open network operating systems. Bruce has served as architect and advisor across Microsoft's Frontend DC, WAN/Metro/DCI, SONiC, SRv6, and AI-backend programs since 2021, working directly with Microsoft's network engineering leadership while account SEs drive production engagements. This account carries the pattern that recurs across the rest of this section: Bruce equips the field and the customer with thought leadership, architecture, education, and labs, and the revenue is realized by others running with it.

**SRv6 for the AI Backend and SONiC on the Cisco 8122:** Beginning in 2024, Bruce argued inside Cisco that SRv6 for the AI backend was a production requirement rather than a research topic. Cisco engineering was skeptical, and the investment case for SRv6 on SONiC was not initially funded. Bruce built the technical and customer evidence that changed that position and led to Cisco support in 2026. Bruce's involvement and accomplishments include:

- Authored the SRv6 uSID multi-tenant AI fabric specification, which became the reference architecture for both the Microsoft and Oracle AI-backend engagements `[todo - upload a copy of the paper to Bruce's DSE onedrive folder and link here]`
- Built and published the [srv6-msft](https://github.com/segmentrouting/srv6-msft) and [srv6-mrc-emulator](https://github.com/segmentrouting/srv6-mrc-emulator) POC repositories, which Microsoft engineers used in their own internal executive presentations
// the srv6-msft repo is private and shared between myself and Microsoft architects. Would it make sense to take a screenshot of the github and upload it to the DSE onedrive and link here?
- Built the first SRv6-for-AI elephant-flow path-pinning demonstration (Nov 2024) as an internal proof point ahead of customer-scale POCs 
// further developed later and leveraged in Cisco Live srv6 lab
- Delivered SONiC training to Microsoft account SEs from 2024 forward, enabling the account team to scale its engagement across Microsoft's expanding SONiC use cases
- Secured MIG commitment for SRv6 on Cisco 8000 SONiC platforms in Q1 FY26 to unblock Microsoft and Oracle testing paths

The June 2026 release of **SRv6 on SONiC for the Cisco 8122 (G200 51.2T ASIC)** (202511 codebase) was the direct product outcome. 
// let's adjust this to SONiC on Cisco 8000 platforms (G-series and P-series silicon)
// also, this point and the last bullet in the list above are redundant

The architecture was validated; unfortunately the timing was not. Cisco has been late to market across successive switch-silicon generations — 12.8T, 25.6T, and 51.2T — and considering the speed at which the hyperscale market is currently moving, it often removes Cisco from consideration entirely. Microsoft and Oracle had both begun SRv6-for-AI deployments on competitor hardware before Cisco shipped, on the architecture Bruce had specified. The recurring pattern is the strategic argument: articulating the superior architecture does not recover the opportunity if the silicon is not there to carry it. FY2027 TAM recovery projection on G300 102.4T silicon: `[pending finance validation]`.

**PhyNet, disaggregated T2 and Regional Hubs:** Bruce is a primary Cisco SME on Microsoft's Frontend DC (PhyNet) and DCI/Metro (Regional Network Gateway or RNG), and on Microsoft's initiatives to disaggregate their chassis-based T2/Spine and DCI fabric layers into upper and lower pizza-box Clos tiers. Bruce's involvement and accomplishments include:

- Designed SRv6 tunnel-mesh architecture between disaggregated Regional Hubs, covering Ti-LFA, micro-loop avoidance, and selective FIB download at ~120k v4/v6 route scale // allowing Microsoft to deploy lower cost platforms with smaller fib scale
- Solved anchor-route, DCIX T2-to-T2 bypass, and IPv4 containment requirements against sub-second convergence targets
- Built both IOS-XR and SONiC/FRR prototypes for BGP GRT (Global Routing Table), BGP confederations, and SRv6-TE, on the disaggregated RH (dRH or disaggregated Regional Hub routing layer)
  // this project was highlighted on the global PSE/DSE call (June 2026 - verify) as the 9-POCs-at-once project, where Bruce was lauded for his use of agent-assisted-work enabling him to rapidly iterate through topologies and scenarios
- Developed and delivered the dRH SRv6-versus-VXLAN architecture comparison and a SONiC GRT lab POC to Microsoft lead architects Abhishek Dosi and Mohan Nanduri with Cisco engineering (Mar 2026)
- Ran the SRv6 DC-frontend POC (Aug 2025) across 4PE, DCIX, and a mixed IOS-XR/SONiC fabric, demonstrating prefix-hiding at scale and SRv6-TE for inter-DC traffic
- Generated lab scenarios — configurations, topologies, and documentation — using agent-assisted tooling, compressing POC development time and enabling MSFT architects to install the setup in their labs and demo internally

**1.6T WAN backbone and SWAN:** Cisco 8000 WAN revenue at Microsoft ran ~$65.9M in FY25 and ~$60M in FY26. The relationship behind it began before Bruce's PSE promotion with the IOS-XR **SL-API SWAN controller integration** — the technique that later transferred to Meta's backbone win and Google's Alphanet program, both detailed at their own entries below — and he has sustained it since in close partnership with **Senior SE Pan Chou**, delivering SR and SRv6 tutorials to the Microsoft WAN team and running a multi-planar architecture design session with them. Pan Chou owns the account relationship; Bruce supplies the architecture and the horizon-2 guidance behind it.
// see new $300M+ number above

Bruce developed the POC labs and field training for Microsoft's 1.6T backbone redesign, modeling node growth from ~1,800 to ~3,000, prefix expansion, sub-3-second convergence targets, and ISIS planes versus geographic domains. He positioned SRv6 uSID as the option that scales for decades — native IPv6 summarization, flow-label entropy, and extension to hosts and SmartNICs — and delivered two SRv6 WAN lunch-and-learn sessions to the Microsoft WAN team (Apr–May 2025).

**Financial impact:** $3.97B in Americas Web/Hyperscale segment bookings 2022–2026, of which ~$2.0B DC/DCI/Metro and ~$500M WAN fall within Bruce's engagement scope `[verify]`. Cisco 8000 WAN revenue specifically: ~$65.9M (FY25) and ~$60M (FY26). **Competitive impact:** Established SRv6-on-SONiC as a supported path on the Cisco 8000, closing the gap against competitor hardware already deployed in Microsoft's AI backend and Frontend DC, and positioned SRv6 uSID against VXLAN in the dRH frontend re-architecture. **Strategic impact:** The multi-tenant AI fabric specification became the reusable reference architecture for Oracle and CoreWeave; SRv6-on-SONiC productization opened the open-NOS AI-backend market across the entire hyperscale and neocloud segment. **Overall customer impact:** A repeatable disaggregated, open-NOS data center and backbone architecture that scales Microsoft's AI infrastructure without the route-scale and convergence ceilings of the prior design.
// see new high level revenue numbers commented in toward the top of the document

**Evidence:** [ASP Web FY20-26 Product Bookings](https://cisco.sharepoint.com/:x:/r/sites/GSPWEB-SalesandFinance/Shared%20Documents/ASP%20Web%20Finance/Adhoc/Q4%2726/ASP%20Web%20FY20-26%20Product%20Bookings.xlsx?d=wf735385979d541b6bdda11cfd8c7993f&csf=1&web=1&e=LUS3pf); GitHub `segmentrouting/srv6-msft`, `segmentrouting/srv6-mrc-emulator`; vault `customers/Microsoft AI-Backend.md`, `customers/Microsoft SRv6.md`, `customers/MSFT octans-drh.md`, `customers/Microsoft-WAN.md`, `innovation/SRv6-MultiTenant-Design-rev3.md`; Talent Assessment 1HFY26; published SWAN architecture reference — [ACM 10.1145/3603269.3604860](https://dl.acm.org/doi/pdf/10.1145/3603269.3604860) `[confirm this paper documents the SL-API/SDN forwarding technique Bruce pioneered]`.

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).
The productization of SRv6-on-SONiC and the multi-tenant specification are detailed in the Innovation section of this document. The internal advocacy that funded them is detailed in Span of Influence.

---

### Meta, 2021 – Present
// see updated revenue numbers commented in at the top of document

| FY22  | FY23  | FY24 | FY25  | FY26   | **Total**  |
| ----- | ----- | ---- | ----- | ------ | ---------- |
| $277M | $367M | $54M | $510M | $1.91B | **$3.11B** |

*Americas Web/Hyperscale segment bookings. First BBF production order — $17M booked, Feb 2026 `[verify]`.*

Meta operates one of the largest private backbones in the world, connecting a global data center estate that serves more than three billion daily users. Cisco had been displaced from Meta's backbone and was competing to re-enter against Arista and Broadcom Jericho silicon. Bruce has served the Meta account team as architecture and strategy consultant from 2021, equipping the account team with the architecture, the technique, and the labs, and they carried it to the customer themselves — enormous revenue impact delivered entirely through other people.

**Backbone Fabric (BBF) re-entry:** In April 2024 Meta opened what became a roughly two-year Express Backbone / Backbone Fabric evaluation cycle. Cisco needed to prove P200 silicon in an account where Arista was incumbent and where the customer validates independently rather than accepting vendor test results. Bruce's involvement and accomplishments include:

- Account strategy and architecture consultant since 2021
- Transferred the SL-API technique from its Microsoft SWAN origin to Meta, where it became the key technical differentiator in the backbone win
- Delivered SL-API, SDN, and Segment Routing enablement sessions to the Cisco account team, modeled on the Microsoft SWAN engagement (2022–2024), together with the technical background, reference material, repositories, and code they needed to run the customer conversation without him
- Built VXR-based POC labs that let the account SEs co-validate the EBB, BBF, and RBB architectures with Meta engineers before hardware was available
- Obtained an 8223 patch through his VXR team relationships in March 2026 when the hardware was not yet GA, unblocking account SEs Asoka DeSaram and Leif Berntsson at a critical point in the evaluation
- Asoka and Leif reused the VXR lab pattern in their participation in the Web-wide AI hackathon (May 2026)

Asoka on the March 2026 lab support: *"Thank you for helping us with the VXR setup. That was huge!!"*

Meta booked a $17M first production order for Cisco 8223-64EH (P200) on the BBF architecture in February 2026. BBF is estimated at ~$300M over two years, with the RBB pipeline cited at ~$350M/year `[verify]`. In February and March 2026 Meta committed RBB to SRv6, building on the same SL-API foundation.

**Financial impact:** $17M first production order booked Feb 2026; BBF estimated at ~$300M over two years and RBB pipeline at ~$350M/year `[verify]`; $3.11B in total segment bookings 2022–2026, including $1.91B in FY26. **Competitive impact:** Countered Arista's incumbency on the backbone and established Cisco as a credible second source in a multi-vendor global deployment — the re-entry point for a franchise Cisco had previously lost `[confirm framing with account team]`. **Strategic impact:** Proved that a technique developed at one hyperscaler transfers directly to another (see Microsoft, above, and Google, below, for the same transfer), and established the VXR co-validation lab as a repeatable pre-GA sales motion now reused across the Web segment. It also demonstrated the return on sustained internal architectural consultancy: five years of education and advocacy on SRv6 and SL-API, carrying no attributable revenue at the time, converted into a backbone franchise won by a team Bruce equipped rather than led. **Overall customer impact:** A validated backbone fabric architecture and a committed SRv6 path for RBB, with pre-GA access that let account SEs and Meta's engineers evaluate on their own terms rather than on vendor timelines.

**Evidence:** [ASP Web FY20-26 Product Bookings](https://cisco.sharepoint.com/:x:/r/sites/GSPWEB-SalesandFinance/Shared%20Documents/ASP%20Web%20Finance/Adhoc/Q4%2726/ASP%20Web%20FY20-26%20Product%20Bookings.xlsx?d=wf735385979d541b6bdda11cfd8c7993f&csf=1&web=1&e=LUS3pf); vault `customers/Meta.md`; DSE General MOC (Mar 2026 Asoka 8223 thread); SWAN architecture reference — [ACM 10.1145/3603269.3604860](https://dl.acm.org/doi/pdf/10.1145/3603269.3604860).

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).

**Note:** Meta was the second customer after Microsoft to adopt the SL-API/SDN/SR technique Bruce pioneered — the transfer is the strategic point, and Google (Alphanet) is now the third.
The origination of the SL-API technique is detailed in the Innovation section of this document. The VXR lab enablement pattern is detailed in the Leadership section.

---

### Oracle Cloud Infrastructure, 2023 – Present

| FY22 | FY23 | FY24  | FY25  | FY26 | **Total** |
| ---- | ---- | ----- | ----- | ---- | --------- |
| $4M  | $45M | $230M | $146M | $21M | **$446M** |

*Americas Web/Hyperscale segment bookings. Bruce-attributed scope: ~$20M `[verify]`; 2026–2028 projection `[verify]`.*

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

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).
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

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).

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

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).
Bruce's host-networking and Isovalent/Cilium advocacy is detailed in the Span of Influence and Innovation sections of this document.

---

### Google, 2021 – Present

| FY22  | FY23  | FY24  | FY25  | FY26   | **Total**  |
| ----- | ----- | ----- | ----- | ------ | ---------- |
| $404M | $103M | $108M | $287M | $1.05B | **$1.95B** |

*Americas Web/Hyperscale segment bookings. Bruce-attributed scope: ~$20M `[verify]`.*

Google operates one of the world's largest data center and AI footprints, and GCP is a rapidly growing competitor to AWS and Azure. Google's B4 transport network is one of the largest and most-studied private WANs in the world. Google Distributed Cloud extends their cloud services into customer and edge environments. Cisco holds a significant share of Google's backbone and GDC footprint, and the account requires engineers who can engage Google's network software teams as peers. Bruce served as strategy consultant, SRv6 architect, and — during a period of account SE leave — interim lead SE for WAN.

**GDC SRv6 and B4:** Bruce's involvement and accomplishments include:

- Developed the end-to-end SRv6 proposal and training program for Google Distributed Cloud, and led the GDCE onsite SRv6 design session (May 2024)
- Stepped in as interim lead SE on B4 SR-MPLS during account SE leave, maintaining continuity on Cisco's largest Google engagement
- Opened the SRv6 for Google AI Backend program (Mar 2026), running introductions and kickoff with Nick Sischo, Pablo Camarillo, and Clarence Filsfils
- Extended the SL-API technique to Alphanet — the third hyperscaler after Microsoft and Meta to adopt it

**Financial impact:** $1.95B in segment bookings 2022–2026, including $1.05B in FY26; ~$250M attributed to Bruce's engagement scope `[verify]`. **Competitive impact:** Maintained Cisco's backbone position through an account SE transition, and opened the SRv6 conversation in the AI backend — an account Cisco is still working into rather than one it has won. **Strategic impact:** A third independent hyperscaler engaged on SL-API, reinforcing that the technique transfers; the SRv6-for-AI thread is early and running with Cisco's SR engineering leadership directly involved. **Overall customer impact:** A defined SL-API path for Alphanet and an opening position on SRv6 for GDC and the AI backend.

**Evidence:** [ASP Web FY20-26 Product Bookings](https://cisco.sharepoint.com/:x:/r/sites/GSPWEB-SalesandFinance/Shared%20Documents/ASP%20Web%20Finance/Adhoc/Q4%2726/ASP%20Web%20FY20-26%20Product%20Bookings.xlsx?d=wf735385979d541b6bdda11cfd8c7993f&csf=1&web=1&e=LUS3pf); vault `customers/Google.md`.

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).

---

### Amazon Web Services, 2021 – Present

| FY22  | FY23 | FY24  | FY25  | FY26  | **Total**  |
| ----- | ---- | ----- | ----- | ----- | ---------- |
| $127M | $69M | $196M | $296M | $717M | **$1.41B** |

*Americas Web/Hyperscale segment bookings. Bruce-attributed scope: ~$20M Direct Connect / Silicon One `[verify]`.*

AWS is the largest public cloud provider in the world and one of the few customers with the scale to justify merchant silicon partnerships. Silicon One is Cisco's entry into that market, and the AWS relationship is the proof point that determines whether Cisco competes as a silicon supplier rather than only a systems vendor. Bruce served as internal consultant on Silicon One strategy for the account.

**Silicon One strategy and feature program:** Bruce's involvement and accomplishments include:

- Built the 12.8T → 25.6T → 51.2T TAM model with the account team and the customer, sizing the multi-generation silicon opportunity
- Project-managed feature development tracking between AWS and Cisco engineering, keeping roadmap commitments aligned to customer qualification timelines
- Opened the SRv6-for-AWS-telco-customers thread with Riggs and Christian Martin (Feb 2023), extending the silicon relationship into architecture. That thread did not convert

Cisco leadership recognized the foundational silicon deals at VP level in Q1 FY23 `[verify $]`.

**Financial impact:** $1.41B in segment bookings 2022–2026, including $717M in FY26; ~$20M Direct Connect / Silicon One attributed to Bruce's scope `[verify]`. **Competitive impact:** Opened a merchant-silicon position at the largest cloud operator, in a category Broadcom had held uncontested. The position is real but under-realized: Silicon One has lost addressable market to the same late-to-market pattern seen across the AI accounts, and the revenue booked is plausibly one to two orders of magnitude below what a closed time-to-market gap would have produced. **Strategic impact:** The generational TAM model became the basis for Silicon One planning across the Web segment, and remains the reference for sizing the recovery. **Overall customer impact:** A multi-generation silicon roadmap aligned to AWS's own qualification cadence.

**Evidence:** [ASP Web FY20-26 Product Bookings](https://cisco.sharepoint.com/:x:/r/sites/GSPWEB-SalesandFinance/Shared%20Documents/ASP%20Web%20Finance/Adhoc/Q4%2726/ASP%20Web%20FY20-26%20Product%20Bookings.xlsx?d=wf735385979d541b6bdda11cfd8c7993f&csf=1&web=1&e=LUS3pf); vault `xarchive-2021-2022/AWS-may-2021.md`, `dse/04-Span-of-Influence-MOC.md`, `dse/DSE General MOC.md`.

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).

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

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).
The Nicklous Morris / IETF connection is also referenced in Industry Impact's Operator Community section — same relationship, two facets (standards-adjacent origin here; commercial/technical thread there).

---

### Akamai, 2023 – 2025

**Revenue Impact:** `[verify]`

Akamai operates the world's largest content delivery network and, through its Linode and Prolexic businesses, a growing cloud and DDoS-mitigation platform. Akamai's backbone was moving off RSVP toward Segment Routing, and the customer's engineering leadership — John Leddy and Russ White — are among the most technically rigorous evaluators in the industry. Bruce led Cisco's SRv6 architecture engagement.

**Backbone SR/SRv6 transition:** Bruce's involvement and accomplishments include:

- Drove the RSVP-to-SR transition on the backbone alongside the 800G deployment, and gave a direct assessment of Silicon One SRv6-TE strengths and limitations rather than a positioning pitch — establishing the credibility the rest of the engagement ran on
- Built the FRR SRv6 L3VPN image and lab for Russ White (Oct 2023) and ran SRv6 use-case workshops with both Leddy and White (Feb 2024)
- Multiple SRv6 innovation threads with John Leddy (2023–2025) including the static uSID POC (Mar 2025) and the Prolexic-over-ADC lab, demo, and POC (Jun 2025)
- Built a POC multi-use case SDN controller (leveraging Bruce's open-source Jalapeno backend), which programmed SRv6 L3VPN routes onto a custom Linux forwarder for Prolexic's redirect-to-scrubber use case (2025 PDP) `[follow up on production status with account team]`

**Financial impact:** `[verify]`. **Competitive impact:** Established SRv6 as the backbone direction and positioned Cisco on the Linode and Prolexic paths. `[verify]` **Strategic impact:** The redirect-to-scrubber controller demonstrated host-based SRv6 policy on commodity Linux forwarding — the clearest customer-facing proof of the host-networking thesis, and a direct antecedent to the Cilium SRv6 product path. **Overall customer impact:** A validated SRv6 transition path for the backbone and a working DDoS-redirect prototype built on open forwarding.

**Evidence:** Vault `customers/Akamai.md`, `customers/Akamai SRv6.md`, `customers/Akamai-Prolexic SRv6.md`; Talent Assessment (May 2025 Jalapeno demo).

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).

---

## Additional ASP+Web Engagements

*Short-form entries. Trim to the summary table if page budget requires.*

---

### Videotron — SRv6 Regional Backhaul — Feb–Apr 2026

Videotron is Quebec's largest cable operator and, following its Freedom Mobile acquisition, a national wireless challenger. Bruce consulted as SRv6 subject-matter expert on the backhaul design interconnecting four MPLS-LDP regions over an IPv6 core with SRv6 gateways, and enabled SE Philippe Vaillancourt by giving him access to his Containerlab SRv6 lab to self-train ahead of the customer workshop. He coordinated Ianik, Jakub, and Dan Voyer for the onsite SRv6 update. **Revenue:** ~$25M `[verify]`.

---

### T-Mobile — Magenta Cloud Segmentation & Cilium — 2024–2025

T-Mobile is the second-largest US wireless operator. Bruce built the macro/micro/nano segmentation architecture narrative — Cilium policy, zone-based firewalling, eBPF/Tetragon, and ACI-versus-Cilium positioning — and supported the Overlay RFP (Nov 2024) and Magenta Cloud RFP (Dec 2024). He drove greenfield DC opportunities (Polaris, Tortugas), v6-only underlay design, and Hypershield/Cilium evaluation in MagentaCloud. `[verify which elements T-Mobile adopted versus deferred before this entry is final]`

**Vault:** `customers/T-Mobile.md`

---

### Dish / Boost Mobile — SRv6 L3VPN on AWS — 2025–2026

Boost Mobile runs the first US cloud-native 5G network, built on public cloud infrastructure. Bruce developed the SRv6 L3VPN over AWS architecture and proposal as a replacement for GRE tunnels — Cilium SRv6 uSID, cloud-native L3VPN at the pod level (`Boost-Cilium-SRv6.pptx`, Jan 2026). Recognizing that Cilium cannot directly address SR-IOV kernel-bypass networking, Bruce authored a multi-use-case Cilium customer requirements document that Cisco engineering has accepted and is working to prioritize — a proposal to position Cilium as the host-networking policy execution engine for both Kubernetes and non-Kubernetes workloads, including transit gateway and service-chain functions. This is the package's clearest example of end-to-end SRv6 and Cilium running entirely in public cloud.

The same Cilium CRD underpins the Verizon and Viasat engagements; it is detailed in the Innovation section of this document.

**Vault:** `customers/Boost SRv6.md`, `customers/cilium-srv6.md`

---

### Equinix — NGN / Disaggregation / SRv6 — 2023–2026

Equinix operates the world's largest interconnection and colocation platform. Bruce serves as SONiC, disaggregation, and SRv6 consultant and subject-matter expert on an ongoing engagement covering universal packet fabric evolution, SONiC/PINS POCs, and AI/ML reference architecture. At the November 2023 EBC he positioned SL-API as Equinix's bridge to disaggregation. The engagement has not yet produced a deployment decision.

**Vault:** `customers/Equinix.md`

---

### AT&T — NaaS / Inference Pods — Aug 2025

Bruce framed the inference pod and private AI cloud POC with Jim Durkin and Josh Fleishman, covering IPE cloud-connect routers and a phased go-to-market leveraging the AT&T network. The engagement ran through 2025 without advancing beyond discussion. `[Bruce decision — retain as breadth evidence or cut]`

**Vault:** `customers/AT&T NaaS.md`

---

### Applied Digital — AI Infrastructure — Sept 2024

Bruce's Web AI Fabrics calculator and rail architecture diagrams (Jun 2024) became a two-year scoping tool for Web SEs across the segment; the same artifacts sized the Applied Digital engagement. **Revenue:** ~$30M `[verify]`.

---

### Digital Realty — SRv6 POC — Oct 2025–present

Digital Realty is one of the two largest global colocation providers. Bruce drove the host-based and Cilium SRv6 component of the POC, standing up the deployment in the DLR lab (PDP Dec 2025), and served as subject-matter expert and evangelist for true end-to-end SRv6 — including the proposal that Digital Realty construct federated SRv6 partnerships with third-party service providers and neo-clouds, extending programmable transport across organizational boundaries rather than only within its own footprint. He presented Jalapeno at the Denver EBC and workshop (Jun 2025), where the second-generation RPO SDN application was deployed. `[verify $]`

On seeing Jalapeno, the customer remarked that they *"would have paid millions of dollars for something like this a couple of years ago — and here it is, open source."* `[confirm wording with account team before quoting]`

---

### Viasat — SRv6 Service Chaining & Slicing — 2024

Bruce designed the SRv6 service function chaining architecture with Don Ewald (May 2024), delivered the slicing and service-chain SRv6 demo with Chris Olson (Jul 2024), and opened the open-source controller thread at the October 2024 EBC. The same Cilium host-networking CRD proposal applies here. `[verify current status with account team]`

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

### eBay — SONiC EBC — Mar 2025

Bruce led the SONiC EBC with account team member Ken Truong, supporting eBay's open-NOS evaluation. `[verify revenue if any]`

---

### Voltage Park — SRv6 for DC — Jan 2024

Bruce presented the SRv6-for-data-center architecture to lead architect Drew Pletcher at an EBC, and again at the OCP 2024 kickoff cohort alongside Microsoft, Oracle, Bell, and Cloudflare. The thread did not convert to deployment `[verify ongoing pipeline with Drew/account team]`.

---

### Salesforce — A9K Displacement and NG DC — Sep 2020 – Oct 2023

Bruce co-led the SFDC A9K POC development and execution with Asoka (Sep 2020), leveraging prior relationship and mindshare. **2022:** $38M win displacing Juniper on A9K `[confirm ASP+Web classification]`. **Oct 2023:** Delivered the Segment Routing presentation positioning Salesforce's next-generation data center.

---

## Out-of-Territory Engagements

The engagements below sit outside Bruce's Americas Service Provider and Web assignment — enterprise, financial services, media, manufacturing, education, public sector, and regional operators. Field teams and enterprise theaters requested him by name for SONiC, SRv6, Cilium and eBPF, and cloud-scale architecture, when they needed a higher level of expertise than they had in their own organization. As with the in-territory accounts, much of this work was delivered through other engineers rather than in front of customers — Bruce supplied the architecture, the designs, the new or creative ideas, and the labs, and the local team ran the engagement.

That reach rests on a deliberate habit: over two decades Bruce has built and maintained working relationships with senior SEs, PSEs, and DSEs across Cisco without regard to geography or vertical alignment — relationships he sustains for the learning and idea exchange as much as for any engagement. It is why an APJC systems engineer, an EMEA data centre specialist, or a public-sector architect knows to call him.

---

### Geico, 2024

**Revenue Impact:** ~$1.6M SONiC on Cisco 8000 `[verify finance]`

Geico is the second-largest auto insurer in the United States and a Berkshire Hathaway company, expanding on-premises data center capacity in Colorado at roughly 118 racks with 32×100G top-of-rack in a leaf-spine design. Geico's infrastructure leadership intended the facility to serve as a shared resource across Berkshire Hathaway companies, which meant enterprise scale with hyperscale architectural and commercial expectations — and no Cisco architect in the enterprise theater with SONiC depth.

**SONiC data center fabric:** Geico had made a strategic decision to go open-source wherever possible and planned to deploy SONiC in a greenfield DC. Cisco Nexus was the incumbent; however, Geico had signaled a willingness to go with a competitor SONiC platform and demanded commercial terms that matched cloud-scale buying rather than traditional enterprise switching quotes. Bruce's involvement and accomplishments include:

- Served as SONiC subject-matter expert for the engagement, leading the data center architecture sessions (Mar 2024)
- Advocated directly with the business entity for a cloud and hyperscale-style pricing model to support Berkshire-wide infrastructure sharing — a commercial argument, not a technical one, made on behalf of an account he did not own
- Enabled the account team on leaf-spine design, the Q2 production timeline, and workload migration framing

**Financial impact:** ~$1.6M Cisco 8000 win `[verify finance]`. **Competitive impact:** Established SONiC on Cisco 8000 as viable for enterprise data center at a customer evaluating white-box alternatives. **Strategic impact:** Proved the hyperscale consumption model transfers to enterprise, and created a Berkshire Hathaway shared-infrastructure reference. **Overall customer impact:** A credible open-NOS data center path for a major insurer, with commercial terms matched to how they actually buy.

**Evidence:** Vault `customers/Geico.md`; 2HFY24 talent assessment.

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).

---

### Honeywell, 2024

**Revenue Impact:** ~$2M Segment Routing / Cisco 8000 `[verify finance]`

Honeywell is a Fortune 100 industrial conglomerate operating a global network spanning six colocation facilities and two private data centers on an NCS 5501 backbone, with SD-WAN headend integration and IoT transport segmentation requirements. Arista was positioning against Cisco in the backbone.

**Segment Routing backbone architecture:** Honeywell needed path preference from SD-WAN into the private backbone, an assessment of Flex-Algo for IGP-based path selection without a controller, and an SR/SRv6 roadmap. Bruce served as architecture subject-matter expert on the backbone design, SD-WAN integration options, and Flex-Algo use cases (Apr 2024), and consulted on future IoT transport segmentation and internal chargeback models.

**Financial impact:** ~$2M Segment Routing / Cisco 8000 win `[verify finance]`. **Competitive impact:** Held the backbone franchise against Arista. `[verify — confirm Arista was actively competing and displaced]` **Strategic impact:** Demonstrated that MIG transport expertise transfers directly to enterprise private backbones outside the SP segment. **Overall customer impact:** A controller-free path selection architecture aligned to Honeywell's global colocation footprint.

**Evidence:** Vault `customers/Honeywell.md`.

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).

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

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).
The Cilium SRv6 product path is detailed in the Innovation section of this document. Bruce's mentoring of Dan Stacks is detailed in the Leadership section.

---

### Fiserv, Jan 2026

**Revenue Impact:** Pipeline `[verify finance]`

Fiserv is one of the largest financial technology providers in the world, operating payment and banking infrastructure for thousands of institutions. The account sits outside ASP+Web; Bruce was engaged because the Enterprise team needed a top-level SME for the effort.

**SRv6 WAN and data center architecture:** Fiserv runs a Juniper RSVP-TE WAN overlay with VXLAN EVPN in the data center, and needed a credible path to extend a Segment Routing overlay end to end, simplify WAN-to-DC stitching, and evaluate geo-fencing and data-sovereignty steering — the same patterns Bruce had developed and fostered in numerous hyperscaler engagements — without a rip-and-replace program. Bruce delivered the SRv6 transfer of information to Fiserv's infrastructure team (Jan 2026), framed the WAN-to-DC extension with SD-WAN-to-SR anchor points and slice/shard/pinning in the data center, assessed Isovalent and Cilium relevance for the wireless private access context, and positioned SRv6 for AI backends for roadmap alignment.

**Financial impact:** Pipeline `[verify finance]`. **Competitive impact:** Opened an SRv6 displacement conversation against an incumbent Juniper RSVP-TE overlay. `[early — verify whether Fiserv has committed to a direction]` **Strategic impact:** Demonstrated that hyperscaler WAN patterns transfer to tier-1 financial services infrastructure. **Overall customer impact:** A staged simplification path from RSVP-TE to end-to-end Segment Routing without a forklift program.

**Evidence:** Vault `customers/Fiserv SRv6.md`. `[open question for Bruce: was this a single Jan 2026 TOI session, or has engagement continued into 2026? If continued, this entry can state more than "pipeline."]`

**Documents:** Supporting materials are accessible in the [external SharePoint repository](https://cisco-my.sharepoint.com/:f:/r/personal/brmcdoug_cisco_com/Documents/Bruce%20McDougall%20DSE%20Nomination?d=w4f5292c9f8444d96bc22a8e59bba44c5&csf=1&web=1&e=Hrh5ii).

---

### Texas Instruments, 2024

Texas Instruments operates a global manufacturing and design network spanning fabs, design centres, and points of presence on four continents. Bruce led an onsite architecture workshop covering the global Segment Routing network and the SRv6 roadmap, against Arista competitive framing. The workshop went well enough that TI attempted to recruit him. `[verify whether revenue followed]`

---

### Additional Americas Enterprise Engagements

| Customer                   | Period    | Bruce's contribution                                                                                                                                                                                     | Outcome                                                     |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Visa**                   | 2025      | Isovalent introduction; SR/SRv6 + demo of Jalapeno Resource Path Optimization app                                                                                                                        | Financial services pipeline `[verify]`                      |
| **Disney**                 | 2025      | Led a pair of SR-MPLS architecture discussions                                                                                                                                                           | Media enterprise; micro-segmentation and DPU considerations |
| **The Trade Desk**         | 2024      | SONiC and IOS-XR platform diversity evaluation                                                                                                                                                           | Ad-tech data center at neo-cloud scale                      |
| **Morgan Stanley**         | 2023      | SRv6 architecture presentation                                                                                                                                                                           | Financial services enablement                               |
| **NSight** *(regional SP)* | 2025–2026 | Cilium, Kubernetes, and AI-services architecture for the packet core team; same host-networking policy model as the Cilium CRD. A small engagement, but one only Bruce could staff — he is effectively the sole Cilium and Kubernetes SME across Americas SP and Web | Regional service provider (Green Bay)                       |

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

## Summary Table — ASP+Web Engagements (draft)

Ordered by strategic and financial weight, matching the body above. Segment bookings are org-level finance figures for Bruce's assigned theater, not individual attribution.

| Customer        | Segment      | Period       | Segment bookings 2022–26 | Outcome / pipeline                                                      | Bruce's role                                  |
| --------------- | ------------ | ------------ | ------------------------ | ----------------------------------------------------------------------- | --------------------------------------------- |
| Microsoft       | Web          | 2021–present | $3.97B                   | SRv6-on-SONiC 8122 shipped Jun 2026; PhyNet/dRH; 1.6T WAN               | Lead field architect; labs; internal advocacy |
| Meta            | Web          | 2021–present | $3.11B                   | $17M BBF booked Feb 2026; BBF ~$300M/2yr, RBB ~$350M/yr `[verify]`  | SL-API pioneer; VXR co-validation labs        |
| Oracle (OCI)    | Web          | 2023–present | $446M                    | SRv6 in limited production end-2025; Acceleron/MRC                      | Lead SRv6-for-AI architect                    |
| CoreWeave       | Neo-cloud    | 2025–present | ~$20M FY26               | FY27 $150M switching + $245M optics `[verify]`; scope → 10–12k switches | SONiC SME; lead SRv6-for-AI architect         |
| Bell Canada     | SP           | 2019–present | `[verify]`               | 400 CPE + $1.8M core, May 2026                                      | End-to-end SRv6 / Cilium / NaaS architect     |
| Google          | Web          | 2021–present | $1.95B                   | GDC SRv6; B4 SR-MPLS; AI backend kickoff Mar 2026                       | Strategy; interim lead SE; SL-API             |
| AWS             | Web          | 2021–present | $1.41B                   | Silicon One TAM model; feature program                                  | TAM modeling; PM tracking                     |
| Verizon         | SP           | 2024–present | `[verify]`               | SRv6 roadmap; Project Yukon NaaS; planned Cilium-SRv6 POC               | Architecture consulting; business case        |
| Akamai          | SP/CDN       | 2023–2025    | `[verify]`               | RSVP→SR backbone; redirect-to-scrubber controller                       | SRv6 SME; FRR/Linux forwarder labs            |
| Videotron       | SP           | 2026         | ~$25M `[verify]`         | SRv6 regional backhaul                                                  | Architect; SE enablement                      |
| T-Mobile        | SP           | 2024–2025    | `[verify]`               | Cilium segmentation; Magenta Cloud RFP                                  | Segmentation architecture                     |
| Dish / Boost    | SP           | 2025–2026    | `[verify]`               | SRv6 L3VPN on AWS underlay + Cilium                                     | Cloud-native L3VPN design                     |
| Equinix         | Web-adjacent | 2023–2026    | `[verify]`               | Universal packet fabric; SONiC/PINS                                     | SL-API disaggregation narrative               |
| AT&T            | SP           | 2025         | `[verify]`               | Inference pod / private AI cloud POC                                    | NaaS and AI pod framing                       |
| Applied Digital | Neo-cloud    | 2024         | ~$30M `[verify]`         | AI fabric sizing                                                        | Rail architecture + AI calculator             |
| Digital Realty  | Colo         | 2025         | `[verify]`               | SRv6 POC; Arista displacement path                                      | SRv6/Cilium POC lab                           |
| Salesforce      | Web          | 2020–2023    | $38M (2022) `[confirm]`  | A9K Juniper displacement; NG DC                                         | Co-led POC; SR positioning                    |
| Viasat          | SP           | 2024         | `[verify]`               | SRv6 SFC / slicing demo                                                 | Design + demo                                 |
| Comcast         | SP           | 2026         | ~$5M `[verify]`          | Load-balancing architecture                                             | Architecture consulting                       |
| Groq            | Web/AI       | 2025         | —                        | SR-TE POC succeeded; acquired by NVIDIA                                 | Flex-Algo / data sovereignty                  |
| Lambda Labs     | Neo-cloud    | 2024–2025    | `[verify]`               | Host-based SRv6; Isovalent EGW concept                                  | EBC lead; DC design                           |
| Cloudflare      | Web          | 2026         | —                        | BMP enhancements targeted 26.4.x                                        | Engineering consultation                      |
| eBay            | Web          | 2025         | —                        | SONiC evaluation                                                        | SONiC EBC lead                                |
| Voltage Park    | Neo-cloud    | 2024         | —                        | Did not convert to deployment                                           | SRv6-for-DC architecture                      |

---

## Vault Harvest Log — June 7, 2026

**Entry:** `dse/06-Business-Impact-MOC.md`
**Hubs:** `Hyperscale-Customers-Hub.md`, `SP-Customers-Hub.md`, `AI-Factory-Hub.md`, `SONiC-Hub.md`, `SRv6-Master-Hub.md`
**Customer notes read:** Microsoft (SRv6, AI-Backend, WAN, octans-drh), Meta, Oracle-SRv6, Coreweave (DC, backbone, lab), Bell Canada, Videotron SRv6, Verizon, Akamai (+ SRv6, Prolexic), T-Mobile, AT&T NaaS, Boost SRv6, Google, Equinix, cilium-srv6
**Revenue placeholders:** `01-exec-summary-draft.md` (all `[verify]`)

**Vault harvest log — PSE time log (2024–2026, full Notes):** Third pass Jun 7 2026 — Adobe rescue story, Geico Berkshire pricing, Meta 8223/VXR, MSFT AI-lab generation + dRH, OCI production by end-2025, Jalapeno RPO lineage, May–Jun 2026 MRC/multi-tenant/global transition.

**Gaps / Bruce to complete:**

- [ ] Finance-validated $ for all rows; reconcile Meta $2B vs $17M booked vs BBF $300M estimate
- [ ] John Dorval / MSFT WAN validation for SWAN claims
- [ ] Confirm: Akamai, Equinix, Salesforce, Lambda Labs, Riot Games, Viasat, Comcast in ASP+Web list
- [ ] Verizon / AT&T / T-Mobile pipeline $ where available
- [ ] **Verizon Cilium-SRv6 POC (new):** once scheduled/delivered, add outcome here and confirm whether it produces a Business Impact revenue line beyond the existing Verizon entry
- [ ] **Adobe ACV figure:** confirm the $750K→$1.6M renewal number and its attribution with the account team before this goes final — currently sourced only from the account SE's own account, not finance

**Open validation (from MOC):** "Would John Dorval agree with everything I write?" — MSFT WAN/SWAN narrative needs stakeholder review before final package.
