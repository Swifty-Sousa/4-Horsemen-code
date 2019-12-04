#gui controller for project.
import tkinter as tk
from tkinter import font as tkfont
from logic import *

holder=["", "", "", ""]
def read(data=[]):
    global holder
    holder=data
    print(holder)
class stu():
    sfname=""
    slname=""
    sid=""
    scnum=""

student= stu()
    
def clear_student(data=[], *args):
    global student
    student.sfname=""
    student.slname=""
    student.sid=""
    student.csnum=""

def create_student(data=[], *args):
    print("data recived:")
    print(data)
    global student
    student.sfname=data[0]
    student.slname=data[1]
    student.sid= data[2]
    student.csnum=data[3]
    print("class bs:")
    print(student.sfname)


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
        for i in (EventLogin, Selector, CardLogin, CardSubmit, ManualLogin, NewLogin):
            page_name= i.__name__
            frame = i(parent=container, controller=self)
            self.frames[page_name]= frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("EventLogin")

    #brings frame to the front of app to be interacted with
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()



class EventLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        controller= controller
        #def create(self):
        #lables and titles and the such
        label= tk.Label(self, text= "Please Enter Event ID to activate Swiper", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        #input Code:
        eventid= tk.StringVar()
        EventId= tk.Entry(self, textvariable= eventid) 
        EventId.pack()
        #buttons to go next:
        b1= tk.Button(self, text="Next", command= lambda: [controller.show_frame("Selector"), eventid.set(EventId.get()), Ver_Event(eventid.get()), EventId.delete(0,'end')])
        b1.pack()
           


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
        #Labels:
        lable= tk.Label(self, text="Please Swipe Card", font=controller.title_font)
        lable.pack(side="top", fill="x", pady=10)
        #Entry for card to be swiped:
        data= tk.StringVar()
        Data= tk.Entry(self, textvariable=data) 
        Data.pack()
        b1= tk.Button(self, text="Submit", command= lambda: [print("step1"),data.set(Data.get()),create_student(parse_card(data.get())), Data.delete(0,'end'), controller.show_frame("CardSubmit")])
        b1.pack()
        

        #button to go back to selector:
        menu= tk.Button(self, text="Menu", command= lambda: controller.show_frame("Selector"))
        menu.pack()

class CardSubmit(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller= controller
        global student
        global holder
        print("this is in card submit")
        print(student.sfname)
        var = tk.StringVar()
        var2= tk.StringVar()
        var3= tk.StringVar()
        self.l= tk.Label(self, textvariable=var)
        l2= tk.Label(self, textvariable=var2)
        l3= tk.Label(self, textvariable=var3)
        self.l.pack()
        l2.pack()
        l3.pack()
        var.set("Student Name:"+ holder[0] + " "+ holder[1]+ '\n')
        var2.set("Student_ID: " + student.sid + '\n')
        var3.set("Card number: "+ student.scnum + '\n')


def pront(a,b,c):
    print(a)
    print(b)
    print(c)

class ManualLogin(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller= controller
        #button to go back to selector:
        menu= tk.Button(self, text="Menu", command=lambda: controller.show_frame("Selector"))
        #lables:
        label_id= tk.Label(self, text="Student ID:")
        label_fname= tk.Label(self, text="First Name:")
        label_lname= tk.Label(self, text="Last Name:")
        #Entry input variables:
        input_id= tk.StringVar()
        input_fname= tk.StringVar()
        input_lname= tk.StringVar()
        #Entries:
        in_id= tk.Entry(self, textvariable=input_id)
        in_fname= tk.Entry(self, textvariable=input_fname)
        in_lname= tk.Entry(self, textvariable=input_lname)
        #packing:
        label_fname.pack()
        in_fname.pack()
        label_lname.pack()
        in_lname.pack()
        label_id.pack()
        in_id.pack()
        submit= tk.Button(self, text="Submit", command= lambda:pront(input_fname.get(),input_lname.get(), input_id.get()))
        submit.pack()
        


        menu.pack()

class NewLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller= controller
        #Das lable:
        label =tk.Label(self, text="Please Visit our website at: WEBSITE URL HERE DONT FORGET THIS U FUCK to create an account", font=controller.title_font )
        label.pack()
        #button to go back to selector:
        menu= tk.Button(self, text="Menu", command= lambda: controller.show_frame("Selector"))
        menu.pack()


if __name__=="__main__":
    #event= Applicaiton().frames["EventLogin"]
    app=Applicaiton()
    app.frames["CardSubmit"].l['text']="puta"
    app.frames["CardSubmit"].l.pack()
    app.mainloop()

