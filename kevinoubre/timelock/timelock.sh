#!/bin/bash

DEBUG=true

# EPOCHSECONDS IS A BUILTIN VARIABLE

# echo $(date)

EPOCHTIME="2017 01 01 00 00 00"
# EPOCHTIME=$2 

GIVENTIME="$1"

if [ $DEBUG == true ]; then
    echo "epoch time is =   " $EPOCHTIME
    echo "given time is =   " $1
fi

# ymd_epoch=$(echo $EPOCHTIME | tr -s " " "-" | cut -c 1-10)
ymd_epoch=$(echo $EPOCHTIME | tr -d " " | cut -c 1-8)
# ymd_given=$(echo $1 | tr -s " " "-" | cut -c 1-10)
ymd_given=$(echo $1 | tr -d " " | cut -c 1-8)

hms_epoch=$(echo $EPOCHTIME | tr -s " " ":" | cut -c 12-)
hms_given=$(echo $1 | tr -s " " ":" | cut -c 12-)

EPOCHTIME=$(echo $ymd_epoch $hms_epoch)
GIVENTIME=$(echo $ymd_given $hms_given)

# EPOCHTIME=$(echo $EPOCHTIME | tr -s " " "-" |  sed 's/-/T/3' | sed 's/T/:/g' )
# GIVENTIME=$(echo $1 | tr -s " " "-" | sed 's/-/T/3' )


if [ $DEBUG == true ]; then
    echo "epoch time is =   " $EPOCHTIME
    echo "given time is =   " $GIVENTIME
fi

# (Year month day) -> seconds
GIVENTIMESECONDS=$( date --date="$GIVENTIME" +%s )
EPOCHINSECONDS=$( date --date="$EPOCHTIME" +%s )
# =$( date --date="$EPOCHTIME" +%s )

# EPOCHSECONDS="2017 01 01 00 00 00"



if [ $DEBUG == true ]; then
    echo "epoch time is =   " $EPOCHINSECONDS 
    echo "given time is =   " $GIVENTIMESECONDS
fi

echo $(( $GIVENTIMESECONDS - $EPOCHINSECONDS))  