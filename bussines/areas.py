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
def verificar_capacidad_campers(name_area,lista_areas, position_area): # function to verify max capacity campers
    """
    Verifica si el número de campers asignados a Sputnik supera la capacidad máxima.
    :param lista_areas: Lista de áreas.
    :param position_area: Posición del área a verificar.
    """
    max_capacity = 33
    current_campers = len(lista_areas[position_area][name_area]['Campers id'])

    if current_campers >= max_capacity:
        print(f'La capacidad máxima de {name_area} ({max_capacity} campers) ha sido alcanzada. No se pueden agregar más campers.')
        return True
    else:
        return False
    
def verificar_capacidad_trainers(name_area,lista_areas, position_area):# function to verify max capacity trainers
  """
  Verifica si el número de campers asignados a Sputnik supera la capacidad máxima.
  :param lista_areas: Lista de áreas.
  :param position_area: Posición del área a verificar.
  """
  max_capacity = 1
  current_campers = len(lista_areas[position_area][name_area]['Trainers id'])
  if current_campers >= max_capacity:
    print(f'La capacidad máxima de {name_area} ({max_capacity} trainers) ha sido alcanzada. No se pueden agregar más trainers.')
    return True
  else:
    return False

# Lista de las areas de entrenamiento
lista_areas = [
  # Position 0
  {'sputnik (netcore)': {'Campers id': []}},
  # Position 1
  {'sputnik (netcore)': {'Trainers id': []}},
  # Position 2
  {'artemis (nodejs)': {'Campers id': []}},
  # Position 3
  {'artemis (nodejs)': {'Trainers id': []}},
  # Position 4
  {'apolo (java)': {'Campers id': []}},
  # Position 5
  {'apolo (java)': {'Trainers id': []}}
]
# load camper list
lista_campers_disponibles = load_campers_json()
# Load trainer list
lista_trainers_disponibles = load_trainers_json()
# Save data in areas.json
guardar_json(lista_areas, 'areas')
# load areas list
lista_areas = load_areas_json()

def agregar_campers(name_area, position_area):
  lista_areas = load_areas_json()
  lista_campers_disponibles = load_campers_json()

  while True:
    try:    
      if verificar_capacidad_campers(name_area, lista_areas, position_area):
        return
      
      print(f'Campers disponibles para {name_area}')
      found_campers = [camper for camper in lista_campers_disponibles if camper.get('Estado del camper') == 'aprobado' and camper.get('Ruta') == 'none']
      if found_campers:
        for camper in found_campers:
          for key, value in camper.items():
            print(f'{key}: {value}')
          print('---------------------------')

        id_add = int(input(f'Ingrese el id del Camper que desea agregar a {name_area}: '))
        camper_found = next((camper for camper in found_campers if camper['Identificacion'] == id_add), None)
        if camper_found:
          # Add the camper to the specified area
          lista_areas[position_area][name_area]['Campers id'].append(camper_found)
          # Update the camper's 'Ruta' in the original list
          for camper in lista_campers_disponibles:
            if camper['Identificacion'] == id_add:
              camper['Ruta'] = name_area
          # Save the modified lists to JSON files
          guardar_json(lista_campers_disponibles, 'campers')
          guardar_json(lista_areas, 'areas')
          # Remove the camper from the available campers
          print(f'Camper con ID {id_add} agregado exitosamente al área {name_area}.')
          key_for_continue()
          break
        else:
          print('Camper no encontrado.')
      else:
        print('No se encontraron campers para el área especificada.')
        key_for_continue()
        break
    except ValueError as e:
      print(f"Error: {e}. Asegúrese de ingresar números en los campos que lo requieren.")
      key_for_continue()    

def listar_campers_area(name_area):
  lista_campers = load_campers_json()
  campers_encontrados = [camper for camper in lista_campers if camper.get('Ruta') == name_area]
  if campers_encontrados:
      print(f'Campers en el área {name_area}:')
      for camper in campers_encontrados:
          for key, value in camper.items():
              print(f'{key}: {value}')
          print('---------------------------')
          key_for_continue()

  else:
      print(f'No se encontraron campers en el área {name_area}.')
      key_for_continue()

def agregar_trainer(name_area, position_area): # Function to add a trainer

  lista_areas = load_areas_json()
  lista_trainers_disponibles = load_trainers_json()
  while True:
    try:
      if verificar_capacidad_trainers(name_area,lista_areas, position_area):
        return # If >33 left to function

      found_trainer = next((trainer for trainer in lista_trainers_disponibles if trainer['Ruta'] == name_area), None)
      if found_trainer:
        print('Trainers Disponibles')
        for key, value in found_trainer.items():
          print(f'{key}: {value}')
        print('---------------------------')
      else:
        print('No se encontraron entrenadores para el área especificada.')
      # Ask to Id of Trainer

      id_add = int(input(f'Ingrese el ID del Trainer que desea agregar a {name_area}: '))
      trainer_found = next((trainer for trainer in lista_trainers_disponibles if trainer['Identificacion'] == id_add), None)

      if trainer_found:
        
        lista_areas[position_area][name_area]['Trainers id'].append(trainer_found)
        guardar_json(lista_areas, 'areas')

      else:

        print('Trainer no encontrado o no disponible.')  
        key_for_continue()

    except ValueError as e:
      print(f"Error: {e}. Asegúrese de ingresar números en los campos que lo requieren.")
      key_for_continue()

def listar_trainers_area(name_area):
  try:
    area_info = next((area[name_area] for area in lista_areas if name_area in area), {})
    trainers_info = area_info.get("Trainers id", [])
    
    if trainers_info:
      print(f'Trainers en el área {name_area}:')
      for trainer in trainers_info:
        for key, value in trainer.items():
          print(key, ':', value)
        print('---------------------------')
      key_for_continue()
    else:
      print(f'No se encontraron trainers en el área {name_area}.')
    key_for_continue()
  except StopIteration:
    print(f'No se encontró el área {name_area} o no tiene trainers.')
