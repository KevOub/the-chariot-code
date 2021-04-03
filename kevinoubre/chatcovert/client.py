import socket
import sys
from time import time
from binascii import unhexlify

DEBUG = True

IP = '127.0.0.1'
PORT = 1337

ONE =  1
ZERO = 0.025

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((IP,PORT))

data = s.recv(4096).decode()
while (data.rstrip("\n") != "EOF"):
    sys.stdout.write(data)
    sys.stdout.flush()
    # data = s.recv(4096).decode()
    covert_bin = ""
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()
    delta = round(t1-t0,3)
    if DEBUG:
        sys.stdout.write(" D: {}\n".format(delta))
        sys.stdout.flush()
    if (delta >= ONE):
        covert_bin += "1"
    else:
        covert_bin += "0"

s.close()



covert = ""
i = 0
while(i < len(covert_bin)):
    # process one byte at a time
    b = covert_bin[i:i+8]
    # convert int to ASCII 
    n = int("0b{}".format(b),2)
    try:
        covert += unhexlify("{0:x}".format(n))
    except:
        covert += "?"
    i += 8