from commons.utils import validar_opcion

def menu_principal():  # Menu principal
    print('*************<MENÚ>************')
    print('* 1.------------------CAMPERS *')
    print('* 2.-----------------TRAINERS *')
    print('* 3.------AREAS ENTRENAMIENTO *')
    print('* 4.--------------------SALIR *')
    print('*******************************')
    op = validar_opcion('Opción: ', 1, 4)
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

def menu_trainers(): # Menú trainers
    print('************<TRAINERS>************')
    print('* 1.---------------CREAR TRAINER *')
    print('* 2.--------------LISTAR TRAINER *')
    print('* 3.-----------MODIFICAR TRAINER *')
    print('* 4.-----------------------SALIR *')
    print('**********************************')
    op = validar_opcion('Opción: ',1,4)
    return op

def menu_areas_entrenamiento ():
    print('************<AREAS ENTRENAMIENTO>************')
    print('* 1.---------MOSTRAR AREAS DE ENTRENAMIENTO *')
    print('* 2.----------------------------------SALIR *')
    print('*********************************************')
    op = validar_opcion('Opción: ',1,2)
    return op