import socket
import sys
from time import time
from binascii import unhexlify

DEBUG = False

IP = '138.47.102.120'
PORT = 33333

ONE =  0.1
ZERO = 0.025

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((IP,PORT))

# Yield list of bytes (n-bits long)
def divideIntoNBits(l, n): 
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  
# Turns binary data to ascii through ITERABLES
def binaryToAsciiChar(l):
    for val in l:
        yield chr(int(val,2))

DELAY = 0
while True:
    try:
            
        data = s.recv(4096).decode()
        covert_bin = ""
        deltastream = []
        counter = 0
        while (data.rstrip("\n") != "EOF"):
            # sys.stdout.write(data)
            # sys.stdout.flush()
            # data = s.recv(4096).decode()
            t0 = time()
            data = s.recv(4096).decode()
            t1 = time()
            delta = round(t1-t0,3)

            deltastream.append(str(delta))
            if DEBUG:
                sys.stdout.write(" D: {}\n".format(delta))
                sys.stdout.flush()
                
            sys.stdout.write("0 = {} 1 = {}\r".format(max(deltastream),min(deltastream)))
            sys.stdout.flush()

            if counter > 8:
                break
            else:
                counter += 1

        s.close()
        # sys.stdout.write
        # sys.stdout.flush()


        break
    except:
        DELAY += 0.1
        time.sleep(0.1)


print("")

print("DELAY = {} 1 = {}  0 = {}".format(DELAY,max(deltastream),min(deltastream)))

# print("\nCOVERT:\t")
# print(covert_bin)

# bits = list(divideIntoNBits(covert_bin,8))
# output = "".join(list(binaryToAsciiChar(bits)))

# print("MESSAGE:\t")
# print(output)

