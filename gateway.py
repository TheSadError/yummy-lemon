import requests 
from colorama import *
import sys 


def gateway():
    print("[+] Starting gateway scanner...")
    for i in range(1,255):
        for j in range(1,255): 
            url = f"http://192.168.{i}.{j}"
            try : 
                gateway = requests.get(url)
                if gateway.status_code == 200:
                    print(Fore.BLUE+f"[+] IP Adress : {url}")
                    sys.exit(0)
            except :
                print(Fore.RED+f"[-] IP Adress : {url}")
