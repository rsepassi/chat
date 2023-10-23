FROM alpine:latest

RUN apk update
RUN apk add python3 py3-pip
ADD requirements.txt /root/chat/requirements.txt
RUN python3 -m pip install -r /root/chat/requirements.txt

WORKDIR /root/chat
