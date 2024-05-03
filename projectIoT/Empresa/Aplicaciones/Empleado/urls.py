from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('registrarEmpleado/', views.registrarEmpleado),
    path('eliminarEmpleado/<id>', views.eliminarEmpleado),
    path('editarEmpleado/<id>', views.editarEmpleado)
]
