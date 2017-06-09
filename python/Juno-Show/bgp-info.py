import sys
from jnpr.junos import Device
from jnpr.junos.op.bgp import bgpTable
from jnpr.junos.op.bgp import bgpView
from getpass import getpass
from pprint import pprint as pp
from sys import exit
from lxml import etree


Host = raw_input('Enter Hostname or IP address of Device: ')
dev = Device(host=Host,user='root',password='Juniper').open()


class style:
   BOLD = '\033[1m'
   END = '\033[0m'



#print BGP Table
#get-BGP Information
print "\n*************************************************************************************"
print style.BOLD + "BGP Information " + style.END
ebgp = bgpTable(dev)
ebgp.get()

# print ebgp

for item in ebgp:
    print 'AS Number: ', item.local_as
    print 'Peer AS: ', item.peer_as
    print 'IP Address: ', item.local_address
    print 'Route Received: ', item.route_received
    


#for fpc in fpcs:
#         print fpc.key," Description:", fpc.desc, "Model:", fpc.model,"Serial:", fpc.sn, "Part-number:", fpc.pn



dev.close()
