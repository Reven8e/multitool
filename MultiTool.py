import subprocess
from colorama import Fore

def start():
    subprocess.call('clear', shell=True)

    print(f"{Fore.BLUE}[1] Port Scanner.\n[2] BoganBuster (web dir searcher).\n[3] DDOS a target.\n[4] Proxy Checker and gen.\n[5] Shodan searcher.")
    print('\n')

    option = input('Please enter a number: ')

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
        from Modules.proxy_checker import start
        start()

    if option == '5':
        from Modules._shodan import Shodan
        shod = Shodan()
        shod.Search()


if __name__ == "__main__":
    start()

    while True:
        yes = ['yes', 'yep', 'y']
        no = ['no', 'nope', 'n']
        again = input(f'{Fore.BLUE}[CONSOLE] Anything else: ')
        print(' ')

        if again in yes:
            start()

        elif again in no:
            print(f'\n{Fore.YELLOW}[CONSOLE] Oke mate cya!')
            break