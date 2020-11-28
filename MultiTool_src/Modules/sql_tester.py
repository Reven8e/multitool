import requests, threading, time, sys, warnings, subprocess
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from colorama import Fore


def get_all_forms(url):
    r = s.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    return soup.find_all("form")


def get_details(form):
    details = {}
    try:
        act = form.attrs.get("action").lower()
    except:
        act = None

    method = form.attrs.get("method", "get").lower()
    
    inputs = []
    for tag in form.find_all("input"):
        input_type = tag.attrs.get("type", "text")
        input_value = tag.attrs.get("value", "")
        input_name = tag.attrs.get("name")
        inputs.append({"type": input_type, "value": input_value, "name": input_name})
    details["method"] = method
    details["action"] = act
    details["inputs"] = inputs
    return details


def is_vuln(response):
    errors = {
        "you have an error in your sql syntax;",
        "warning: mysql",
        "unclosed quotation mark after the character string",
        "quoted string not properly terminated",
    }
    try:
        for e in errors:
            if e in response.content.decode().lower():
                return True

        return False
    except UnicodeDecodeError:
        return False
    
    except requests.exceptions.RequestException:
        pass


def scan_sql_inj(url):
    f = open("vuln.txt", "a+")
    try:
        for b in "\"'":
            new_url = f"{url}{b}"
            print(f"{Fore.WHITE}[CONSOLE] Trying: {new_url}")
            r = s.get(new_url)
            if is_vuln(r):
                print(f"{Fore.GREEN}[CONSOLE] Found SQL injection vulnerability! " + new_url.strip(f"{b}"))
                f.write(new_url.strip(f"{b}"))
                f.close()
                return

    except requests.exceptions.RequestException:
        pass

    try:
        forms = get_all_forms(url)
        print(f"{Fore.CYAN}[CONSOLE] Detected {len(forms)} forms on {url}")
        for form in forms:
            form_details = get_details(form)
            for b in "\"'":
                data = {}
                for tag in form_details['inputs']:
                    if tag["type"] == "hidden" or tag["value"]:
                        try:
                            data[tag["name"]] = tag["value"] + b
                        except:
                            pass
                    elif tag["type"] != "submit":
                        data[tag["name"]] = f"test{b}"
                    url = urljoin(url, form_details["action"])
                    if form_details["method"] == "post":
                        r = s.post(url, params=data)
                    elif form_details["method"] == "get":
                        r = s.get(url, params=data)

                    if is_vuln(r):
                        f.write(url.strip(f"{b}"))
                        print(f"{Fore.GREEN}[CONSOLE] Found SQL injection vulnerability! " + url.strip(f"{b}"))
                        return
                    else:
                        pass
        f.close()
    except requests.exceptions.RequestException:
        pass

def start_scan():
    global checked
    try:
        threads = []
        with open('urls.txt', 'r') as f:
            R = f.readlines()
            for _ in range(thr):
                if checked < len(R):
                    for url in R:
                        time.sleep(delay)
                        t = threading.Thread(target=scan_sql_inj, args=(url,))
                        t.start()
                        checked += 1
                        threads.append(t)

                    for t in threads:
                        t.join()

        f.close()

    except FileNotFoundError:
        print(f"{Fore.RED}[CONSOLE] please create one, and add the url/s to it.")
    except requests.exceptions.RequestException:
        pass    


def start_sql_():
    global thr, delay, FILE, checked, s
    subprocess.call('clear', shell=True)

    print(f"""{Fore.CYAN}
  ██████   █████   ██▓       ▄▄▄█████▓▓█████   ██████ ▄▄▄█████▓▓█████  ██▀███  
▒██    ▒ ▒██▓  ██▒▓██▒       ▓  ██▒ ▓▒▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██▒  ██░▒██░       ▒ ▓██░ ▒░▒███   ░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
  ▒   ██▒░██  █▀ ░▒██░       ░ ▓██▓ ░ ▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░▒███▒█▄ ░██████▒     ▒██▒ ░ ░▒████▒▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░ ▒░▓  ░     ▒ ░░   ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░ ░ ▒░  ░ ░ ░ ▒  ░       ░     ░ ░  ░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░
░  ░  ░     ░   ░   ░ ░        ░         ░   ░  ░  ░    ░         ░     ░░   ░ 
      ░      ░        ░  ░               ░  ░      ░              ░  ░   ░     


    """)

    thr = int(input(f'{Fore.BLUE}[CONSOLE] Please enter threads number (30 for best resulsts): '))
    delay = int(input(f'{Fore.BLUE}[CONSOLE] Please enter delay (enter 0 to skip): '))
    FILE = input(f'{Fore.BLUE}[CONSOLE] Please load your url/s file without.txt extention: ')
    time.sleep(1)
    subprocess.call('clear', shell=True)

    checked = 0
    warnings.filterwarnings('ignore', message='Unverified HTTPS request')

    s = requests.Session()
    s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"

    s.verify = False
    start_scan()