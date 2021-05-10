import sys
from itertools import cycle

# Read the file
cipher = sys.stdin.buffer.read()
with open("key", "rb") as binary_file:
    # Read the whole file at once
    key = binary_file.read()


# inline function
xor = lambda a, b : (int(a) ^ int(b))
# apply to value in the cipher, key combo



if len(key) > len(cipher):
    combo = zip(cycle(cipher),key)
if len(cipher) > len(key):
    combo = zip(cipher,cycle(key))
else:
    combo = zip(cipher,key)

xorData = bytes(map(lambda x : xor(x[0],x[1]) ,combo))

# write to terminal
sys.stdout.buffer.write(xorData)
