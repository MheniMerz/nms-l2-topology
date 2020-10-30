#!/bin/sh
tmux new-session -d 'nms' \; \
tmux split-window -v 'main.py' \; \ 
tmux new-window 'models' \; \
tmux new-window 'terminal' \; \
tmux -2 attach-session -d \;
