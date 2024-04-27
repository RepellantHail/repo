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

def main():
    print("\fPráctica 4")
    # Get the absolute path to the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Read mock data
    mockDataLines = readFile(os.path.join(current_dir, 'MOCK_DATA.txt'))
    #Send Alumno
    for id, alumno in enumerate(mockDataLines, start = 0):
        # Read oficio
        oficio = readFile(os.path.join(current_dir, 'oficio.txt'))
        # Insert Mock Data into oficio
        oficio_filled = insertData(oficio, alumno)
        print(oficio_filled)
        # Export oficios
        exportFile(oficio_filled, id)

def readFile(src):
    with open(src, 'r') as file:
        return file.readlines()

def insertData(oficio, alumno):
    # Iterate over each mock data entry
    filled_oficio = insertInstitution(''.join(oficio))
    filled_oficio = insertAlumno(filled_oficio, alumno.split(','))
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

def insertAlumno(oficio, alumno):
    # Replace placeholders in the template with actual data from the institution dictionary
    filled = oficio.replace("[Nombre]"              , alumno[0])
    filled = filled.replace("[Apellido Paterno]"    , alumno[1])
    filled = filled.replace("[Apellido Materno]"    , alumno[2])
    filled = filled.replace("[Fecha de Nacimiento]" , alumno[14])
    filled = filled.replace("[Edad]"                , alumno[3])
    filled = filled.replace("[Teléfono]"            , alumno[12])
    filled = filled.replace("[Correo Electrónico]"  , alumno[13])
    filled = filled.replace("[Calle]"               , alumno[5])
    filled = filled.replace("[Número Exterior]"     , alumno[6])
    filled = filled.replace("[Número Interior]"     , alumno[7])
    filled = filled.replace("[Colonia]"             , alumno[8])
    filled = filled.replace("[Municipio]"           , alumno[9])
    filled = filled.replace("[Estado]"              , alumno[10])
    filled = filled.replace("[Código Postal]"       , alumno[11])
    filled = filled.replace("[Puesto]"              , alumno[3])
    filled = filled.replace("[Empresa]"             , alumno[4])
    # Return the filled oficio
    return filled

def exportFile(oficio_filled, id):    
    # Get the absolute path to the current directory
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Create a folder for exported files if it doesn't exist
    export_folder = os.path.join(current_dir, 'exportedFiles')
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)

    # Export the filled document to a file within the folder
    export_path = os.path.join(export_folder, f'oficio_filled_{id}.txt')
    with open(export_path, 'w') as file:
        file.write(oficio_filled)
    print(f"Oficio {id} exportado con éxito.")


main()
