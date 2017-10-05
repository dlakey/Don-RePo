import sys
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from getpass import getpass
from pprint import pprint
from sys import exit
from lxml import etree
from jnpr.junos.utils.config import Config


Host = raw_input('Enter Hostname or IP address of Device: ')
dev = Device(host=Host,user='root',password='Juniper').open()

Peer = raw_input('Enter Peering Device: ')

class style:
   BOLD = '\033[1m'
   END = '\033[0m'

route_table = RouteTable(dev)

route_table.get(protocol='bgp')

for key in route_table:
    if key.nexthop == Peer:
       print key.name + 'Nexthop: ' + key.nexthop + 'Via: ' + key.via + ' Protocol: ' + key.protocol

Continue = raw_input('Do you wish to pull route, Yes or No: ')

if Continue == 'Yes':
   proute = raw_input('Enter route to pull in format X.X.X.X/X: ')
   bgroup = raw_input('Enter BGP group: ')

dev.bind(cu=Config)
dev.cu
from lxml import etree

PPolicy = "set policy-options prefix-list PROUTE " + proute
result = dev.cu.load(PPolicy)
etree.dump(result)

PPolicy = "set policy-options policy-statement DROUTE term Deny-Route from prefix-list-filter PROUTE exact local-preference 25"
result = dev.cu.load(PPolicy)
etree.dump(result)

PPolicy = "set policy-options policy-statement DROUTE term Deny-Route then accept"
result = dev.cu.load(PPolicy)
etree.dump(result)

PPolicy = "set protocols bgp group " + bgroup + " neighbor " + Peer + " import DROUTE"
result = dev.cu.load(PPolicy)
etree.dump(result)



