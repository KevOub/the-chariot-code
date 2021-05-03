from random import choice, uniform
from sys import stdout, stderr
from time import sleep, time
from datetime import datetime
from numpy import array
from tkinter import Tk

DEBUG = True

SLEEP_TIME = 3
MIN_KHT = 0.1
MAX_KHT = 1.0
MIN_KIT = 0.1
MAX_KIT = 1.0
# TEXTS = [ "My password is incorrect.", "Are you frustrated or excited?","Can you believe cyberstorm is in two weeks?","Can you smell the popcorn?" ]
TEXTS = ["test"]
#TEXTS = [ "My password is incorrect.", "Dr. Gourd is 1337!", "Dr. Kiremire knows his stuff.", "Dr. Cherry is in this class." ]
VALID_KEYS = [ chr(c) for c in range(ord("a"), ord("z") + 1) ] + [ chr(c) for c in range(ord("A"), ord("Z") + 1) ]
# VALID_KEYS = None
VALID_KEYCODES = [ "Return" ]
ACCEPTABLE_THRESHOLD = 0.005

# gets the text, features, and matching data for the features
def get_features():
    # randomly select a text
    text = choice(TEXTS)

    # determine the features for this text
    # first, the characters
    features = list(text)
    # next, the character transitions
    for i in range(len(features) - 1):
        features.append("{}{}".format(features[i], features[i+1]))

    # get random values for KHTs
    data = []
    for i in range(len(features) // 2 + 1):
        data.append("%.2f" % uniform(MIN_KHT, MAX_KHT))
    # and for KITs
    for i in range(len(features) // 2):
        data.append("%.2f" % uniform(MIN_KIT, MAX_KIT))

    return text, features, data

# invoked when a key is pressed
def pressed(key):
    global keys, press_times

    # we only care about valid keys
#    if (key.char == key.keysym and key.char in VALID_KEYS):
    if (key.char in VALID_KEYS):
        # append the key
        keys.append(key.char)
        # and add the press time
        press_times.append(time())
        # display the key
        stdout.write(key.char)
        stdout.flush()

# invoked when a key is released
def released(key):
    global keys, press_times, release_times
    # VALID_KEYS = list(set(c for c in text))
    # we only care about valid keys
    # if (key.char == key.keysym and key.char in VALID_KEYS):
    tmp = key.char
    tmp = tmp.strip("\n")
    if DEBUG:
        if (tmp in VALID_KEYS):
            # stdout.write("IS NOT IN VALID_KEYS \n")
            stdout.write("\n")  
            stdout.write(str(type(key.char)))
            stdout.write("\n")
        
    if (key.char in "".join(VALID_KEYS)):
        # if (True):
        # add the release time
        # stdout.write("\n")  
        # stdout.write(str(time()))
        # stdout.write("\n")

        release_times.append(time())
    
    # although we also care about soe special keys
    elif (key.keysym in VALID_KEYCODES):

        # return/enter ends the sample
        if (key.keysym == "Return"):
            stdout.write("\n")
            stdout.flush()

        # invalidate the sample if it isn't the same as the text
        if ("".join(keys) != text):
            stderr.write("Sample does not match the specified text!\n")
        else:
            if (DEBUG):
                stderr.write("Keys: ")
                stderr.write(print_sample(keys))
                stderr.write("Press times: ")
                stderr.write(print_sample(press_times))
                stderr.write("Release times: ")
                stderr.write(print_sample(release_times))

            # calculate key hit times (KHTs) and key interval times (KITs)
            sample_KHTs = []
            sample_KITs = []
            try:                    
                sample_KHTs = (array(release_times) - array(press_times)).tolist()
                sample_KITs = (array(press_times[1:]) - array(release_times[:-1])).tolist()
            except:
                print(array(release_times))
                print(type(release_times))
                
                print(array(press_times))
                print(type(press_times))
                


            if (DEBUG):
                stderr.write("Sample KHTs: ")
                stderr.write(print_sample(sample_KHTs))
                stderr.write("Sample KITs: ")
                stderr.write(print_sample(sample_KITs))

            ### check if valid
            KHTs = [ float(n) for n in data[:len(data) // 2 + 1] ]
            KITs = [ float(n) for n in data[len(data) // 2 + 1:] ]
            if (DEBUG):
                stderr.write("KHTs: ")
                stderr.write(print_sample(KHTs))
                stderr.write("KITs: ")
                stderr.write(print_sample(KITs))
            try:
                KHT_diffs = (array(sample_KHTs) - array(KHTs)).tolist()
                KIT_diffs = (array(sample_KITs) - array(KITs)).tolist()
            except:
                pass
            if (DEBUG):
                stderr.write("KHT_diffs: ")
                stderr.write(print_sample(KHT_diffs))
                stderr.write("KIT_diffs: ")
                stderr.write(print_sample(KIT_diffs))
            if (all(abs(n) <= ACCEPTABLE_THRESHOLD for n in KHT_diffs) and all(abs(n) <= ACCEPTABLE_THRESHOLD for n in KIT_diffs)):
                stdout.write("SAMPLE ACCEPTED ({})!\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                stdout.flush()
            else:
                stdout.write("SAMPLE REJECTED.\n")
                stdout.flush()

            # clear the sample
            keys = []
            press_times = []
            release_times = []

        # destroy the window
        w.destroy()

# prints the samples in the specified list
def print_sample(sample):
    s = ""

    # build a string from the samples
    for item in sample:
        s += "{}, ".format(item)

    return s[:-2] + "\n"

######
# MAIN
######
# get the text, features, and data
text, features, data = get_features()
VALID_KEYS = list(set(c for c in text))

# display a header
print("For this sample, type the following text (followed by Enter): {}".format(text))
print()
print("Here are the features:")
print(features)
print()
print("Here are the matching KHTs and KITs:")
print(data)
print()

# wait for user to press Enter
stdout.write("Press Enter when ready (listener will be enabled {} seconds afterward)...".format(SLEEP_TIME))
stdout.flush()
input()

# delay to ignore any buffered key presses/releases
stdout.write("Delaying for {} seconds".format(SLEEP_TIME))
for i in range(SLEEP_TIME):
    sleep(1)
    stdout.write(".")
    stdout.flush()
stdout.write("\n\n")
stdout.flush()

# start training by taking samples
# initialize keys, press times, release times, and a sample counter
keys = []
press_times = []
release_times = []

# display the prompt
stdout.write("Type the text (make sure that the popup window has focus):\n")
stdout.flush()
# create the Tkinter window to capture text
w = Tk()
w.geometry("800x600")
w.configure(background="black") 
# bind key press and release events
w.bind("<KeyPress>", pressed)
w.bind("<KeyRelease>", released)
# show the window
w.mainloop()

