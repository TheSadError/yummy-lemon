import socket 
from colorama import *
# Created by TheSadError
"""
Lemon [Version 1.1.0]
(c) Lemon terminal created & developed by TheSadError [For more information type whoislemon].
"""
def scan(url):
    url = socket.gethostbyname(url)
    plst = [20,21,22,23,25,53,69,80,137,139,443,445,8080,8443]
    print(Fore.BLUE+"\tPort  \tSTATE  \tVersion")
    
    for port in range(0,len(plst)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((url,plst[port]))
        if result ==0:
            version = socket.getservbyport(plst[port], "tcp")
            print(f"\t{plst[port]}  \topen  \t{version}")
        s.close()
