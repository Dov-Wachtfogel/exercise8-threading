import random
import time
import threading
import os

def check_time(func, args=None):
    start = time.time()
    if args==None:
        func()
    else:
        func(*args)
    end = time.time()
    return end-start
def remove_files(start_file_name, n):
    for i in range(n):
        os.remove(start_file_name+str(i))
class counter:
    def __init__(self):
        self.c = 0
    def __add__(self, other:int):
        self.c+=other

def create_file(file_name):
    f = open(file_name, 'a')
    for _ in range(100000):
        f.write(str(random.randint(1, 1000))+'\n')
    f.close()

def create_n_files(start_file_name, n):
    for i in range(n):
        create_file(start_file_name+str(i))

def create_using_threads(start_file_name, n):
    threads = []
    for i in range(n):
        threads.append(threading.Thread(target=create_file, args=(start_file_name+str(i),)))
        threads[i].start()
    for i in range(n):
        threads[i].join()
def calculate_file(file_name, c=None):
    f = open(file_name, 'r')
    l = [int(x) for x in f.readlines()]
    if c!=None:
        c+=sum(l)/len(l)
    return sum(l)/len(l)
def calculate_n_files(start_file_name, n):
    s = 0
    for i in range(n):
        s+=calculate_file(start_file_name+str(i))
    return s/n

def calculate_using_threads(start_file_name, n):
    c = counter()
    threads = []
    for i in range(n):
        threads.append(threading.Thread(target=calculate_file, args=(start_file_name+str(i),c)))
        threads[i].start()
    for i in range(n):
        threads[i].join()
    return c.c/n
if __name__ == '__main__':
    f1 = 'aaa'
    f2 = 'bbb'
    # n=10
    n=100
    print('create files without threading',check_time(create_n_files, (f1,n)))
    print('create files with threading',check_time(create_using_threads, (f2,n)))
    print('calculate files without threading',check_time(calculate_n_files, (f1,n)))
    print('calculate files with threading',check_time(calculate_using_threads, (f2,n)))
    remove_files(f1,n)
    remove_files(f2,n)

