#!/bin/sh

echo "starting deploying"
cd ~/a/ms_listings_project/ || exit
docker-compose down
export RTE=dev
docker-compose up -d
