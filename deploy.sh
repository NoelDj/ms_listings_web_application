#!/bin/sh

echo "starting deploying"
cd ~/ms_listings_web_application/ || exit
docker-compose down
RTE=dev docker-compose up -d
