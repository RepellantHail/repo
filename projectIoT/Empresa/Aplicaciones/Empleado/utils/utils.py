import os

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