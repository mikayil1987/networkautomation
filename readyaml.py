#! /usr/bin/env python3


import pprint
import yaml
import sys


with open('hosts.yaml', 'r') as f:
    doc = yaml.full_load(f)


## Get SFO Routers IP addresses from yaml
SFORouters = doc["Network"]["SFO"]["Core"]["Router"]
## Get SFO Switches IP addresses from yaml
SFOSwitches = doc["Network"]["SFO"]["Access"]["Switch"]

def RoutersIP():
    for iprouters in SFORouters:
        IP = iprouters.get('IP')
        print (IP)

def SwitchesIP():
    for ipswitches in SFOSwitches:
        IP = ipswitches.get('IP')
        print (IP)

RoutersIP()
SwitchesIP()
