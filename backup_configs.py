from netmiko import ConnectHandler
import time
import getpass
import concurrent.futures
import datetime
import re

user1 = raw_input("Enter your Username")
pass1 = getpass.getpass()

ip_address_file = input('Enter name of file for host addresses: ').strip()
t1 = time.perf_counter()

def fetch_ip_addresses():
    with open(ip_address_file) as devices:
        addresses = devices.read().splitlines()
    return addresses
    
def backgup_file(filename, output):    
    with open(filename.group(0),'w') as backup_file:
        backup_file.write(output)
        print('Configurations were successfully backed up!')
    return

def backup_rtr_configuration(address):
    todays_date = datetime.datetime.now()
    year = todays_date.year
    day = todays_date.day
    month = todays_date.month

    ios_device_info = {
        'ip': address,
        'port': 22,
        'username': user1,
        'password': pass1,
        'device_type': 'cisco_ios',
        'verbose': True
    }

    print(f'Connecting to host {address}...')
    ssh_connection = ConnectHandler(**ios_device_info)

    print(f'Generating running configuration for host {address}...')
    output = ssh_connection.send_command('show run')
    prompt_hostname = ssh_connection.find_prompt()[0:-1]
    filename = f'{prompt_hostname}_{month}_{day}_{year}_backgup.cfg'
 
    print(f'Backing up configuration for host {address}')
    time.sleep(1)
    backgup_file(filename, output)
    ssh_connection.disconnect()
    return

with concurrent.futures.ThreadPoolExecutor() as exe:
    ip_addresses = fetch_ip_addresses()
    results = exe.map(backup_rtr_configuration, ip_addresses)

t2 = time.perf_counter()
print(f'The script finished executing in {round(t2-t1,2)} seconds.')