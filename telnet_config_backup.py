#!/usr/bin/env python

import getpass
import sys
import telnetlib

user = raw_input("Enter your telnet Username: ")
password = getpass.getpass()

f = open("switchips")

for line in f :
    print "Getting Configuration from Device " + (line)
    HOST = line.strip()
    tn = telnetlib.Telnet(HOST)


    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("terminal length 0\n")
    tn.write("show run\n")
    tn.write("exit\n")

    readoutput = tn.read_all()
    saveoutput = open("switch_" + HOST,"w")
    saveoutput.write(readoutput)
    saveoutput.write("\n")
    saveoutput.close

    print tn.read_all()