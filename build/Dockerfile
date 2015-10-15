# VERSION 0.1
# DESCRIPTION:    btsync server conatiner
# TO_BUILD:       docker build -rm -t btsync .
# TO_RUN:         docker run -d --name=btsync -i -t -p 8888:8888 -p 55555:55555 -v /PATHDATA/:/data/ -v /PATHCONFIG/:/opt/btsync IMAGENAME

FROM ubuntu-debootstrap:14.04
MAINTAINER : Alexan Andrieux <alexan.andrieux@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN useradd btsync -b /data --no-create-home

RUN apt-get update
RUN apt-get dist-upgrade -yq
RUN apt-get install sudo tar curl -yq

RUN mkdir -p /etc/btsync/
RUN mkdir -p /opt/btsync/

WORKDIR /etc/btsync

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get -y install tar curl ca-certificates wget \
    && apt-get clean \
    && curl -k -L https://download-cdn.getsyncapp.com/stable/linux-x64/BitTorrent-Sync_x64.tar.gz | tar zxv

RUN chown -R btsync:btsync /etc/btsync
RUN ./btsync --dump-sample-config >> btsync.conf \
    && mv -n ./btsync.conf /opt/btsync/btsync.conf

WORKDIR /

EXPOSE 8888
EXPOSE 55555

VOLUME ["/opt/btsync"]
VOLUME ["/data"]

#CMD ["/etc/btsync/start.sh"]
ENTRYPOINT ["/etc/btsync/btsync", "--config", "/opt/btsync/btsync.conf", "--nodaemon"]
