import threading
import time

class Mythred(threading.Thread):
    def __init__(self ,mylist):
        super().__init__()
        self.mylist=mylist

    def show(self):
        for i in self.mylist:
            print("squre: ",i*i)
            time.sleep(1)

class Mythred1(threading.Thread):
    def __init__(self, mylist) :
        super().__init__()
        self.mylist=mylist
    
    def show(self):
        for i in self.mylist:
            print("cube :",i*i*i)
            time.sleep(1)
    
numlist=[2,3,4,5,6,7,8,9]
m1=Mythred(numlist)
m2=Mythred1(numlist)
m1.start()
m2.start()
m1.join()
m2.join()
print("thank you...")