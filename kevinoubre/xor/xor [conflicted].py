
import sys

# with open("ciphertext", "rb") as binary_file:
    # Read the whole file at once
    # cipher = binary_file.read()
cipher = sys.stdin.buffer.read()
with open("key2", "rb") as binary_file:
    # Read the whole file at once
    key = binary_file.read()

xorHex = lambda a, b : hex(a ^ b) 
xorString = lambda a, b : str(a ^ b)
xorDataHex = map(lambda x : xorHex(x[0],x[1])[2:],zip(cipher,key))
xorDataHex = map(lambda x : xorString(x[0],x[1])[2:],zip(cipher,key))
print(list(xorData))

# sys.stdout.buffer.write("".join(list(map(lambda x : hex((int(x[0]) ^ int(x[1])))[2:],zip(cipher,key)))).encode())