[[Microsoft AI-Backend]]
[[07-Innovation-MOC]]
[[05-Industry-Impact-MOC]]
[[06-Business-Impact-MOC]]
[[microsoft-srv6-ai-backend-2025]]
### Partner with NIC providers
ConnectX8 - Coreweave
Bluefield3
AMD Pollara - need updated firmware

Which NICs are MSFT and OCI prioritizing
Team has CX8 and a few AMD servers w/Pollara NICs, ordering CX9

### Summary

Microsoft has developed a groundbreaking AI datacenter architecture, exemplified by its **Fairwater** superfactory, which utilizes a specialized, high-performance network fabric called ==**Multi-Path Reliable Connected (MRC)**==. This infrastructure is designed to treat geographically distributed datacenters as a single, cohesive AI compute system, designed to accelerate training for frontier models.

MRC moves the path selection decision from the network to the senders giving them explicit control over path selection. Senders distribute load on to different paths based on observed end-to-end path feedback such as ECN marks. This makes path selection adaptive with a closed end-to-end control loop. In contrast, traditional path selection in the network can be viewed as “open loop,” with switches making deterministic or adaptive load balancing decisions based on local or global visibility, but unaware of the impact of their decisions to the endpoint transport.

MRC defines two methods for selecting a path. It can modify the entropy of a packet by changing the UDP source port and rely on ECMP in the fabric. This allows for seamless usage over a traditional IP-routed network with BGP or controller-based route distribution.

A second approach relies on SRv6 micro-segments to explicitly define segment routed paths. The SRv6 approach, while seemingly contradictory to dynamic path selection, **allows a sender to associate *each connection with a group of paths*, and adaptively distribute load over them based on path feedback**. It gives senders precise control and awareness of the physical paths traversed in a network.

An additional advantage of the SRv6 approach is that segment-based forwarding tables in switches are small and can be statically computed based on topology construction at initialization time. When paths fail, the MRC protocol itself detects failures within a delay of a few RTTs (microseconds) and routes around them. The segment forwarding tables in switches don’t change. There is no dependency on BGP and longer transient convergence periods (often seconds) while the network state recovers from a topology change. Network-wide operational controllers can also proactively remove paths for maintenance by configuring path “black lists” at senders.

![[Pasted image 20260506133609.png]]

### Notes from MRC Paper

- Every data packet contains the RDMA virtual address and remote key so the receiving NIC can write each arriving packet to memory immediately, no matter the arrival order

- Each packet contains an entropy value (EV) that dictates its path through the network. The 32-bit EV is striped across the UDP source port and IPv6 flow label in an MRC packet. In a conventional network, changing the EV causes switches to hash each packet to a different path from the ECMP set. At QP startup, the sender generates an EV set for that QP—typically 128 to 256 entries. The sender then rotates through this set, using a different EV for each packet, so that all packets of a QP are sprayed across many paths on all planes in a multi-plane network without the application needing to know. This serves to load balance the network

- Spraying is hard to combine with the priority flow control (PFC) mechanism used in lossless Ethernet because a single flow reaches the last-hop switch over hundreds of paths. Further, PFC tends to create head-of-line blocking between different collectives, hurting tail latency. Thus MRC disables PFC and uses Ethernet in best-effort (lossy) mode

- The combination of best-effort Ethernet and out-of-order delivery places a greater burden on recovering losses quickly. MRC implements fast selective retransmission, using Selective ACK (SACK) packets to indicate precisely which packets have arrived at the receiver

- To further increase retransmission speed, especially under incast, MRC can use packet trimming [10, 20]. With packet trimming, a packet that would have been dropped due to congestion has its payload trimmed off and is priorityforwarded to the destination. The receiving NIC then generates a NACK to trigger fast retransmission. This also lets MRC distinguish congestion loss from other packet loss, which in AI clusters is mostly due to link flaps and failures

- A protocol like MRC, designed around packet spraying, is a very good fit for a multi-plane network. Each EV corresponds to a specific path on a specific network plane. When MRC generates its EV set, it chooses an equal number of EVs per plane. This immediately equalizes the traffic between planes. For each EV, MRC keeps a few bits of state about path health. In each switch, we enable Explicit Congestion Notification (ECN) in the normal randomized manner, but disable ECN on the last hop to the receiver.

- the traffic aggregate should not experience congestion, except from incast on the last hop, so ECN now acts as a load-balancing signal. The receiver echoes the ECN signal back to the sender, indicating that this specific path is more congested than others, and the sender temporarily avoids it. Different MRC senders do not coordinate when choosing their EV sets, so even though each sender load balances well, the aggregate may be slightly uneven. ECN-based load balancing smooths out this unevenness, keeping internal queues from growing enough to cause congestive loss

- When a packet is not trimmed but actually lost, MRC assumes the path has failed and immediately stops using the corresponding EV. Of course, not all loss is due to failed paths - packets can suffer bit errors or other issues - so permanently retiring an EV after one lost packet may leave us short of working EVs. To avoid this, MRC sends background path probes to determine whether paths it assumed were bad are actually bad, and also detect if failed links have recovered. If enough probes succeed, the EV is resurrected. 

- At this point **we have a transport protocol that can detect path failures and bypass them in a few tens of microseconds**



### Notes for srv6-ai-fabric project

- Every data packet contains the RDMA virtual address and remote key so the receiving NIC can write each arriving packet to memory immediately 
	- user note: for our emulator we simply substitute UDP to destination host lo (or ethX anycast)
- Each packet contains an entropy value (EV) that dictates its path through the network. The 32-bit EV is striped across the UDP source port and IPv6 flow label in an MRC packet. In a conventional network, changing the EV causes switches to hash each packet to a different path from the ECMP set. At QP startup, the sender generates an EV set for that QP—typically 128 to 256 entries. The sender then rotates through this set, using a different EV for each packet, so that all packets of a QP are sprayed across many paths on all planes in a multi-plane network without the application needing to know. This serves to load balance the network
	- user note: currently our host-routes are deployed as one route per plane per destination (each with an SRv6 encapsulation instruction. it sounds like we could emulate an EV set by having multiple host-routes per plane per destination...no need to go crazy, but perhaps 4 per plane per destination (16 total). the 4 per plane could be striped across spine nodes using srv6 uSID combinations. in this case the payload would be sprayed across 16 paths to a given destination. does that sound doable? In order to support this, and to account for which traffic used which EV/SRv6-path, should we include some index number in the generated packet?

	- user note: no pfc
	- user note: no need to reproduce the selective ack mechanism
	- user note: no need to process ECN
	- 
- other note, should our payload traffic use UDP port 4791?