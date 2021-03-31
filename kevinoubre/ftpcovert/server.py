from ftplib import FTP

# FTP server details
IP = "192.168.122.8"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/7/"
USE_PASSIVE = True # set to False if the connection times out

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the FTP server
ftp.quit()

data = []
justperms = []
print("FILES:")
# display the folder contents
for f in files:
    print(f)
    data.append(f)
    justperms.append(f[:10])



MODE=10

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

    # binaryMessage = [f"{ord(m):010b}" for m in message]
    binaryMessage = [f"{ord(m):010b}" for m in message]
    print(binaryMessage)
    for rune in binaryMessage:
        print("---")
        # if the first bit is 1, it is directory time
        if rune[0] == "1":
            # os.system(mkdir $FILE)
            # chmod but with magics
            # print("mkdir FILE")
            print("chmod {}".format(handlePermissions(rune[1:])))
        else:
            # os.system(touch $FILE)
            # test = handlePermissions(rune[1:])
            # print(test)
            # print("touch FILE")
            print(rune[1:])
            print(chr(int(rune[1:],2)))

            print("chmod {} FILE".format(handlePermissions(rune[1:])))


def binaryToAsciiChar(l):
    for val in l:
        yield chr(int(val,2))

# takes the array justperms and iterates through them to create the message back 
def decodeMessageToBinary(perms):
    output = ""
    validChars = ["r","w","x"]        
    for index,perm in enumerate(perms):
        if MODE == 7:
            pass
        if MODE == 10:
            # print("LOUD: {}".format(perm))
            binPerm = "".join(["1" if p in validChars else "0" for p in perm]) 
            print(binPerm)
            # runePermission = chr(int("0b"+binPerm,2))
            runePermission = ""
            print(int(binPerm,2))
            output += runePermission
    
    return output

encodeMessage("A")
print("~~~")
print(decodeMessageToBinary(justperms))

