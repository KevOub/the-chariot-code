import sys
import os,stat
from itertools import cycle
import string

DECODE = False

# How I handled flags
def handleFlag(flags):
    # have counter going to get next item in list nicely
    for i,flag in enumerate(flags):
        if (i+1) < len(flags):
            if flag == "-e" and flags[i+1] != None :
                # print("ENCODING WITH THE FOLLOWING KEY:\t{}".format(flags[i+1]))
                return True,flags[i+1]
            if flag == "-d" and flags[i+1] != None :
                # print("DECODING WITH THE FOLLOWING KEY:\t{}".format(flags[i+1]))
                return False,flags[i+1]
        # error handling
        else:
            if flag in ["-e","-d"]:
                print("{} needs a key to decrypt!".format(flag))
                raise SyntaxWarning
            else:
                print("{} is not a recognized flag".format(flag))
                print("-e $KEY encrypts")
                print("-d $KEY decrypts")
                raise SyntaxWarning



""" 
let p0,p1,p2...pn be the plaintext translated to ascii
let k0,k1,k2...kn be the key translated to ascii

ENCRYPTION:
ci = pi + (kj % 26)
kj = i % x where x is len(kj)
"""

def encrypt(plain,key):

    lookuptable = string.ascii_lowercase + string.ascii_uppercase
    output = ""

    # nasty code that does the following: creates a tuple pair such that the key and plaintext have a corrresponding match
    if len(plain) >= len(key):
        loopedVals = list(zip(stringToNum(plain), cycle(stringToNum(key))))
    else:
        loopedVals = list(zip(stringToNum(key), cycle(stringToNum(plain))))[:len(plain)]

    # iterate through the looped vals 
    for p,k in loopedVals:
        """ 
        if not all([False if val != chr(p) else True for val in lookuptable ]):
            output += chr(p) 
        """
        # this means this code was unrecognized and sent back as negative!
        if p < 0:
            output += chr(abs(p))
        if p > 26:
            output += lookuptable[((p+k) % 26) + 26]
        else:
            output += lookuptable[((p+k) % 26)]

    return output
        

def decrypt(plain,key):
    lookuptable = string.ascii_lowercase + string.ascii_uppercase
    output = ""

    if len(plain) >= len(key):
        loopedVals = list(zip(stringToNum(plain), cycle(stringToNum(key))))
    else:
        loopedVals = list(zip(stringToNum(key), cycle(stringToNum(plain))))[:len(plain)]

    for p,k in loopedVals:
        """ 
        if not all([False if val != chr(p) else True for val in lookuptable ]):
            output += chr(p)
         """
        if p < 0:
            output += chr(abs(p))
        if p > 26:
            output += lookuptable[((p-k) % 26) + 26]
        else:
            output += lookuptable[((p-k) % 26)]
    return output

DECODE,key = handleFlag(sys.argv)


# converts the characters to 0-52 range where 0-26 is lower and 26-52 is upper
def stringToNum(runes):
    lookuptable = string.ascii_lowercase + string.ascii_uppercase
    for rune in runes:
        if rune not in lookuptable:
            # TODO broken
            yield -ord(rune)
        else:
            yield  lookuptable.index(rune)


# numKey = list(stringToNum(key))
mode = os.fstat(0).st_mode
while True:
    
    if DECODE:
        usr = input("")
        numUsr = list(stringToNum(usr))
        print("\n{}\n".format(encrypt(usr,key)))
    else:
        usr = input("")
        numUsr = list(stringToNum(usr))
        print("\n{}\n".format(decrypt(usr,key)))
        