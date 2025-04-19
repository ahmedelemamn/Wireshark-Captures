# Network Address Translation (NAT) Packet Captures
Collection of Wireshark `.pcapng` files. Currently contains:
  - NAT44 using dynamic pools and port translation (PAT)
  - Twice NAT44 (concurrent source and destination translations)
  - Stateful NAT64 using dynamic pools and port translation (PAT)
  - Stateless NAT64
  - Stateless NAT66 (also called Network Prefix Translation or NPTv6)
  - All examples include port-based (UDP) and non-port based (ICMP) flows

## Usage and Warranty
I recommend using these files to see "what right looks like" and to use
as references during your own design and troubleshooting efforts. I am
not liable for any damages caused by the packet captured provided therein.
All addresses used (IP, MAC, etc.) are examples from lab environments
and any overlap in your production environment is coincidental.

## Copyright
Copyright 2020 Nicholas Russo.

Consumers may download and edit any document in this collection for personal
use only. Downloading and editing any document in this collection for
redistribution is prohibited.

All rights reserved.
