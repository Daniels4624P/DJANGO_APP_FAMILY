web: gunicorn Tareas_Casa.wsgi --bind 0.0.0.0:${PORT}
worker: celery -A mi_proyecto worker --loglevel=info --uid=admin123
beat: celery -A mi_proyecto beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler --uid=admin123
