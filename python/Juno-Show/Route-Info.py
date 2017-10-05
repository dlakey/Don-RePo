import sys
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from getpass import getpass
from pprint import pprint
from sys import exit
from lxml import etree


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
