import os
import mmap

fl = open('Peer-Table.txt')
str = mmap.mmap(fl.fileno(), 0, access=mmap.ACCESS_READ)

if str.find('38.104.102.33') != -1:
    print 'Valid BGP Peering partner!'
else:
    print 'BGP Peer does not exits!!!'
