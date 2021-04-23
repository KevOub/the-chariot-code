import socket
import time
from binascii import hexlify
import sys

ONE =  0.1
ZERO = 0.025
DELAY = 3
DEBUG = True
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 1337
s.bind(("",port))
s.listen(0)
c,addr = s.accept()

# message from https://www.gutenberg.org/files/30142/30142-0.txt, a random public domain hacker book
 
covert = "Jane McGonical, Designer, I Love Bees" 
covert_bin = ""
for i in covert:
    covert_bin += bin(int(hexlify(i.encode()),16))[2:].zfill(8)

covert_bin.encode()
 
msg = '''
Cory Doctorow is a fast and furious storyteller who gets all the
details of alternate reality gaming right, while offering a startling,
new vision of how these games might play out in the high-stakes context
of a terrorist attack. Little Brother is a brilliant novel with a bold
argument: hackers and gamers might just be our country's best hope for
the future.
'''
while True:
    try:
                
        n = 0
        time.sleep(DELAY)
        for i in msg:
            c.send(i.encode())
            if n < len(covert_bin):
                if DEBUG:
                    print("DATA:\t",covert_bin[n]) 
                if covert_bin[n] == "1":
                    time.sleep(ONE)
                else:
                    time.sleep(ZERO)
                n = (n+1)
            else:
                time.sleep(ZERO)
            
            if DEBUG and n % 8 == 0:
                print("\n   ")


        c.send("EOF".encode())
        c.close()
    except:
        sys.stdout.write("RESTARTING...")
        time.sleep(DELAY)