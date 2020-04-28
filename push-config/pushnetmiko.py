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

## if it is not in enable mode, it will switch to enable mode.
prompt = connection.find_prompt()

if '>' in prompt:
    connection.enable()


mode = connection.check_config_mode()

if not mode:
    connection.config_mode()

connection = ConnectHandler(**cisco_device)
output = connection.send_command('do sho ip int br')
print(output)
connection.disconnect()
