#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from docker import Client

name='btsync'

#Get the hostname
hostname = socket.gethostname()
imagename = hostname+'/'+name

#Connect to docker socket
cli = Client(base_url='unix://docker.sock')

#Stop and remove container
print("Stop container")
cli.stop(container=name)
print("Remove container")
cli.remove_container(container=name, force=True)

#Remove docker image
print("Remove image...")
cli.remove_image(image=imagename, force=True)
print("Container fully remove")

exit()

