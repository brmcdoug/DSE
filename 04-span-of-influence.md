## span of influence section


### Package criteria / section description:

Span of Influence
Suggested length: 2-3 pages 

•	Provide a high-level summary of how your span of influence has expanded, using a bulleted list or a table to show the transition. A detailed version of the span of influence can be added to the appropriate section of the package (business impact, innovation, SE leadership, etc.).
•	Chronological format with the most recent span of influence first.
•	See slides 24-25 in the Nomination Kit for a detailed overview of the criteria.

•	Interact and impact at higher levels internally in Cisco and externally with customers and partners.
•	Specialization & Focus (see PSE criteria) for at least two technology domains/architectures etc., 
•	The impact is more strategic and focuses on horizon 2-3


### Body of work:

Explain the impact
Web, hyperscale, SRv6 for AI, SONiC and SR in GES, Yukon++, SP-NaaS-cloud-like consumption, host-based SRv6, SR-Apps, SL-OnDemand, FE-Segmentation, EMEA NetCo/ServCo, programmability SME,  (Skylight & YANG), Isovalent acquisition

I put host-based networking and host-based SR/SRv6 on the map
* Isovalent acquisition - began advocating for Cisco to have a host-networking strategy and solution circa 2014-2015, really focused after PSE promotion on K8s/cloud-native aspect. Saw Cilium and their use of eBPF as a strategic gamechanger and began advocating for acquisition as early as 2021. Isovalent may become one of our most impactful acquisitions in a decade as the underlying eBPF technology will play a huge role in not only networking and segmentation, but also security in the AI era - runtime security, the Live Protect product in all route/switch products
* SONiC in general and SONiC SRv6 in particular - see MSFT/Oracle/OpenAI/Coreweave efforts and MRC architecture/innovation
* Single OS working gtroup - with DSEs Brenden Buresh, Craig Hill, Virginia Teixeira, and PSE Rob Murphy; produced and presented a recommendation to senior leadership which articulated the market share risks and dynamics tied to Cisco's dated multi-OS product siloes. Recommended a multi-year project where we collapse down to a single NOS based on SONiC or an open-source sonic-like solution
  * With the advent of Mythos and truly advanced AI security challenges the single-OS working group will reform and push very hard on security and patching as a key driver for collapsing/reducing our NOS', which will enormously reduce our vulnerability surface.
* Future Enterprise Segmentation working group - led findings and advocacy for reduction in the number of segmentation technologies (VXLAN, SRv6) and to use SGTs as a common micro-segmentation technology end-to-end. Led to my realization that SGTs and uSIDs are the same 16-bit length and could be combined to form new end-to-end services that cross domains (enterprise/SP) all while carrying and maintainning identity and microsegmentation capability 
* PSE committee - served three years as subcommittee / voting member

This is not necessarily a CL outcome, but both the SDWAN and SSE engineering teams have started talking about SRv6 support as a key differentiator for them as they justify development resources
The future - the OS will be linux, routing and other packet processing services will be hardware accelerated apps. they may be decoupled, underlay control plane is still a routing protocol, but service control plane could be Cilium

### MOC notes
## Summary
Evidence of strategic influence expanding from regional technical SME to global cross-functional leadership. Impact spans Cisco Engineering (Business Units), Product Management, and CXO-level customer engagements, focusing on Horizon 2-3 architectures.

## span of influence section


### Package criteria / section description:

Span of Influence
Suggested length: 2-3 pages 

•	Provide a high-level summary of how your span of influence has expanded, using a bulleted list or a table to show the transition. A detailed version of the span of influence can be added to the appropriate section of the package (business impact, innovation, SE leadership, etc.).
•	Chronological format with the most recent span of influence first.
•	See slides 24-25 in the Nomination Kit for a detailed overview of the criteria.

•	Interact and impact at higher levels internally in Cisco and externally with customers and partners.
•	Specialization & Focus (see PSE criteria) for at least two technology domains/architectures etc., 
•	The impact is more strategic and focuses on horizon 2-3


### Body of work:

### Explain the impact

My span of influence: i'm a trusted advisor to customers and Cisco account teams covering Web, hyperscale, Cloud, service provider, Enterprise, and Public Sector. I am often called upon to discuss or consult on leading edge products and architectures, or when the goal is to demonstrate Cisco's thought leadership and ability to be visionary. I am the sought after horizon 2-3 guy, the "2030 guy"

My span of influence with Cisco product engineering includes IMI BU (Cisco 8000 and predecessor platforms), SRv6 for AI, SONiC, SR and SRv6 in Enterprise focused platforms like SDWAN, IOS-XE, NXOS, Cisco Secure Access, and Isovalent/Cililum. 

in GES, Yukon++, SP-NaaS-cloud-like consumption, host-based SRv6, SR-Apps, SL-OnDemand, FE-Segmentation, EMEA NetCo/ServCo, programmability SME,  (Skylight & YANG), Isovalent acquisition

### Span of Influence Transitions

| Level of Influence | From (Principal SME - Horizon 1) | To (Distinguished Leader - Horizon 2/3) |
| :--- | :--- | :--- |
| **Cisco Engineering & Product** | Technical SME for individual SRv6 features and protocol testing. | **Strategic Advisor to IMI (Cisco 8000), SDWAN, and Security BUs.** Driving the adoption of SRv6 uSID as a unified "Network API" across all OS platforms (IOS-XE, NXOS, SONiC). |
| **Customer & Partner Architecture** | Delivering regional SRv6 pilots and design validation (e.g., Bell Canada). | **The "2030 Guy" for Global Hyperscalers.** Architecting 1B-scale AI Fabrics and cloud-native service brokerage for Web, SP, and Enterprise giants globally. |
| **Strategic Innovation** | Prototyping individual apps in labs. | **Visionary for Host-Based Networking.** Provided the architectural validation for host-based SRv6 that informed the Isovalent acquisition and the "Single OS" (SOSIE) vision. |

### My Most Important Contributions and Their Impact

#### 1. Host-Based Networking 
*   **The Vision:** I was an early visionary identifying that the center of gravity for network services was shifting to the host. My advocacy for host-based SR/SRv6 effectively put this architecture on the Cisco map.
*   **The Impact:** My technical validation of eBPF/Cilium integration with SRv6 preceded and informed the **Isovalent acquisition**, bridging the gap between Cloud-Native (K8s) and SP Transport.
*   **Links:** [[07-Innovation-MOC]], [[06-Business-Impact-MOC]], [[04-Span-of-Influence-MOC]], [[05-Industry-Impact-MOC]], [[03-Global-Impact-MOC]]

- CIPOL 2013, 2015
- First CL host-based SRv6 lab: 2023

 - **MRC** & SRv6 - validation of host-networking from industry titans OpenAI, Microsoft, Nvidia, AMD, BRCM: https://cdn.openai.com/pdf/resilient-ai-supercomputer-networking-using-mrc-and-srv6.pdf
 
 - **Empowering applications**: "A core principle of SRv6 is to give applications control over their network experience" - nearly word-for-word my framing since 2020. See CF LinkedIn/blog post: https://blogs.cisco.com/datacenter/mrc-and-srv6-how-foundational-networking-innovations-are-enabling-the-next-generation-of-ai-supercomputers

#### 2. SONiC SRv6 & AI Backend Strategy
*   **The Contribution:** Crucial contributor to the development of SONiC support for SRv6. While the "Phoenix Wing" effort (Alibaba-led) focuses on DCI/Metro, I am driving the **AI Backend and DC frontend** use cases.
*   **The Impact:** Securing Cisco's relevance in the open-source NOS market for Tier-1 Hyperscalers.
*   **Links:** [[07-Innovation-MOC]], [[06-Business-Impact-MOC]], [[05-Industry-Impact-MOC]]

#### 3. Cross-Domain "Network as an API" (SDWAN & SSE)
*   **The Contribution:** Driving SRv6 beyond traditional SP/Hyperscale boundaries into Enterprise platforms like SDWAN and Cisco Secure Access (SSE).
*   **The Impact:** Influencing SDWAN and SSE engineering teams to adopt SRv6 as a **key differentiator** for multi-domain policy enforcement and service steering.
*   **Links:** [[07-Innovation-MOC]]

#### 4. End-to-End Identity: SGT in uSID
*   **The Innovation:** Developed the architecture for populating Security Group Tags (SGT) in a uSID slot, carrying identity and micro-segmentation truly end-to-end within the SRv6 network program.
*   **The Impact:** Solved the "policy gap" between Enterprise identity and Hyperscale transport.
*   **Links:** [[07-Innovation-MOC]], [[03-Global-Impact-MOC]]

#### 5. Future Network OS (SOSIE) & Enterprise Segmentation
*   **The Vision:** Leading the **Single OS (SOSIE)** working group, envisioning a future where the NOS is Linux, with hardware-accelerated packet processing apps and a Cilium-based service control plane.
*   **The Impact:** Shaping the long-term (Horizon 3) strategy for how Cisco builds and sells networking software.
*   **Links:** [[07-Innovation-MOC]]

#### 6. SE Community & Talent Development
*   **The Contribution:** Active member of the **PSE Committee**, driving the standards for the next generation of technical talent within Cisco.
*   **Links:** [[10-SE-Leadership-MOC]]




### Engineering & BU Partnership (The "Field-to-BU" Bridge)
- **Collaboration with SR Inventor (Clarence Filsfils)**: Direct architectural exchange on SRv6 simplicity and "Network as an IPv6 Header" concepts (2020-2026).
- **Influence on Silicon Strategy**: Tracked and influenced AWS silicon strategy shifts (25.6T to 12.8T) at the steering committee level (2021).
- **Bold Bets Leadership**: Led the **only field-submitted project (Jalapeno)** to advance to the Validate phase in Cisco’s Bold Bets program.

### Executive & Global Influence
- **VP-Level Recognition**: Documented impact by VPs Eric Knipp, John Dorval, and Patrick Morrissey, citing over **$1B in influence** and "foundational silicon deals" (Amazon Q1FY23).
- **Global Theater Support**: Provided technical architecture for the first SRv6 deployment in ASEAN (Indosat Ooredoo) and global Cisco Live events.

## Strategic Transitions (Chronological)

### 2024 - 2026: Holistic Multi-Domain Leadership (Horizon 3)
- **Initiative: AI Factory & Hyperscale Strategy**
    - **Influence:** Driving the intersection of [[Silicon-Hardware-Hub|Silicon (G800)]], [[SONiC-Hub|SONiC]], and [[AI-Factory-Hub|AI Backends]].
    - **Cross-Domain:** Bridging Hardware (ASIC) and Software (SONiC) teams to deliver a unified AI infrastructure narrative.
- **Initiative: Phoenix Wing (Global Standards)**
    - **Influence:** External partnership with Alibaba and Microsoft; Internal alignment with Cisco Engineering to open-source SRv6 uSID for SONiC.
    - **Impact:** Strategic shift toward open-source NOS in the Tier-1 Hyperscale market.

### 2022 - 2024: Cross-Architecture Integration (Horizon 2)
- **Initiative: SRv6 Everywhere (Host to DC to WAN)**
    - **[[SRv6-Master-Hub|SRv6 in the DC]]**: Influencing Nexus/Data Center BU to adopt SRv6 uSID.
    - **[[Isovalent-Cilium-Hub|Cilium & eBPF Integration]]**: Strategic partnership with Isovalent (pre-acquisition) to drive SRv6 into the host/K8s layer.
    - **SRv6 for SDWAN**: Bridging the gap between Enterprise SDWAN and SP Core transport.
- **Project: [[Jalapeno|Jalapeno Network Service Broker]]**
    - **Influence:** Leading cross-functional teams (Eng, PM, Sales) to build a programmable network services platform.

### 2021: Regional to Theater SME (Horizon 1)
- **Initiative: SR-Apps & Programmability Roadshows**
    - **Influence:** Driving architectural adoption of SR-PCE and Segment Routing across the North American SP theater.
    - **Impact:** Established as the primary SME for Hyperscale network architecture.

## Holistic Technology Connections
- [[AI-Factory-Hub]]
- [[SONiC-Hub]]
- [[SRv6-Master-Hub]]
- [[Isovalent-Cilium-Hub]]
- [[Linux-Labs-Jalapeno-Hub]]
