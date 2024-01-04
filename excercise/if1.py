import math
import threading
import tkinter
import time


class GUI:
    def __init__(self,root) -> None:
        self.root=root
        self.root.geometry("340x720")
        self.start_btn=tkinter.Button(self.root,text="start",command=self.set_thred)
        self.start_btn.pack()
        self.stop_btn=tkinter.Button(self.root,text="stop",command=self.stop_fun)
        self.stop_btn.pack()

    def set_thred(self):
        self.my_thred=threading.Thread(target=self.show_num)
        self.my_thred.start()
        self.stop_thred=False
    def stop_fun(self):
        self.stop_thred=False

    def show_num(self):
        for i in range(1,31):
            print(math.pow(i,2))
            time.sleep(1)
            if self.stop_thred==True:
                break


root=tkinter.Tk()
obj=GUI(root)
root.mainloop()
        
