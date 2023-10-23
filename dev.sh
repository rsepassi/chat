#!/bin/sh

set -e

podman build . -t chat
podman run -v $PWD:/root/chat -it chat /bin/sh
