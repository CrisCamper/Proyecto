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