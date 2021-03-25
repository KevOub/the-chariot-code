
import sys


def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 

# Yield list of bytes (n-bits long)
def divideIntoNBits(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  
# Checks to see if size is right
def checkValidSeq(l,n):
    for val in l:
        if len(l) != n:
            return False
    
    return True

# Turns binary data to ascii
def binaryToAsciiChar(l):
    for val in l:
        yield chr(int(val,2))


for line in sys.stdin:
    line = line.strip('\n')
    bitsSeven = list(divideIntoNBits(line,7))
    bitsEight = list(divideIntoNBits(line,8))
    # print(bitsSeven)
    # print(bitsEight)
    data = "".join(list(binaryToAsciiChar(bitsEight)))
    print("\n\n")
    prGreen("8-bit val:\n{}".format(data))
    # print("8-bit val:\t{}".format(data))
    print("~~~")
    data = "".join(list(binaryToAsciiChar(bitsSeven)))
    prRed("7-bit val:\n{}".format(data))
    # print("7-bit val:\t{}".format(data))
    