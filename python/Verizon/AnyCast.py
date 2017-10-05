from getpass import getpass
from pprint import pprint
from sys import exit
from lxml import etree
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

VerizonDevice = raw_input('Enter Hostname or IP address of Device under test: ')
dev = Device(host=VerizonDevice,user='root',password='Juniper').open()

class style:
   BOLD = '\033[1m'
   END = '\033[0m'


bgppeer = dev.cli('show bgp summary')

print bgppeer
peertable = {}

counter = 0

with open("Peer-Device-Master-Table.txt", "r") as peerfile:
    for line in peerfile:
        line = line.strip().lower()
        if line in bgppeer:
            peertable[counter] = line
            counter = counter + 1

print peertable

ncounter = 0

while ncounter < counter:
    with open("AnyCast-Master-Table.txt", "r") as anyfile:
        #dev.get_route_information(bgp=True, neighbor=peertable[ncounter])
        anycastroutes = dev.cli('show route advertising-protocol bgp ' + peertable[ncounter])
        for line in anyfile:
            line = line.strip().lower()
            if line in anycastroutes:
                print 'Anycast match route ' + line
            else:
                print 'Missing Anycast route ' + line
        ncounter = ncounter + 1
