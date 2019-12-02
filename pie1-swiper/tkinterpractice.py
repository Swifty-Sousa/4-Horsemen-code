#this is my practice gui
import tkinter as tk
from tkinter import font as tkfont
class Applicaiton(tk.Frame):
    def __init__(self, master= None):
        tk.TK.__init__(self)
        #create a container where we can stack multiple gui pages 
        #use frame raising to move the current page to the top so that it is visible
        container= tk.Frame(self)
        container.pack(side="top", fill= "both", expand= True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames={}
        for i in (EventLogin, CardLogin, ManualLogin, NewLogin):


        
class Card_login
root =tk.Tk()
root["height"]=400
root["width"]=400
app= Applicaiton(master=root)
app.mainloop()