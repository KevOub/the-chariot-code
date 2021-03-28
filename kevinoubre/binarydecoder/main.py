####
# Team Chariot
# March 29th - binary decoder
###

# We also managed to get it in one line!
""" 
import sys;bintoascii = lambda li, x : "".join([chr(int(val,2)) for val in [li[i:i+(8 if len(li) % 8 == 0 else 7)] for i in range(0,len(li),8 if len(li) % 8 == 0 else 7)]]);print(bintoascii(sys.stdin.read().strip("\n"),8))
"""

import sys



# Yield list of bytes (n-bits long)
def divideIntoNBits(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  
# Turns binary data to ascii through ITERABLES
def binaryToAsciiChar(l):
    for val in l:
        yield chr(int(val,2))

""" 
CODE-FLOW:
* Split string into 7/8 bits list [bitsSeven/bitsEight]
* Use the function binaryToAscii to turn the bits to an array of ascii characters
* Use "".join() to combine the list together to make a single string
* Finally, print both because why not!
"""

# Loop through stdin
for line in sys.stdin:
    line = line.strip('\n')
    # splits the bits
    bitsSeven = list(divideIntoNBits(line,7))
    bitsEight = list(divideIntoNBits(line,8))
    # Combine the list iterable to create a string
    data = "".join(list(binaryToAsciiChar(bitsEight)))
    print("\n\n")
    print("8-bit val:\n{}".format(data))
    print("-----------------------------")
    # Combine the list iterable to create a string
    data = "".join(list(binaryToAsciiChar(bitsSeven)))
    print("7-bit val:\n{}".format(data))
    