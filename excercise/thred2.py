import threading

def show():
    obj=threading.current_thread()
    print(obj.name)
mainthred=threading.current_thread()
print("hello",mainthred.name)
mythred=threading.Thread(target=show())
mythred.start()
print("bye",mythred.name)
