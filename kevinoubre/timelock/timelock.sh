#!/bin/bash

DEBUG=false

# EPOCHSECONDS IS A BUILTIN VARIABLE

# EPOCHTIME="2017 04 26 15 14 30"
# if not testing
printf -v EPOCHTIME '%(%Y %m %d %H %M %S)T\n' -1 

GIVENTIME=""

# check whether piped in or not
if (( $# == 0 )) ; then
    read var
    GIVENTIME=$var
    # echo $GIVENTIME
    # echo
else
    GIVENTIME="$1"
    # echo
fi

if [ $DEBUG == true ]; then
    echo "epoch time is =   " $EPOCHTIME
    echo "given time is =   " $GIVENTIME
fi

# get the year month date through magic
ymd_epoch=$(echo $EPOCHTIME | tr -d " " | cut -c 1-8)
ymd_given=$(echo $GIVENTIME | tr -d " " | cut -c 1-8)

# make hte hours minutes seconds in the form HH:MM:SS
hms_epoch=$(echo $EPOCHTIME | tr -s " " ":" | cut -c 12-)
hms_given=$(echo $GIVENTIME | tr -s " " ":" | cut -c 12-)

# finally combine them together
EPOCHTIME=$(echo $ymd_epoch $hms_epoch)
GIVENTIME=$(echo $ymd_given $hms_given)

# EPOCHTIME=$(echo $EPOCHTIME | tr -s " " "-" |  sed 's/-/T/3' | sed 's/T/:/g' )
# GIVENTIME=$(echo $1 | tr -s " " "-" | sed 's/-/T/3' )


if [ $DEBUG == true ]; then
    echo "epoch time is =   " $EPOCHTIME
    echo "given time is =   " $GIVENTIME
fi

# (Year month day) -> seconds
# Through the magic of other peoples work, this converts the date to the second
# Technical specification is ISO 8601:2004
GIVENTIMESECONDS=$( date --date="$GIVENTIME" +%s )
EPOCHINSECONDS=$( date --date="$EPOCHTIME" +%s )
# =$( date --date="$EPOCHTIME" +%s )

# EPOCHSECONDS="2017 01 01 00 00 00"

if [[ $GIVENTIMESECONDS -gt $EPOCHINSECONDS ]]; then
    seconds=$(( $GIVENTIMESECONDS - $EPOCHINSECONDS ))  
else
    seconds=$(( $EPOCHINSECONDS - $GIVENTIMESECONDS   ))  
fi


if [ $DEBUG == true ]; then
    echo "epoch time is =   " $EPOCHINSECONDS 
    echo "given time is =   " $GIVENTIMESECONDS
fi

# Calculate the difference

if [ $DEBUG == true ]; then
    echo "time differnece [seconds] = " $seconds
fi

# take off to get the start of the 60 second interval
seconds=$(( $seconds - ($seconds % 60) ))

HASH=$(echo $seconds | tr -d "\n" | md5sum | cut -c -32 | tr -d "\n" | md5sum | cut -c -32)
# echo $HASH
alpha=$(echo $HASH | grep -Po '[a-f]{2}' | head -n 1)
numeric=$(echo $HASH | rev |  grep -Po '[0-9]{2}' | head -n 1)

echo $alpha$numeric

