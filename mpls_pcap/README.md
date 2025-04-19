# Multi-Protocol Label Switching (MPLS) Captures
Collection of Wireshark `.pcapng` files. Currently contains:
  - Label Distribution Protocol (LDP) for IPv4 and IPv6 LSPs
  - Pseudowires: Ethernet, HDLC, PPP, Frame Relay, Interworking, and Flow-Aware Transport
  - RSVP-TE and TE-FRR (coalesced across entire path)
  - Active TE-FRR repair for unicast and multicast LSPs
  - TE extensions for IS-IS and OSPF (with mesh groups)
  - MPLS over Dynamic Multipoint VPN (DMVPN) phases 1, 2, and 3
  - MPLS-in-IP tunneling for IPv4 and IPv6 (protocol 137)
  - Multicast LDP (mLDP) default MDT (MP2MP) and in-band (P2MP) signaling
  - Draft Rosen PIM/GRE Multicast default VPN
  - Tag Distribution Protocol (TDP) basic init
  - MPLS Transport Profile (TP) with OAM and BFD
  - LSP Verification (LSPV) for IPv4/v6, pseudowire, RSVP-TE, mLDP, and TP

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