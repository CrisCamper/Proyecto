#procesar las inscripciones a el programa; la información que se tiene por cada camper es la siguiente : nro de identificación, nombre, apellidos, dirección, acudiente, teléfonos de contacto(Nro celular y nro fijo),estado.
import json
import os

def limpiar_pantalla(): # Funcion para limpiar pantalla
    os.system('clear' if os.name == 'posix' else 'cls')   

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

def promedio (teoric_note,practical_note): # Funcion para calificar la prueba
    promedy = (teoric_note + practical_note)/2
    return promedy

def guardar_json(lista, archivojson): # Funcion para guardar la informacion en JSON
    try:
      with open(os.path.join("data", f"{archivojson}.json"), 'w') as archivo_json:
        json.dump(lista, archivo_json, indent = 4)
        print("La lista de campers ha sido guardada")
    except FileNotFoundError: # Si el archivo no existe imprime un mensaje
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido:{e}")