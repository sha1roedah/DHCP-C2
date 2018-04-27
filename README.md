# DHCP-C2
Basic server/client program to issue remote commands over DHCP

Utilizes unreserved Option Header 181 to transmit data.

# Instructions

- Server side

  - Run the arpspoof.py script to spoof

  - Run the DHCP.py script. 

  - This will start the DHCP server and the listener will create a window where you can see DHCP DORAI packets in real time. 

  - Make sure to edit the Options Headers.

- Client-Side

  - Run DHCPSniffer.py. 

  - This will use SCAPY to sniff for DHCP packets and append option 181 to an executable .bat file in a specified directory
