from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establece el módulo de configuración de Django para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tareas_Casa.settings')

app = Celery('Tareas_Casa')

# Configura Celery para usar las configuraciones de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubre automáticamente tareas en apps registradas
app.autodiscover_tasks()