import json
import os
from commons.utils import limpiar_pantalla, promedio

def load_campers_json():
    try:
      with open(os.path.join("data", "campers.json"), 'r') as archivo_json:        
        lista_campers = json.load(archivo_json)
        return lista_campers
    except Exception as e:
      print(f"Error al cargar el archivo: {e}")

lista_campers = load_campers_json()

def crear_camper (): # Funcion para crear un nuevo camper
    while True:        
        try:
            teoric_note = int(input('Ingrese Nota de la prueba teorica del aspirante : '))
            practical_note = int(input('Ingrese la Nota Practica del aspirane: '))

            # Aplicamos la funcion promedio para verificar el promedio entre la nota teorica y la nota practica
            resultado_prueba = promedio(teoric_note,practical_note)
            if resultado_prueba < 60:
                condicion_aspirante = 'No inscrito'
            else:
                condicion_aspirante = 'Inscrito'
            
            # Si la condicion del aspirante es Inscrito, accionamos este bloque de codigo el cual convertira en camper al aspirante
            if condicion_aspirante == 'Inscrito':
                name = input('Ingrese nombre del Camper: ')
                last_names = input('Ingrese apellidos del camper: ')
                id = int(input('Ingrese Numero de identificacion: '))
                direction = input('Ingrese direccion del camper: ')
                attendant = input('Ingrese nombre del acudiente: ')
                contact = int(input('Numero de contacto: '))
                permanent_contact = int(input('Numero de telefono fijo [Puede ser el mismo de contacto]: '))

                #Según el promedio, el aspirante será inscrito o no
                state = condicion_aspirante

                camper = { # Creamos un diccionario con la informacion del camper
                    'Nombres del Camper': name,
                    'Apellidos del Camper': last_names,
                    'Identificacion': id,
                    'Direccion': direction,
                    'Acudiente': attendant,
                    'Numero de contacto': contact,
                    'Telefono fijo': permanent_contact,
                    'Estado del camper': state

                }

                lista_campers.append(camper)
                guardar_json()

                while True: # Creamos un bucle temporal para Preguntar al usuario si desea ingresar un nuevo camper
                    limpiar_pantalla() # Limpiamos la pantalla
                    another_entry = input("¿Desea agregar otro posible Camper? (y/n): ")
                    if another_entry.lower() == 'y':
                        print('Guardando...')
                        # Rompemos el bucle interno para entrar al principal
                        break
                    elif another_entry.lower() == 'n':
                        print('Guardando...')
                        print('Campers guardados exitosamente!')
                        limpiar_pantalla() # limpiamos pantalla antes de pasar al menú principal
                        return camper
                    else:
                        print('Opcion no reconocida :(')

            # Si la condicion del aspirante es 'no inscrito', activamos el siguiente bloque de codigo
            elif condicion_aspirante == 'No inscrito':
                limpiar_pantalla()
                print(f'Lo sentimos, nota del aspirante menor a 60, estado del aspirante: {condicion_aspirante}')
                while True:
                    another_entry = input('¿Desea agregar otro aspirante? [y/n]: ') # Preguntamos al usuario si desea agragar otro aspirante
                    if another_entry.lower() == 'y':
                        print('------>[ningun dato guardado]<------')
                        # Rompemos el bucle interno para entrar al principal
                        break
                    elif another_entry.lower() == 'n':
                        limpiar_pantalla() # limpiamos pantalla antes de pasar al menú principal
                        return None
                    else:
                        print('Opcion no reconocida :(')


        except ValueError as e:  # Capturamos la excepción específica para errores de valor
            print(f"Error: {e}. Asegúrese de ingresar números en los campos que lo requieren.")

def guardar_json(): # Funcion para guardar la informacion de un camper en JSON
    try:
      with open(os.path.join("data", "campers.json"), 'w') as archivo_json:
        json.dump(lista_campers, archivo_json, indent = 4)
        print("La lista de campers ha sido guardada")
    except FileNotFoundError: # Si el archivo no existe imprime un mensaje
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido:{e}")

def listar_campers(): # Funcion para listar los campers
    for camper in lista_campers:
        for data in camper:
            print(data,':',camper[data])
        print('---------------------------')

def modificar_camper(): # Funcion para modificar campers
    # Mostrar la lista de campers
    print("Lista de campers:")
    listar_campers()
    
    try:
        id_modificar = int(input("Ingrese el ID del camper que desea modificar: "))
        limpiar_pantalla()
        
        # Buscar el camper por ID
        camper_encontrado = None
        for camper in lista_campers:
            if camper['Identificacion'] == id_modificar:
                camper_encontrado = camper
                break

        if camper_encontrado:
            # Mostrar la información actual del camper
            print("Información actual del camper:")
            print(camper_encontrado)

            # Solicitar la nueva información del camper
            print("Ingrese la nueva información del camper:")
            camper_encontrado['Nombre'] = input('Nuevo nombre del Camper: ')
            camper_encontrado['Apellidos'] = input('Nuevos apellidos del camper: ')
            camper_encontrado['Direccion'] = input('Nueva direccion del camper: ')
            camper_encontrado['Acudiente'] = input('Nuevo nombre del acudiente: ')
            camper_encontrado['Numero de contacto'] = int(input('Nuevo numero de contacto: '))
            camper_encontrado['Telefono fijo'] = int(input('Nuevo numero de telefono fijo: '))
            camper_encontrado['Estado del camper'] = input('Nuevo estado del camper: ')

            # Guardar los cambios en el archivo JSON
            guardar_json()
            limpiar_pantalla() # limpiamos la pantalla para mostrar el siguiente mensaje gratificante :)
            print(f"\nCamper con ID {id_modificar} modificado exitosamente.")
        else:
            print(f"\nNo se encontró un camper con el ID {id_modificar}.")

    except ValueError as e:
        print(f"Error: {e}. Asegúrese de ingresar un número válido como ID.")
