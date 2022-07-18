#!/usr/bin/env python

from netmiko import ConnectHandler
import getpass

#Get to input  Username and Password at Prompt
user1 = raw_input("Enter your Username: ")
pass1 = getpass.getpass()

PE1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.224.101',
    'username': user1,
    'password': pass1,
    }

PE2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.224.104',
    'username': user1,
    'password': pass1,
}

P1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.224.102',
    'username': user1,
    'password': pass1,
}

P2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.224.103',
    'username': user1,
    'password': pass1,
}

with open('pe1_configs') as f:
    lines = f.read().splitlines()
print lines

west_devices = [PE1]

for devices in west_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output 

with open('pe2_configs') as f:
    lines = f.read().splitlines()
print lines

east_devices = [PE2]

for devices in east_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output

with open('p1_configs') as f:
    lines = f.read().splitlines()
print lines

c1_devices = [P1]

for devices in c1_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output  

with open('p2_configs') as f:
    lines = f.read().splitlines()
print lines

c2_devices = [P2]

for devices in c2_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output 