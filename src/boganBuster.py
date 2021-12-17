from src.ascii import headers
import random, time, sys, subprocess, requests, threading


class Buster():
    def __init__(self, thr, target, wordlist, proxylist):
        self.thr = thr
        self.target= target
        self.wordlist = wordlist
        self.proxylist = proxylist

    
    def load_wordlist(self):
        try:
            with open(self.wordlist, 'r+') as f:
                return [i.replace('\n', '') for i in f]
        except FileNotFoundError:
            raise FileNotFoundError(f'Wordlist not found. Inputed path: {self.wordlist}')
        except FileExistsError:
            raise FileExistsError(f'Wordlist not found. Inputed path: {self.wordlist}')
    

    def load_proxylist(self):
        if self.proxylist != None:
            try:
                with open(self.proxylist, 'r+') as f:
                    return [i.replace('\n', '') for i in f]
            except FileNotFoundError:
                raise FileNotFoundError(f'Wordlist not found. Inputed path: {self.wordlist}')
            except FileExistsError:
                raise FileExistsError(f'Wordlist not found. Inputed path: {self.wordlist}')



class busterChecker(threading.Thread):
    def __init__(self, use_proxy, dir, busterData):
        threading.Thread.__init__(self)
        self.use_proxy = use_proxy
        self.dir = dir
        self.target= busterData.target
        self.proxy_type = busterData.proxy_type
        self.busterData = busterData


    def proxy_req(self):
        while True:
            proxy = random.choice(self.busterData.proxylist)

            if 'http' in self.proxy_type.lower():
                proxy_conf = {
                    "https": f'https://{proxy}'
                }

            elif self.proxy_type == 'socks4':
                proxy_conf = {
                    "https": f'socks4://{proxy}'
                }

            elif self.proxy_type == 'socks5':
                proxy_conf = {
                    "https": f'socks5://{proxy}'
                }

            try:
                r = requests.get(f'{self.target}/{self.dir}', headers={"User-Agent": random.choice(headers)}, proxies=proxy_conf)
                if r.ok:
                    self.busterData.good_dirs.append(self.dir)
                    return
                else:
                    return
            except requests.exceptions.ProxyError:
                pass


    def run(self):
        if not self.use_proxy:
            r = requests.get(f'{self.target}/{self.dir}', headers={"User-Agent": random.choice(headers)})
            if r.ok:
                self.busterData.good_dirs.append(self.dir)

        if self.use_proxy:
            self.proxy_req()
