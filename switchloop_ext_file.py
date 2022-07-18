#!/usr/bin/env python

import getpass
import sys
import telnetlib

user = raw_input("Enter your telnet Username: ")
password = getpass.getpass()

f = open("switchips")

for line in f :
    print "Connecting to Device " + (line)
    HOST = line.strip()
    tn = telnetlib.Telnet(HOST)


    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password.encode('ascii') + "\n")

    tn.write("conf t\n")
    for n in range (2,11):
        tn.write("vlan " + str(n) + "\n")
        tn.write("name Python_VLAN_" + str(n) + "\n")
    tn.write("end\n")
    tn.write("write memory\n")
    tn.write("exit\n")

    print tn.read_all()