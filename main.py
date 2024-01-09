#programa que le permita llevar el seguimiento académico de todos los campers que se encuentran matriculados en el programa intensivo de programación.
#Registro de campers
from commons.utils import limpiar_pantalla, key_for_continue
from commons.menus import *
from bussines.campers import registrar_camper, listar_campers, modificar_camper, inscribir_camper
from bussines.trainers import crear_trainer, listar_trainers, modificar_trainers
from bussines.areas import agregar_campers, listar_campers_area, agregar_trainer, listar_trainers_area
from bussines.reportes import campers_inscritos, campers_aprobados, campers_reprobados_riesgo, trainers_list, camper_trainer
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
        name_area = 'sputnik (netcore)' # Authomatizy code
        # if the option is add a camper to sputnik
        if op == 1: 
            limpiar_pantalla()
            agregar_campers(name_area,0)
        # If the option is list campers of sputnik
        elif op == 2:
            limpiar_pantalla()
            listar_campers_area(name_area)
        ## TRAINERS
        # If option is add trainer
        elif op == 3: 
            limpiar_pantalla()
            agregar_trainer(name_area,1)
        # list trainer
        elif op == 4:
            limpiar_pantalla()
            listar_trainers_area(name_area)
        # exit
        elif op == 5:
            print('Saliendo...')
    # If the option is ARTEMIS, i will show the artemi's main
    elif op == 2:
        limpiar_pantalla()
        op = submenu_areas('ARTEMIS')
        name_area = 'artemis (nodejs)' # Authomatizy code
        # add campers
        if op == 1: 
            limpiar_pantalla()
            agregar_campers(name_area,2)
        # list campers
        elif op == 2:
            limpiar_pantalla()
            listar_campers_area(name_area)
        ## TRAINERS
        # If option is add trainer
        elif op == 3: 
            limpiar_pantalla()
            agregar_trainer(name_area,3)
        # list trainer
        elif op == 4:
            limpiar_pantalla()
            listar_trainers_area(name_area,3)
        # Exit
        elif op == 5:
            print('Saliendo...')
    # If the option is APOLO, i will show the apolo's main
    elif op == 3:
        limpiar_pantalla()
        op = submenu_areas('APOLO')
        name_area = 'apolo (java)' # Authomatizy code
        # if the option is add a camper to apolo
        if op == 1: 
            limpiar_pantalla()
            agregar_campers(name_area,4)
        # If the option is list campers of apolo
        elif op == 2:
            limpiar_pantalla()
            listar_campers_area(name_area,4)
        ## TRAINERSi
        # If option is add trainer
        elif op == 3: 
            limpiar_pantalla()
            agregar_trainer(name_area,5)
        # If option is list trainers
        elif op == 4:
            limpiar_pantalla()
            listar_trainers_area(name_area)
        # If option is exit
    elif op == 4:
        # menu info areas
        limpiar_pantalla()
        info_area()
    elif op == 5:
        print('Saliendo...')

def reportes():
    limpiar_pantalla()
    op = menu_reportes()
    # inscribied campers
    if op == 1:
        limpiar_pantalla()
        campers_inscritos()
    # aprobated campers
    elif op == 2:
        limpiar_pantalla()
        campers_aprobados()
    # reprobateed/Danger camper list
    elif op == 3:
        limpiar_pantalla()
        campers_reprobados_riesgo()
    # Trainer list
    elif op == 4:
        limpiar_pantalla()
        trainers_list()
    # Camper & trainer list
    elif op == 5:
        limpiar_pantalla()
        camper_trainer()
    elif op == 6:
        print('Saliendo...')


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
        reportes()
    elif op == 5:
        break