#!/bin/bash

mkdir output
export SHELL=$(type -p bash)

# command line arguments
MODE="B"
SR="r"
# CRACKILE="stegged-bit.bmp"
CRACKILE="test1.bmp"

# ranges for the loop
UPPERINTERVAL="8"

UPPEROFFSET="124"
LOWEROFFSET="2048"

WEBHOOK_URL="https://discord.com/api/webhooks/798558263427596318/bXkR78gpWAZ2QtZbl-QReZMZN7mW6fv71c7e3HfOJFP4EaHPDaoMhuiKFi3uNyg-Bz4s"

if ! type "discord.sh" > /dev/null; then
    echo "[_]   discord.sh not installed..." 
    sudo wget "https://raw.githubusercontent.com/ChaoticWeg/discord.sh/master/discord.sh" -O /bin/discord.sh
    sudo chmod +x /bin/discord.sh
fi

solveme () {
    FILENAME=$(tr -dc A-Za-z </dev/urandom | head -c 10 ; echo '')
    if [ $MODE = "b" ]; then
        # sh -c "pypy3 steg.py -$SR -$MODE -o$1 -i$2 -w$CRACKILE > /dev/shm/$FILENAME"
        sh -c "python3 steg.py -$SR -$MODE -o$1 -i$2 -w$CRACKILE > /dev/shm/$FILENAME"
    else
        sh -c "python3 steg.py -$SR -$MODE -o$1 -i$2 -w$CRACKILE > /dev/shm/$FILENAME"
    fi

    NEWFILE=$(echo $NEWFILE |  awk '{print $1}')
    if [[ $NEWFILE == "ASCII" ]]; then
        # discord.sh --webhook-url=$WEBHOOK_URL --username "BSDS" --text "GOT A $NEWFILE"
        # discord.sh --webhook-url=$WEBHOOK_URL --username "BSDS" --text "FOUND AT OFFSET $1 AND INTERVAL $2"
        # discord.sh --webhook-url=$WEBHOOK_URL --username "BSDS" --text "$(cat /dev/shm/$FILENAME)"
        echo "OFFSET: $1   INTERVAL: $2"  $(cat "/dev/shm/$FILENAME") | tee -a "output/ascii"

    fi

    if [[ $(identify /dev/shm/$FILENAME &> /dev/null; echo $?) -eq 0 ]]; then
        NEWFILE=$(sh -c "file -b /dev/shm/$FILENAME")
       
        if [[ $NEWFILE != "data" && $NEWFILE != "empty" ]]; then

            echo "GOT A $NEWFILE"
            echo "FOUND AT OFFSET $1 AND INTERVAL $2"
            mv /dev/shm/$FILENAME $(pwd)/output/$i.$NEWFILE

            discord.sh --webhook-url=$WEBHOOK_URL --username "" --text ""
            discord.sh --webhook-url=$WEBHOOK_URL --username "BSDS" --text "FOUND AT OFFSET $1 AND INTERVAL $2"
            discord.sh --webhook-url=$WEBHOOK_URL --username "BSDS" --file $(pwd)/output/$i.$NEWFILE --text "$(head -n 1 /dev/shm/$FILENAME)"

        fi 
    fi
     
}

export -f solveme

for i in $(seq 124 2048); do 

    # seq 1 8 | xargs -n -P 4  bash -c "solveme $i" 

    
    for j in $(seq 1 $UPPERINTERVAL); 
    do  
        solveme $i $j &
    #     #sem -j+0 solveme $i $j
    done
    
    

    # wait
    # echo "INTERVAL IS @ = " $i
done
