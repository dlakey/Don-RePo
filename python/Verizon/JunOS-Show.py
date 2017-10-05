import sys
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from getpass import getpass
from pprint import pprint
from sys import exit
from lxml import etree
from jnpr.junos.utils.config import Config

dev = Device(host='core1.den',user='dlakey',password='Mickeym!2').open()
response = dev.cli('show configuration | display set')

print response
