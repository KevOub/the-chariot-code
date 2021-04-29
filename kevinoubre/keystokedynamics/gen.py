
from random import randint,choice
from string import ascii_letters

LENGTH = 100000
CHARACTERSPLITTER = "\t"
typethis      = [choice(ascii_letters) for _ in range(LENGTH)]
pressing      = [randint(1,10)*0.01 for _ in range(LENGTH)]
releasing     = [randint(1,10)*0.01 for _ in range(LENGTH)]

for val in zip(pressing,typethis,releasing):
    print("\t".join(map(str,val)))