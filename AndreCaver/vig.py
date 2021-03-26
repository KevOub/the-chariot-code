import sys
import time
#key initilization

#gets the position of the letter from 0-25
def Poscheck(value):
    if (122>=ord(value)>=97):
            return(ord(value)-97)
    else:
            return(ord(value)-65)
        
# purge the key of all non letters
def KeyPurge(k):
    newkey=""
    for i in k : 
        if(122>=ord(i)>=97 or 90>=ord(i)>=65 ):
            newkey+=i
    return newkey
            

# encrypts messgae using the key
def encr():
    while True:
        # "asks" for a message to encrypt
        message = input("")
        # variable set up
        x=0
        new=""
        # character by character, convert the encrypt message
        for i in message:
            #checks whether its a captial letter or not
            if (122>=ord(i)>=97):
                code=(Poscheck(i)+Poscheck(key[x]))%26
                new+=chr(code+97)
                x+=1
                if(x>len(key)-1):
                    x=0
            elif (90>=ord(i)>=65):
                code=(Poscheck(i)+Poscheck(key[x]))%26
                new+=chr(code+65)
                x+=1
                if(x>len(key)-1):
                    x=0
            else:
                # if not a letter add character to the message as is
                new+=i
        print(new)

def decr():
    while True:
        # "asks" for a message to encrypt
        message = input("")
        # variable set up
        x=0
        new=""
        # character by character, convert the encrypt message
        for i in message:
            #checks whether its a captial letter or not
            if (122>=ord(i)>=97):
                code=(26+Poscheck(i)-Poscheck(key[x]))%26
                new+=chr(code+97)
                x+=1
                if(x>len(key)-1):
                    x=0
            elif (90>=ord(i)>=65):
                code=(26+Poscheck(i)-Poscheck(key[x]))%26
                new+=chr(code+65)
                x+=1
                if(x>len(key)-1):
                    x=0
            else:
                # if not a letter add character to the message as is
                new+=i
        print(new)
# set the key

key=KeyPurge(sys.argv[2])

# check for encryption or decryption
if (sys.argv[1]== "-e") :
    encr()
elif (sys.argv[1] == "-d"):
    decr()
else:
    print("-e/-d was not given")
            
            
        
        
    
