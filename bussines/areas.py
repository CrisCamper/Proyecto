import os
import json
from commons.utils import guardar_json, limpiar_pantalla, key_for_continue
from bussines.campers import load_campers_json
from bussines.trainers import load_trainers_json

def load_areas_json(): # Funtion to load Json
    try:
        with open(os.path.join("data", "areas.json"), 'r') as archivo_json:
            lista_areas = json.load(archivo_json)
        return lista_areas
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")

lista_areas = [
    # Position 0
    {'sputnik': {'Campers id': []}},
    # Position 1
    {'sputnik': {'Trainers id': []}},
    # Position 2
    {'artemis': {'Campers id': []}},
    # Position 3
    {'artemis': {'Campers id': []}},
    # Position 4
    {'apolo': {'Campers id': []}},
    # Position 5
    {'apolo': {'Campers id': []}}
]

def eliminar_camper(name_area,position_area): # Function to delete a camper
  while True:
    try:
      lista_areas = load_areas_json()
      id_remove = int(input('Ingrese el id del camper que queire elimnar: '))
      camper_to_remove = next((camper for camper in lista_areas[position_area][name_area]['Campers id'] if camper['Identificacion'] == id_remove), None)
      if camper_to_remove:
          lista_areas[position_area][name_area]['Campers id'].remove(camper_to_remove)
          guardar_json(lista_areas, 'areas')
          print(f'Camper con ID {id_remove} eliminado exitosamente del área {name_area}.')
      else:
          print('Camper no encontrado en el área especificada.')
      
      another_delete = input('¿Desea eliminar otro camper? [y/n]: ')
    
      if another_delete.lower() == 'y':
        print('Guardando...')
        key_for_continue()
        

    except ValueError as e:
        print(f"Error: {e}. Asegúrese de ingresar números en los campos que lo requieren.")
        key_for_continue()

guardar_json(lista_areas, 'areas')

def agregar_campers(name_area, position_area): # Function to fill a camper area with it name and position
  while True:
    try:
        lista_campers = load_campers_json()
        lista_areas = load_areas_json()

        print(f'Campers disponibles para {name_area}')
        for camper in lista_campers:
            if camper.get('Estado del camper') == 'aprobado':
                for data in camper:
                    print(data, ':', camper[data])
                print('---------------------------')

        id_add = int(input(f'Ingrese el id del Camper que desea agregar a {name_area}: '))

        camper_found = next((camper for camper in lista_campers if camper['Identificacion'] == id_add and camper['Estado del camper'] == 'aprobado'), None)

        if camper_found:
            lista_areas[position_area][name_area]['Campers id'].append(camper_found)
            guardar_json(lista_areas, 'areas')

            while True:
                limpiar_pantalla()
                another_entry = input("¿Desea agregar otro Camper? [y/n]: ")
                if another_entry.lower() == 'y':
                    print('Guardando...')
                    key_for_continue()
                    break
                elif another_entry.lower() == 'n':
                    print('Guardando... \nCampers agregados exitosamente!')
                    key_for_continue()
                    return None
                else:
                    print('Error, opción inválida')
        else:
            print('Camper no encontrado')
            key_for_continue()

    except ValueError as e:
        print(f"Error: {e}. Asegúrese de ingresar números en los campos que lo requieren.")

def agregar_trainer(name_area, position_area):
  while True:
    try:
        lista_trainers = load_trainers_json()
        lista_areas = load_areas_json()

        print(f'Trainers disponibles para {name_area}')
        for trainer in lista_trainers:
            if trainer.get('Estado del trainer') == 'disponible':
                for data in trainer:
                    print(data, ':', trainer[data])
                print('---------------------------')

        id_add = int(input(f'Ingrese el ID del Trainer que desea agregar a {name_area}: '))

        trainer_found = next((trainer for trainer in lista_trainers if trainer['Identificacion'] == id_add), None)

        if trainer_found:
            lista_areas[position_area][name_area]['Trainers id'].append(trainer_found)
            guardar_json(lista_areas, 'areas')
            print(f'Trainer con ID {id_add} agregado exitosamente al área {name_area}.')
        else:
            print('Trainer no encontrado o no disponible.')

    except ValueError as e:
        print(f"Error: {e}. Asegúrese de ingresar números en los campos que lo requieren.")
