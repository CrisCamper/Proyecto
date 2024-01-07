import os
import json
from commons.utils import guardar_json
from bussines.campers import lista_campers

def load_areas_json(): # Funcion para cargar las areas disponibles
    try:
      with open(os.path.join("data", "areas.json"), 'r') as archivo_json:        
        lista_areas = json.load(archivo_json)
        return lista_areas
    except Exception as e:
      print(f"Error al cargar el archivo: {e}")

def crear_area (): 
  areas
   
def llenar_areas():
    lista_areas = load_areas_json()
    for camper in lista_campers:
      if len(areas["artemis"]["id"]) < 33:
        areas = {
            'artemis': [camper['Identificacion']],
          }
        lista_areas.append(areas)

    guardar_json(lista_areas, 'areas')
    input('press')
#{"id":["14214","12314"]}
#len(areas["artemis"]["id"]) < 33
 #   append
 #elif len(areas["sputnik"]["id"]) < 33
 #elif len(areas["apolo"]["id"]) < 33
 #else
    #print("ESta llena, elija otra area")