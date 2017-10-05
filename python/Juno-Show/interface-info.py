import sys
from jnpr.junos import Device
from jnpr.junos.op.bgp import bgpTable
from jnpr.junos.op.bgp import bgpView
from jnpr.junos.op.ethport import EthPortTable
from getpass import getpass
from pprint import pprint
from sys import exit
from lxml import etree


Host = raw_input('Enter Hostname or IP address of Device: ')
dev = Device(host=Host,user='root',password='Juniper').open()


class style:
   BOLD = '\033[1m'
   END = '\033[0m'

eth_ports = EthPortTable(dev)

eth_ports.get()

pprint(eth_ports())
