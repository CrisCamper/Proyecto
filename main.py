#programa que le permita llevar el seguimiento académico de todos los campers que se encuentran matriculados en el programa intensivo de programación.
#Registro de campers
from commons.utils import limpiar_pantalla
from commons.menus import menu_pricipal, menu_campers
from bussines.campers import crear_camper

while True:
    menu_pricipal()
    if 1:
        limpiar_pantalla()
        menu_campers()
        if 1:
            limpiar_pantalla()
            crear_camper()