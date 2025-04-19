# OpenFlow Packet Captures
Collection of Wireshark `.pcapng` files. Currently contains:
  - OpenFlow session setup to Faucet with flow modifications
  - Reactive flow modifications
  - Port statistics reporting

## Usage and Warranty
I recommend using these files to see "what right looks like" and to use
as references during your own design and troubleshooting efforts. I am
not liable for any damages caused by the packet captured provided therein.
All addresses used (IP, MAC, etc.) are examples from lab environments
and any overlap in your production environment is coincidental.

These captures use the standard OpenFlow TCP port of 6653 for Facuet
(SDN policy) and a custom TCP port of 6654 for Gauge (port statistics only).
Decode both "OpenFlow" if Wireshark does not automatically recognize them.

## Copyright
Copyright 2021 Nicholas Russo.

Consumers may download and edit any document in this collection for personal
use only. Downloading and editing any document in this collection for
redistribution is prohibited.

All rights reserved.
