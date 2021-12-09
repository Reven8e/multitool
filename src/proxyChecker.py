from src.ascii import headers
import random, requests, threading


class Checker(threading.Thread):
    def __init__(self, proxy, proxyData):
        threading.Thread.__init__(self)
        self.proxy = proxy
        self.proxy_type= proxyData.proxy_type
        self.proxyData = proxyData


    def run(self):
        if 'http' in self.proxy_type.lower():
            proxies = {
                "https": f'https://{self.proxy}'
            }

        elif self.proxy_type == 'socks4':
            proxies = {
                "https": f'socks4://{self.proxy}'
            }

        elif self.proxy_type == 'socks5':
            proxies = {
                "https": f'socks5://{self.proxy}'
            }

        try:
            r = requests.get('https://www.google.com', headers={"User-Agent": random.choice(headers)}, proxies=proxies)
            if r.status_code == 200:
                self.proxyData.good_proxies.append(f"{self.proxy}")
        except requests.exceptions.ProxyError:
            pass
