# Layer-2 Encapsulation Packet Captures
Collection of Wireshark `.pcapng` files. Currently contains:
  - Ethernet, including 802.1Q and and ISL encapsulations
  - Ethernet Jumbo frames
  - Layer-2 tunneling via QinQ (802.1ad plus legacy Ethertypes) and QinISL
  - Provider Backbone Bridging (PBB) with 802.1ah MAC-in-MAC
  - Point-to-Point Protocol (PPP), including PAP and CHAP
  - PPP over Ethernet (PPPoE), including BNG connections
  - Cisco High-level Data Link Control (HDLC)
  - Frame Relay (FR), both Cisco and IETF encapsulations
  - FR DE/FECN/BECN signaling and Ethernet bridging
  - Asynchronous Transfer Mode (ATM) using AAL5-SNAP
  - Collection of all 802.1Q and 802.1ah priority and DEI values

## Usage and Warranty
For the legacy 802.1ad Ethertypes of 0x9100 and 0x9200, you may need
to manually use "Decade As ..." then select "VLAN" to see the packets.

I recommend using these files to see "what right looks like" and to use
as references during your own design and troubleshooting efforts. I am
not liable for any damages caused by the packet captured provided therein.
All addresses used (IP, MAC, etc.) are examples from lab environments
and any overlap in your production environment is coincidental.

## Copyright
Copyright 2021 Nicholas Russo.

Consumers may download and edit any document in this collection for personal
use only. Downloading and editing any document in this collection for
redistribution is prohibited.

All rights reserved.