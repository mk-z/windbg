#! python3
# coding: utf-8

import time
from threading import Thread

value = 0

def getlock(tid):
    global value
    new = value + 1
    time.sleep(0.001)
    value = new
    print('{}, value:{}'.format(tid, value))

threads = []

for i in range(100):
    t = Thread(target=getlock, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print('{}'.format(value))