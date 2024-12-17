from celery import shared_task
from django.utils.timezone import timedelta, now
from .models import UserTask, Profile

@shared_task
def descompletar_tareas():
    tasks = UserTask.objects.filter(completed=True)
    for task in tasks:
        task.completed = False
        task.save()
    print(f"Tareas completadas reiniciadas a las {now()}")

@shared_task
def quitar_puntos():
    perfiles = Profile.objects.all()
    for perfil in perfiles:
        perfil.puntos = 0
        perfil.save()
    print(f"Puntos reiniciados a las {now()}")

@shared_task
def email_mama():
    mama = User.objects.get(username="mbaquero")
    mama.email = "elenabaquerorozo@gmail.com"
    mama.save()
    print("Correo Puesto")
