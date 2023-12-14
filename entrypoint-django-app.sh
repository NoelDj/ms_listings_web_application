#!/bin/sh

python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py test --verbosity 2
python manage.py runserver 0.0.0.0:8000
