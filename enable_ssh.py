#!/usr/bin/env python

#Import the correct Libraries 
import getpass
import sys
import telnetlib

#Get to input  Username and Password at Prompt
user = raw_input("Enter your username: ")
password = getpass.getpass()

#  Open file with list of Routers
f = open ("mydev")
#Loop through lines in files
for line in f:
	print "Configuring Device " + (line)
	HOST = line.strip()
	tn = telnetlib.Telnet(HOST)

	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
	    tn.read_until("Password: ")
	    tn.write(password + "\n")
#Send the block of commands to get ssh up and running
	tn.write("terminal length 0\n")
	tn.write("conf t\n")
	tn.write("ip domain name yubz.local\n")
	tn.write("crypto key generate rsa modulus 1024\n")
	tn.write("ip ssh version 2\n")
	tn.write("line vty 0 4\n")
	tn.write("transport input ssh\n")
	tn.write("end\n")
	tn.write("write memory\n")
	tn.write("exit\n")
	print tn.read_all()
f.close()
