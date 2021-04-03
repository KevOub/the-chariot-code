import socket
import time
from binascii import hexlify

ONE =  1
ZERO = 0.025
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 1337
s.bind(("",port))
s.listen(0)
c,addr = s.accept()

""" 
covert = "blah" + "EOF"
covert_bin = ""
for i in covert:
    covert_bin += bin(int(hexlify(i),16))[2:].zfill(8)

covert_bin.encode()
 """
 
msg = "Test"
for i in msg:
    c.send(i.encode())
    if i == "1":
        time.sleep(ONE)
    else:
        time.sleep(ZERO)

c.send("EOF".encode())
c.close()