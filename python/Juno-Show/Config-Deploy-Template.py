import os
import sys
import jnpr.junos
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import yaml

host = raw_input('Enter Hostname or IP address of Device: ')
r0 = Device(host=Host,user='root',password='Juniper').open()

data = yaml.load(open('protocol_data.yml'))

r0.cu = Config(r0)

r0cu.load(template_path='protocol_temp.j2', template_vars=data, format='text')

r0.cu.pdiff()

if r0.cu.commit_check():
    cu.commit()
else:
    cu.rollback()

r0.close()
