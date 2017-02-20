#! python3
# coding: utf-8

import time
import threading
from random import random
from queue import Queue

q = Queue()

def double(n):
    return n*2

def producer():
    count = 0
    while 1:
        if count > 5:
            break
        wt = random()
        time.sleep(wt)
        q.put((double, wt))
        count +=1
    
def consumer():
    while 1:
        if q.empty:
            break
        task, arg = q.get()
        print('{} .. {}'.format(arg, task(arg)))
        q.task_done()

#for target in (producer, consumer):
#    t = threading.Thread(target=target)
#    t.start()
t = threading.Thread(target = producer)
t.start()
time.sleep(1)
t = threading.Thread(target=consumer)
t.start()