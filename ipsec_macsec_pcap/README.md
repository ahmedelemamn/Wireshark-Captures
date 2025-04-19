# IPsec and MACsec Packet Captures
Collection of Wireshark `.pcapng` files. Currently contains a combination
of Authentication Header (AH) and Encapsulating Security Payload (ESP)
encapsulation techniques combined with NAT Traversal (NAT-T) and Generic
Routing Encapsulation (GRE) across tunnel and transport modes:
  - AH transport
  - AH transport + GRE
  - AH tunnel
  - AH tunnel + GRE
  - ESP-null transport
  - ESP-null transport + GRE
  - ESP-null transport + NAT-T
  - ESP-null transport + NAT-T + GRE
  - ESP-null tunnel
  - ESP-null tunnel + NAT-T
  - ESP-null tunnel + GRE
  - ESP-null tunnel + NAT-T + mGRE
  - ESP-null tunnel + GETVPN
  - ESP-AES transport
  - ESP-AES transport + GRE
  - ESP-AES transport + NAT-T + GRE
  - ESP-AES tunnel
  - ESP-AES tunnel + GRE
  - ESP-AES tunnel + NAT-T + mGRE
  - ESP-AES tunnel + GETVPN

Note that not all IPsec combinations are possible. For example:
  - AH can never transit NAT
  - ESP tunnel over NAT-T does not work with P2P GRE
  - GETVPN only supports tunnel mode, ESP, and can never transit NAT

MACsec 802.1ae captures:
  - Basic MACsec initialization
  - Encrypted and plain-text 802.1q tags
  - Various onfidentiality offsets and ICV indicator presence

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