# IP Tunnel Packet Captures
Collection of Wireshark `.pcapng` files. Currently contains:
  - GRE basic (no options)
  - GRE key, check, and sequence number options
  - GRE entropy key flows and keepalives
  - Encapsulated Remote Switchport Analyzer (ERSPAN)
  - Dynamic Multipoint VPN (DMVPN) Phases 1, 2, and 3
  - IPinIP and NOS/KAQ9 encapsulation for IPv4 only
  - Rate Based Satellite Control Protocol (RBSCP)
  - Locator/ID Separator Protocol (LISP) for IPv4/IPv6 EIDs
  - LISP PxTR native and LISP-encapsulated non-LISP connectivity
  - Automatic Multicast Tunneling (AMT) with IPv4/v6 overlay

## Usage and Warranty
I recommend using these files to see "what right looks like" and to use
as references during your own design and troubleshooting efforts. I am
not liable for any damages caused by the packet captured provided therein.
All addresses used (IP, MAC, etc.) are examples from lab environments
and any overlap in your production environment is coincidental.

NOS/KAQ9 compatible IPinIP encapsulation is not recognized by Wireshark.
Use "Decode As" to decode protocol 94 as "IPv4" for better visibility.

## Copyright
Copyright 2021 Nicholas Russo.

Consumers may download and edit any document in this collection for personal
use only. Downloading and editing any document in this collection for
redistribution is prohibited.

All rights reserved.