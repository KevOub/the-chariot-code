#!/bin/bash


time python3 steg.py -r -B -o1024 -i8 -wtest1.bmp > newfile; file newfile
sleep 0.1
time python3 steg.py -r -B -o1025 -i8 -wtest1.bmp > newfile; file newfile
sleep 0.1
time python3 steg.py -r -B -o1023 -i7 -wtest1.bmp > newfile; file newfile
