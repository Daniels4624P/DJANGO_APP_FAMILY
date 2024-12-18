from django.db import models
from django.contrib.auth.models import User  # Usar el modelo de usuario integrado de Django

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} tiene {self.puntos} puntos"

class Tasks(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    puntaje = models.IntegerField()

    def __str__(self):
        return self.nombre

class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.task.nombre} - {self.completed_at.strftime('%d-%m-%Y')}"

class Proyectos(models.Model):
    proyecto = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    completado = models.BooleanField(default=False)

    def __str__(self):
        return f"Proyecto: {self.proyecto} - Completado: {self.completado}"
    
class TaskHistory(models.Model):
    tarea = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tarea.nombre} - {self.completed_at.strftime('%d-%m-%Y')}"
