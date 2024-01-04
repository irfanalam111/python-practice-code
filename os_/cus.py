from typing import Optional, Tuple, Union
import customtkinter as ctk

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('green')

class view(ctk.CTk):
    def __init__(self):
        super.__init__()
        self.geometry('720x600')
        self.resizable(False,False)
        self.title('Notebook')
        self.TopLbl=ctk.CTkLabel(self,text="File")
        self.TopLbl.grid(row=0,column=0,padx=20,pady=40)





if __name__=="__main__":
    app=view()
    app.mainloop()