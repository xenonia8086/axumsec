import socket
import sys
import requests
import re
import subprocess
import datetime
import time
from colorama import Fore

                                                                           
argv2 = "port"
status1 = "Open"
status2 = "Close"

port_numbers = [21,22,23,80,139,137,443,3386]

port_nums = list(range(10,1025))

def port_scan(h_addr, port_num):
    
   
    try: 
        p_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        p_sock.settimeout(1)

        c_sock = p_sock.connect_ex((h_addr, port_num))
         
        if c_sock == 0:

              
            print( str(port_num) + "\t\t\t" + status1 + "\n")
    except Exception as p_err:
        print("\033[1;31;40m Cannot lookup Host Address\n")
        print(f" \033[1;31;40m Error Occured: {p_err}")



  
   