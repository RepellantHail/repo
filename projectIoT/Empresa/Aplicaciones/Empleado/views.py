from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Employee
import datetime
from django.conf import settings
import os
from .utils.utils import exportFile, insertData, readFile, importData

# Create your views here.
def home(request):
    empleados = Employee.objects.all()
    # importData() Importa mock data
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
    fechaNac_str = request.POST['txtFNAC']

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

def getEmpleado(request, id):
    empleado = Employee.objects.get(id = id)
    return render(request, "getEmpleado.html", {"empleado": empleado})

def editarEmpleado(request):
    id        = request.POST['id']
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
    fechaNac_str = request.POST['txtFNAC']

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

    #Get Empleado
    empleado = Employee.objects.get(id = id)

    empleado.name = name
    empleado.apellido1 = apellido1
    empleado.apellido2 = apellido2
    empleado.cargo = cargo
    empleado.empresa = empresa
    empleado.calle = calle
    empleado.numeroExt = numeroExt
    empleado.numeroInt = numeroInt
    empleado.colonia = colonia
    empleado.municipio = municipio
    empleado.estado = estado
    empleado.codPos = codPos
    empleado.telefono = telefono
    empleado.email = email
    empleado.fechaNac = fechaNac
    empleado.edad = age

    empleado.save()
    return redirect('/')

def gestionOficio(request):
    empleados = Employee.objects.all()
    file_path = os.path.dirname(os.path.abspath(__file__))
    file_content = readFile(os.path.join(file_path, './static/documents/oficio.txt'))
    return render(request, "oficio.html", {'file_content': file_content, "empleados": empleados})

def procesarOficio(request):
    if request.method == 'POST':
        selected_employee_ids = request.POST.getlist('selected_empleados')
        
        # Perform processing with the selected employee IDs
        selected_employees = Employee.objects.filter(id__in=selected_employee_ids)
        
        # Get the content of the oficio template
        file_path = os.path.dirname(os.path.abspath(__file__))
        file_content = readFile(os.path.join(file_path, './static/documents/oficio.txt')) 

        # Export Employee
        for employee_id in selected_employee_ids:
            employee = Employee.objects.get(id=int(employee_id))
            # Assuming oficio_filled is the content formatted with oficio.txt
            filled_oficio = insertData(file_content, employee)
            exportFile(filled_oficio, employee_id)
        
        # Redirect or render a response as needed
        return HttpResponseRedirect('/') # Redirect to a success page
    else:
        # Handle GET request
        return HttpResponseRedirect('/')