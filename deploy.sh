#!/bin/bash

docker-compose stop || exit

docker-compose up --build -d
