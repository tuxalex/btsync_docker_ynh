#!/bin/bash
set -e

if [ ! -z "$IPV6ADDR" ]; then
	echo  $IPV6ADDR
	ip -6 addr add "$IPV6ADDR" dev eth0
fi

sleep 2

if [ ! -z "$IPV6GW" ]; then
	echo $IPV6GW
	ip -6 route add  default via "$IPV6GW" dev eth0
fi

sudo cp -aR /etc/btsync/ /opt/
sudo rm /opt/btsync/start.sh
sudo chown -R btsync:btsync /etc/btsync

if [[ ! -f "/etc/btsync/btsync.conf" ]]
then
   /opt/btsync/btsync --dump-sample-config > /opt/btsync/btsync.conf
fi

#chown btsync:btsync /data -R

sudo /opt/btsync/btsync --config /opt/btsync/btsync.conf --nodaemon
#sudo -H -u btsync /opt/btsync/btsync --config /opt/btsync/btsync.conf --nodaemon
#/usr/lib/btsync/btsync-daemon --config /etc/btsync/btsync.conf --nodaemon


#if [[ ! -f "/etc/btsync/btsync.conf" ]]
#then
#   /etc/btsync/btsync --dump-sample-config > /etc/btsync/btsync.conf
#fi

#chown btsync:btsync /data -R

#sudo -H -u btsync /etc/btsync/btsync --config /etc/btsync/btsync.conf --nodaemon
