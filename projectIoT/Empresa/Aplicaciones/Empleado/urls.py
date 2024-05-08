from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,  name='home'),
    path('registrarEmpleado/', views.registrarEmpleado),
    path('eliminarEmpleado/<id>', views.eliminarEmpleado),
    path('getEmpleado/<id>', views.getEmpleado),
    path('editarEmpleado/', views.editarEmpleado),
    path('gestionOficio/', views.gestionOficio, name='gestion_oficio'),
    path('procesarOficio/', views.procesarOficio, name='exportar_oficio'),
]
