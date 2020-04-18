#! /usr/bin/env python3


import pprint
import yaml
import sys


with open('hosts.yaml', 'r') as f:
    doc = yaml.full_load(f)



SFORouters = doc["Network"]["SFO"]["Core"]["Router"]
SFOSwitches = doc["Network"]["SFO"]["Access"]["Switch"]

def RoutersIP():
    for iprouters in SFORouters:
        IP = iprouters.get('IP')

def SwitchesIP():
    for ipswitches in SFOSwitches:
        IP = ipswitches.get('IP')

RoutersIP()
SwitchesIP()
