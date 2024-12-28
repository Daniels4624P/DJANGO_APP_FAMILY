web: gunicorn Tareas_Casa.wsgi --bind 0.0.0.0:${PORT}
worker: celery -A Tareas_Casa worker --loglevel=info
beat: celery -A Tareas_Casa beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler
