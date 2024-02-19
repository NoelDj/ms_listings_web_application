#!/bin/sh

echo "Starting deployment"
cd ~/ms_listings_web_application/ || exit
RTE=prod docker-compose pull svelteapp djangoapp
RTE=prod docker-compose up -d --no-deps --build
echo "Deployment completed"
