import socket

# server conection set up
ip = "localhost"
port = 1337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

# timeing settings
ZERO = 0.025
ONE = 0.1

covert_bin = ""
import sys
data = s.recv(4096).decode()

# receve message from server and mark timeings
while (data.rstrip("\n") != "EOF"):
    sys.stdout.write(data)
    sys.stdout.flush()
    
    from time import time
    
    # converting timeings to binary
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()
    delta = round(t1 - t0, 3)
    #print(delta)
    if (delta >= ONE):
        #print("Hit 1")
        covert_bin += "1"
    else:
        covert_bin += "0"

s.close()
#print("\n")
#print(covert_bin)
#print(len(covert_bin))

# convert timing binary to actual message
covert = ""
i = 0
while (i < len(covert_bin)):
    # process one byte at a time
    b = covert_bin[i:i + 8]
    # convert it to ASCII
    covert += chr(int("0b{}".format(b), 2))
    i += 8
    #print(covert)
    #print(covert[-4:-1])

    # check for end of file
    if covert[-4:-1] == "EOF":
        covert = covert[0:-4]
        break
print(f"\n{covert}")