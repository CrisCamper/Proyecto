from commons.utils import key_for_continue
from bussines.campers import load_campers_json
from bussines.trainers import load_trainers_json

def campers_inscritos (): # Function inscribed camper list
    # load camper's list
    lista_campers = load_campers_json()

    print('Campers inscritos')
    print('---------------------------')
    # Find nscribed campers
    found_campers = [camper for camper in lista_campers if camper.get('Estado del camper') == 'inscrito']
    if found_campers:
      for camper in found_campers:
        for key, value in camper.items():
          print(f'{key}: {value}')
        print('---------------------------')
    key_for_continue()

def campers_aprobados(): # function aprobated camper list
   # load camper's list
    lista_campers = load_campers_json()

    print('Campers aprobados')
    print('---------------------------')
    # Find nscribed campers
    found_campers = [camper for camper in lista_campers if camper.get('Estado del camper') == 'aprobado']
    if found_campers:
      for camper in found_campers:
        for key, value in camper.items():
          print(f'{key}: {value}')
        print('---------------------------')
    key_for_continue()

def campers_reprobados_riesgo(): # Function reprobated/danger camper list
       # load camper's list
    lista_campers = load_campers_json()

    print('Campers reprobados/riesgo')
    print('---------------------------')
    # Find nscribed campers
    found_campers = [camper for camper in lista_campers if camper.get('Estado del camper') == 'reprobado/riesgo']
    if found_campers:
      for camper in found_campers:
        for key, value in camper.items():
          print(f'{key}: {value}')
        print('---------------------------')
    key_for_continue()

def trainers_list(): # function trainer list
    lista_trainers = load_trainers_json()
    print('Trainers en Campus')
    print('---------------------------')
    for trainer in lista_trainers:
        for data in trainer:
            print(data,':',trainer[data])
        print('---------------------------')
    key_for_continue()
 
def camper_trainer(): # function trainer & camper list
    lista_campers = load_campers_json()
    lista_trainers = load_trainers_json()

    print('Sputnik')
    name_room = 'sputnik (netcore)'

    print('CAMPERS')
    found_campers = [camper for camper in lista_campers if camper.get('Ruta') == name_room]
    if found_campers:
      for camper in found_campers:
        for key, value in camper.items():
          print(f'{key}: {value}')
        print('---------------------------')

    print('TRAINERS')
    found_trainers = [trainer for trainer in lista_trainers if trainer.get('Ruta') == name_room]
    if found_trainers:
      for trainer in found_trainers:
        for key, value in trainer.items():
          print(f'{key}: {value}')
        print('---------------------------')

    print('Artemis')
    name_room = 'artemis (nodejs)'

    print('CAMPERS')
    found_campers = [camper for camper in lista_campers if camper.get('Ruta') == name_room]
    if found_campers:
      for camper in found_campers:
        for key, value in camper.items():
          print(f'{key}: {value}')
        print('---------------------------')

    print('TRAINERS')
    found_trainers = [trainer for trainer in lista_trainers if trainer.get('Ruta') == name_room]
    if found_trainers:
      for trainer in found_trainers:
        for key, value in trainer.items():
          print(f'{key}: {value}')
        print('---------------------------')
   
    print('Apolo')
    name_room = 'apolo (java)'

    print('CAMPERS')
    found_campers = [camper for camper in lista_campers if camper.get('Ruta') == name_room]
    if found_campers:
      for camper in found_campers:
        for key, value in camper.items():
          print(f'{key}: {value}')
        print('---------------------------')

    print('TRAINERS')
    found_trainers = [trainer for trainer in lista_trainers if trainer.get('Ruta') == name_room]
    if found_trainers:
      for trainer in found_trainers:
        for key, value in trainer.items():
          print(f'{key}: {value}')
        print('---------------------------')
    key_for_continue()