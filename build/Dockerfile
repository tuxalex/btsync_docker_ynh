# VERSION 0.1
# DESCRIPTION:    btsync server conatiner
# TO_BUILD:       docker build -rm -t btsync .
# TO_RUN:         docker run -d --name=btsync -i -t -p 8888:8888 -p 55555:55555 -v /PATHDATA/:/home/btsync/data -v /PATHCONFIG/:/home/btsync/.config IMAGENAME

FROM ubuntu-debootstrap:14.04
MAINTAINER : Alexan Andrieux <alexan.andrieux@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN useradd -m btsync
RUN mkdir -p "/etc/btsync"
RUN mkdir -p "/home/btsync/.config"
RUN mkdir -p "/home/btsync/.config/btsync"
RUN mkdir -p "/home/btsync/Sync"
RUN apt-get update && apt-get install -qy --force-yes ca-certificates curl tar && apt-get clean

WORKDIR /etc/btsync

RUN set -x \
    && curl -k -L https://download-cdn.getsyncapp.com/stable/linux-x64/BitTorrent-Sync_x64.tar.gz | tar zxv \
    && mv ./btsync /sbin/btsync \
    && rm ./BitTorrent-Sync_x64.tar.gz \
    && ln -s /home/btsync/Sync /home/btsync/data

RUN ./btsync --dump-sample-config >> btsync.conf \
    && mv -n ./btsync.conf ./home/btsync/.config/btsync.conf

RUN chown -R ntsync:btsync /home/btsync/
RUN find /home/btsync/ -type f | while read LINE; do chmod 640 "$LINE" ; done
RUN find /home/btsync/ -type d | while read LINE; do chmod 750 "$LINE" ; done

WORKDIR /home/btsync/
USER btsync

EXPOSE 8888
EXPOSE 55555

VOLUME ["/home/btsync/.config" "/home/btsync/data"]

ENTRYPOINT ["/sbin/btsync", "--config", "/home/btsync/.config/btsync.conf", "--nodaemon"]
