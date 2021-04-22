#!/bin/bash

mkdir output
export SHELL=$(type -p bash)


solveme () {
    FILENAME=i:$i:$(tr -dc A-Za-z </dev/urandom | head -c 10 ; echo '')
    sh -c "python3 steg.py -r -B -o$1 -i$2 -wtest1.bmp > /dev/shm/$FILENAME"


    if [[ $(identify /dev/shm/$FILENAME &> /dev/null; echo $?) -eq 0 ]]; then
        NEWFILE=$(sh -c "file -b /dev/shm/$FILENAME")
        NEWFILE=$(echo $NEWFILE |  awk '{print $1}')
        if [[ $NEWFILE ==  "JPEG" || $NEWFILE == "PNG" ]]
        then
            echo "GOT A $NEWFILE"
            echo "FOUND AT OFFSET $1 AND INTERVAL $2"
            mv /dev/shm/$FILENAME $(pwd)/output/$FILENAME.$NEWFILE
        fi
    fi
}

export -f solveme

for i in $(seq 124 2048); do 

    # seq 1 8 | xargs -n -P 4  bash -c "solveme $i" 

    for j in $(seq 1 8); 
        do  
        solveme $i $j & 
          #sem -j+0 solveme $i $j
        done
    wait
    # echo "INTERVAL IS @ = " $i
done
