import socket
import time
from binascii import hexlify

ONE =  0.1
ZERO = 0.025
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

n = 0
for i in msg:
    c.send(i.encode())
    if n < len(covert_bin):
            
        if covert_bin[n] == "1":
            time.sleep(ONE)
        else:
            time.sleep(ZERO)
        n = (n+1)
    else:
        time.sleep(ZERO)


c.send("EOF".encode())
c.close()