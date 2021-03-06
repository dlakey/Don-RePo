#!/usr/bin/python3

import paramiko
import getpass
import time
import json

with open('devices.json', 'r') as f:
    devices = json.load(f)

with open('command1.txt', 'r') as f: 
    commands = [line for line in f.readlines()]

username = 'cisco'
password = 'cisco'

max_buffer = 65535

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)

# Starts the loop for devices
for device in devices.keys(): 
    outputFileName = device + '_output.txt'
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(devices[device]['ip'], username=username, password=password, look_for_keys=False, allow_agent=False)
    new_connection = connection.invoke_shell()
    output = clear_buffer(new_connection)
    time.sleep(2)
    new_connection.send("terminal length 0\n")
    output = clear_buffer(new_connection)
    with open(outputFileName, 'wb') as f:
        for command in commands:
            new_connection.send(command)
            time.sleep(4)
            output = new_connection.recv(max_buffer)
 #          print(output)
            f.write(output)
    
    new_connection.close()
    
