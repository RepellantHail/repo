from django.shortcuts import render, redirect
from .models import Employee
import datetime

# Create your views here.
def home(request):
    empleados = Employee.objects.all()
    return render(request, "gestionEmpleado.html", {"empleados": empleados})

def registrarEmpleado(request):
    name      = request.POST['txtID']
    apellido1 = request.POST['txtAPP']
    apellido2 = request.POST['txtAPM']
    cargo     = request.POST['txtCargo']
    empresa   = request.POST['txtEmpresa']
    calle     = request.POST['txtCalle']
    numeroExt = request.POST['txtNExt']
    numeroInt = request.POST['txtNInt']
    colonia   = request.POST['txtColonia']
    municipio = request.POST['txtMunicipio']
    estado    = request.POST['txtEstado']
    codPos    = request.POST['txtPO']
    telefono  = request.POST['txtPhone']
    email     = request.POST['txtEmail']
    fechaNac_str = request.POST['txtFNAC']  # Get fechaNac or set default value

    if fechaNac_str:
        # Convert fechaNac string to datetime.date object
        fechaNac = datetime.datetime.strptime(fechaNac_str, '%Y-%m-%d').date()

        # Calculate age based on fechaNac
        today = datetime.date.today()
        age = today.year - fechaNac.year - ((today.month, today.day) < (fechaNac.month, fechaNac.day))
    else:
        # Set default values if fechaNac is not provided
        fechaNac = None
        age = None

    empleado = Employee.objects.create(
        name = name,
        apellido1 = apellido1,
        apellido2 = apellido2,
        cargo = cargo,
        empresa = empresa,
        calle = calle,
        numeroExt = numeroExt,
        numeroInt = numeroInt,
        colonia = colonia,
        municipio = municipio,
        estado = estado,
        codPos = codPos,
        telefono = telefono,
        email = email,
        fechaNac = fechaNac,
        edad = age,    
    )

    return redirect('/')
    
def eliminarEmpleado(request, id):
    empleado = Employee.objects.get(id = id)
    empleado.delete()

    return redirect('/')

def editarEmpleado(request, id):
    empleado = Employee.objects.get(id = id)
    return render(request, "editarEmpleado.html", {"empleado": empleado})