#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docker import Client

name='btsync'
cli = Client(base_url='unix://var/run/docker.sock')
[line for line in cli.build(path='../build/', rm=True, tag='test/'+name)]
cli.create_container(image="test/"+name, detach=True, ports=[8888, 5555], tty=True, volumes=["/home/yunohost.app/owncloud/data/:/data/", "/home/btsync_config/:/opt/btsync"], name=name)
cli.inspect_container(container=name)
cli.start(container=name, publish_all_ports=True)
cli.containers()
exit()

