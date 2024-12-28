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
python manage.py migrate django_celery_beat
echo "Creando superusuario..."
python manage.py shell <<EOF
from django.contrib.auth.models import User

# Datos del superusuario
username = "admin"
email = "admin@example.com"
password = "admin123"

# Crear superusuario solo si no existe
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superusuario creado: {username}")
else:
    print(f"Superusuario ya existe: {username}")
EOF
echo "Iniciando Celery Worker y Beat..."
