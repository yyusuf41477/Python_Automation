#!/usr/bin/env python

from netmiko import ConnectHandler
import getpass

#Get to input  Username and Password at Prompt
user1 = raw_input("Enter your Username: ")
pass1 = getpass.getpass()

PE1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.17',
    'username': user1,
    'password': pass1,
    }

PE2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.19',
    'username': user1,
    'password': pass1,
}

P1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.45',
    'username': user1,
    'password': pass1,
}

P2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.46',
    'username': user1,
    'password': pass1,
}

with open('isis_configs') as f:
    lines = f.read().splitlines()
print lines

all_devices = [PE1, PE2, P1, P2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output 