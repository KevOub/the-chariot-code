from pynput.keyboard import Key, Controller
from time import sleep
from sys import stdin



keyboard = Controller()

for line in stdin:
    data = line.split("\t")
    data = [l.strip("\n") for l in data]
    keyboard.press(data[1])
    sleep(float(data[0]))
    keyboard.release(data[1])
    sleep(float(data[2]))