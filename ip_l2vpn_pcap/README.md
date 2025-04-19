# IP-based Layer-2 VPN Captures
Collection of Wireshark `.pcapng` files. Currently contains:
  - Layer-2 Tunneling Protocol version 3 (L2TPv3)
  - Overlay Transport Virtualization (OTV)
  - Virtual eXtensible LAN (VxLAN)
  - Network Virtualization using Generic Routing Encapsulation (NVGRE)
  - Stateless Transport Tunneling (STT)
  - Generic Network Virtualization Encapsulation (GENEVE)

## Notes on L2TP Captures
Wireshark can decode these captures, but sometimes it can be challenging.
Follow these tips:
  * For all L2TPv3 captures, decode the L2TPv3 payload as "Ethernet".
  * For any `uti` captures, decode the IP protocol 120 as "L2TP".
  * For any `auth` captures, adjust your Wireshark "Preferences" for the Protocol "L2TP" to statically identify the cookie size, in bytes, based on the capture you are exploring.

## Notes on OTV Captures
For all OTV-encapsulated traffic, decode the MPLS payload as "MPLS Protocol / Ethernet PW (no CW)".
Wireshark thinks there is a control-word (CW) by default, but there is not.

## Notes on STT Captures
These packets look like regular TCP to Wireshark by default. Right-click the TCP header and
"Disable TCP" to tell Wireshark to stop treating it as such.

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
