import jnpr.junos
import os
import sys
from pprint import pprint
from jnpr.junos import Device
Host = raw_input('Enter Hostname or IP address of Device: ')
r0 = Device(host=Host,user='root',password='Juniper').open()
response = r0.cli('show bgp group NTT')
print response
