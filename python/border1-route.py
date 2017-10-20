import jnpr.junos
import os
import sys
from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.op.route import routes
r0 = Device(host='172.16.1.250',user='root',password='Juniper').open()
r0.bind(route_table=routes)
r0.cu
route_table = routes(r0)
route_table.get()
pprint(route_table.items())
