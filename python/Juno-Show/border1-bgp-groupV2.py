import jnpr.junos
import os
import sys
from pprint import pprint
from jnpr.junos import Device
Host = raw_input('Enter Hostname or IP address of Device: ')
r0 = Device(host=Host,user='root',password='Juniper').open()
bgproute = r0.rpc.get_bgp_group_information(group_name='NTT')
print bgproute 
