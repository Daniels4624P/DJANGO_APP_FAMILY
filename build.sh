#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

cd theme/static_src
npm install
npm run build
cd ..
cd ..

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py populate_tasks
python manage.py populate_proyetcs
python manage.py tailwind build
celery -A Tareas_Casa worker --loglevel=info
celery -A Tareas_Casa beat --loglevel=info
python manage.py migrate django_celery_beat
