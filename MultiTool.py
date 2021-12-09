from src.boganBuster import busterChecker, threading
from src.DataClasses import boganBusterData

data = boganBusterData(target='https://www.bogan.cool/', proxy_type='http')


l = [i for i in range(1000)]
l[50] = 'mighty-manager'
data.wordlist = l
data.thr = 30

threads = []
for dir_ in l:
	while True:
		if threading.active_count() < data.thr:
			i = busterChecker(False, dir_, data)
			i.start()
			threads.append(i)
			break

for t in threads:
	t.join()


print(data.good_dirs)
