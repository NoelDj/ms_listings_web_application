# makersupplies.dk listings web application

Run with Alpine Linux


## Development mode

python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

npm i
npm run dev

## Deployment

Build docker files with:

docker build -t astroapp -f Dockerfile.astroapp .
<br>
docker build -t djangoapp -f Dockerfile.djangoapp .

Deploy with:

RTE=prod docker-compose up
