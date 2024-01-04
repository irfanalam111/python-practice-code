import threading

obj=threading.current_thread()
print("multi threding",obj.getName())

a=dir(threading)
for i in a:
    print(i)