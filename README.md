# makersupplies.dk listings web application

Run with Alpine Linux


## Development

python manage.py runserver
npm run dev

## Deployment

Build docker files with:

docker build -t astroapp -f Dockerfile.astroapp .
<br>
docker build -t djangoapp -f Dockerfile.djangoapp .

Deploy with:

RTE=prod docker-compose up
