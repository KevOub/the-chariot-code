import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1337
s.bind(("", port))

while True:
    s.listen(0)
    print("server is listening")

    c, addr = s.accept()

    from binascii import hexlify
    covert = "would you kindly" + "EOF"
    covert_bin = ""
    for i in covert:
        # convert each character to a full byte
        # hexlify converts ASCII to hex
        # int converts the hex to a decimal integer# bin provides its binary representation (with a 0b#  prefix that must be removed)
        # that's the [2:] (return the string from the third#  character on)
        # zfill left-pads the bit string with 0s to ensure a
        # full byte
        covert_bin += bin(int(hexlify(i.encode()),16))[2:].zfill(8)

    import time
    ZERO = 0.025
    ONE = 0.1
    msg = "The assassin has overcome my final line of defense, and now he plans to murder me. In the end what separates a man from a slave? Money? Power? No, a man chooses, and a slave obeys! "
    n = 0
    for i in msg:
        c.send(i.encode())
        if (covert_bin[n] == "0"):
            time.sleep(ZERO)
        else:
            time.sleep(ONE)
        n = (n + 1) % len(covert_bin)
    c.send("EOF".encode())
    c.close()
    print("message sent")