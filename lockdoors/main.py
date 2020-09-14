import os
import sys
from pathlib import Path
from lockdoors import infogathering
from lockdoors import webhack
from lockdoors import exploitation
from lockdoors import reverse
from lockdoors import encdyc
from lockdoors import passattack
from lockdoors import shells
from lockdoors import privesc
from lockdoors import soceng
from lockdoors import psafrt
from lockdoors import wtpp
from lockdoors import about
from lockdoors import update
from datetime import datetime
from time import sleep
def printlogo():
    print("""
\033[94m            ..',,,'..           \033[0m
\033[94m         .',;;;;;;;;,'.         \033[0m
\033[94m      ..,;;;;;;;;;;;;;;,..      \033[0m
\033[94m     .,;;;,'..'''''.',;;;,.     \033[0m
\033[94m     .;;;;.  ..   .. .;;;;'     \033[0m\033[91m (                                         \033[0m
\033[94m     .,;;;.  ...     .;;;;.     \033[0m\033[91m )\ )               )  (                   \033[0m
\033[94m      ..,;,.  ...   .,;,..      \033[0m\033[91m (()/(            ( /(  )\ )           (   \033[0m
\033[94m        .';;'.    .',;'.        \033[0m\033[91m /(_))  (    (   )\())(()/(  (    (   )(   \033[0m
\033[94m    ..',,;;;;;,,,,;;;;;,,'..    \033[0m\033[91m (_))    )\   )\ ((_)\  ((_)) )\   )\ (()\ \033[0m
\033[94m  .','.....................''.  \033[0m\033[91m | |    ((_) ((_)| |(_) _| | ((_) ((_) ((_)\033[0m
\033[94m .',..',,,,,,,,,,,,,,,,,,,..,,. \033[0m\033[91m | |__ / _ \/ _| | / // _` |/ _ \/ _ \| '_|\033[0m
\033[94m .;,..,;;;;;;'....';;;;;;;..,;. \033[0m\033[91m |____|\___/\__| |_\_\\__,_|\___/\___/|_|  \033[0m
\033[94m ';;..,;;;;;,..,,..';;;;;,..,;' \033[0m\033[92m           © Sofiane Hamlaoui | 2020       \033[0m
\033[94m.';;..,;;;;,. .... .,;;;;,..;;,.\033[0m\033[92m Lockdoor : A Penetration Testing framework\033[0m
\033[94m ';;..,;;;;'  ....  .;;;;,..;;,. \033[0m\033[92m                 v2.2.4           \033[0m
\033[94m .,;'.';;;;'.  ..  .';;;;,.';,.  \033[0m
\033[94m   ....;;;;;,'''''',;;;;;'...    \033[0m
\033[94m       ..................\033[0m""")
config = str(Path.home()) + "/.config/lockdoor/"
def oktocont():
    ans = input("\033[0;36mPress Enter to Continue...\033[0m")
def clr():
    os.system('clear')
def spc():
    print("")
def prilogspc():
    printlogo()
    spc()
def clscprilo():
    clr()
    printlogo()
def popp():
    spc()
    oktocont()
    printlogo()
    spc()
def okenc():
    spc()
    oktocont()
    menu()
def pop():
    spc()
    oktocont()
    spc()
def okex():
    spc()
    oktocont()
    menu()
def okinf():
    spc()
    oktocont()
    menu()
def okpa():
    spc()
    oktocont()
    menu()
def okpr():
    spc()
    oktocont()
    menu()
def okrev():
    spc()
    oktocont()
    menu()
def oksh():
    spc()
    oktocont()
    menu()
def okso():
    spc()
    oktocont()
    menu()
def okwe():
    spc()
    oktocont()
    menu()
def getinstalldir():
    f = open(config + 'lockdoor.conf')
    contents = f.read().rstrip('\n')
    f.close()
    installdirc = contents.replace('Location:', '')
    return installdirc
def menu():
    os.system('clear')
    printlogo()
    print("""
    \033[94m         [ R00T MENU ]

            Make A Choice :\033[0m

        \033[93m1)  Information Gathering
        2)  Web Hacking
        3)  Exploitation
        4)  Reverse Engineering
        5)  Encryption/Decryption
        6)  Password Attacks
        7)  Shells
        8)  Privilege Escalation
        9)  Social Engineering
        10) Pentesting & Security Assessment Findings Report Templates
        11) Help with Walk Throughs & Pentest Processing\033[0m
        ------------------------
        \033[94ma)    About  Lockdoor
        u)    Update Lockdoor
        q)    Leave  Lockdoor\033[90m
        """)
    choice = input("\033[92mLockdoor~# \033[0m")
    os.system('clear')
    if choice == "1":
        infogathering.menu()
    elif choice == "2":
        webhack.menu()
    elif choice == "3":
        exploitation.menu()
    elif choice == "4":
        reverse.menu()
    elif choice == "5":
        encdyc.menu()
    elif choice == "6":
        passattack.menu()
    elif choice == "7":
        shells.menu()
    elif choice == "8":
        privesc.menu()
    elif choice == "9":
        soceng.menu()
    elif choice == "10":
        psafrt.psafrt()
    elif choice == "11":
        wtpp.wtpp()
    elif choice == "a":
        about.show()
    elif choice == "u":
        update.lockdoor()
    elif choice == "q":
        printlogo()
        print("")
        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        print("                 \033[91m-[!]- LOCKDOOR IS EXITING -[!]-\033[0m")
        print("")
        print("                 \033[91m-[!]- EXITING AT " + date + " -[!]-\033[0m")
        sys.exit()
    elif choice == "":
        menu()
    else:
        menu()