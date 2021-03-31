import os

""" 
ignore three dashes at front
"""
MODE=7

# takes blob of data and returns corresponding rwx
def handlePermissions(permissions):
    splitPermissions = divideIntoNBits(permissions,3)
    output = ""
    data = 0
    for p in splitPermissions:
        data += 4 if p[2] == "1" else 0
        data += 2 if p[1] == "1" else 0
        data += 1 if p[0] == "1" else 0
        output += str(data)
        data = 0
    return output[::-1]




# Yield list of bytes (n-bits long) borrowed from bindecoder
def divideIntoNBits(l, n): 
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  

def encodeMessage(message):
    # numberMessage = [ for m in message]

    binaryMessage = [f'{ord(m):010b}' for m in message]
    for rune in binaryMessage:
        print("---")
        # if the first bit is 1, it is directory time
        if rune[0] == "1":
            # os.system(mkdir $FILE)
            # chmod but with magics
            print("mkdir FILE")
            print("chmod {}".format(handlePermissions(rune[1:])))
        else:
            # os.system(touch $FILE)
            # test = handlePermissions(rune[1:])
            # print(test)
            print("touch FILE")
            print("chmod {} FILE".format(handlePermissions(rune[1:])))
            
def decodeMessage(perms):
    output = ""
    validChars = ["r","w","x"]        
    for index,perm in enumerate(perm):
        if MODE == 7:
            pass
        if MODE == 10:
            output += "1" if perm in validChars else "0"


        
mess = "Encode this please"
encodeMessage(mess)
# print(handlePermissions("1110100"))
print("!!!\n")
decodeMessage("/home/kevin/programming/the-chariot-code/kevinoubre/binarydecoder")