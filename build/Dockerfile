# VERSION 0.1
# DESCRIPTION:    btsync server conatiner
# TO_BUILD:       docker build -rm -t btsync .
# TO_RUN:         docker run -d --name=btsync -i -t -p 8888:8888 -p 55555:55555 -v /home/yunohost.app/owncloud/data/:/data/ -v /home/btsync_config/:/opt/btsync tuxcloud.fr/btsync

FROM ubuntu-debootstrap:14.04
MAINTAINER : Alexan Andrieux <alexan.andrieux@gmail.com>
#BASE ON Martijn van Maurik <docker@vmaurik.nl>


ENV DEBIAN_FRONTEND noninteractive

RUN useradd btsync -b /data --no-create-home

RUN apt-get update
RUN apt-get dist-upgrade -yq
RUN apt-get install sudo tar curl -yq

RUN mkdir -p /etc/btsync/

WORKDIR /etc/btsync

#RUN curl -k -L http://download.getsyncapp.com/endpoint/btsync/os/linux-x64/track/stable | tar zxv
RUN curl -k -L https://download-cdn.getsyncapp.com/stable/linux-x64/BitTorrent-Sync_x64.tar.gz | tar zxv
ADD start.sh /etc/btsync/start.sh
RUN chmod +x /etc/btsync/start.sh
RUN chown -R btsync:btsync /etc/btsync

#RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 6BF18B15
#RUN echo deb http://debian.yeasoft.net/btsync trusty main > ~/btsync.list
#RUN echo deb-src http://debian.yeasoft.net/btsync trusty main >> ~/btsync.list
#RUN mv ~/btsync.list /etc/apt/sources.list.d/btsync.list
#RUN chown root:root /etc/apt/sources.list.d/btsync.list
#RUN apt-get update
#RUN apt-get install btsync -y

WORKDIR /

EXPOSE 8888
EXPOSE 55555

VOLUME ["/opt/btsync"]
VOLUME ["/data"]

CMD ["/etc/btsync/start.sh"]
