#procesar las inscripciones a el programa; la información que se tiene por cada camper es la siguiente : nro de identificación, nombre, apellidos, dirección, acudiente, teléfonos de contacto(Nro celular y nro fijo),estado.
import json
import os

def limpiar_pantalla(): # Funcion para limpiar pantalla
    os.system('clear' if os.name == 'posix' else 'cls')    
def save_to_json(camper): # Funcion para guardar los datos en JSON
    data_folder = 'data'
    os.makedirs(data_folder, exist_ok=True)  # Crea la carpeta 'data' si no existe

    json_file_path = os.path.join(data_folder, 'camper.json')

    with open(json_file_path, 'a') as file:
        json.dump(camper, file, indent=2)
def validar_opcion(enunciando,inferior,superior): # Funcion para validar opciones
    while True:
        try:
            opcion =int(input(enunciando))
            if opcion>=inferior and opcion<=superior:
                return opcion
            else:
                print(f"Opción no está entre el intervalo de ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número válido. ")
