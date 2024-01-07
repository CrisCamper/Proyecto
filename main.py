#programa que le permita llevar el seguimiento académico de todos los campers que se encuentran matriculados en el programa intensivo de programación.
#Registro de campers
from commons.utils import limpiar_pantalla
from commons.menus import menu_principal, menu_campers, menu_trainers
from bussines.campers import crear_camper,listar_campers, modificar_camper
from bussines.trainers import crear_trainer,listar_trainers, modificar_trainers

#Functions
def campers(): # Funcion general de camper (abraca toda la parte logica que tiene que ver con campers)
    limpiar_pantalla()
    op = menu_campers()
    if op == 1:
        limpiar_pantalla()
        crear_camper()
        limpiar_pantalla()
    elif op == 2:
        limpiar_pantalla()
        listar_campers()
        input('[Presione cualquier tecla para continuar]')
        limpiar_pantalla()
    elif op == 3:
        limpiar_pantalla()
        modificar_camper()
        input('[Presione cualquier tecla para continuar]')
        limpiar_pantalla()
    elif op == 4:
        print('Saliendo...')
        limpiar_pantalla()

def trainers(): # Funcion general de trainer (abraca toda la parte logica que tiene que ver con trainers)
    limpiar_pantalla()
    op = menu_trainers()
    if op == 1:
        limpiar_pantalla()
        crear_trainer()
        limpiar_pantalla()
    elif op == 2:
        limpiar_pantalla()
        listar_trainers()
        input('[Presione cualquier tecla para continuar]')
        limpiar_pantalla()
    elif op == 3:
        limpiar_pantalla()
        modificar_trainers()
        input('[Presione cualquier tecla para continuar]')
        limpiar_pantalla()
    elif op == 4:
        print('Saliendo...')
        limpiar_pantalla()

# start
while True:
    op = menu_principal()
    if op == 1:
        campers()
    elif op == 2:
        trainers()
    elif op == 4:
        break