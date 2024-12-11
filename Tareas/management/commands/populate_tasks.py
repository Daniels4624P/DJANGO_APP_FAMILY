from django.core.management.base import BaseCommand
from Tareas.models import Tasks  # Cambia 'app_name' por el nombre de tu aplicación

class Command(BaseCommand):
    help = 'Poblar la tabla Task con tareas predeterminadas'

    def handle(self, *args, **kwargs):
        tareas_y_puntajes = [
            {"descripcion": "Organizar Cocina", "puntos": 20},
            {"descripcion": "Lavar un baño", "puntos": 30},
            {"descripcion": "Organizar Lavandería", "puntos": 25},
            {"descripcion": "Tender Cama", "puntos": 5},
            {"descripcion": "Organizar Comedor", "puntos": 10},
            {"descripcion": "Organizar Area", "puntos": 15},
            {"descripcion": "Barrer y Trapear Area", "puntos": 20},
            {"descripcion": "Lavar Ropa", "puntos": 35},
            {"descripcion": "Organizar Arena Gato", "puntos": 15},
            {"descripcion": "Organizar Nevera", "puntos": 20},
            {"descripcion": "Sacar Basura", "puntos": 20},
            {"descripcion": "Planear y Hacer Mercado", "puntos": 35},
            {"descripcion": "Llevar Botellas de Amor y Sacar Reciclaje", "puntos": 15}
        ]

        for tarea in tareas_y_puntajes:
            Tasks.objects.get_or_create(nombre=tarea["descripcion"], puntaje=tarea["puntos"])

        self.stdout.write(self.style.SUCCESS('Tareas creadas exitosamente'))
