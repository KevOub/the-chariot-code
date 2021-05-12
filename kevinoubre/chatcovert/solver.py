import socket
import sys
from time import time,sleep
from binascii import unhexlify
from jenkspy import JenksNaturalBreaks


DEBUG = False

IP = '192.168.122.1'
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


jnb = JenksNaturalBreaks()


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
            # if DEBUG:
            #     sys.stdout.write(" D: {}\n".format(delta))
            #     sys.stdout.flush()
                
            sys.stdout.write("0 = {} 1 = {}\r".format(max(deltastream),min(deltastream)))
            sys.stdout.flush()



            if counter > 32:
                break
            else:
                counter += 1

        s.close()
        # sys.stdout.write
        # sys.stdout.flush()


        break
    except:
        DELAY += 0.1
        sleep(0.1)


print("")


deltastream = list(map(float,deltastream))
jnb.fit(deltastream)
try:
    # sys.stdout.write("LABELS: {} \n".format(jnb.labels_))
    sys.stdout.write("GROUPS: {} \n".format(jnb.groups_))
    sys.stdout.write("INNER BREAKS: {} \n".format(jnb.inner_breaks_))
    sys.stdout.flush()

except:
    sys.stdout.write("FAIL\n")

print("DELAY = {} 1 = {}  0 = {}".format(DELAY,max(deltastream),min(deltastream)))

# print("\nCOVERT:\t")
# print(covert_bin)

# bits = list(divideIntoNBits(covert_bin,8))
# output = "".join(list(binaryToAsciiChar(bits)))

# print("MESSAGE:\t")
# print(output)

