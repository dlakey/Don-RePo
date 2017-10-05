import sys
import ast
import yaml
import json
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.bgp import bgpTable
from getpass import getpass
from pprint import pprint
from sys import exit
from lxml import etree
from pprint import pprint
from jnpr.junos.utils.config import Config
from difflib import Differ
import json
import os
os.linesep

Host = raw_input('Enter Hostname or IP address of Device: ')
dev = Device(host=Host,user='root',password='Juniper').open()

bgp_table = bgpTable(dev)
bgp_table.get()

try:
    os.remove(Host + '_Peers')
except OSError:
    pass

counter = 0

with open(Host + '_Peers', 'w') as f:
    for item in bgp_table:
        f.write(item.peer_as + os.linesep)
        counter = counter + 1

counter = 0
with open(Host + '_PeerIP', 'w') as f:
    for item in bgp_table:
        f.write(item.peer_id + os.linesep)
        counter = counter + 1

peer_sum = Host + '_Peers'
peer_IP = Host + '_PeerIP'
peertable = {}
peerIPtable = {}
peerIP = {}
counter = 0
scounter = 0

test = open('no_peer.txt', 'r')
t1 = test.read()


with open(peer_sum, "r") as peerfile:
    for line in peerfile:
        line = line.strip().lower()
        if line in t1:
            scounter = scounter + 1
        else:
            peertable[counter] = line
            counter = counter + 1



#print peertable
#peersum = dev.cli('show bgp summary ')
#peersum.split()
#psum = peersum.split()
#key = psum.pop(0)
#peerIPtable[key] = psum
#print peerIPtable

allpeer = {}
peersum = dev.rpc.get_bgp_summary_information(normalize=True)
allpeer = peersum.findtext("bgp-information/bgp-peer/description")

while line in peersum:
    print peersum


ncounter = 0
while ncounter < counter:
    print peertable[ncounter]
    with open("AnyCast-Master-Table.txt", "r") as anyfile:
        anycastroutes = dev.cli('show route advertising-protocol bgp 172.16.1.2')
        for line in anyfile:
            line = line.strip().lower()
            if line in anycastroutes:
                print 'Anycast match route ' + line
            else:
                print 'Missing Anycast route ' + line

    ncounter = ncounter + 1

























#with open('no_peer.txt', 'r') as file1:
 #  with open(peer_sum, 'r') as file2:
  #      same = set(file1).intersection(file2)

#same.discard('\n')

#for line in same:
 #   pprint (line)






