import json
import os
from commons.utils import key_for_continue, guardar_json
from bussines.campers import load_campers_json
from bussines.trainers import load_trainers_json

def load_matriculas_json():
    try:
      with open(os.path.join("data", "matriculas.json"), 'r') as archivo_json:        
        lista_matriculas = json.load(archivo_json)
        return lista_matriculas
    except Exception as e:
      print(f"Error al cargar el archivo: {e}")

lista_matriculas = [
    # Position 0
    {'matricula (sputnik)': []},
    # Position 1
    {'matricula (apolo)': []},
    # Position 2
    {'matricula (artemis)': []},
]

def crear_matricula(): #Function create tution
    ## MATRICULA SPUTNIK
    lista_campers = load_campers_json()
    # Filtrar campers aprobados en la ruta 'sputnik (netcore)'
    campers_sputnik = [c for c in lista_campers if c.get('Estado del camper') == 'aprobado' and c.get('Ruta') == 'sputnik (netcore)']
    lista_trainers = load_trainers_json()
    # Filtrar trainers en la ruta 'sputnik (netcore)'
    trainers_sputnik = [t for t in lista_trainers if t.get('Ruta') == 'sputnik (netcore)']

    # Verificar si se encontró al menos un camper aprobado y un trainer
    if campers_sputnik and trainers_sputnik:
        matricula_sputnik = {
            "Camper": campers_sputnik,
            "Experto Encargado": trainers_sputnik,
            "Ruta de Entrenamiento": 'NetCore',
            "Fecha de Inicio": '01/01/2024',
            "Fecha de Finalización": '01/10/2024',
            "Salón de Entrenamiento": 'Sputnik'
        }

        # Agregar la matrícula a la lista de esa área
        lista_matriculas[0]['matricula (sputnik)'].append(matricula_sputnik)

    ## MATRICULA ARTEMIS
    lista_campers = load_campers_json()
    # Filtrar campers aprobados en la ruta 'apolo (java)'
    campers_apolo = [c for c in lista_campers if c.get('Estado del camper') == 'aprobado' and c.get('Ruta') == 'apolo (java)']
    # Filtrar trainers en la ruta 'sputnik (netcore)'
    trainers_apolo = [t for t in lista_trainers if t.get('Ruta') == 'apolo (java)']

    # Verificar si se encontró al menos un camper aprobado y un trainer
    if campers_apolo and trainers_apolo:
        matricula_apolo = {
            "Camper": campers_apolo,
            "Experto Encargado": trainers_apolo,
            "Ruta de Entrenamiento": 'Java',
            "Fecha de Inicio": '01/01/2024',
            "Fecha de Finalización": '01/10/2024',
            "Salón de Entrenamiento": 'Apolo'
        }

        # Agregar la matrícula a la lista de esa área
        lista_matriculas[1]['matricula (apolo)'].append(matricula_apolo)

    ## MATRICULA ARTEMIS
    lista_campers = load_campers_json()
    # Filtrar campers aprobados en la ruta 'apolo (java)'
    campers_artemis = [c for c in lista_campers if c.get('Estado del camper') == 'aprobado' and c.get('Ruta') == 'apolo (java)']
    # Filtrar trainers en la ruta 'sputnik (netcore)'
    trainers_artemis = [t for t in lista_trainers if t.get('Ruta') == 'sputnik (netcore)']

    # Verificar si se encontró al menos un camper aprobado y un trainer
    if campers_artemis and trainers_artemis:
        matricula_artemis = {
            "Camper": campers_artemis,
            "Experto Encargado": trainers_artemis,
            "Ruta de Entrenamiento": 'NodeJs',
            "Fecha de Inicio": '01/01/2024',
            "Fecha de Finalización": '01/10/2024',
            "Salón de Entrenamiento": 'Artemis'
        }

        # Agregar la matrícula a la lista de esa área
        lista_matriculas[2]['matricula (artemis)'].append(matricula_artemis)

    # Guardar la lista de matrículas en un archivo JSON
    guardar_json(lista_matriculas, 'matriculas')

    key_for_continue()

def ver_matriculas(): # Function show tutions
    for i, matricula_area in enumerate(lista_matriculas):
        for key, matriculas in matricula_area.items():
            print(f'{key}:')
            for matricula in matriculas:
                print(f'  - Camper: {matricula["Camper"]}')
                print(f'    Experto Encargado: {matricula["Experto Encargado"]}')
                print(f'    Ruta de Entrenamiento: {matricula["Ruta de Entrenamiento"]}')
                print(f'    Fecha de Inicio: {matricula["Fecha de Inicio"]}')
                print(f'    Fecha de Finalización: {matricula["Fecha de Finalización"]}')
                print(f'    Salón de Entrenamiento: {matricula["Salón de Entrenamiento"]}')
                print('---------------------------')
