#!/bin/bash

session="CYBERSTORM"
tmux new-session -d -s $session
# tmux rename-window -t 0 'CHAT COVERT'
tmux selectp -t 0
tmux selectp -t 0

tmux send-keys  "clear" C-m
tmux send-keys  "sh -c 'for i in $(seq 0 1000); do python3 steg.py -r -B -o$i -i2 -wtest1.bmp; done'" C-m



tmux attach-session -t $session

echo "DONE"