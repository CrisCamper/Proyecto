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
    print('* 1.-----------REGISTRAR CAMPER *')
    print('* 2.-----------INSCRIBIR CAMPER *')
    print('* 3.--------------LISTAR CAMPER *')
    print('* 4.-----------MODIFICAR CAMPER *')
    print('* 5.----------------------SALIR *')
    print('*********************************')
    op = validar_opcion('Opción: ',1,5)
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

def menu_areas_entrenamiento (): # Main train area´s
    print('************<AREAS ENTRENAMIENTO>************')
    print('* 1.--------------------------------SPUTNIK *')
    print('* 2.--------------------------------ARTEMIS *')
    print('* 3.----------------------------------APOLO *')
    print('* 4.----------------------------------SALIR *')
    print('*********************************************')
    op = validar_opcion('Opción: ',1,4)
    return op

def submenu_areas(name_area): # Submain of main train area´s
    print(f'******[¡BIENVENIDO A {name_area}!]******')
    print('* 1.----------------AGREGAR CAMPER *')
    print('* 2.---------------ELIMINAR CAMPER *')
    print('* 3.----------------LISTAR CAMPERS *')
    print('* 4.---------------AGREGAR TRAINER *')
    print('* 5.--------------ELIMINAR TRAINER *')
    print('* 6.---------------LISTAR TRAINERS *')
    print('* 7.-------------------------SALIR *')
    print('************************************')
    op = validar_opcion('Opción: ',1,7)
    return op
