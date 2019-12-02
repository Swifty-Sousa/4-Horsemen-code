#this is my practice gui
import tkinter as tk
from tkinter import font as tkfont
from logic import *

class Applicaiton(tk.Tk):
    def __init__(self, master= None):
        tk.Tk.__init__(self)
        #create a container where we can stack multiple gui pages 
        #use frame raising to move the current page to the top so that it is visible
        self.title_font= tkfont.Font(family= "Helvetica", size=18, weight="bold")
        container= tk.Frame(self)
        container.pack(side="top", fill= "both", expand= True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames={}
        for i in (EventLogin, Selector, CardLogin, ManualLogin, NewLogin):
            page_name= i.__name__
            frame = i(parent=container, controller=self)
            self.frames[page_name]= frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("EventLogin")

    #brings frame to the front of app to be interacted with
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    #reloads frame such that is can be used again. This is used when going back and fourth between frames.
    def reload_frame(self, name):
        frame= EventLogin(parent=tk.Frame(self), controller=self)
        self.frames[name]=frame
        frame.grid(row=0, column=0,sticky="nsew")
    def give(self,name):
        return self.frames[name]



class EventLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller= controller
        #def create(self):
        #lables and titles and the such
        self.label= tk.Label(self, text= "Please Enter Event ID to activate Swiper", font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        #input Code:
        eventid= tk.StringVar()
        self.EventId= tk.Entry(self, textvariable= eventid) 
        self.EventId.pack()
        #buttons to go next:
        self.b1= tk.Button(self, text="Next", command= lambda: [controller.show_frame("Selector"), eventid.set(self.EventId.get()), Ver_Event(eventid.get()), self.EventId.delete(0,END)])
        self.b1.pack()
        
        
           


class Selector(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller= controller
        #labels:
        lable= tk.Label(self, text="Please Select how you would like to Sign in:", font= controller.title_font)
        lable.pack(side="top", fill="x", pady=10)
        #buttonies
        card= tk.Button(self, text="Sign in with BuffOne card", command= lambda: controller.show_frame("CardLogin"))
        man= tk.Button(self, text="Sign in with Student ID number", command= lambda: controller.show_frame("ManualLogin"))
        new= tk.Button(self, text="Don't have an account", command= lambda: controller.show_frame("NewLogin"))
        back= tk.Button(self, text="Back", command= lambda: [controller.show_frame("EventLogin")])
        card.pack()
        man.pack()
        new.pack()
        back.pack()


class CardLogin(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller= controller
        #button to go back to selector:
        menu= tk.Button(self, text="Menu", command= controller.show_frame("Selector"))

class ManualLogin(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller= controller

class NewLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller= controller



if __name__=="__main__":
    app=Applicaiton()
    #event= Applicaiton().frames["EventLogin"]

    app.mainloop()

