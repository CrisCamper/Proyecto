import json
import os
from commons.utils import limpiar_pantalla, promedio

def load_trainers_json():
    try:
      with open(os.path.join("data", "trainers.json"), 'r') as archivo_json:        
        lista_trainers = json.load(archivo_json)
        return lista_trainers
    except Exception as e:
      print(f"Error al cargar el archivo: {e}")

lista_trainers = load_trainers_json()
# Rutas disponibles ['Ruta NodeJS', 'Ruta Java', 'Ruta NetCore']
paths = ['nodejs', 'java', 'netcore']

def crear_trainer (): # Funcion para crear un nuevo trainer

    while True:        
        try:
                name = input('Ingrese nombre del Trainer: ')
                last_names = input('Ingrese apellidos del trainer: ')
                id = int(input('Ingrese Numero de identificacion: '))
                direction = input('Ingrese direccion del Triner: ')
                contact = int(input('Numero de contacto: '))
                emergency_contact = int(input('Numero de emergencia: '))
                while True:
                    path = input('Ingrese la ruta del trainer: ')
                    if path.lower() in paths:
                        break # Si la ruta ingresada está en paths, rompemos el bucle interno para pasar al principal
                    else:
                        print('Lo sentimos, Ruta no encontrada :[')
                        print('Ingrese una ruta valida')

                trainer = { # Creamos un diccionario con la informacion del trainer
                    'Nombres del Trainer': name,
                    'Apellidos del Trainer': last_names,
                    'Identificacion': id,
                    'Direccion': direction,
                    'Numero de contacto': contact,
                    'Numero de emergencia': emergency_contact,
                    'Ruta del Trainer': path

                }

                lista_trainers.append(trainer)
                guardar_json()

                while True: # Creamos un bucle temporal para Preguntar al usuario si desea ingresar un nuevo trainer
                    limpiar_pantalla() # Limpiamos la pantalla
                    another_entry = input("¿Desea agregar otro Trainer? (y/n): ")
                    if another_entry.lower() == 'y':
                        print('Guardando...')
                        # Rompemos el bucle interno para entrar al principal
                        break
                    elif another_entry.lower() == 'n':
                        print('Guardando...')
                        print('Trainers guardados exitosamente!')
                        limpiar_pantalla() # limpiamos pantalla antes de pasar al menú principal
                        return trainer
                    else:
                        print('Opcion no reconocida :(')

        except ValueError as e:  # Capturamos la excepción específica para errores de valor
            print(f"Error: {e}. Asegúrese de ingresar números en los campos que lo requieren.")

def guardar_json(): # Funcion para guardar la informacion de un trainer en JSON
    try:
      with open(os.path.join("data", "trainers.json"), 'w') as archivo_json:
        json.dump(lista_trainers, archivo_json, indent = 4)
        print("La lista de trainers ha sido guardada")
    except FileNotFoundError: # Si el archivo no existe imprime un mensaje
        print("El archivo no existe. Puede que aún no haya trainers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido:{e}")

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
            # Mostrar la información actual del trainer
            print("Información actual del trainer:")
            print(trainer_encontrado)

            # Solicitar la nueva información del trainer
            print("Ingrese la nueva información del trainer:")
            trainer_encontrado['Direccion'] = input('Nueva direccion del trainer: ')
            trainer_encontrado['Numero de contacto'] = int(input('Nuevo numero de contacto: '))
            trainer_encontrado['Numero de emergencia'] = int(input('Nuevo numero de emergencia: '))
            
            while True: 
                nueva_ruta = input('Nueva ruta del trainer: ')
                if nueva_ruta.lower() in paths:
                    trainer_encontrado['Ruta del Trainer'] = nueva_ruta
                    break
                else:
                    print('Lo sentimos, Ruta no encontrada :[')
                    print('Ingrese una ruta valida')


            # Guardar los cambios en el archivo JSON
            guardar_json()
            limpiar_pantalla() # limpiamos la pantalla para mostrar el siguiente mensaje gratificante :)
            print(f"\ntrainer con ID {id_modificar} modificado exitosamente.")
        else:
            print(f"\nNo se encontró un trainer con el ID {id_modificar}.")

    except ValueError as e:
        print(f"Error: {e}. Asegúrese de ingresar un número válido como ID.")
