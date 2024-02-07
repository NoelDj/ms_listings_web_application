#!/bin/sh

echo "Runtime Environment: $RTE"

python manage.py check
python manage.py makemigrations
python manage.py migrate

case "$RTE" in
    dev )
        echo "Development mode"
#        coverage run --source="." --omit="manage.py" manage.py test --verbosity 2
#        coverage report -m
        python manage.py runserver 0.0.0.0:8000
        ;;
    test )
        echo "Test mode"
        #pip-audit || exit 1
        coverage run --source="." --omit="manage.py" manage.py test --verbosity 2
        coverage report -m --fail-under=75
        ;;
    prod )
        echo "Production mode"
        #pip-audit || exit 1
        python manage.py check --deploy
        ;;
esac
