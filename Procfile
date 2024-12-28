web: gunicorn mi_proyecto.wsgi:application --bind 0.0.0.0:${PORT}
worker: celery -A mi_proyecto worker --loglevel=info
beat: celery -A mi_proyecto beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler
