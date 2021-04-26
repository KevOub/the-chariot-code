
import sys

# with open("ciphertext", "rb") as binary_file:
    # Read the whole file at once
    # cipher = binary_file.read()
cipher = sys.stdin.buffer.read()
with open("key", "rb") as binary_file:
    # Read the whole file at once
    key = binary_file.read()

# assert(len(key) == len(cipher) )

xorHex = lambda a, b : hex((int(a) ^ int(b))) 
xorString = lambda a, b : str(int(a) ^ int(b))
xorBest = lambda a, b : (int(a) ^ int(b))


def bitstreamOfData(stringdata):
    for data in stringdata:
        for i in bin(data)[2:]:
            yield i



# xorDataHex = "".join(list(map(lambda x : xorHex(x[0],x[1])[2:],zip(cipher,key))))
xorDatTest = bytes(map(lambda x : xorBest(x[0],x[1]) ,zip(cipher,key)))

# xorDataString = "".join(list(map(lambda x : xorDataHex(x[0],x[1])[2:],zip(cipher,key))))


# print(xorDataString)
# print(xorDataHex)
sys.stdout.buffer.write(xorDatTest)

# print(list(bitstreamOfData(cipher)))

# sys.stdout.buffer.write("".join(list(map(lambda x : hex((int(x[0]) ^ int(x[1])))[2:],zip(cipher,key)))).encode())