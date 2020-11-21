# © Proxy checker- Discord.py- Made by Yuval Simon. For bogan.cool

import random, time, sys, subprocess

import requests

from colorama import Fore, Style

import multiprocessing

subprocess.call('clear', shell=True)

thr = int(input(f"{Fore.BLUE}[CONSOLE] Please enter threading number (10-100): "))
timeout = int(input(f"{Fore.BLUE}[CONSOLE] Please enter timeout(1-10): "))
TARGET = input(f"{Fore.BLUE}[CONSOLE] Please full url site target: ")
FILE = input(f"{Fore.BLUE}[CONSOLE] Please enter filename without the extension: ")
TYPE = input(f"{Fore.BLUE}[CONSOLE] Please enter proxy type: ")
BAD_PROXIES = input(f"{Fore.BLUE}[CONSOLE] Shoud I input bad proxies too? (y/n): ")

fe = open('good.txt', 'a+')
checked = 0

def check(proxy):
    global timeout, BAD_PROXIES, checked, TYPE, fe
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
    
    if TYPE == "http":
        try:
            req = requests.get(f'{TARGET}', headers=headers, proxies={'https': f'https://{proxy}', 'http': f'http://{proxy}'}, timeout=timeout)
            if req.ok:
                print(f'{Fore.GREEN} {checked} Good request: {proxy}')
                fe.write(proxy)
                fe.close()

            else:
                print(req.status_code)
                pass
        except:
            if BAD_PROXIES == 'y':
                print(f"{Fore.RED} {checked} Bad request: {proxy}")
            else:
                pass
    
    elif TYPE == "socks4":
        try:
            req = requests.get(f'{TARGET}', headers=headers, proxies={'https': f'socks4://{proxy}', 'http': f'socks4://{proxy}'}, timeout=timeout)
            if req.ok:
                print(f'{Fore.GREEN} {checked} Good request: {proxy}')
                fe.write(proxy)
                fe.close()

            else:
                print(req.status_code)
                pass
        except:
            if BAD_PROXIES == 'y':
                print(f"{Fore.RED} {checked} Bad request: {proxy}")
            else:
                pass

    elif TYPE == "socks5":
        try:
            req = requests.get(f'{TARGET}', headers=headers, proxies={'https': f'socks5://{proxy}', 'http': f'socks5://{proxy}'}, timeout=timeout)
            if req.ok:
                print(f'{Fore.GREEN} {checked} Good request: {proxy}')
                fe.write(proxy)
                fe.close()

            else:
                print(req.status_code)
                pass
        except:
            if BAD_PROXIES == 'y':
                print(f"{Fore.RED} {checked} Bad request: {proxy}")
            else:
                pass

def start():
    try:
        with open(f"{FILE}.txt", 'r', encoding="utf-8", errors='ignore') as f:
            proxs = f.readlines()
            LEN = len(proxs)
            processes = []
            for _ in range(thr):
                if checked < LEN:
                    for proxy in proxs:
                            p = multiprocessing.Process(target=check, args=[proxy])
                            p.start()
                            checked += 1
                            processes.append(p)

                    for process in processes:
                        process.join()

                elif checked > LEN:
                    time.sleep(0.03)
                    for process in processes: 
                        process.stop
                    fe.close()            

    except FileNotFoundError:
        print(f'{Fore.RED}[CONSOLE] File not found.')
        sys.exit()


lines_seen = set()
outfile = open('good_no_dups.txt', "w")
for line in open('good.txt', "r"):
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

print(f'{Fore.YELLOW}[CONSOLE] Done checking {checked} proxies. \nFound {len(lines_seen)} good proxies.')