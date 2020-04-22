#! /usr/local/bin/python3

import os
import time

hostnames = open('hosts.txt','r')
lines = hostnames.read().splitlines()


with open('output.txt','w+') as file: # open output.txt file and write
    for host in lines:
        response = os.system("ping -c 1 " + str(host)) # ping hosts with count 1
        if response == 0:
            file.write(str(host) + " is UP\n")
            time.sleep(1)
        else:
            file.write(host + " is Down\n")


hostnames.close()
