from commons.utils import validar_opcion

def menu_principal():  # Menu principal
    print('*******<MENÚ>*******')
    print('* 1.-------Campers *')
    print('* 2.---------Salir *')
    print('********************')
    op = validar_opcion('Opción: ', 1, 2)
    return op  # this line to return the user's choice

def menu_campers(): # Menú campers
    print('************<CAMPERS>************')
    print('* 1.---------------CREAR CAMPER *')
    print('* 2.--------------LISTAR CAMPER *')
    print('* 3.-----------MODIFICAR CAMPER *')
    print('* 4.----------------------SALIR *')
    print('*********************************')
    op = validar_opcion('Opción: ',1,4)
    return op