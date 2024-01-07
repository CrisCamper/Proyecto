#programa que le permita llevar el seguimiento académico de todos los campers que se encuentran matriculados en el programa intensivo de programación.
#Registro de campers
from commons.utils import limpiar_pantalla, key_for_continue
from commons.menus import menu_principal, menu_campers, menu_trainers, menu_areas_entrenamiento,submenu_areas
from bussines.campers import registrar_camper,listar_campers, modificar_camper,inscribir_camper
from bussines.trainers import crear_trainer,listar_trainers, modificar_trainers
from bussines.areas import agregar_campers, eliminar_camper

#Functions
def campers(): # Funcion general de camper (abraca toda la parte logica que tiene que ver con campers)
    limpiar_pantalla()
    op = menu_campers()
    if op == 1:
        limpiar_pantalla()
        registrar_camper()
    elif op == 2:
        limpiar_pantalla()
        inscribir_camper()
    elif op == 3:
        limpiar_pantalla()
        listar_campers()
        key_for_continue()
    elif op == 4:
        limpiar_pantalla()
        modificar_camper()
        key_for_continue()
    elif op == 5:
        print('Saliendo...')

def trainers(): # Funcion general de trainer (abraca toda la parte logica que tiene que ver con trainers)
    limpiar_pantalla()
    op = menu_trainers()
    if op == 1:
        limpiar_pantalla()
        crear_trainer()
    elif op == 2:
        limpiar_pantalla()
        listar_trainers()
        key_for_continue()
    elif op == 3:
        limpiar_pantalla()
        modificar_trainers()
        key_for_continue()
    elif op == 4:
        pass

def areas (): # Function general of areas (It covers all the logical part that has to do with areas)
    limpiar_pantalla()
    op = menu_areas_entrenamiento()
    # If the option is SPUTNIK, i will show the sputnik's main
    if op == 1:
        limpiar_pantalla()
        op = submenu_areas('SPUTNIK')
        # if the option is add a camper to sputnik
        if op == 1: 
            agregar_campers('sputnik',0)
            key_for_continue()
        # If the options is delete a camper of sputnik
        elif op == 2:
            eliminar_camper('sputnik',0)
            key_for_continue()
    # If the option is ARTEMIS, i will show the artemi's main
    elif op == 2:
        limpiar_pantalla()
        op = submenu_areas('ARTEMIS')
        # if the option is add a camper to sputnik
        if op == 1:
            agregar_campers('artemis',2)
            key_for_continue()
        # If the options is delete a camper of sputnik
        elif op == 2: 
            eliminar_camper('artemis',2)
            key_for_continue()
    # If the option is APOLO, i will show the Apolo's main
    elif op == 3:
        limpiar_pantalla()
        op = submenu_areas('APOLO')
        # if the option is add a camper to apolo
        if op == 1:
            agregar_campers('apolo',4)
            key_for_continue()
        # If the options is delete a camper of apolo
        elif op == 2: 
            eliminar_camper('apolo',4)
            key_for_continue()
    elif op == 7:
        print('Saliendo..')

# start
while True:
    limpiar_pantalla()
    op = menu_principal()
    if op == 1:
        campers()
    elif op == 2:
        trainers()
    elif op == 3:
        areas()
    elif op == 4:
        break