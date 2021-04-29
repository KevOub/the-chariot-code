from pynput.keyboard import Key, Listener
from termios import tcflush, TCIFLUSH
from sys import stdin,stdout

def on_press(key):
    try:
        print(key.char.encode("ascii"))
    except AttributeError:
        print(str(key))
    # print("{} pressed ".format(key))


def on_release(key):
    # print("{} released ".format((key)))
    if (key == Key.esc):
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

tcflush(stdin,TCIFLUSH)