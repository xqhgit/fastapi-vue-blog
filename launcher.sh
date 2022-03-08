#!/bin/bash

docker-compose -f webappSimple-compose.yml up -d --build
sleep 1

echo "Preparing initialize data..."
sleep 2
docker-compose -f webappSimple-compose.yml exec webapp python db/init_db.py
sleep 1

docker-compose -f webappSimple-compose.yml restart all

docker-compose -f webappSimple-compose.yml ps
