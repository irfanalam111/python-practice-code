from threading import *

class Alive(Thread):
    
    def show(self):
        for i in range(10):
            print("ping")

obj=Alive()
obj.start()
for i in range(10):
    print("pong")