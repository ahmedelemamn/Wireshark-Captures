# Database Packet Captures
Collection of Wireshark `.pcapng` files. Currently contains:
  - MySQL Relational Database
  - Mongo Document Database
  - Influx Time-series Database

## Usage and Warranty
I recommend using these files to see "what right looks like" and to use
as references during your own design and troubleshooting efforts. I am
not liable for any damages caused by the packet captured provided therein.
All addresses used (IP, MAC, etc.) are examples from lab environments
and any overlap in your production environment is coincidental.

Wireshark may try to interpret Mongo as "SSL" or "TLS". Manually
choose "MONGO" for TCP port 27017 (*not* TLS port 27017).

## Copyright
Copyright 2021 Nicholas Russo.

Consumers may download and edit any document in this collection for personal
use only. Downloading and editing any document in this collection for
redistribution is prohibited.

All rights reserved.
