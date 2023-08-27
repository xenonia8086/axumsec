import socket
import sys
import requests
import re
import subprocess
import datetime
import time
from colorama import Fore



def dns_resolv(domain_name):


    resolv  = socket.gethostbyname(domain_name)
    print("\033[1;32;40m\n[+]Domain-name: " + domain_name)
    time.sleep(5)
    print("\033[1;32;40m \n[+]Host Address: " + resolv + "\n")


