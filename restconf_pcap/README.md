# RESTCONF Packet Captures
Collection of Wireshark `.pcapng` files. Currently contains:
  - GET, POST, PUT, DELETE, PATCH, and HEAD requests using JSON payloads
  - Device configuration management
  - Service management and application

__Note:__ RFC-8040 demands that RESTCONF always use HTTPS, but Cisco NSO
also allows it via plain HTTP. This may not be true in future releases.

Be sure to decode TCP port 8080 as HTTP before exploring these captures.

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
