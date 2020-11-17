#!/bin/bash

rm ~/.ssh/known_hosts

HOSTS_FILE=/etc/hosts

while read host; do
        ssh-keyscan $host >> ~/.ssh/known_hosts
done < $HOSTS_FILE

