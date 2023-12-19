#!/bin/sh

echo "starting deploying"
cd ~/ms_listings_project/ || exit
docker-compose down
export RTE=dev
docker-compose up -d
