#programa que le permita llevar el seguimiento académico de todos los campers que se encuentran matriculados en el programa intensivo de programación.
#Registro de campers
from commons.utils import limpiar_pantalla
from commons.menus import menu_principal, menu_campers
from bussines.campers import crear_camper,listar_campers, modificar_camper

#Functions
def campers():
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

# start
while True:
    op = menu_principal()
    if op == 1:
        campers()
    elif op == 2:
        break