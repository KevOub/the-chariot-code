import sys

# Read the file
cipher = sys.stdin.buffer.read()
with open("key2", "rb") as binary_file:
    # Read the whole file at once
    key = binary_file.read()


# inline function
xor = lambda a, b : (int(a) ^ int(b))
# apply to value in the cipher, key combo
xorData = bytes(map(lambda x : xor(x[0],x[1]) ,zip(cipher,key)))

# write to terminal
sys.stdout.buffer.write(xorData)
