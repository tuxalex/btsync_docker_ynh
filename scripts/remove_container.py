#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docker import Client

name='btsync'
cli = Client(base_url='unix://docker.sock')
print("Stop container")
cli.stop(container=name)
print("Remove container")
cli.remove_container(container=name, force=True)
print("Remove image...")
cli.remove_image(image='test/'+name, force=True)
print("Container fully remove")
exit()

