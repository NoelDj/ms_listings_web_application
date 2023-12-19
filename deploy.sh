#!/bin/sh

echo "starting deploying"
cd ~/ms_listings_web_appilcation/ || exit
docker-compose down
export RTE=dev
docker-compose up -d
