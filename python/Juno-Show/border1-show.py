import jnpr.junos
import os
import sys
from pprint import pprint
from jnpr.junos import Device
r0 = Device(host='172.16.155.254',user='root',password='Juniper').open()
response = r0.cli('show configuration | display set')
print response
