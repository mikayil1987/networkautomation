#! /usr/bin/python3

import paramiko
import time

ip_address = "192.168.60.10"
username = "cisco"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print ("Successful connection"), ip_address

remote_connection = ssh_client.invoke_shell()

remote_connection.send("enable\n")
remote_connection.send("configure terminal\n")
remote_connection.send("end\n")
remote_connection.send("exit\n")

## Loop configuration method.
## you can make configuration here.
#for n in range (2,21):
#    print "Creating VLAN " + str(n)
#    remote_connection.send("vlan " + str(n) +  "\n")
#    remote_connection.send("name Python_VLAN_" + str(n) +  "\n")
#    time.sleep(0.5)

remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print (output)


## adding comment from atom 
