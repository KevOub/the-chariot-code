##############################################################################
# Name: Brianna Stewart
# Date: 04/21/2021
# Description: 04- FTP (timing) Covert Channel Program | Client | Ver: 3.8.5
##############################################################################
import socket
from sys import stdout
from time import sleep, time
from binascii import unhexlify

IP = "138.47.102.120"
PORT = 33333
ZERO = 0.3
ONE = 0.1
DEBUG = True
ROUND_TO = 3

# Connect to the chat server.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

# Receive an overt message until the end of it is reached (EOF).
covert_binary = ""
overt = s.recv(4096).decode()
while(overt.rstrip("\n") != "EOF"):
    # Display the overt message as it is being received (to stdout).
    stdout.write(overt)
    stdout.flush()

    # Time the delays between the characters recieved of an overt message.
    t0 = time()
    overt = s.recv(4096).decode()
    t1 = time()
    delta = round((t1 - t0) , ROUND_TO)

    # Debug.
    if(DEBUG):
        stdout.write(" {}\n".format(delta))
        stdout.flush()

    # Store the timed delays of the overt message.
    if(delta >= ONE):
        covert_binary += "1"
    else:
        covert_binary += "0"
# Disconnect from the chat server.
s.close()

# Covert the binary covert message to ASCII.
covert_message = ""
index = 0
while(covert_message[len(covert_message)-3:] != "EOF"):
    # Process one byte at a time.
    binary = covert_binary[index:(index + 8)]
    print("Binary: " + binary)
    try:
        decimal = int("0b{}".format(binary), 2)
        #print("Decimal: " + str(decimal))
        covert_message += chr(decimal)
    except:
        covert_message += "?"
        break

    index += 8
# Output the covert message (to stdout).
print("\nCovert message:", covert_message[:-3])
