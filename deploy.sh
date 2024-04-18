#!/bin/bash

ENV_FILE=".private/dev.env"
if [ ! -f "$ENV_FILE" ]; then
   echo "GK> Error: can't find private environment file"
   exit 1
fi
. "$ENV_FILE"

docker-compose stop || exit

cp services/python/*.py shared/python/

docker-compose up --build -d
