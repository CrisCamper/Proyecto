import os
import json
from commons.utils import guardar_json

def load_areas_json(): # Funcion para cargar las areas disponibles
    try:
      with open(os.path.join("data", "areas.json"), 'r') as archivo_json:        
        lista_areas = json.load(archivo_json)
        return lista_areas
    except Exception as e:
      print(f"Error al cargar el archivo: {e}")

lista_areas = load_areas_json

def crear_area (): 
   areas= {
        'artemis':[{"id":["14214","12314"]}],
        'sputnik':[],
        'apolo':[]
        #len(areas["artemis"]["id"]) < 33
        #   append
        #elif len(areas["sputnik"]["id"]) < 33
        #elif len(areas["apolo"]["id"]) < 33
        #else
        #print("ESta llena, elija otra area")
    }