"""
URL configuration for Tareas_Casa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Tareas.views import SignUp, Tareas, SignIn, Home, Logout, UpPoints, DecrementPoints, Anadir_Tarea, Proyectos_Function, Eliminar_Tarea, tabla_posiciones, Anadir_Proyecto, Completar_Proyectos, Descompletar_Proyectos, Crear_Observacion, Editar_Observacion, UpPointsAreas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home,name='Home'),
    path('register/', SignUp, name='Register'),
    path('tareas/', Tareas, name='Tareas'),
    path('login/', SignIn, name='Login'),
    path('logout/', Logout, name='Logout'),
    path('subir_puntos/<int:task_id>', UpPoints, name='UpPoints'),
    path('bajar_puntos/<int:task_id>', DecrementPoints, name='DecrementPoints'),
    path('anadir_tarea/', Anadir_Tarea, name='AnadirTarea'),
    path('eliminar_tarea/<int:task_id>', Eliminar_Tarea, name='EliminarTarea'),
    path('proyectos/', Proyectos_Function, name='Proyectos'),
    path('posiciones/', tabla_posiciones, name='Posiciones'),
    path('anadir_proyecto/', Anadir_Proyecto, name='AnadirProyecto'),
    path('completar_proyecto/<int:task_id>', Completar_Proyectos, name='CompletarProyecto'),
    path('descompletar_proyecto/<int:task_id>', Descompletar_Proyectos, name='DescompletarProyecto'),
    path('crear_observacion/<int:task_id>', Crear_Observacion, name='CrearObservacion'),
    path('editar_observacion/<int:task_id>', Editar_Observacion, name='EditarObservacion'),
    path('subir_puntos_areas/<int:task_id>', UpPointsAreas, name='UpPointsAreas'),
    path("__reload__/", include("django_browser_reload.urls")),
    path("Tareas_Persona/", Tabla_Tareas_Persona, name='TareasPorPersona'),
]
