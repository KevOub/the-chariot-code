from pynput.keyboard import Key, Controller
from time import sleep
from random import randint
from termios import tcflush, TCIFLUSH

from sys import stdin,stdout


DEBUG = True


# string = "a really long string"
password = input()
features = input()

password = password.split(",")
password = password[:len(password)//2+1]
password = "".join(password)

features = features.split(",")
features = [float(a) for a in features]
# features = list(map(float,features))
keypress = features[:len(features)//2+1]
keyinterval = features[len(features)//2+1:]


if DEBUG:    
    print("password = {}".format(password))
    print("keypress = {}".format(keypress))
    print("keyinterval = {}".format(keyinterval))
    print("features = {}".format(features))

keyboard = Controller()

# for char in string:
#     keyboard.press(char)
#     sleep(randint(1,10)*0.01)
#     keyboard.release(char)
#     sleep(randint(1,10)*0.01)

# # keyboard.press('a')
# # keyboard.release('a')


# # tcflush(stdin,TCIFLUSH)
# tcflush(stdout,TCIFLUSH)
# # print()

""" 
*TEMPLATE* [measurements, key to press] 
while True:
    press key
    wait 
    release key
    wait 
    
"""