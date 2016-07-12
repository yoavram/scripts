from __future__ import print_function
import time


def beep(times=5, interval=0.5):
    for _ in range(times):
        print("\7", end='', flush=True)
        time.sleep(interval)

if __name__ == '__main__':
    beep()
