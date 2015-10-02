#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import socket
from docker import Client

name='btsync'

#Get the hostname
hostname = socket.gethostname()
imagename = hostname+'/'+name

#Connect to docker socket
cli = Client(base_url='unix://docker.sock')

#Define port binding
config=cli.create_host_config(port_bindings={
        			8888: 8888,
        			5555: 5555
    	})

#Build docker image with the Dockerfile and disply the output
for line in cli.build(path='../build/', rm=True, tag=imagename):
	out = json.loads(line)
	print(out['stream'])


#Force stop and remove container with the same name
cli.stop(container=name)
cli.remove_container(container=name, force=True)

#Create the container and display result
container = cli.create_container(
			image=imagename, 
			detach=True,  
			tty=True, 
			volumes=["/home/yunohost.app/owncloud/data/:/data/", "/home/yunohost.docker/btsync/:/opt/btsync"], 
			name=name,
			host_config=config
)
print(container)		

#Start the container and display result
cli.start(container=name)
print(cli.containers())
	
exit()

