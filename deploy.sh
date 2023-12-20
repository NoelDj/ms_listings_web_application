#!/bin/sh

git pull
echo "Starting deployment"
cd ~/ms_listings_web_application/ || exit
docker pull registry.gitlab.com/noel100/ms_listings_web_application/djangoapp
docker pull registry.gitlab.com/noel100/ms_listings_web_application/astroapp
RTE=dev docker-compose down
RTE=dev docker-compose up -d
echo "Deployment completed"