#!/bin/bash

HOSTS_FILE=/etc/hosts
cat $1 >> $HOSTS_FILE

#while read host; do
#        ssh-keyscan $host >> ~/.ssh/known_hosts
#done < $HOSTS_FILE

python3 main.py
