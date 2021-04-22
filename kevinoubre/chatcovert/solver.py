import socket
import sys
from time import time
from binascii import unhexlify

DEBUG = False

IP = '127.0.0.1'
PORT = 1337

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

    deltastream.append(delta)
    if DEBUG:
        sys.stdout.write(" D: {}\n".format(delta))
        sys.stdout.flush()
    

    sys.stdout.write(max(deltastream))
    sys.stdout.write(min(deltastream))
    sys.stdout.flush()

s.close()


# print("\nCOVERT:\t")
# print(covert_bin)

# bits = list(divideIntoNBits(covert_bin,8))
# output = "".join(list(binaryToAsciiChar(bits)))

# print("MESSAGE:\t")
# print(output)

