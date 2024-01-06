from commons.utils import validar_opcion

def menu_pricipal(): # Menu principal
    print('-----MENÚ-----')
    print('1.     Campers')
    print('1.       Salir')
    op = validar_opcion('Opción: ',1,1)
def menu_campers(): # Menú campers
    print('**********<CAMPERS>**********')
    print('1.               CREAR CAMPER')
    print('2.              LISTAR CAMPER')
    print('3.           MODIFICAR CAMPER')
    print('4.                      SALIR')
    op = validar_opcion('Opción: ',1,4)