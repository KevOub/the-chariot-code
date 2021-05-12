###############################################################################
# Name: Team Chariot- Ahmed Mudhish, Andre Caver, Avery Miller, Brianna Stewart
# Garrett Gresham, Kevin Oubre, Sydney Holland
# Date: 05/07/2021
# Description: 05- Timelock Program | Ver: 3.8.5
###############################################################################
import sys
import datetime as dt
from dateutil import tz
import hashlib

SECONDS = 60
TIMEZONE = tz.gettz("America/Chicago")
DEBUG = True
TESTING = True

# Get the epoch time (from terminal) in a list.
epoch_time = list(map(int, (sys.stdin.readline()).split()))
# Get the current system time in a list.
formatted_time = (dt.datetime.now()).strftime("%Y %m %d %H %M %S")
current_time = list(map(int, formatted_time.split()))

# Create datetime objects for epoch and current system times.
if(DEBUG and TESTING):
    # epoch_dt = dt.datetime(2020, 5, 7, 10 ,00 ,00 , tzinfo=TIMEZONE)
    # current_dt = dt.datetime(2021, 5, 7, 11, 19, 5, tzinfo=TIMEZONE)

    # epoch_dt = dt.datetime(2017, 1, 1, 0, 0, 0, tzinfo=TIMEZONE)
    # current_dt = dt.datetime(2017, 3, 23, 18, 2, 6, tzinfo=TIMEZONE)
    # epoch_dt = dt.datetime(1999, 12, 31, 23, 59, 59, tzinfo=TIMEZONE)
    # current_dt = dt.datetime(2017, 4, 23,18, 2, 30, tzinfo=TIMEZONE)
    # epoch_dt = dt.datetime(2001, 2, 3, 4, 5, 6, tzinfo=TIMEZONE)
    # current_dt = dt.datetime(2010, 6, 13, 12, 55, 34, tzinfo=TIMEZONE)
    # epoch_dt = dt.datetime(2001, 2, 3, 4, 5, 6, tzinfo=TIMEZONE)
    # current_dt = dt.datetime(2010, 6, 13, 12, 55, 34, tzinfo=TIMEZONE)
    epoch_dt = dt.datetime(2015, 1, 1, 0, 0, 0, tzinfo=TIMEZONE)
    # current_dt = dt.datetime(2015, 5, 15, 14, 0, 0, tzinfo=TIMEZONE)
    # epoch_dt = dt.datetime(2014, 12, 31, 0, 0, 0, tzinfo=TIMEZONE)
    # current_dt = dt.datetime(2015, 1, 1, 0, 0, 0, tzinfo=TIMEZONE)
    # epoch_dt = dt.datetime(2014, 12, 31, 0, 0, 0, tzinfo=TIMEZONE)
    # current_dt = dt.datetime(2015, 1, 1, 0, 0, 30, tzinfo=TIMEZONE)
    # epoch_dt = dt.datetime(2014, 12, 31, 0, 0, 0, tzinfo=TIMEZONE)
    # current_dt = dt.datetime(2015, 1, 1, 0, 1, 0, tzinfo=TIMEZONE)
    # epoch_dt = dt.datetime(2014, 12, 31, 0, 0 , 0, tzinfo=TIMEZONE)
    # current_dt = dt.datetime(2015, 1, 1, 0, 1, 30, tzinfo=TIMEZONE)
    # epoch_dt = dt.datetime(1974, 6, 1, 8, 57, 23, tzinfo=TIMEZONE)
    # current_dt = dt.datetime(2017, 4, 26, 15, 14, 30, tzinfo=TIMEZONE)
    # print("Epoch Time: {}\nCurrent Time: {}\n".format(epoch_dt, current_dt))
# else:
    # epoch_dt = dt.datetime(epoch_time[0], epoch_time[1], epoch_time[2], \
    #                        epoch_time[3], epoch_time[4], epoch_time[5], \
    #                        tzinfo=TIMEZONE)
    current_dt = dt.datetime(current_time[0], current_time[1], \
                             current_time[2], current_time[3], \
                             current_time[4], current_time[5], \
                             tzinfo=TIMEZONE)
    print("Epoch Time: {}\nCurrent Time: {}\n".format(epoch_dt, current_dt))

# Calculate the elapsed time between the epoch and current system times.
elapsed_time = int((current_dt - epoch_dt).total_seconds())

if(DEBUG):
    print("Elasped Time Before DST: {}".format(elapsed_time))

# Accommodate if there is a difference in Daylight Savings Time (DST).
# If the current time is affected by DST (an hour forward), subtract an hour
# in seconds. Otherwise, add an hour in seconds.
if(epoch_dt.dst() < current_dt.dst()):
    elapsed_time -= 3600
elif(epoch_dt.dst() > current_dt.dst()):
    elapsed_time += 3600

if(DEBUG):
    print("Epoch DST: {}\nCurrent DST: {}".format(epoch_dt.dst(), current_dt.dst()))
    print("Elasped Time After DST: {}\n".format(elapsed_time))

# Determine the beginning interval based on the epoch's seconds.
seconds_past = ((SECONDS - epoch_dt.second) + current_dt.second) % SECONDS
beginning_interval = elapsed_time - seconds_past

if(DEBUG):
    print("Seconds Past: {}\nBeginning Interval: {}\n".format(seconds_past, beginning_interval))


# Create MD5 hashes of the beginning interval.
first_hash = (hashlib.md5(str(beginning_interval).encode())).hexdigest()
second_hash = (hashlib.md5(first_hash.encode())).hexdigest()

if(DEBUG):
    print("First Hash: {}\nSecond Hash: {}".format(first_hash, second_hash))

# Create the 5-character code of the second hash.
code = ""
letter_count = 0
digit_count = 0
# Get the first two letters from left-to-right.
for character in second_hash:
    if(character.isalpha()):
        if(letter_count == 2):
            break
        code += character
        letter_count += 1

# Get the first two single-digit integers from right-to-left.
for character in reversed(second_hash):
    if(character.isdigit()):
        if(digit_count == 2):
            break
        code += character
        digit_count += 1

# Get the middle character
#code += second_hash[len(second_hash) // 2]

# Send the calculated 4-character code to stdout.
print(code)