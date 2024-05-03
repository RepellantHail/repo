from django.shortcuts import render
from .models import Employee

# Create your views here.
def home(request):
    empleados = Employee.objects.all()
    return render(request, "gestionEmpleado.html", {"empleados": empleados})
