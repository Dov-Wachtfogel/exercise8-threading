import threading
import time
def thread(l1:threading.Lock,l2:threading.Lock):
    l1.acquire()
    time.sleep(1)
    l2.acquire()
if __name__ == '__main__':
    l1 = threading.Lock()
    l2 = threading.Lock()
    t1 = threading.Thread(target=thread, args=(l1,l2))
    t2 = threading.Thread(target=thread, args=(l2, l1))
    t1.start()
    t2.start()