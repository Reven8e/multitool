# © Port Scanner- Made by Yuval Simon. For bogan.cool

import socket, subprocess, sys, time, os, threading

from datetime import datetime
from colorama import Fore

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


server = input(f"{Fore.BLUE}[CONSOLE] Enter ip/domain to scan: ")
thr = int(input("Please enter threads number: "))
to_scan = int(input("How many ports to scan (1k-10k): "))
server_ip = socket.gethostbyname(server)


now = datetime.now()
checked = 0
good = 0
f = open('port_scanner_results.txt', 'a+')

try:
    os.remove('port_scanner_results.txt')
except:
    pass

print('\n\nStarting scan...')
time.sleep(1)
subprocess.call('clear', shell=True)

print(f"{Fore.YELLOW}[CONSOLE] Target's IP: {server_ip}\n")
print('-' * 30)
print('\n')

def scan(p):
    global checked, good, f
    checked += 1
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        r = sock.connect_ex((server_ip, p))
        if r == 0:
            print(f'{Fore.GREEN}[CONSOLE] Found open port: {p}')
            f.write(f"Found open port: {p}\n")
            good += 1

    except KeyboardInterrupt:
        subprocess.call('clear', shell=True)
        print("Exitting as you wish...")
        sys.exit()

    except socket.gaierror:
        subprocess.call('clear', shell=True)
        print('Hostname not found. Exiting...')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()


def start_scan():
    global checked, f
    threads = []
    for _ in range(thr):
        for p in range(1, to_scan):
            t = threading.Thread(target=scan, args=[p])
            t.start()
            threads.append(t)

        for t in threads:
            t.join()
    f.close()
