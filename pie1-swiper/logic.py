#swiper logic and gui.
from tkinter import *


def card():
    numid= input("Buff One card or student ID 1/0.\n")
    if(numid):
        buffone_raw= input("please swipe your BuffOne card.\n")
        #print(buffone_raw)
        buffone_holder= buffone_raw.split('=')
        buffone_holder[0]= buffone_holder[0][2:]
        card_name= buffone_holder[0]
        card_sid= buffone_holder[1]
        holder= buffone_holder[2].split('/')
        card_first= holder[0][0]+ holder[0][1:].lower()
        card_last= holder[1][0]+ holder[1][1:].lower()
        #print(card_first + '\n')
        #print(card_last + '\n')
        #print(card_sid + '\n')
        #print(card_name+ '\n')
        # send off to server or something
def Ver_Event(eventid):
    print(eventid)
    #actually verify the garbage

def somethingorother():    
    first = input("Enter your first name")
    first= first[0].upper()+ first[1:].lower()
    last= input("Enter your last name")
    last= last[0].upper()+ last[1:].lower()
    sid= input("Enter your student ID")







