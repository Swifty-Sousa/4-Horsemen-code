


def parse_card(buffone_raw):
    print("reached parse card")
    buffone_holder= buffone_raw.split('=')
    buffone_holder[0]= buffone_holder[0][2:]
    card_name= buffone_holder[0]
    card_sid= buffone_holder[1]
    holder= buffone_holder[2].split('/')
    card_first= holder[0][0]+ holder[0][1:].lower()
    card_last= holder[1][0]+ holder[1][1:].lower()
    reply= [card_first, card_last, card_sid, card_name]
    print("sending reply")
    return reply

def Ver_Event(eventid):
    print(eventid)
    #actually verify the garbage

def somethingorother():    
    first = input("Enter your first name")
    first= first[0].upper()+ first[1:].lower()
    last= input("Enter your last name")
    last= last[0].upper()+ last[1:].lower()
    sid= input("Enter your student ID")







