
#set up for code
import sys
s = sys.stdin.read()
b7=False
b8=False

# code for 7 bit
def Sbit(code):
    # set up messages and split the string into 7 character sized chucks
    message =""
    bit7=[code[i:i+7] for i in range(0, len(code), 7)]
    for i in bit7:
        # if a chunk is a number convert into into decimal and then
        ##into a charcter adding it to the end of the message
        if i.isnumeric():
            part=int(i, 2)
            message += chr(part)
        else:
        # if a chunk isn't a number add it as it is
            part=i
            message += (part)
    #print resulting message
    print (message)
# code for 8 bit
def Ebit(code):
    message =""
    # set up messages and split the string into 8 character sized chucks

    bit8=[code[i:i+8] for i in range(0, len(code), 8)]
    for i in bit8:
        # if a chunk is a number convert into into decimal and then
        ##into a charcter adding it to the end of the message
        if i.isnumeric():
            part=int(i, 2)
            message += chr(part)
        else:
        # if a chunk isn't a number add it as it is
            part=i
            message += (part)
    #print resulting message
    print (message)

# counts the number of digits in string provided
v=sum(c.isdigit() for c in s)

# check to see if the provided string is divisible by 7 or 8
if v%7==0:
    b7=True
    Sbit(s)
if v%8==0:
    b8=True
    Ebit(s)
# if now divisible by 7 or 8
if b7 ==False and b8 == False:
    print("No message was found")
    


