#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import socket
import sys
from docker import Client

app=sys.argv[1]
username=sys.argv[2]
datapath=sys.argv[3]
containername=sys.argv[4]
yunohostid=sys.argv[5]
dockerized=sys.argv[6]

#Get the hostname
hostname = socket.gethostname()
imagename = hostname+'/'+app

#Connect to docker socket
cli = Client(base_url='unix://docker.sock')

#Define port binding
#if dockerized:
#	config=cli.create_host_config(network_mode='container:'+yunohostid)
#else:
#	config=cli.create_host_config(port_bindings={8888: ('127.0.0.1',8888), 55555: ('127.0.0.1',55555)})

config=cli.create_host_config(port_bindings={8888: ('127.0.0.1',8888), 55555: ('0.0.0.0',55555)})
#Build docker image with the Dockerfile and disply the output
for line in cli.build(path='../build/', tag=imagename):
	out = json.loads(line)
	#sys.stdout.write('\r')
	#print(out['stream'])
	#sys.stdout.flush()

#Create the container and display result
container = cli.create_container(
			image=imagename,  
			tty=True,
			volumes=[datapath+":/data", "/home/yunohost.docker/container-"+app+"/"+username+"/config:/opt/btsync"], 
			name=containername,
			host_config=config
)		

#Start the container and display result
cli.start(container=containername)

details=cli.inspect_container(container=containername)
#First print IP, then print redirect port, finaly print not redirect ports
#print(","+details['NetworkSettings']['IPAddress']
#      +",8888"
#      +",55555")

exit()

