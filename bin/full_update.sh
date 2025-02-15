#!/bin/sh

cd ..
git pull origin master
docker-compose -f production.yml down
docker-compose -f production.yml up -d --build
docker-compose -f production.yml run --rm django python manage.py migrate

echo "Successfully deployed."
