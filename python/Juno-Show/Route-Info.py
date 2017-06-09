from jnpr.junos import Device
from jnpr.junos.op.routes import RouteSummaryTable



Host = raw_input('Enter Hostname or IP address of Device: ')
dev = Device(host=Host,user='root',password='Juniper').open()


class style:
   BOLD = '\033[1m'
   END = '\033[0m'
   

tbl = RouteSummaryTable(dev)
tbl.get()

# print tbl
for item in tbl:
    print 'Border1.chm Route Summary:', item.dests
    print 'Total Routes:', item.total
    print 'Total Hiddent Routes:', item.hidden
    print

dev.close()
