# Quality of Service (QoS) Packet Captures
Collection of Wireshark `.pcapng` files. Currently contains:
  - RFC-4594 DSCP Markings on IPv4 and IPv6 packets
  - Ethernet 802.1p Class of Service (CoS) bits based on DSCP
  - MPLS Experimental (EXP) bits based on DSCP
  - IP Precedence (IPP) low delay, throughput, and reliability bits
  - Explicit Congestion Notification (ECN) for TCP flows
  - Resource Reservation Protocol (RSVP) for IPv4 VOIP
  - 802.3x Ethernet Flow Control ("Pause") frames
  - 802.1Qbb Priority-based Flow Control (PFC) frames

## Usage and Warranty
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