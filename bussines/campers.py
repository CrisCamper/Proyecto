import json
import os
from commons.utils import limpiar_pantalla, promedio, guardar_json, key_for_continue

def load_campers_json(): # Funcion para cargar campers.json y retornar una lista
    try:
      with open(os.path.join("data", "campers.json"), 'r') as archivo_json:        
        lista_campers = json.load(archivo_json)
        return lista_campers
    except Exception as e:
      print(f"Error al cargar el archivo: {e}")

# load camper list
lista_campers = load_campers_json()

def inscribir_camper (): # Funcion para inscribir un camper
    limpiar_pantalla()
    while True:
        try:
            name = input('Type camper´s name: ')
            last_names = input('Type camper´s last name: ')
            id = int(input('Type camper´s number ID: '))
            direction = input('Type camper´s direction: ')
            attendant = input('Type camper´s attendant´s name: ')
            contact = int(input('Type camper´s contact number: '))
            permanent_contact = int(input('Type camper´s permanent contact: '))
            state = 'inscrito'
            path = 'none'
            # Creamos un diccionario con la informacion del camper
            camper = { 
                'Nombres del Camper': name,
                'Apellidos del Camper': last_names,
                'Identificacion': id,
                'Direccion': direction,
                'Acudiente': attendant,
                'Numero de contacto': contact,
                'Telefono fijo': permanent_contact,
                'Estado del camper': state,
                'Ruta': path
            }
            # Agregamos aspirante_camper al final de la lista_campers
            lista_campers.append(camper)
            guardar_json(lista_campers, 'campers')
            
            # Bucle para preguntar si desea agregar un camper nuevo:
            while True:
                limpiar_pantalla()
                another_entry = input('\n¿Desea agragar otro aspirante? [y/n]: ')
                if another_entry.lower() == 'y':
                    print('Datos guardados exitosamente...')
                    key_for_continue()
                    break
                elif another_entry.lower() == 'n':
                    print('Datos guardados exitosamente...')
                    key_for_continue()
                    return camper
                else:
                    input('¡Intenta ingresar un valor correcto!')
                    key_for_continue

        except ValueError:
            print('Error, asegurese de ingresar valores correctos')
            key_for_continue()
        
def registrar_camper (): # Funcion para crear un nuevo camper
    while True:   
        try:
            listar_campers()
            if lista_campers == []:
                print('No se encontró ningun camper')
                key_for_continue()

            id_modificar = int(input("Ingrese el ID del camper que desea registrar: "))
            limpiar_pantalla()
            camper_encontrado = None
            for camper in lista_campers:
                if camper['Identificacion'] == id_modificar and camper['Estado del camper'] == 'inscrito' or 'aprobado':
                    camper_encontrado = camper

            teoric_note = int(input('Ingrese Nota de la prueba teorica del aspirante : '))
            practical_note = int(input('Ingrese la Nota Practica del aspirane: '))
            #funcion promedio para verificar el promedio entre la nota teorica y la nota practica
            resultado_prueba = promedio(teoric_note,practical_note)
            if resultado_prueba < 60:
                estado = 'reprobado/riesgo'
            else:
                estado = 'aprobado'
            if camper_encontrado:
                camper_encontrado['Estado del camper'] = estado
                # Guardar los cambios en el archivo JSON
                guardar_json(lista_campers,'campers')
                limpiar_pantalla() # limpiamos la pantalla para mostrar el siguiente mensaje gratificante :)
                print(f"\nCamper con ID {id_modificar} registrado exitosamente.")
            else:
                print(f"\nNo se encontró un camper con el ID {id_modificar}.")
            break
        except ValueError as e:  # Capturamos la excepción específica para errores de valor
            print(f"Error: {e}. Asegúrese de ingresar números en los campos que lo requieren.")
            key_for_continue()

def listar_campers(): # Funcion para listar los campers
    print('Lista de campers')
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

            # Solicitar la nueva información del camper
            print("Ingrese la nueva información del camper:")
            camper_encontrado['Direccion'] = input('Nueva direccion del camper: ')
            camper_encontrado['Acudiente'] = input('Nuevo nombre del acudiente: ')
            camper_encontrado['Numero de contacto'] = int(input('Nuevo numero de contacto: '))
            camper_encontrado['Telefono fijo'] = int(input('Nuevo numero de telefono fijo: '))
            camper_state = input('Nuevo estado del camper: ')
            # Convertimos en minuscula el camper_state
            camper_encontrado['Estado del camper'] = camper_state.lower()

            # Guardar los cambios en el archivo JSON
            guardar_json(lista_campers,'campers')
            limpiar_pantalla() # limpiamos la pantalla para mostrar el siguiente mensaje gratificante :)
            print(f"\nCamper con ID {id_modificar} modificado exitosamente.")
        else:
            print(f"\nNo se encontró un camper con el ID {id_modificar}.")

    except ValueError as e:
        print(f"Error: {e}. Asegúrese de ingresar un número válido como ID.")

guardar_json(lista_campers, 'campers') # function to save info in json