# © Port Scanner- Made by Yuval Simon. For bogan.cool

import socket, subprocess, sys, time, os, threading
from colorama import Fore


class scanner():
    def __init__(self):
        subprocess.call('clear', shell=True)
        print(f"""{Fore.GREEN}
 ██▓███       ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▓██░  ██▒   ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒     ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░   ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░        ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░░          ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
                  ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
                     ░   
                                                                          
""")
        self.server = input(f"{Fore.BLUE}[CONSOLE] Enter ip/domain to scan: ")
        self.thr = int(input("Please enter threads number: "))
        self.to_scan = int(input("How many ports to scan (1k-10k): "))
        self.server_ip = socket.gethostbyname(self.server)

        try:
            os.remove('PortScanner/open_ports.txt')
        except:
            pass

        self.f = open('PortScanner/open_ports.txt', 'a+')
        self.good = 0

        print('\n\nStarting scan...')
        time.sleep(1)
        subprocess.call('clear', shell=True)

        print(f"{Fore.YELLOW}[CONSOLE] Target's IP: {self.server_ip}\n")
        print('-' * 30)
        print('\n')

    def scan(self, p):
        try: 
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            r = sock.connect_ex((self.server_ip, p))
            if r == 0:
                print(f'{Fore.GREEN}[CONSOLE] Found open port: {p}')
                self.f.write(f"Found open port: {p}\n")
                self.good += 1

        except KeyboardInterrupt:
            subprocess.call('clear', shell=True)
            print("Exitting as you wish...")
            sys.exit(0)

        except socket.gaierror:
            print('Hostname not found.')

        except socket.error:
            print("Couldn't connect to server.")


    def main(self):
        threads = []
        for p in range(0, self.to_scan):
            if threading.active_count() < self.thr:
                t = threading.Thread(target=self.scan, args=(p,))
                t.start()
                threads.append(t)

        for t in threads:
            t.join()
        self.f.close()
        print(f"{Fore.YELLOW}[CONSOLE] Found {self.good} ports out of {self.to_scan}")        
