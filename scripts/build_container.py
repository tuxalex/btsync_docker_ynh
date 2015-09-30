#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from docker import Client

name='btsync'
cli = Client(base_url='unix://var/run/docker.sock')
config=cli.create_host_config(port_bindings={
        			8888: 8888,
        			5555: 5555
    	})

for line in cli.build(path='../build/', rm=True, tag='test/'+name):
	out = json.loads(line)
	print(out['stream'])

container = cli.create_container(
			image="test/"+name, 
			detach=True,  
			tty=True, 
			volumes=["/home/yunohost.app/owncloud/data/:/data/", "/home/btsync_config/:/opt/btsync"], 
			name=name,
			host_config=config
)


print(container)		
out = cli.start(container=name) 
print(out)
	
exit()

