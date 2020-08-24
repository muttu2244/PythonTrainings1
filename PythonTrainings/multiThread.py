import threading
import time

def infiniteloop1(a):
    while True:
        print(a)
        time.sleep(1)


for i in range(2):
    #print("in Main {}".format(i))
    thread1 = threading.Thread(target=infiniteloop1(i,))
    thread1.start()
    thread1.join()


# thread1 = threading.Thread(target=infiniteloop1, args=('aaa',))
# thread1.start()
#
# thread2 = threading.Thread(target=infiniteloop1, args=('bbb',))
# thread2.start()

#thread2 = threading.Thread(target=infiniteloop1('bbb'))
#thread2.start()