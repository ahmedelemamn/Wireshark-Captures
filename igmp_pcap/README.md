# IGMP and MLD Packet Captures
Collection of Wireshark `.pcapng` files. Currently contains:
  - IPv4 Internet Group Management Protocol (IGMP) versions 1, 2, and 3
  - IPv6 Multicast Listener Discovery (MLD) versions 1 and 2
  - Any-source captures for all versions
  - Source-specific captures for IGMPv3 and MLDv2
  - Multicast Traceroute request and response
  - IGMPv2 and MLDv1 SSM mapping using DNS resolution
  - IGMPv2 SSM mapping using URL Rendezvous Discovery (URD)
  - Python Flask source code for trivial URD web server

# Pluralsight Course
These packet captures support my Pluralsight course titled
"Protocol Deep Dive: IGMP and MLD", accessible here:
`https://www.pluralsight.com/courses/protocol-deep-dive-igmp-mld`

Please check out this course if you'd like to better understand
the context/applicability of these packet captures.

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