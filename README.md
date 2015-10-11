BitTorrent Sync for Yunohost.
============================

BitTorrent Sync by BitTorrent, Inc is a proprietary peer-to-peer file synchronization tool available for Windows, Mac, Linux, Android, iOS, Windows Phone and BSD. It can sync files between devices on a local network, or between remote devices over the Internet via secure, distributed P2P technology.

Although not touted by the developers as an intended direct replacement nor competitor to cloud-based file synchronization services, it has attained much of its publicity in this potential role.[2] This is mainly due to the ability of BitTorrent Sync to address many of the concerns in existing services relating to file storage limits, privacy, cost, and performance.

Source: Wikipedia

Licensing
---------

BitTorrent Sync , unlike the open source frontend, is proprietary software.

Source: Wikipedia

Installation information
------------------------
This package installs BitTorrent Sync in a container with docker and use redirection in nginx to add the app in yunohost SSO.
The install script install docker if yunohost have installed on the host.
Docker-py has been used as a docker client to interact with docker thus this package can be used on a host with yunohost installed (not tested yet) or on a yunohost docker container.
The first installation can take time, because docker download the base image and construct the ajenti image, so be patient.
In yunohost this app will be installed with the name "btsync_docker"
BitTorrent Sync doesn't support multi-user so this app is multi-instance, each user must have an install of this app to access to it. The first instance installed will be called "btsync_docker", after "__NUMBEROFINSTANCE" will be added to "btsync_docker" (Example: the secondary instance will be called "btsync_docker__2") 
The package creates for each install a container with a name composed of "btsync" and the username concatened like btsyncUSERNAME. 

Credit
------
This work is based on Scith work : https://github.com/scith/redirect_ynh
