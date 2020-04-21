
#! /usr/bin/env python3

import os
import time

listhosts = ['google.com','facebook.com','dasdasdasdasdasdas.com']

file = open('testfile.txt','w')

for host in listhosts:
    response = os.system("ping -c 1 " + str(host))
    if response == 0:
        file.write(host + " is UP\n")
    else:
        file.write(host + " is Down\n")

file.close()
