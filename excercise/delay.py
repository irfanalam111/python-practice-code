import time
def squre(mylist):
    for i in mylist:
        print(i*i)
        time.sleep(1)

def cube(mylist):
    for i in mylist:
        print(i*i*i)
        time.sleep(1)
 
x=time.time()
mylist=[2,3,4,5,6]
squre(mylist)
cube(mylist)
y=time.time()
print(y-x)