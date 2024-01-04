import threading
import time

def squre(mylist):
    for i in mylist:
        print("squre is",i*i)
        time.sleep(1)

def cube(mylist):
    for i in mylist:
        print("cube is ",i*i*i)
        time.sleep(1)

mylist=[2,3,4,5,6]
print("total thres",threading.active_count())
t1=threading.Thread(target=squre,args=(mylist,))
t2=threading.Thread(target=cube,args=(mylist,))
t1.start()
print("total thres",threading.active_count())
t2.start()
print("total thres",threading.active_count())
t1.join()
t2.join()
print("total thres",threading.active_count())
