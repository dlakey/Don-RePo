#!/usr/bin/python

import paramiko
import sys
import getpass
from pprint import pprint
import time
import json
import os
os.linesep

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
    peeroutput = device + '_peer.txt'
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(devices[device]['ip'], username=username, password=password, look_for_keys=False,
                       allow_agent=False)
    new_connection = connection.invoke_shell()
    output = clear_buffer(new_connection)
    time.sleep(2)
    new_connection.send("terminal length 0\n")
    output = clear_buffer(new_connection)
    with open(outputFileName, 'wb') as f:
        for command in commands:
            new_connection.send(command)
            time.sleep(5)
            output = new_connection.recv(max_buffer)
            # print(output)
            f.write(output)

    dlog = open(outputFileName)
    mpeer = dlog.read()

    peertable = {}

    peertab = open(peeroutput, "w")

    counter = 0

    with open("peers-master.txt", "r") as peerfile:
        for line in peerfile:
            line = line.strip().lower()
            if line in mpeer:
                peertable[counter] = line
                peercommand = "show ip nei " + peertable[counter] + " adv" + "\n"
                peertab.write(peercommand)

    with open("sw1_peer.txt", 'r') as f:
        commands = [line for line in f.readlines()]

    for command in commands:
        new_connection.send(command)
        time.sleep(5)
        output = new_connection.recv(max_buffer)
        print(output)
        #f.write(output)

    new_connection.close()
