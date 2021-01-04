import random, time, sys, os, subprocess
import requests
from colorama import Fore
import threading


class Bogan():
    def __init__(self):
        subprocess.call('clear', shell=True)

        print(f"""{Fore.RED}
 ▄▄▄▄   ▒█████   ▄████ ▄▄▄      ███▄    █ ▄▄▄▄   █    ██  ██████▄▄▄█████▓█████ ██▀███  
▓█████▄▒██▒  ██▒██▒ ▀█▒████▄    ██ ▀█   █▓█████▄ ██  ▓██▒██    ▒▓  ██▒ ▓▓█   ▀▓██ ▒ ██▒
▒██▒ ▄█▒██░  ██▒██░▄▄▄▒██  ▀█▄ ▓██  ▀█ ██▒██▒ ▄█▓██  ▒██░ ▓██▄  ▒ ▓██░ ▒▒███  ▓██ ░▄█ ▒
▒██░█▀ ▒██   ██░▓█  ██░██▄▄▄▄██▓██▒  ▐▌██▒██░█▀ ▓▓█  ░██░ ▒   ██░ ▓██▓ ░▒▓█  ▄▒██▀▀█▄  
░▓█  ▀█░ ████▓▒░▒▓███▀▒▓█   ▓██▒██░   ▓██░▓█  ▀█▒▒█████▓▒██████▒▒ ▒██▒ ░░▒████░██▓ ▒██▒
░▒▓███▀░ ▒░▒░▒░ ░▒   ▒ ▒▒   ▓▒█░ ▒░   ▒ ▒░▒▓███▀░▒▓▒ ▒ ▒▒ ▒▓▒ ▒ ░ ▒ ░░  ░░ ▒░ ░ ▒▓ ░▒▓░
▒░▒   ░  ░ ▒ ▒░  ░   ░  ▒   ▒▒ ░ ░░   ░ ▒▒░▒   ░░░▒░ ░ ░░ ░▒  ░ ░   ░    ░ ░  ░ ░▒ ░ ▒░
 ░    ░░ ░ ░ ▒ ░ ░   ░  ░   ▒     ░   ░ ░ ░    ░ ░░░ ░ ░░  ░  ░   ░        ░    ░░   ░ 
 ░         ░ ░       ░      ░  ░        ░ ░        ░          ░            ░  ░  ░     
      ░                                        ░                                       

        """)


        self.thr = 5
        self.TARGET = input(f"{Fore.BLUE}[CONSOLE] Please enter full url site target: ")
        self.FILE = input(f"{Fore.BLUE}[CONSOLE] Please enter wordlist file without the extension: ")
        self.bad_requests = input(f"{Fore.BLUE}[CONSOLE] Shoud I input bad requests too? (y/n): ")
        self.use_proxy = input(f"{Fore.BLUE}[CONSOLE] Should I use (http) proxies (y/n): ")

        if self.use_proxy == 'y':
            get_proxies = input(f'{Fore.BLUE}[CONSOLE] Should I get the proxies or you already have http proxy list? (get/n):')

            if get_proxies == 'get':
                try:
                    os.remove("BoganBuster/http_proxies.txt")
                    os.remove("BoganBuster/good_proxies.txt")
                except:
                    pass
                
                proxylist = open('BoganBuster/http_proxies.txt', 'a+')
                try:
                    r1 = requests.get('https://api.proxyscrape.com?request=getproxies&proxytype=http')
                    proxylist.write(r1.text)
                except:
                    pass
                try:
                    r2 = requests.get("https://www.proxy-list.download/api/v1/get?type=https")
                    proxylist.write(r2.text)
                except:
                    pass
                try:
                    r3 = requests.get("https://www.proxyscan.io/download?type=http")
                    proxylist.write(r3.text)
                except:
                    pass
                try:
                    r4 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt")
                    proxylist.write(r4.text)
                except:
                    pass
                proxylist.close()
                self.proxy_file = 'BoganBuster/http_proxies'

            else:
                self.proxy_file = input(f"{Fore.BLUE}[CONSOLE] Please enter the proxy filename without the extension: ")
            self.timeout = int(input(f"{Fore.BLUE}[CONSOLE] Please enter proxy timeout (10-50): "))
        else:
            pass

        self.f = open('BoganBuster/good.txt', 'a+')

        self.checked = 0
        self.proxy_checked = 0


    def proxy_checker(self, proxy):
        time.sleep(0.05)
        f_p = open('BoganBuster/good_proxies.txt', 'a+')
        headers = {'User-Agent': ''}
        user_agent_list = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
            'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000',
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", 
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)", 
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", 
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)", 
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)", 
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)", 
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)", 
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)", 
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6", 
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1", 
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0", 
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5", 
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6", 
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11", 
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20", 
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]
        headers['User-Agent'] = random.choice(user_agent_list)

        try:
            req = requests.get(f'https://www.google.com', headers=headers, proxies={'https': f'https://{proxy}', 'http': f'http://{proxy}'}, timeout=self.timeout)
            if req.ok:
                f_p.write(f"{proxy}")
                f_p.close()

        except:
            pass

    def checker(self, buster, proxy, max_trys = 3):
        headers = {'User-Agent': ''}
        user_agent_list = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
            'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000',
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", 
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)", 
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", 
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)", 
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)", 
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)", 
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)", 
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)", 
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6", 
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1", 
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0", 
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5", 
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6", 
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11", 
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20", 
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]
        headers['User-Agent'] = random.choice(user_agent_list)

        if self.use_proxy == 'y':
            try:
                req = requests.get(f'{self.TARGET}/{buster}', headers=headers, proxies={'https': f'https://{proxy}', 'http': f'https://{proxy}'}, timeout=self.timeout)
                if req.ok:
                    print(f'{Fore.GREEN}{self.checked}: Good request {req.status_code}- /{buster} Proxy- {proxy}')
                    self.f.write(f'\n{self.checked}: Good request {req.status_code}- /{buster}')

                else:
                    print(f'{Fore.RED}{self.checked} Bad request {req.status_code}: /{buster} Proxy- {proxy}' if self.bad_requests == 'y' else None)

            except:
                print(f'{Fore.RED}{self.checked} The proxy might have been blocked by the website! Proxy- {proxy}' if self.bad_requests == 'y' else None)

        elif self.use_proxy == 'n':
            try:
                req = requests.get(f'{self.TARGET}/{buster}', headers=headers)
                if req.ok:
                    print(f'{Fore.GREEN}{self.checked}: Good request {req.status_code}- /{buster}')
                    self.f.write(f"Found /{buster} code:{req.status_code}")

                else:
                    print(f'{Fore.RED}{self.checked} Bad request {req.status_code}: /{buster}' if self.bad_requests == 'y' else None)

            except:
                print(f'{Fore.RED}{self.checked} You might have been blocked by the website!' if self.bad_requests == 'y' else None)
        


    def start_proxy_checker(self):
        try:
            with open(f"{self.proxy_file}.txt", 'r+', encoding="utf-8", errors='ignore') as f:
                proxs = f.readlines()
                p_LEN = len(proxs)
                p_processes = []
                for _ in range(self.thr):
                    if self.proxy_checked < p_LEN:
                        for proxie in proxs:
                            self.proxy_checked += 1
                            p = threading.Thread(target=self.proxy_checker, args=(proxie,), daemon=True)
                            p.start()
                            p_processes.append(p)

                    elif self.proxy_checked >= p_LEN:
                        time.sleep(0.1)
                        for process in p_processes: 
                            process.join()

        except FileNotFoundError:
            print(f'{Fore.RED}[CONSOLE] Proxylist file not found.')

        except KeyboardInterrupt:
            print("Caught KeyboardInterrupt, terminating workers")


    def start_checker(self):
        if self.use_proxy == 'y':
            Fl = open('BoganBuster/good_proxies.txt', 'r+', encoding="utf-8", errors='ignore')
            read = Fl.readlines()
            try:
                with open(f"{self.FILE}.txt", 'r+', encoding="utf-8", errors='ignore') as f:
                    busts = f.readlines()
                    LEN = len(busts)
                    processes = []
                    for _ in range(self.thr):
                        if self.checked < LEN:
                            for buster in busts:
                                self.checked += 1
                                p = threading.Thread(target=self.checker, args=(buster, random.choice(read),), daemon=True)
                                p.start()
                                processes.append(p)

                        elif self.checked >= LEN:
                            time.sleep(0.03)
                            for process in processes: 
                                process.join()
                    

            except FileNotFoundError:
                print(f'{Fore.RED}[CONSOLE] Wordlist not found.')
                sys.exit()
            
            except KeyboardInterrupt:
                print("Caught KeyboardInterrupt, terminating workers")
                sys.exit()

            except IndexError:
                print(f"{Fore.RED}[CONSOLE] There are no valid proxies! Please try again.")
                sys.exit()

            self.f.close()

        elif self.use_proxy == 'n':
            try:
                with open(f"{self.FILE}.txt", 'r+', encoding="utf-8", errors='ignore') as f:
                    busts = f.readlines()
                    LEN = len(busts)
                    processes = []
                    for _ in range(self.thr):
                        if self.checked < LEN:
                            for buster in busts:
                                self.checked += 1
                                p = threading.Thread(target=self.checker, args=(buster, None,), daemon=True)
                                p.start()
                                processes.append(p)

                        elif self.checked >= LEN:
                            time.sleep(0.03)
                            for process in processes: 
                                process.join()

            except FileNotFoundError:
                print(f'{Fore.RED}[CONSOLE] Wordlist not found.')
                sys.exit()
            
            except KeyboardInterrupt:
                print("Caught KeyboardInterrupt, terminating workers")
                p.terminate()

            self.f.close()


    def start_all(self):
        Fg = open('BoganBuster/good_proxies.txt', 'a+', encoding="utf-8", errors='ignore')
        if self.use_proxy == 'y':
            self.start_proxy_checker()
            time.sleep(0.03)
            print(f'{Fore.YELLOW}[CONSOLE] Found {len(Fg.readlines())} good proxies from {self.proxy_checked} proxies.')
            op = input(f'{Fore.BLUE}[CONSOLE] Should I start checking dirs? (y/n): ')
            Fg.close()

            if op == 'y':
                self.start_checker()
            else:
                pass

        elif self.use_proxy == 'n':
            self.start_checker()