#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docker import Client

name='btsync'
cli = Client(base_url='unix://docker.sock')
cli.stop(container=name)
cli.remove_container(container=name, force=True)
for line in cli.remove_image(image='test/'+name, force=True):
	print(line)
exit()

