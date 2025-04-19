# Collaboration Packet Captures
Collection of Wireshark `.pcapng` files. Currently contains:
  - Dual-tone Multi-Frequency (DTMF)
  - Fax/modem
  - H.323 and H.245
  - Media Gateway Control Protocol (MGCP)
  - Real-time Transport Protocol (RTP) with various codecs
  - Skinny Client control Protocol (SCCP)
  - Session Initiation Protocol (SIP)

## Notes on captures containing RTP packets
The Wireshark-recognized UDP port range for RTP packets is 16384 to 32767.
Some captures use ports outside of this range. If you see large blocks of
unidentified UDP packets, this is voice traffic, and you should use
the Wireshark "Decode As" feature to select "RTP" to explore further.

## Usage and Warranty
I recommend using these files to see "what right looks like" and to use
as references during your own design and troubleshooting efforts. I am
not liable for any damages caused by the packet captured provided therein.
All addresses used (IP, MAC, etc.) are examples from lab environments
and any overlap in your production environment is coincidental.

## Copyright
Unlike most packet captures in the library, the collaboration resources are not
protected by copyright. You are free to distribute them without attribution.
Special thanks to Patrick Kinane for his help with this project.