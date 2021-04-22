#!/bin/bash

session="CYBERSTORM"
tmux new-session -d -s $session
# tmux rename-window -t 0 'CHAT COVERT'
tmux selectp -t 0

tmux send-keys  "clear" C-m
tmux send-keys  'python3 server.py' C-m

tmux split-window -h
tmux select-pane -t 1
tmux send-keys  "clear" C-m

# tmux send-keys  "python3 solver.py | tee /dev/tty | tee output | xclip -i -selection clipboard" C-m

tmux send-keys  "python3 client.py | tee /dev/tty | tee output | xclip -i -selection clipboard" C-m

tmux send-keys "tmux kill-session -t $session" C-m

tmux attach-session -t $session

echo "DONE"