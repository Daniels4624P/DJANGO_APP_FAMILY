web: gunicorn Tareas_Casa.wsgi
worker: celery -A Tareas_Casa worker --loglevel=info
beat: celery -A Tareas_Casa beat --loglevel=info
