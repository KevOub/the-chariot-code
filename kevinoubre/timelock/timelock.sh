#!/bin/bash

DEBUG=false

# EPOCHSECONDS IS A BUILTIN VARIABLE


# CURRENTTIME="2017 04 26 15 14 30"
# CURRENTTIME="2013 05 06 07 43 25"
# if not testing

printf -v CURRENTTIME '%(%Y %m %d %H %M %S)T\n' -1 

# CURRENTTIME=$2

EPOCHTIMEGIVEN=""

# check whether piped in or not
if (( $# == 0 )) ; then
    read var
    EPOCHTIMEGIVEN=$var
    # echo $EPOCHTIMEGIVEN
    # echo
else
    EPOCHTIMEGIVEN="$1"
    # echo
fi

if [ $DEBUG == true ]; then
    echo "current time is =   " $CURRENTTIME
    echo "epoch time is =   " $EPOCHTIMEGIVEN
fi

# get the year month date through magic
ymd_epoch=$(echo $CURRENTTIME | tr -d " " | cut -c 1-8)
ymd_given=$(echo $EPOCHTIMEGIVEN | tr -d " " | cut -c 1-8)

# make hte hours minutes seconds in the form HH:MM:SS
hms_epoch=$(echo $CURRENTTIME | tr -s " " ":" | cut -c 12-)
hms_given=$(echo $EPOCHTIMEGIVEN | tr -s " " ":" | cut -c 12-)


# finally combine them together
CURRENTTIME=$(echo $ymd_epoch $hms_epoch)
EPOCHTIMEGIVEN=$(echo $ymd_given $hms_given)

# CURRENTTIME=$(echo $CURRENTTIME | tr -s " " "-" |  sed 's/-/T/3' | sed 's/T/:/g' )
# EPOCHTIMEGIVEN=$(echo $1 | tr -s " " "-" | sed 's/-/T/3' )


if [ $DEBUG == true ]; then
    echo "current time is =   " $CURRENTTIME
    echo "epoch time is =   " $EPOCHTIMEGIVEN
fi

# (Year month day) -> seconds
# Through the magic of other peoples work, this converts the date to the second
# Technical specification is ISO 8601:2004
EPOCHTIMEGIVENSECONDS=$( date --date="$EPOCHTIMEGIVEN" +%s )
CURRENTTIMESECONDS=$( date --date="$CURRENTTIME" +%s )
# =$( date --date="$CURRENTTIME" +%s )


seconds=$(( $CURRENTTIMESECONDS - $EPOCHTIMEGIVENSECONDS  ))  

# if [[ $EPOCHTIMEGIVENSECONDS -gt $CURRENTTIMESECONDS ]]; then
#     seconds=$(( $EPOCHTIMEGIVENSECONDS - $CURRENTTIMESECONDS ))  
# else
#     seconds=$(( $CURRENTTIMESECONDS - $EPOCHTIMEGIVENSECONDS   ))  
# fi


if [ $DEBUG == true ]; then
    echo "current time is =   " $CURRENTTIMESECONDS 
    echo "epoch time is =   " $EPOCHTIMEGIVENSECONDS
fi

# Calculate the difference

if [ $DEBUG == true ]; then
    echo "time differnece [seconds] = " $seconds
fi


# The ignore Daylight savings
# seconds=$($seconds - $(date +%S ))
# seconds=$(( $seconds - $(date +%S) ))
seconds=$(( $seconds - $(( $seconds % 60 )) ))


# take off to get the start of the 60 second interval
# echo $second | tr -d "\n" | md5sum
HASH=$(echo $seconds | tr -d "\n" | md5sum | cut -c -32 | tr -d "\n" | md5sum | cut -c -32)
# echo $HASH


# alpha=$(echo $HASH | grep -Po '[a-f]{2}' | head -n 1)
alpha=$(echo $HASH | grep -Po "[a-f]" | head -n2 | tr -d '\n')
# numeric=$(echo $HASH | rev |  grep -Po '[0-9]{2}' | head -n 1)
numeric=$(echo $HASH | rev |  grep -Po "[0-9]" | head -n2 | tr -d '\n' )
echo $alpha$numeric



