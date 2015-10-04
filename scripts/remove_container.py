#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
from docker import Client

app=sys.argv[1]
username=sys.argv[2]
containername=app+'_'+username

#Get the hostname
hostname = socket.gethostname()
imagename = hostname+'/'+app

#Connect to docker socket
cli = Client(base_url='unix://docker.sock')

#Stop and remove container
print("Stop container")
cli.stop(container=containername)
print("Remove container")
cli.remove_container(container=containername, link=True, force=True)

#Remove docker image
print("Remove image...")
cli.remove_image(image=imagename, force=True)
print("Container fully remove")

exit()

