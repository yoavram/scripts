import sys
from time import time, sleep

def timedelta(start):
	end = time()
	hours, rem = divmod(end - start, 3600)
	minutes, seconds = divmod(rem, 60)
	params = int(hours), int(minutes), int(seconds)
	return "{:0>2}:{:0>2}:{:0>2}".format(*params)

if __name__ == '__main__':
	start = time()
	try:
		while True:			
			msg = timedelta(start)
			sys.stdout.write(msg)
			sys.stdout.flush()
			sleep(1)
			sys.stdout.write('\b'*len(msg))
			sys.stdout.flush()
	except KeyboardInterrupt:
		sys.stdout.write('\b'*len(msg)*2)
		sys.stdout.write(timedelta(start))
