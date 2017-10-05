from fabric.api import *

env.hosts = "172.16.145.101"
env.user = "dlakey"
env.password = "Mickeym!2"

def host_type():
    sudo('apt-get update && sudo apt-get upgrade')
    sudo('apt-get install apache2 apache2-doc apache2-utils')
