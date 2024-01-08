#programa que le permita llevar el seguimiento académico de todos los campers que se encuentran matriculados en el programa intensivo de programación.
#Registro de campers
from commons.utils import limpiar_pantalla, key_for_continue
from commons.menus import menu_principal, menu_campers, menu_trainers, menu_areas_entrenamiento,submenu_areas
from bussines.campers import registrar_camper, listar_campers, modificar_camper, inscribir_camper
from bussines.trainers import crear_trainer, listar_trainers, modificar_trainers
from bussines.areas import agregar_campers, eliminar_camper, listar_campers_area, agregar_trainer, eliminar_trainer, listar_trainers_area

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
        name_area = 'sputnik' # Authomatizy code
        # if the option is add a camper to sputnik
        if op == 1: 
            limpiar_pantalla()
            agregar_campers(name_area,0)
            
        # If the options is delete a camper of sputnik
        elif op == 2:
            limpiar_pantalla()
            eliminar_camper(name_area,0)
        # If the option is list campers of sputnik
        elif op == 3:
            limpiar_pantalla()
            listar_campers_area(name_area,0)
           
        ## TRAINERS
        # If option is add trainer
        elif op == 4: 
            limpiar_pantalla()
            agregar_trainer(name_area,1)
            
        # If the options is delete a trainers of sputnik
        elif op == 5:
            limpiar_pantalla()
            eliminar_trainer(name_area,1)
            
        # If the option is list trainers of sputnik
        elif op == 6:
            limpiar_pantalla()
            listar_trainers_area(name_area,1)

        elif op == 7:
            print('Saliendo...')
    # If the option is ARTEMIS, i will show the artemi's main
    elif op == 2:
        limpiar_pantalla()
        op = submenu_areas('ARTEMIS')
        name_area = 'artemis' # Authomatizy code
        # if the option is add a camper to artemis
        if op == 1: 
            limpiar_pantalla()
            agregar_campers(name_area,2)
 
        # If the options is delete a camper of artemis
        elif op == 2:
            limpiar_pantalla()
            eliminar_camper(name_area,2)

        # If the option is list campers of artemis
        elif op == 3:
            limpiar_pantalla()
            listar_campers_area(name_area,2)

        ## TRAINERS
        # If option is add trainer
        elif op == 4: 
            limpiar_pantalla()
            agregar_trainer(name_area,3)

        # If the options is delete a trainers of artemis
        elif op == 5:
            limpiar_pantalla()
            eliminar_trainer(name_area,3)

        # If the option is list trainers of artemis
        elif op == 6:
            limpiar_pantalla()
            listar_trainers_area(name_area,3)

        elif op == 7:
            print('Saliendo...')
    elif op == 3:
        limpiar_pantalla()
        op = submenu_areas('APOLO')
        name_area = 'apolo' # Authomatizy code
        # if the option is add a camper to apolo
        if op == 1: 
            limpiar_pantalla()
            agregar_campers(name_area,4)

        # If the options is delete a camper of apolo
        elif op == 2:
            limpiar_pantalla()
            eliminar_camper(name_area,4)

        # If the option is list campers of apolo
        elif op == 3:
            limpiar_pantalla()
            listar_campers_area(name_area,4)

        ## TRAINERSi
        # If option is add trainer
        elif op == 4: 
            limpiar_pantalla()
            agregar_trainer(name_area,5)

        # If the options is delete a trainers of apolo
        elif op == 5:
            limpiar_pantalla()
            eliminar_trainer(name_area,5)

        # If the option is list trainers of apolo
        elif op == 6:
            limpiar_pantalla()
            listar_trainers_area(name_area,5)

        elif op == 7:
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
        break