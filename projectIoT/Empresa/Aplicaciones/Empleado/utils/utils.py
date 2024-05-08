import os
import datetime
from ..models import Employee

# Create an instance of the Institution class
class Institution :
    def __init__(self):
        self.nombre_programa = "Practicas NASA"
        self.nombre_institucion = "CETI COLOMOS"
        self.current_date = "26 Abril 2024"
        self.nombre_director = "ELON MUSK"
        self.telefono_institucion = "01 800 CETI"
        self.mail_institucion = "ceti@ceti.mx"

# Create an instance of the Institution class
institution = Institution()

def exportFile(oficio_filled, id):    
    # Get the absolute path to the current directory
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Get the parent directory (one level up)
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    # Create a folder for exported files if it doesn't exist
    export_folder = os.path.join(parent_dir, 'exportedFiles')
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)

    # Export the filled document to a file within the folder
    export_path = os.path.join(export_folder, f'oficio_filled_{id}.txt')
    with open(export_path, 'w') as file:
        file.write(oficio_filled)
    print(f"Oficio {id} exportado con éxito.")

def insertData(oficio, empleado):
    # Iterate over each mock data entry
    filled_oficio = insertInstitution(''.join(oficio))
    filled_oficio = insertAlumno(filled_oficio, empleado)
    # Return the filled oficio
    return filled_oficio

def insertInstitution(oficio):
    # Replace placeholders in the template with actual data from the institution dictionary
    filled_oficio = oficio.replace         ("[Nombre del Programa]"         , institution.nombre_programa)
    filled_oficio = filled_oficio.replace  ("[Nombre de la Institución]"    , institution.nombre_institucion)
    filled_oficio = filled_oficio.replace  ("[Fecha actual]"                , institution.current_date)
    filled_oficio = filled_oficio.replace  ("[Nombre del Director]"         , institution.nombre_director)
    filled_oficio = filled_oficio.replace  ("[Teléfono]"                    , institution.telefono_institucion)
    filled_oficio = filled_oficio.replace  ("[Correo Electrónico]"          , institution.mail_institucion)
    # Return the filled oficio
    return filled_oficio

def insertAlumno(oficio, empleado):    
    filled = oficio.replace("[Nombre]"              , str(empleado.name))
    filled = filled.replace("[Apellido Paterno]"    , str(empleado.apellido1))
    filled = filled.replace("[Apellido Materno]"    , str(empleado.apellido2))
    filled = filled.replace("[Fecha de Nacimiento]" , str(empleado.fechaNac))
    filled = filled.replace("[Edad]"                , str(empleado.edad))
    filled = filled.replace("[Teléfono]"            , str(empleado.telefono))
    filled = filled.replace("[Correo Electrónico]"  , str(empleado.email))
    filled = filled.replace("[Calle]"               , str(empleado.calle))
    filled = filled.replace("[Número Exterior]"     , str(empleado.numeroExt))
    filled = filled.replace("[Número Interior]"     , str(empleado.numeroInt))
    filled = filled.replace("[Colonia]"             , str(empleado.colonia))
    filled = filled.replace("[Municipio]"           , str(empleado.municipio))
    filled = filled.replace("[Estado]"              , str(empleado.estado))
    filled = filled.replace("[Código Postal]"       , str(empleado.codPos))
    filled = filled.replace("[Puesto]"              , str(empleado.cargo))
    filled = filled.replace("[Empresa]"             , str(empleado.empresa))
    # Return the filled oficio
    return filled

def readFile(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
    
def importData():
    # Get the absolute path to the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Read mock data
    mockDataLines = readFile(os.path.join(current_dir, '../static/documents/MOCK_DATA.txt'))
    
    # Iterate over each line of mock data
    for id, alumno_data in enumerate(mockDataLines, start=1):
        # Parse the comma-separated values
        alumno_fields = alumno_data.strip().split(',')
        if len(alumno_fields) != 15:
            print(f"Error: Invalid data format in line {id} of MOCK_DATA.txt")
            continue
        
        # Extract individual fields
        name = alumno_fields[0]
        apellido1 = alumno_fields[1]
        apellido2 = alumno_fields[2]
        cargo = alumno_fields[3]
        empresa = alumno_fields[4]
        calle = alumno_fields[5]
        numeroExt = alumno_fields[6]
        numeroInt = alumno_fields[7]
        colonia = alumno_fields[8]
        municipio = alumno_fields[9]
        estado = alumno_fields[10]
        codPos = alumno_fields[11]
        telefono = alumno_fields[12]
        telefono = ''.join(filter(str.isdigit, alumno_fields[12])) 
        email = alumno_fields[13]
        fechaNac_str = alumno_fields[14]
        
        # Convert fechaNac string to datetime.date object
        try:
            fechaNac = datetime.datetime.strptime(fechaNac_str, '%m/%d/%Y').date()
        except ValueError:
            print(f"Error: Invalid date format in line {id} of MOCK_DATA.txt")
            continue
        
        # Calculate age based on fechaNac
        today = datetime.date.today()
        age = today.year - fechaNac.year - ((today.month, today.day) < (fechaNac.month, fechaNac.day))
        
        # Create and save Employee object
        empleado = Employee.objects.create(
            name=name,
            apellido1=apellido1,
            apellido2=apellido2,
            cargo=cargo,
            empresa=empresa,
            calle=calle,
            numeroExt=numeroExt,
            numeroInt=numeroInt,
            colonia=colonia,
            municipio=municipio,
            estado=estado,
            codPos=codPos,
            telefono=telefono,
            email=email,
            fechaNac=fechaNac,
            edad=age,
        )