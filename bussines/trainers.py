import json
import os
import random
from commons.utils import guardar_json, limpiar_pantalla, key_for_continue

def load_trainers_json():
    try:
      with open(os.path.join("data", "trainers.json"), 'r') as archivo_json:        
        lista_trainers = json.load(archivo_json)
        return lista_trainers
    except Exception as e:
      print(f"Error al cargar el archivo: {e}")

# Load trainer list
lista_trainers = load_trainers_json()
# Rutas disponibles ['Ruta NodeJS', 'Ruta Java', 'Ruta NetCore']
paths = ['artemis (nodejs)', 'apolo (java)', 'sputnik (netcore)']
journeys = ['mañana','tarde']

def crear_trainer (): # Funcion para crear un nuevo trainer

    while True:        
        try:
            name = input('Input trainer´s name: ')
            last_names = input('Input trainer´s last name: ')
            id = int(input('Input trainer´s number ID: '))
            direction = input('Input trainer´s direction: ')
            contact = int(input('Input trainer´s contact number: '))
            permanent_contact = int(input('Input trainer´s permanent contact: '))
            while True:
                print('correct example: mañana')
                journey = input('Type trainer journey: ')              
                if journey.lower() in journeys:
                    journey = journey.lower()
                    break
                else:
                    print('Lo sentimos, jornada no valida:[')
                    print('Ingrese una jornada valida')

            while True:
                print('correct example: sputnik (netcore)')
                path = input('Input path route: ')                
                if path.lower() in paths:
                    path = path.lower()
                    break
                else:
                    print('Lo sentimos, Ruta no encontrada :[')
                    print('Ingrese una ruta valida')

            trainer= { # Creamos un diccionario con la informacion del trainer
                'Nombres del trainer': name,
                'Apellidos del trainer': last_names,
                'Identificacion': id,
                'Direccion': direction,
                'Numero de contacto': contact,
                'Telefono fijo': permanent_contact,
                'Jornada': journey,
                'Ruta': path
            }
            
            lista_trainers.append(trainer)
            guardar_json(lista_trainers, 'trainers')
            key_for_continue()
            break
        except ValueError as e:  # Capturamos la excepción específica para errores de valor
            print(f"Error: {e}. Asegúrese de ingresar números en los campos que lo requieren.")

def listar_trainers(): # Funcion para listar los trainers
    for trainer in lista_trainers:
        for data in trainer:
            print(data,':',trainer[data])
        print('---------------------------')

def modificar_trainers(): # Funcion para modificar trainers
    # Mostrar la lista de trainers
    print("Lista de trainers:")
    listar_trainers()
    
    try:
        id_modificar = int(input("Ingrese el ID del trainer que desea modificar: "))
        limpiar_pantalla()
        
        # Buscar el trainer por ID
        trainer_encontrado = None
        for trainer in lista_trainers:
            if trainer['Identificacion'] == id_modificar:
                trainer_encontrado = trainer
                break

        if trainer_encontrado:
     
            # Solicitar la nueva información del trainer
            print("Ingrese la nueva información del trainer:")
            trainer_encontrado['Direccion'] = input('Nueva direccion del trainer: ')
            trainer_encontrado['Numero de contacto'] = int(input('Nuevo numero de contacto: '))
            
            while True: 
                nueva_ruta = input('Nueva ruta del trainer: ')
                if nueva_ruta.lower() in paths:
                    nueva_ruta = nueva_ruta.lower()
                    trainer_encontrado['Ruta'] = nueva_ruta
                    break
                else:
                    print('Lo sentimos, Ruta no encontrada :[')
                    print('Ingrese una ruta valida')


            # Guardar los cambios en el archivo JSON
            guardar_json(lista_trainers, 'trainers')
            limpiar_pantalla() # limpiamos la pantalla para mostrar el siguiente mensaje gratificante :)
            print(f"\ntrainer con ID {id_modificar} modificado exitosamente.")
        else:
            print(f"\nNo se encontró un trainer con el ID {id_modificar}.")

    except ValueError as e:
        print(f"Error: {e}. Asegúrese de ingresar un número válido como ID.")

guardar_json(lista_trainers, 'trainers') # function to save data in trainers.json