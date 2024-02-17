#!/bin/sh

echo "Starting deployment"
cd ~/ms_listings_web_application/ || exit
RTE=dev docker-compose pull svelteapp djangoapp
RTE=dev docker-compose up -d --no-deps --build
echo "Deployment completed"