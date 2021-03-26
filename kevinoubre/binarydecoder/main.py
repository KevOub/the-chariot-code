
import sys


def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 

# Yield list of bytes (n-bits long)
def divideIntoNBits(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  
# Turns binary data to ascii
def binaryToAsciiChar(l):
    for val in l:
        yield chr(int(val,2))

""" 
CODE-FLOW:
* Split string into 7/8 bits list [bitsSeven/bitsEight]
* Use the function binaryToAscii to turn the bits to an array of ascii characters
* Use "".join() to combine the list together to make a single string
* print with prGreen to print green colors
"""

# Loop through stdin
for line in sys.stdin:
    line = line.strip('\n')
    bitsSeven = list(divideIntoNBits(line,7))
    bitsEight = list(divideIntoNBits(line,8))
    # Combine the list iterable to create a string
    data = "".join(list(binaryToAsciiChar(bitsEight)))
    print("\n\n")
    prGreen("8-bit val:\n{}".format(data))
    print("-----------------------------")
    data = "".join(list(binaryToAsciiChar(bitsSeven)))
    prRed("7-bit val:\n{}".format(data))
    