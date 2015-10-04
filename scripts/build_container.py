#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import socket
import sys
from docker import Client

app=sys.argv[1]
username=sys.argv[2]
datapath=sys.argv[3]
containername=app+'_'+username

#Get the hostname
hostname = socket.gethostname()
imagename = hostname+'/'+app

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


# TODO: Force stop and remove container with the same name
#cli.stop(container=containername)
#cli.remove_container(container=containername, force=True)

#Create the container and display result
container = cli.create_container(
			image=imagename, 
			detach=True,  
			tty=True, 
			volumes=[datapath+":/data", "/home/yunohost.docker/"+app+"/"+username+"/config:/opt/btsync"], 
			name=containername,
			host_config=config
)
print(container)		

#Start the container and display result
cli.start(container=containername)
print(cli.containers())
	
exit()

