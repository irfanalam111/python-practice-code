import threading
import time
import tkinter

class mygui:
    def __init__(self,root) -> None:
        self.root=root
        self.root.geometry("722x400")
        btn1=tkinter.Button(self.root,text="start",command=self.setup_thred)
        btn1.pack()
        btn2=tkinter.Button(self.root,text="stop",command=self.stop_thred)
        btn2.pack()
    def setup_thred(self):
        self.mt_thred=threading.Thread(target=self.shownos)
        self.mt_thred.start()
        self.should_thred_stop=False

    def stop_thred(self):
        self.should_thred_stop=True

    def shownos(self):
        for i in range(1,21):
            print(i)
            time.sleep(1)
            if self.should_thred_stop==True:
                break


root=tkinter.Tk()
obj=mygui(root)
root.mainloop()