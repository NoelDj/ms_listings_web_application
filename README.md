# makersupplies.dk listings web application

Run with Alpine Linux using Docker



## Development mode

cd backend
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

cd frontend
npm i
npm run dev

## Deployment

Build docker files with:

docker build -t svleteapp -f Dockerfile.svelteapp .
<br>
docker build -t djangoapp -f Dockerfile.djangoapp .

Deploy with:

RTE=prod docker-compose up
