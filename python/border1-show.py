from jnpr.junos.op.arp import ArpTable
from jnpr.junos import Device
r0 = Device(host='172.16.1.250',user='root',password='Juniper').open()
arp_table = ArpTable(r0)
arp_table.get()
type(arp_table)
from pprint import pprint
pprint(arp_table())

