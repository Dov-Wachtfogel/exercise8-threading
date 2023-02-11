from q1 import create_file, check_time
import random
import threading
import os
def add_rands_to_file(f, n, l:threading.Lock):
    for _ in range(10000):
        s = str(random.randint(1, 1000)) + '\n'
        l.acquire()
        f.write(s)
        l.release()
def create_file_with_threads(file_name):
    f = open(file_name, 'a')
    f_lock = threading.Lock()
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=add_rands_to_file,args=(f,10000, f_lock)))
        threads[i].start()
    for i in threads:
        i.join()
    f.close()
def calculate_file_sum(f, use_global = False):
    l = [int(x) for x in f.splitlines()]
    if use_global:
        global a
        a=sum(l)
    return sum(l)
def calculate_file_sum_start(f, use_global = False):
    l = [int(x[0]) for x in f.splitlines()]
    if use_global:
        global b
        a=sum(l)
    return sum(l)
def calculate_file_sum_end(f, use_global = False):
    l = [int(x[-1]) for x in f.splitlines()]
    if use_global:
        global c
        a=sum(l)
    return sum(l)
def calculate_file(file_name):
    f = open(file_name, 'r').read()
    return calculate_file_sum(f), calculate_file_sum_start(f), calculate_file_sum_end(f)

def calculate_file_threading(file_name):
    global a,b,c
    f = open(file_name, 'r').read()
    t1 = threading.Thread(target=calculate_file_sum, args=(f,True))
    t2 = threading.Thread(target=calculate_file_sum_start, args=(f,True))
    t3 = threading.Thread(target=calculate_file_sum_end, args=(f,True))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    return a,b,c

if __name__ == '__main__':
    f1 = 'aaa'
    f2 = 'bbb'
    a = 0
    b = 0
    c = 0
    print('create files without threading',check_time(create_file, (f1,)))
    print('create files with threading',check_time(create_file_with_threads, (f2,)))
    print('calculate files without threading',check_time(calculate_file, (f1,)))
    print('calculate files with threading',check_time(calculate_file_threading, (f2,)))
    os.remove(f1)
    os.remove(f2)

