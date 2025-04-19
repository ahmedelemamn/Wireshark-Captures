# Network Services Packet Captures
Collection of Wireshark `.pcapng` files. Currently contains:
  - Dynamic Host Configuration Protocol (DHCP) for IPv6 and IPv6 basics
  - DHCP IPv4/v6 relay and renewal operations
  - DHCPv6 prefix delegation (PD) over DMVPN
  - DHCP IPv4 for DMVPN spokes
  - Domain Name System (DNS) A, AAAA, PTR, NS, MX, SOA lookups
  - RFC-6555 Happy Eyeballs DNS Resolution Failover
  - Simple Network Management Protocol (SNMP) versions 1, 2c, and 3 polls/traps
  - SNMPv3 noauth/nopriv, sha1/nopriv, and sha1/aes128
  - Syslog with various facilities, formats, and transports
  - Network Time Protocol (NTP) with MD5 authentication
  - NTP client/server, symmetric active/passive, and multicast/broadcast
  - Remote Shell (RSH)
  - Telnet
  - Wake On LAN (WOL)
  - Windows Remote Desktop Protocol (RDP)
  - Virtual Network Computing (VNC)
  - Certificate Management Protocol (CMP)

To decode the Windows RDP packet capture, right-click any TCP port 3389
packet and select "Decode As". Then, select "TPKT" to see the details.

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
redistribution is prohibited. CMP PCAPs are not protected by this copyright.

All rights reserved.
