#!/bin/bash

rm ~/.ssh/known_hosts

HOSTS_FILE=/etc/hosts

ssh-keyscan $(cat $HOSTS_FILE) >> ~/.ssh/known_hosts

