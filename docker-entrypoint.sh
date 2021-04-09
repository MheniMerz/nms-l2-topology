#!/bin/bash

# add dns-bindings to /etc/hosts
# this will enable the container to reach devices with their hostname

HOSTS_FILE=/etc/hosts
cat $1 >> $HOSTS_FILE

# scan ssh fingerprints of devices and add them to known_hosts file
touch /usr/src/app/.ssh/known_hosts
while read host; do
        ssh-keyscan $host >> /usr/src/app/.ssh/known_hosts
done < $HOSTS_FILE

# run the agent
python3 main.py
