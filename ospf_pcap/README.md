# Open Shortest Path First (OSPF) Captures
Collection of Wireshark `.pcapng` files. Currently these OSPF versions/AFIs:
  - OSPFv2 for IPv4
  - OSPFv3 for IPv4
  - OSPFv3 for IPv6

The following captures exist for all AFIs:
  - Neighbor initialization with various network types
  - Authentication techniques
  - Various LSAs in isolation (including LSA6 for MOSPF)
  - Various area types
  - Multi-area adjacency
  - Prefix-suppression
  - Virtual-links
  - Common problems, such as neighbor MTU mismatch and flood war

Some speciality captures, such as TTL security for OSPFv2 and IPsec
encryption for OSPFv3, are also included.

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