import os
import mmap

fl = open('Peer-Table.txt')
str = mmap.mmap(fl.fileno(), 0, access=mmap.ACCESS_READ)

if str.find('2001:1890:1fff:31d:192:205:32:117') != -1:
    print 'Valid BGP Peering partner!'
else:
    print 'BGP Peer does not exits!!!'