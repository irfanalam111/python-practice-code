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
x=time.time()
t1=threading.Thread(target=squre,args=(mylist,))
t2=threading.Thread(target=cube,args=(mylist,))
t1.start()
t2.start()
t1.join()
t2.join()
y=time.time()
print("total time is ",y-x)
