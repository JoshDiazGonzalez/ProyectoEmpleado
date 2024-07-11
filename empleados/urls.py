from django.contrib import admin
from django.urls import path
from . import views

#se refiere al conjunto de todas las urls
app_name = "empleado_app"

urlpatterns = [
    path(
      '',
      views.InicioView.as_view(),
      name='inicio'
    ),
    
    path(
      'listar-todo-empleados/',
      views.ListaAllEmpleados.as_view(), 
      name='empleados_all'
    ),

    path(
      'lista-by-area/<shor_name>', 
      views.ListByAreaEmpleado.as_view(),
      name='empleados_area'
    ),
    path(
      'lista-empleados-admin/',
      views.ListEmpleadosAdmin.as_view(),
      name='empleados_admin'
    ),

    path('buscar-empleado/', views.ListEmpleadoByKword.as_view()),
    path('lista-habilidades-empleado/', views.ListaHabilidadesEmpleado.as_view()),
    path(
      'ver-empleado/<pk>',
      views.EmpleadoDetailView.as_view(),
      name='empleado_detail'),
      
    path(
      'add-empleado/', 
      views.EmpleadoCreateView.as_view(),
      name='empleado_add'
    ),

    path('success/', views.SuccessView.as_view(), name='correcto'),

    path(
      'update-empleado/<pk>/', 
      views.EmpleadoUpdateView.as_view(), 
      name='modificar_empledo'
    ),
    path(
      'delete-empleado/<pk>/', 
      views.EmpleadoDeleteView.as_view(), 
      name='eliminar_empleado'
    ),
]
