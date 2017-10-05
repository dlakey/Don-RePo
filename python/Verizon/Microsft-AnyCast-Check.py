import os
import mmap

with open("Microsoft-Peer-IP.txt", "r") as myfile:
    for line in myfile:
        line = line.strip().lower()
        fl = open('border1-sem-peer.txt', 'r')
        if line in fl.read():
          print line + ' Valid BGP Peering partner!'
        else:
          print line + ' BGP Peer does not exits!!!'