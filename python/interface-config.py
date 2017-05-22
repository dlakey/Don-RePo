from jnpr.junos import Device
from jnpr.junos.utils.config import Config
r0 = Device(host='172.16.155.254',user='root',password='Juniper').open()
r0.bind(cu=Config)
r0.cu
from lxml import etree
result = r0.cu.load(path='interface.set')
etree.dump(result)
