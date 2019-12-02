#this is my practice gui
import tkinter as tk
class Applicaiton(tk.Frame):
    def __init__(self, master= None):
        tk.Frame.__init__(self,master)
        self.pack()
        self.log()
        self.buff()
        self.hold()
    def log(self):
        self.test= tk.Button(self)
        self.test["text"]="this is test"
        self.test["command"]=self.buff
        self.test.pack(side="top")
        self.hold= tk.Button(self)
        self.hold["text"]= "manual"
        self.hold["command"]=self.hold
        self.QUIT= tk.Button(self, text="exit", command= root.destroy)
        self.QUIT.pack(side="bottom")

    def buff(self):
        
        
    def hold(self):

    def hellothere(self):
        print("hello there.")

root =tk.Tk()
root["height"]=400
root["width"]=400
app= Applicaiton(master=root)
app.mainloop()