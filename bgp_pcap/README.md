# Border Gateway Protocol (BGP) Packet Captures
Collection of Wireshark `.pcapng` files. Currently contains:
  - IPv4/v6 unicast
  - IPv4/v6 multicast
  - IPv4/v6 flowspec
  - VPNv4/v6 unicast (6VPE)
  - VPNv4/v6 flowspec
  - IPv4/v6 Multicast MVPN (MVPN), AD and C-multicast signaling
  - IPv4 Multicast Delivery Tree (MDT)
  - IPv4 QoS Policy Propagation via BGP (QPPB) with communities
  - EIGRP and OSPF PE-CE extended communities
  - Route Target Constraint (RTC)
  - IPv4v6 labeled-unicast (6PE)
  - Link-state for MPLS TE topology transport
  - LDP-signaled VPLS
  - BGP-signaled VPLS
  - EVPN MPLS

For the sake of brevity, minor BGP features and behaviors
are limited to IPv4/v6 unicast captures and contain:
  - Standard communities
  - DMZ link bandwidth
  - Site of Origin (SoO)
  - Aggregation and AS set
  - Route reflection
  - Confederations
  - IPv4 NLRI over IPv6 session (including BGP unnumbered)
  - IPv6 NLRI over IPv4 session
  - 4-byte AS numbers: 4-to-4 and 4-to-2 interop
  - Graceful Restart (GR)
  - BGP additional paths capability (add-path)
  - Route refresh and peer reset
  - TTL security and TCP MD5/AO authentication
  - Various misconfigurations (duplicate RID, wrong ASN, etc.)
  - BGP Monitoring Protocol (BMP) initialization and exchange

## Usage and Warranty
I recommend using these files to see "what right looks like" and to use
as references during your own design and troubleshooting efforts. I am
not liable for any damages caused by the packet captured provided therein.
All addresses used (IP, MAC, etc.) are examples from lab environments
and any overlap in your production environment is coincidental.

For any BMP captures, be sure to use the "Decode As" feature for
TCP port 20000 and select "BMP" to view the messages.

## Copyright
Copyright 2021 Nicholas Russo.

Consumers may download and edit any document in this collection for personal
use only. Downloading and editing any document in this collection for
redistribution is prohibited.

All rights reserved.
