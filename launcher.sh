#!/bin/bash

docker-compose -f webappSimple-compose.yml up -d --build
sleep 1

echo "Prepare initialization data. Please wait ..."
sleep 6
docker-compose -f webappSimple-compose.yml exec webapp python db/init_db.py
sleep 2

docker-compose -f webappSimple-compose.yml restart
sleep 2

docker-compose -f webappSimple-compose.yml ps
