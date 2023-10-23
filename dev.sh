#!/bin/sh

set -e

podman build . -t chat
podman run \
  -e OPENAI_API_KEY="$OPENAI_API_KEY" \
  -v $PWD:/root/chat -it chat /bin/sh
