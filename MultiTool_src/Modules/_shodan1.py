import shodan
import subprocess, sys
from colorama import Fore


class Shodan1():
    def __init__(self):
        subprocess.call('clear', shell=True)

        print(f"""{Fore.RED}
  ██████  ██░ ██  ▒█████  ▓█████▄  ▄▄▄      ███▄    █ 
▒██    ▒ ▓██░ ██▒▒██▒  ██▒▒██▀ ██▌▒████▄    ██ ▀█   █ 
░ ▓██▄   ▒██▀▀██░▒██░  ██▒░██   █▌▒██  ▀█▄ ▓██  ▀█ ██▒
  ▒   ██▒░▓█ ░██ ▒██   ██░░▓█▄   ▌░██▄▄▄▄██▓██▒  ▐▌██▒
▒██████▒▒░▓█▒░██▓░ ████▓▒░░▒████▓  ▓█   ▓██▒██░   ▓██░
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░  ▒▒▓  ▒  ▒▒   ▓▒█░ ▒░   ▒ ▒ 
░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░  ░ ▒  ▒   ▒   ▒▒ ░ ░░   ░ ▒░
░  ░  ░   ░  ░░ ░░ ░ ░ ▒   ░ ░  ░   ░   ▒     ░   ░ ░ 
      ░   ░  ░  ░    ░ ░     ░          ░  ░        ░ 
                           ░                          
                           
        """)

        print(f"{Fore.BLUE}[CONSOLE] Please insert your Shodan api key.")
        print(f"{Fore.YELLOW}[INFO] Get your Shodan api key here: https://account.shodan.io/\n")
        shodan_key = input(f"{Fore.BLUE}Key: ")
        self.api = shodan.Shodan(shodan_key)
        print('')
        self.Type = print(f"{Fore.BLUE}[1] Shodan Searcher. (massive searcher)\n[2] IP Lookup. (Get info about an IP)")
        self.T = input('\nEnter a number: ')
        

    def Search(self):
        if self.T == '1':
            print('')
            obj = input(f"{Fore.BLUE}What do you want me to search for: ")

            try:
                search = self.api.search(obj)
                print(f'{Fore.YELLOW}Total results found: ' + str(search['total']))
                for result in search['matches']:
                    print(f"{Fore.GREEN}[FOUND] {result['ip_str']}")
                    print(f"{Fore.WHITE}{result['data']}")
                    print(f'{Fore.WHITE}-'*50)         
            except shodan.APIError:
                print(f"{Fore.RED}[ERROR] Api key is invalid!")

        elif self.T == '2':
            ip = input(f"{Fore.BLUE}\nEnter IP to check: ")
            host = self.api.host(ip)

            try:
                print(f'{Fore.YELLOW}\n----------INFO {ip}----------\n')
                print(f"{Fore.GREEN}IP: {host['ip_str']}\nOrganization: {host.get('org', 'n/a')}\nOperating System: {host.get('os', 'n/a')}")
                print('')
                for i in host['data']:
                    print(f"{Fore.GREEN}Port: {i['port']}\nBanner: {i['data']}")
            except shodan.APIError:
                print(f'{Fore.RED}[ERROR] Api key is invalid!')

            except shodan.exception.APIError:
                print(f"{Fore.RED} This IP does not exsists in Shodan's database")
