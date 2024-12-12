from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Tasks, UserTask, Profile, Proyectos
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from datetime import datetime

def Home(request):
    return render(request, 'home.html')

def SignUp(request):
    if request.method == "GET":
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            if request.POST['password1'] == '':
                return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'El parametro que ingresaste no es valido'})
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('Tareas')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'El usuario ya fue creado'})
        return render(request, 'signup.html', {'form': UserCreationForm(), 'error': 'La contrasena no coincide'})

def SignIn(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
        return render(request, 'signin.html', {'form': AuthenticationForm, 'error': 'El usuario que ha ingresado no existe'})
    else:
        login(request, user)
        return redirect('Tareas')


@login_required
def Tareas(request):
    Tareas = Tasks.objects.all().order_by('-puntaje')
    user_tasks = UserTask.objects.filter(user=request.user)
    completed_tasks_id = user_tasks.filter(completed=True).values_list('task_id', flat=True)
    return render(request, 'tareas.html', {'tareas': Tareas, 'completed_task_ids': completed_tasks_id})

@login_required
def Logout(request):
    logout(request)
    return redirect('Home')
    
@login_required
def UpPoints(request, task_id):
    try:
        tarea = Tasks.objects.get(id=task_id)

        # Crear o actualizar la relación entre usuario y tarea
        user_task, created = UserTask.objects.get_or_create(
            task=tarea,
            user=request.user,
            defaults={'completed': False}
        )

        if user_task.completed:
            return redirect('Tareas')

        profile, created = Profile.objects.get_or_create(user=request.user)

        user_task.completed = True
        user_task.save()

        profile.puntos += tarea.puntaje
        profile.save()

        return redirect('Tareas')
    except Tasks.DoesNotExist:
        return redirect('Tareas')

@login_required
def UpPointsAreas(request, task_id):
    if request.method == 'GET':
        return render(request, 'sumar_puntos_areas.html')
    try:
        tarea = Tasks.objects.get(id=task_id)

        # Crear o actualizar la relación entre usuario y tarea
        user_task, created = UserTask.objects.get_or_create(
            task=tarea,
            user=request.user,
            defaults={'completed': False}
        )

        if user_task.completed:
            return redirect('Tareas')

        profile, created = Profile.objects.get_or_create(user=request.user)

        user_task.completed = True
        user_task.save()

        profile.puntos += tarea.puntaje * int(request.POST['areas'])
        profile.save()

        return redirect('Tareas')
    except:
        return render(request, 'sumar_puntos_areas.html', {'error': 'Fallo en la suma de puntos'})

@login_required 
def DecrementPoints(request, task_id):
    try:
        tarea = Tasks.objects.get(id=task_id)
        
        profile, created = Profile.objects.get_or_create(user=request.user)

        profile.puntos -= tarea.puntaje
        profile.save()

        return redirect('Tareas')
    except UserTask.DoesNotExist:
        return redirect('Tareas')
    
@login_required
def Anadir_Tarea(request):
    if request.method == 'GET':
        return render(request, 'anadir_tarea.html')
    try:
        if request.POST['nombre'] == '' or request.POST['puntaje'] == '':
            return render(request, 'anadir_tarea.html', {'error': 'Ingresa caracteres validos'})
        Tarea_Nueva = Tasks.objects.create(nombre=request.POST['nombre'], puntaje=request.POST['puntaje'])
        Tarea_Nueva.save()
        return render(request, 'anadir_tarea.html', {'hecho': 'Se creo tu tarea nueva correctamente'})
    except:
        return render(request, 'anadir_tarea.html', {'error': 'No se pudo crear tu tarea'})

@login_required
def Eliminar_Tarea(request, task_id):
    tarea = Tasks.objects.filter(id=task_id)
    tarea.delete()
    return redirect('Tareas')

@login_required
def Proyectos_Function(request):
    proyectos = Proyectos.objects.all()
    return render(request, 'proyectos.html', {'proyectos': proyectos})

@login_required
def Anadir_Proyecto(request):
    if request.method == 'GET':
        return render(request, 'anadir_proyecto.html')
    try:
        if request.POST['proyecto'] == '' or request.POST['descripcion'] == '':
            return render(request, 'anadir_proyecto.html', {'error': 'Ingresa caracteres validos'})
        Proyecto_Nuevo = Proyectos.objects.create(proyecto=request.POST['proyecto'], descripcion=request.POST['descripcion'])
        Proyecto_Nuevo.save()
        return render(request, 'anadir_proyecto.html', {'hecho': 'Se creo tu proyecto nueva correctamente'})
    except:
        return render(request, 'anadir_proyecto.html', {'error': 'No se pudo crear tu proyecto'})

@login_required
def Completar_Proyectos(request, task_id):
    proyecto = Proyectos.objects.filter(id=task_id)
    proyecto.update(completado=True)
    return redirect('Proyectos')

@login_required
def Descompletar_Proyectos(request, task_id):
    proyecto = Proyectos.objects.filter(id=task_id)
    proyecto.update(completado=False)
    return redirect('Proyectos')

@login_required
def Crear_Observacion(request, task_id):
    if request.method == "GET":
        return render(request, 'observaciones.html')
    try:
        proyecto = Proyectos.objects.filter(id=task_id)
        proyecto.update(observaciones=request.POST['observaciones'])
        return redirect('Proyectos')
    except:
        return render(request, 'observaciones.html', {'error': 'No se pudo hacer la observacion'})

@login_required
def Editar_Observacion(request, task_id):
    observacion = Proyectos.objects.filter(id=task_id)
    if request.method == "GET":
        return render(request, 'editar_observacion.html', {'observacion': observacion})
    try:
        observacion.update(observaciones=request.POST['observaciones'])
        return redirect('Proyectos') 
    except:
        return render(request, 'editar_observacion.html', {'error': 'No se pudo editar la observacion'})

@login_required
def tabla_posiciones(request):
    usuarios_completos = User.objects.all()
    puntajes = Profile.objects.all().order_by('-puntos')
    return render(request, 'tabla_posiciones.html', {'usuarios': usuarios_completos, 'puntajes': puntajes})
