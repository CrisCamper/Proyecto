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

# FUNCTIONS FOR DATA
def verificar_capacidad_area(name_area, lista_areas, position_area): # Function to verify the maximum capacity
  """
  Verifica si el número de campers asignados a Sputnik supera la capacidad máxima.
  :param lista_areas: Lista de áreas.
  :param position_area: Posición del área a verificar.
  """
  MAX_CAPACITY = 33
  current_campers = len(lista_areas[position_area][name_area]['Campers id'])
  if current_campers >= MAX_CAPACITY:
      print(f'La capacidad máxima de la sala ({MAX_CAPACITY} campers) ha sido alcanzada. No se pueden agregar más campers.')
      return True
  else:
      return False

def eliminar_camper_disponible(camper_id, lista_campers_disponibles): #Function to delete a camper of list
  """
  Removes a camper from the list of available campers.
  :param camper_id: ID of the camper to be removed.
  :param lista_campers_disponibles: List of available campers.
  """
  camper_to_remove = next((camper for camper in lista_campers_disponibles if camper['Identificacion'] == camper_id), None)
  if camper_to_remove:
    lista_campers_disponibles.remove(camper_to_remove)
    print(f'Camper con ID {camper_id} eliminado de la lista de campers disponibles.')
  else:
    print('Camper no encontrado en la lista de campers disponibles.')

def eliminar_trainer_disponible(trainer_id, lista_trainers_disponibles): #Function to delete a trainer of list
  """
  Removes a trainer from the list of available trainers.
  :param trainer_id: ID of the trainer to be removed.
  :param lista_trainers_disponibles: List of available trainers.
  """
  camper_to_remove = next((trainer for trainer in lista_trainers_disponibles if trainer['Identificacion'] == trainer_id), None)
  if camper_to_remove:
    lista_trainers_disponibles.remove(camper_to_remove)
    print(f'Trainer con ID {trainer_id} eliminado de la lista de trainers disponibles.')
  else:
    print('trainer no encontrado en la lista de trainers disponibles.')

# Lista de las areas de entrenamiento
lista_areas = [
  # Position 0
  {'sputnik': {'Campers id': []}},
  # Position 1
  {'sputnik': {'Trainers id': []}},
  # Position 2
  {'artemis': {'Campers id': []}},
  # Position 3
  {'artemis': {'Trainers id': []}},
  # Position 4
  {'apolo': {'Campers id': []}},
  # Position 5
  {'apolo': {'Trainers id': []}}
]
# load camper list
lista_campers_disponibles = load_campers_json() 
# Load trainer list
lista_trainers_disponibles = load_trainers_json()
# load areas list
lista_areas = load_areas_json()

def agregar_campers(name_area, position_area): # Function to fill a camper area with it name and position
  while True:
    try:
      if verificar_capacidad_area(name_area,lista_areas, position_area):
        return # If >33 left to function

      print(f'Campers disponibles para {name_area}')
      for camper in lista_campers_disponibles:
        if camper.get('Estado del camper') == 'aprobado':
          for data in camper:
            print(data, ':', camper[data])
          print('---------------------------')

      # Ask to id of camper
      id_add = int(input(f'Ingrese el id del Camper que desea agregar a {name_area}: '))
      camper_found = next((camper for camper in lista_campers_disponibles if camper['Identificacion'] == id_add and camper['Estado del camper'] == 'aprobado'), None)

      if camper_found:
        lista_areas[position_area][name_area]['Campers id'].append(camper_found)
        guardar_json(lista_areas, 'areas')
        eliminar_camper_disponible(id_add, lista_campers_disponibles)

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
        print('Camper no encontrado o no disponible')
        key_for_continue()

    except ValueError as e:
      print(f"Error: {e}. Asegúrese de ingresar números en los campos que lo requieren.")

def eliminar_camper(name_area,position_area): # Function to delete a camper
  while True:
    try:
      print(f'Campers en {name_area}')
      for camper in lista_areas[position_area][name_area]['Campers id']:
          for data in camper:
            print(data, ':', camper[data])
          print('---------------------------')
      # get the id of camper
      id_remove = int(input('Ingrese el id del camper que queire elimnar: '))
      camper_to_remove = next((camper for camper in lista_areas[position_area][name_area]['Campers id'] if camper['Identificacion'] == id_remove), None)

      if camper_to_remove:
          lista_areas[position_area][name_area]['Campers id'].remove(camper_to_remove)
          guardar_json(lista_areas, 'areas')
          print(f'Camper con ID {id_remove} eliminado exitosamente del área {name_area}.')
      else:
          print('Camper no encontrado en el área especificada.')
      
      while True:
        # Ask to user if he wants to add other camper
        another_delete = input('¿Desea eliminar otro camper? [y/n]: ')
        if another_delete.lower() == 'y':
          print('Guardando...')
          key_for_continue()
        elif another_delete.lower() == 'n':
          print('Guardando...')
          key_for_continue()
          return
        else:
           print('Opcion no reconocida')
           key_for_continue()

    except ValueError as e:
        print(f"Error: {e}. Asegúrese de ingresar números en los campos que lo requieren.")
        key_for_continue()

def listar_campers_area(name_area, position_area): # Function to list campers in a specific area
  try:
    lista_areas = load_areas_json()
    campers_info = lista_areas[position_area][name_area]['Campers id']
    print(f'Campers en el área {name_area}:')

    for camper in campers_info:
      for key, value in camper.items():
        print(key, ':', value)
      print('---------------------------')
    key_for_continue()

  except Exception as e:
    print(f"Error: {e}")

def agregar_trainer(name_area, position_area): # Function to add a trainer
  while True:
    try:
      lista_areas = load_areas_json()

      print(f'Trainers disponibles para {name_area}')
      for trainer in lista_trainers_disponibles:
        for data in trainer:
          print(data, ':', trainer[data])
        print('---------------------------')

      # Ask to Id of Trainer
      id_add = int(input(f'Ingrese el ID del Trainer que desea agregar a {name_area}: '))
      trainer_found = next((trainer for trainer in lista_trainers_disponibles if trainer['Identificacion'] == id_add), None)

      if trainer_found:
        lista_areas[position_area][name_area]['Trainers id'].append(trainer_found)
        guardar_json(lista_areas, 'areas')
        eliminar_trainer_disponible(id_add, lista_trainers_disponibles)
        while True:
          limpiar_pantalla()
          another_entry = input("¿Desea agregar otro Trainer? [y/n]: ")
          if another_entry.lower() == 'y':
            print('Guardando...')
            key_for_continue()
            break
          elif another_entry.lower() == 'n':
            print('Guardando... \nTrainers agregados exitosamente!')
            key_for_continue()
            return None
          else:
            print('Error, opción inválida')
            
      else:
        print('Trainer no encontrado o no disponible.')
        key_for_continue

    except ValueError as e:
      print(f"Error: {e}. Asegúrese de ingresar números en los campos que lo requieren.")

def eliminar_trainer(name_area, position_area): # Function to delete a trainer
  while True:
    try:
      print(f'Trainers en {name_area}')
      for trainer in lista_areas[position_area][name_area]['Trainers id']:
        for data in trainer:
          print(data, ':', trainer[data])
        print('---------------------------')
      # Get the id of trainer
      id_remove = int(input('Ingrese el id del trainer que quiere eliminar: '))
      trainer_to_remove = next((trainer for trainer in lista_areas[position_area][name_area]['Trainers id'] if trainer['Identificacion'] == id_remove), None)

      if trainer_to_remove:
        lista_areas[position_area][name_area]['Trainers id'].remove(trainer_to_remove)
        guardar_json(lista_areas, 'areas')
        print(f'Trainer con ID {id_remove} eliminado exitosamente del área {name_area}.')
      else:
        print('Trainer no encontrado en el área especificada.')

      while True:
        # Ask to user if he wants to add other camper
        another_delete = input('¿Desea eliminar otro camper? [y/n]: ')
        if another_delete.lower() == 'y':
          print('Guardando...')
          key_for_continue()
        elif another_delete.lower() == 'n':
          print('Guardando...')
          key_for_continue()
          return
        else:
          print('Opcion no reconocida')
          key_for_continue()
    except ValueError as e:
      print(f"Error: {e}. Asegúrese de ingresar números en los campos que lo requieren.")

def listar_trainers_area(name_area, position_area): # Function to list trainers in a specific area
  try:
    lista_areas = load_areas_json()
    trainers_info = lista_areas[position_area][name_area]['Trainers id']
    print(f'Trainers en el área {name_area}:')
    
    for trainer in trainers_info:
      for key, value in trainer.items():
        print(key, ':', value)
      print('---------------------------')
    key_for_continue()

  except Exception as e:
    print(f"Error: {e}")

# Save data in areas.json
guardar_json(lista_areas, 'areas')