import socket
import sys
import requests
import re
import subprocess
from colorama import Fore
import datetime
import time
from dns import *
from port import *
from ping import *
from osx import *
from liscence import *

argv1 = "dns"
argv2 = "os"
argv3 = "netscan"
argv4 = "service"
argv5 = "ping"
argv6 = "all"




def banner():
    print(
        '''
        $$$$$$\  $$\   $$\ $$\   $$\ $$\      $$\        $$$$$$\  $$$$$$$$\  $$$$$$\  
        $$  __$$\ $$ |  $$ |$$ |  $$ |$$$\    $$$ |      $$  __$$\ $$  _____|$$  __$$\ 
        $$ /  $$ |\$$\ $$  |$$ |  $$ |$$$$\  $$$$ |      $$ /  \__|$$ |      $$ /  \__|
        $$$$$$$$ | \$$$$  / $$ |  $$ |$$\$$\$$ $$ |      \$$$$$$\  $$$$$\    $$ |      
        $$  __$$ | $$  $$<  $$ |  $$ |$$ \$$$  $$ |       \____$$\ $$  __|   $$ |      
        $$ |  $$ |$$  /\$$\ $$ |  $$ |$$ |\$  /$$ |      $$\   $$ |$$ |      $$ |  $$\ 
        $$ |  $$ |$$ /  $$ |\$$$$$$  |$$ | \_/ $$ |      \$$$$$$  |$$$$$$$$\ \$$$$$$  |
        \__|  \__|\__|  \__| \______/ \__|     \__|       \______/ \________| \______/ 
            ''')

def helpx():
    print('''                                                                            
    ------------------------------------------------------
                AXUM SEC TERMINAL HELP PAGE
    ------------------------------------------------------

    Welcome to AXUM SEC's Terminal Help Page! Below are


    DNS Commands:

        dns [domain-name]

    OS Commands:

        os [host]
        os [domain-name]

    Network Scanning:

        netscan [host]
        netscan [domain-name]

    Ping Commands:

        ping [host]           
        
    Service Scan: 

        service [host]

    ALL Scans: 

        all [host]
    ''')
banner()

port_nums = list(range(10,1025))
user_license_key = input("Enter your license key: ")
if user_license_key == stored_key:
    
   
   
        


    if len(sys.argv) > 1 and sys.argv[1] == argv1:
            if sys.argv[2] != 0:
                
                scan_time = datetime.datetime.now()
                print("\nAxum-Sec Scan Started at", scan_time)
                dns_resolv(sys.argv[2])
                exit()

    if len(sys.argv) > 1 and sys.argv[1] == argv3:
            if sys.argv[2] != 0:
                
                scan_time = datetime.datetime.now()
                print("\nAxum-Sec Scan Started at", scan_time)
                print("\033[1;32;40m \nPort\t\t\tStatus\n")
                for port_num in port_nums:
                    port_scan(sys.argv[2],port_num)
                    

            else: 
                banner()
                helpx()

    if len(sys.argv) > 1 and sys.argv[1] == argv5:
        if sys.argv[2] != 0:
            
            scan_time = datetime.datetime.now()
            print("\nAxum-Sec Scan Started at", scan_time)
            target_ip = sys.argv[2]
            idnt = 12345
            num_of_requests = 10  
            

            for sequence_number in range(1, num_of_requests+1):
                try:
                    pingy(target_ip, idnt, sequence_number)
                    print(f"\nICMP request {sequence_number} Sending to {target_ip}")
                    if sequence_number == 10:
                        print(Fore.GREEN + f"\nHost address {target_ip} is up\n")
                except PermissionError:
                    banner()
                    print("\nRun Commands as root\n")
                    exit()
                
                time.sleep(1)

            raw_socket.close()

    if len(sys.argv) > 1 and sys.argv[1] == argv2:
        if sys.argv[2] != 0:
           
            scan_time = datetime.datetime.now()
            print("\nAxum-Sec Scan Started at", scan_time)
            target_address = sys.argv[2] 

            operating_inf = os_fingerprinting(target_address)
            print(f"\033[1;31;40m\nThe guessed operating system of {target_address} is: {operating_inf}")
        
else:
    print("\nLicense is not valid.\n")
    exit()

