from multiprocessing import Process
import sys

rocket = 0

def func1(int):
    print(int)
    global rocket
    print('start func1')

    print('end func1')

def func2():
    global rocket
    print('start func2')

    print('end func2')

if __name__=='__main__':
    for i in range(3):
        p = Process(target = func1,args=(i,))
        p.start()
        #p2 = Process(target = func2)
        #p2.start()
        # This is where I had to add the join() function.
        p.join()
        #p2.join()