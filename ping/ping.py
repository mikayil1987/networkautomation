#! /usr/bin/env python3

import os
import time

file = open('output.txt','w+')
hostnames = open('hosts.txt','r')
lines = hostnames.read().splitlines()

for host in lines:
    response = os.system("ping -c 1 " + str(host))
    if response == 0:
        file.write(str(host) + " is UP\n")
        time.sleep(1)
    else:
        file.write(host + " is Down\n")

file.close()
hostnames.close()
