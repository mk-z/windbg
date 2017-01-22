import multiprocessing
import time

def daemon():
    while 1:
        time.sleep(10)

def non_daemon():
    while 1:
        time.sleep(100)

def non_daemon_break():
    time.sleep(3)      

if __name__ == '__main__':
    f = []
    f.append(multiprocessing.Process(name='daemon', target=daemon))
    f.append(multiprocessing.Process(name='non-daemon', target=non_daemon))
    f.append(multiprocessing.Process(name='non-daemon', target=non_daemon_break))

    for i in f:
        i.daemon = True
        i.start()
        while 1:
            time.sleep(1)