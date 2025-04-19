# HyperText Transfer Protocol (HTTP) Captures
Collection of Wireshark `.pcapng` files. Currently contains:
  - HTTP version 1.1
  - TLS-protected HTTPS/2 with optional decode
  - TLS-protected HTTPS/3 (QUIC) with optional decode
  - HTTP Proxy Caching with Squid
  - JSON-RPC payload exploration
  - Web Cache Communications Protocol (WCCP) version 2 setup
  - WCCP Layer-2 redirection with standard and dynamic services
  - WCCP GRE redirection with standard and dynamic services

To decode any HTTPS packet captures, configure Wireshark by updating
`Preferences > Protocols > TLS` to reference the pre-master SSL key
using the log file included.

Regarding the HTTPv1.1 capture, be sure to decode TCP port 5000 as HTTP.

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
