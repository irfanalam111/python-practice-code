import threading
def show():
    obj=threading.current_thread()
    print(obj.name)

mainthred=threading.current_thread()
print(mainthred.name)
mythred=threading.Thread(target=show,name="mythred")
mythred.start()
mythred1=threading.Thread(target=show,name="mythred2")
mythred1.start()
print(mythred.name)