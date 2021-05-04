#!/bin/bash

echo "---------"
echo "BYTE MODE"
echo "---------"

echo "valid"
time python3 steg.py -r -B -o1024 -i8 -wtest1.bmp > newfile; file newfile
sleep 0.1
echo "invalid"
time python3 steg.py -r -B -o1025 -i8 -wtest1.bmp > newfile; file newfile
sleep 0.1
echo "invalid"
time python3 steg.py -r -B -o1023 -i7 -wtest1.bmp > newfile; file newfile

echo "---------"
echo "BIT MODE"
echo "---------"

echo "valid"
time pypy3 steg.py -r -b -o1024 -i1 -wstegged-bit.bmp > newfile; file newfile

echo "invalid"
time pypy3 steg.py -r -b -o1023 -i1 -wstegged-bit.bmp > newfile; file newfile
echo "invalid"
time pypy3 steg.py -r -b -o223 -i1 -wstegged-bit.bmp > newfile; file newfile
