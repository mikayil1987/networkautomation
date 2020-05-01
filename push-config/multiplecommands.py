#! /usr/bin/env python3

from netmiko import Netmiko
from netmiko import ConnectHandler
import time

#connection = Netmiko(host='10.1.1.1', username='cisco', password='cisco', device_type='cisco_ios')

cisco_device = {
        'device_type': 'cisco_ios',
        'ip': '192.168.60.20',
        'username': 'cisco',
        'password': 'cisco',
        'port': 22,
        'secret': '1234',
        'verbose': True
}

### Connecting to device
connection = ConnectHandler(**cisco_device)

## checking for enable mode. it will change it to enable mode.
prompt = connection.find_prompt()
if '>' in prompt:
    connection.enable()
'''
### checking for config mode. it will change it to config mode.
mode = connection.check_config_mode()
if not mode:
    connection.config_mode()

### multiple commands for pushing to device
commands = ['interface loopback0', 'ip address 1.1.1.1 255.255.255.255', 'end']
connection.send_config_set(commands)

### send commands to the device
output = connection.send_command_expect('write memory')

### showing the output from the devices.
print(output)
connection.disconnect()
