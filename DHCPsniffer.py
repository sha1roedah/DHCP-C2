# Script developed to sniff for DHCP packets and 
# append Option header 181 to an executable file

# Developed by Sean Roe

#! python

import sys, os, re
from scapy.all import *



def print_options(pkt):
    if DHCP in pkt: 
        return pkt.sprintf("%DHCP.options%")

if __name__ == "__main__":
    while True:
        targetFile = os.path.join('C:/Users/user/Desktop/options.txt') 
        newFile = os.path.join('C:/Users/user/Desktop/custom_options.bat')

        os.system('ipconfig /release')
        time.sleep(10)
        os.system('ipconfig /renew')

        sys.stdout = open(targetFile, 'w')
        print(sniff(prn=print_options, filter="DHCP", count=300))
        sys.stdout.close()


        with open(targetFile, 'rt') as openFile:
            for line in openFile:
                m = re.search(r'181\=.+?(?=\')', line)
                if m:
                    text=m.group()
                    sys.stdout = open(newFile, 'w')
                    print(text[5:])
                    sys.stdout.close()

                    with open (newFile, 'rb+') as swagFile:
                        swagFile.seek(-1, os.SEEK_END)
                        swagFile.truncate
                        swagFile.close()
                    break
            openFile.close()
        os.remove(targetFile)
        #time.sleep(10)

        
   

