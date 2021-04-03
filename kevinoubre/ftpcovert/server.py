from ftplib import FTP

# FTP server details
# IP = "192.168.122.8"
IP = "138.47.102.120"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/7/"
MODE=7
USE_PASSIVE = True # set to False if the connection times out
REMOTE = False

if REMOTE:
        
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

else:
    # used for remote testing 
    if MODE==7:
        files = open('ftp7')
    else:
        files = open('ftp10')
    
    lines = files.readlines()
    data = []
    for f in lines:
        # print(f.rstrip("\n"))
        data.append(f.rstrip("\n"))

# Converts the permissions from the ftp server to binary data
def permToBin(permissions):
    validChars = ["r","w","x"]        
    if MODE == 10:
        # if it is mode 10, include d in chars
        validChars.append("d")
        # Then, create a string where dashes are 0 and vice versa
        return "".join(["1" if p in validChars else "0" for p in permissions])
    if MODE == 7:
        # if any characters are not --- in the first 3 bits, break
        # Could this be better? Yes
        if any([True for p in permissions[:3]  if p in validChars]):
            return "0"
        
        # otherwise, convert to binary:
        else:
            return "".join(["1" if p in validChars else "0" for p in permissions[3:]])

# Yield list of bytes (n-bits long)
def divideIntoNBits(l, n): 
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  
# Turns binary data to ascii through ITERABLES
def binaryToAsciiChar(l):
    for val in l:
        yield chr(int(val,2))


# mode 7 decoding
def decode7(perms):
    output = ""
    for p in perms:
        # get the 7 bits and fill out to 8 bits
        binData = permToBin(p[:10]).zfill(8)
        # add the corresponding char to the output
        output += chr(int(binData,2))
    # return it to match the style of the other decode
    return output
    
# mode 10 decoding
def decode10(perms):
    # create long binary string from permissions
    data = "".join([permToBin(p[:10]) for p in perms])
    # borrowed code from binary decoder
    bitsSeven = list(divideIntoNBits(data,7))
    output = "".join(list(binaryToAsciiChar(bitsSeven)))
    return output

       


if MODE == 7:
    print(decode7(data))
if MODE == 10:
    print(decode10(data))
    