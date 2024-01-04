import threading
def show():
    obj=threading.current_thread()
    print(obj.getName())

obj=threading.current_thread()
print(obj.getName())
show()