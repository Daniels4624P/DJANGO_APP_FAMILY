from django.core.management.base import BaseCommand
from Tareas.models import Proyectos  # Cambia 'app_name' por el nombre de tu aplicación

class Command(BaseCommand):
    help = 'Poblar la tabla Proyectos con proyectos predeterminados'

    def handle(self, *args, **kwargs):
        tareas_y_puntajes = [
            {"proyecto": "Lampara Cocina", "descripcion": "Elegir y comprar una lampara para la cocina"},
            {"proyecto": "Cortina o separador cocina", "descripcion": "Comprar un separador para la cocina que separe la cocina del cuarto de ropas"},
            {"proyecto": "Silla Mamá", "descripcion": "Comprar una silla para MBR"},
            {"proyecto": "Limpiar Paredes", "descripcion": "Limpiar las paredes del apartamento"},
            {"proyecto": "Area Gato", "descripcion": "Planear y organizar el area del gato"},
            {"proyecto": "Definir areas en la cocina", "descripcion": "Planear como se va a organizar y que se va a comprar para la lavanderia y la cocina"},
            {"proyecto": "Area Trabajo Papás", "descripcion": "Planear y organizar el area de papas"},
            {"proyecto": "Comprar Tapetes", "descripcion": "Elegir Tapetes y comprarlos"},
            {"proyecto": "Mandar Hacer Gafas", "descripcion": "Elegir Montura, Lugar y hacer examen de ojos para comprar gafas"},
            {"proyecto": "Actividades mantener carro", "descripcion": "Actividades para mantener el carro"},
            {"proyecto": "Inversiones", "descripcion": ""},
            {"proyecto": "Compras de elementos para el televisor", "descripcion": "Comprar cosas como el Roku y otros elementos para el televisor"},
            {"proyecto": "Montar presupuesto y contabilidad", "descripcion": ""}
        ]

        for tarea in tareas_y_puntajes:
            Proyectos.objects.get_or_create(proyecto=tarea["proyecto"], descripcion=tarea["descripcion"])

        self.stdout.write(self.style.SUCCESS('Proyectos creados exitosamente'))
