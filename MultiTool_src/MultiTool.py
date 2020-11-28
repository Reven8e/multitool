# © MultiTool- Made by Yuval Simon. For www.bogan.cool

import subprocess, time, sys
from colorama import Fore


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
    print(f"{Fore.BLUE}[1] Port Scanner.\n[2] BoganBuster (web dir searcher).\n[3] DDOS a target.\n[4] Proxy Checker and gen.\n[5] Shodan searcher.\n[6] Vulnerabilities searcher. (exploit db)\n[7] SQL Injection tester.\n[8] Quit. ")
    print('\n')

    option = input(f'{Fore.BLUE}[CONSOLE] Please enter a number: ')


    if option == '1':
        from Modules.port_scanner import start_scan
        start_scan()

    if option == '2':
        from Modules.BoganBuster import start_all
        start_all()

    if option == '3':
        from Modules.ddos import start_all
        start_all()

    if option == '4':
        from Modules.proxy_checker import start_proxy
        start_proxy()

    if option == '5':
        from Modules._shodan1 import Shodan1
        shod = Shodan1()
        shod.Search()

    if option == '6':
        from Modules.exploit_db import exploit_db_
        e = exploit_db_()
        e.searcher()

    if option == '7':
        from Modules.sql_tester import start_sql_
        start_sql_()

    if option == '8':
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

        yes = ['yes', 'yep', 'y']
        no = ['no', 'nope', 'n']
        again = input(f'{Fore.BLUE}[CONSOLE] Anything else: ')
        print(' ')

        if again in yes:
            start()

        elif again in no:
            print(f'\n{Fore.YELLOW}[CONSOLE] Oke mate cya!')
            break
        