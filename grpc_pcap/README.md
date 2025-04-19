# Google Remote Procedure Call (gRPC) Packet Captures
Collection of Wireshark `.pcapng` files. Currently contains:
  - IOS-XR Configuration RPCs: GetConfig, MergeConfig, ReplaceConfig, and DeleteConfig
  - Telemetry encodings: Google Protocol Buffer (GPB), key/value GPB, and JSON
  - gRPC Network Management Interface (gNMI) RPCs: Capabilities, Get, Set, and Subscribe

## Usage and Warranty
I recommend using these files to see "what right looks like" and to use
as references during your own design and troubleshooting efforts. I am
not liable for any damages caused by the packet captured provided therein.
All addresses used (IP, MAC, etc.) are examples from lab environments
and any overlap in your production environment is coincidental.

Be sure to decode all TCP 5740 and 57400 packets as "HTTP2".

Optionally, Wireshark can expand the protocol buffer details if you supply the
`.proto` files, which are included in the `protobuf/` directory. You must
configure your Preferences/Protocols/Protobuf to reference this directory first.
Then, you will see additional details in Wireshark relating to protobuf fields.

## Copyright
Copyright 2020 Nicholas Russo.

Consumers may download and edit any document in this collection for personal
use only. Downloading and editing any document in this collection for
redistribution is prohibited.

All rights reserved.
