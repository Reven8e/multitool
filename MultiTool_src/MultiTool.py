# © MultiTool- Made by Yuval Simon. For www.bogan.cool

import subprocess, time, sys
from colorama import Fore
from Modules.BoganBuster import Bogan
from Modules.proxy_checker import Proxy_Checker
from Modules._shodan1 import Shodan1
from Modules.exploit_db import exploit_db_
from Modules.ssh import Main
from Modules.port_scanner import scanner

yes = ["yes", "y", "ye", "Y", "YES", 'YE']
no = ["no", "n", "NO", "n"]

def start():
    global el
    subprocess.call('clear', shell=True)

    print(f"""{Fore.YELLOW}                                                              
 ███▄ ▄███▓ █    ██  ██▓  ▄▄▄█████▓ ██▓▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓██▒▀█▀ ██▒ ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██▒▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▓██    ▓██░▓██  ▒██░▒██░  ▒ ▓██░ ▒░▒██▒▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
▒██    ▒██ ▓▓█  ░██░▒██░  ░ ▓██▓ ░ ░██░░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
▒██▒   ░██▒▒▒█████▓ ░██████▒▒██▒ ░ ░██░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░▓    ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░  ░      ░░░▒░ ░ ░ ░ ░ ▒  ░  ░     ▒ ░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░      ░    ░░░ ░ ░   ░ ░   ░       ▒ ░  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
       ░      ░         ░  ░        ░               ░ ░      ░ ░      ░  ░
                                                                                                                          
        """)

    el = False
    print(f"{Fore.BLUE}[1] Port Scanner.\n[2] BoganBuster (web dir searcher).\n[3] DDOS a target.\n[4] Proxy Checker and gen.\n[5] Shodan searcher.\n[6] Vulnerabilities searcher. (exploit db)\n[7] SQL Injection tester.\n[8] SSH Bruteforcer\n[9] Quit.")
    print('\n')

    option = input(f'{Fore.BLUE}[CONSOLE] Please enter a number: ')


    if option == '1':
        scanner().main()

    elif option == '2':
        Bogan().main()

    elif option == '3':
        from Modules.ddos import DDOS
        DDOS().start_all()

    elif option == '4':
        Proxy_Checker().start()

    elif option == '5':
        Shodan1().Search()

    elif option == '6':
        exploit_db_().searcher()

    elif option == '7':
        from Modules.sql_tester import start_sql_
        start_sql_()

    elif option == '8':
        Main().start()

    elif option == '9':
        sys.exit()

    else:
        print('Incorrect number! ')
        el = True


if __name__ == "__main__":
    start()

    while True:
        while True:
            if el == True:
                time.sleep(1.5)
                start()
            else:
                break

        again = input(f'{Fore.BLUE}[CONSOLE] Anything else: ')
        print(' ')

        if again in yes:
            start()

        elif again in no:
            print(f'\n{Fore.YELLOW}[CONSOLE] Oke mate cya!')
            break
        