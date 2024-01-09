from commons.utils import key_for_continue, validar_opcion

def menu_principal():  # Menu principal
    print('*************<MENÚ>************')
    print('* 1.------------------CAMPERS *')
    print('* 2.-----------------TRAINERS *')
    print('* 3.------AREAS ENTRENAMIENTO *')
    print('* 4.-----------------REPORTES *')
    print('* 5.-------------- MATRICULAS *')
    print('* 6.--------------------SALIR *')
    print('*******************************')
    op = validar_opcion('Opción: ', 1, 6)
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
    print('* 4.-----------INFO. AREAS DE ENTRENAMIENTO *')
    print('* 5.----------------------------------SALIR *')
    print('*********************************************')
    op = validar_opcion('Opción: ',1,5)
    return op

def submenu_areas(name_area): # Submain of main train area´s
    print(f'******[¡BIENVENIDO A {name_area}!]******')
    print('* 1.----------------AGREGAR CAMPER *')
    print('* 2.----------------LISTAR CAMPERS *')
    print('* 3.---------------AGREGAR TRAINER *')
    print('* 4.---------------LISTAR TRAINERS *')
    print('* 5.-------------------------SALIR *')
    print('************************************')
    op = validar_opcion('Opción: ',1,5)
    return op

def info_area(): # Function to see the info routes
    print("Cada ruta tiene módulos específicos relacionados con diferentes tecnologías y áreas de programación. \nAdemás, cada ruta tiene un Sistema de Gestión de Bases de Datos (SGDB) principal y un alternativo. Aquí hay una breve descripción de cada ruta")


    print("Ruta NodeJS:")
    print("- Fundamentos de programación")
    print("- Programación Web")
    print("- Programación formal (JavaScript)")
    print("- Bases de datos (MongoDb)")
    print("- Backend (NodeJS)")

    print("\nRuta Java:")
    print("- Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)")
    print("- Programación Web")
    print("- Programación formal (Java)")
    print("- Bases de datos (Mysql)")
    print("- Backend (Spring Boot)")

    print("\nRuta NetCore:")
    print("- Fundamentos de programación")
    print("- Programación Web")
    print("- Programación formal (C#)")
    print("- Bases de datos (Postgresql)")
    print("- Backend (NetCore)")
    key_for_continue()
    return

def menu_reportes ():# main reports
    print('******************[REPORTES]*****************')
    print('* 1.----------------------CAMPERS INSCRITOS *')
    print('* 2.----------------------CAMPERS APROBADOS *')
    print('* 3.--------------CAMPERS REPROBADOS/RIESGO *')
    print('* 4.-------------------------------TRAINERS *')
    print('* 5.------------CAMPERS & TRAINERS EN COMUN *')
    print('* 6.----------------------------------SALIR *')
    print('*********************************************')
    op = validar_opcion('Opción: ',1,6)
    return op

def menu_matriculas (): # main tutions
    print('****************[MATRICULAS]***************')
    print('* 1.----------------------CREAR MATRICULA *')
    print('* 2.-----------------------VER MATRICULAS *')
    print('* 3.--------------------------------SALIR *')
    print('*******************************************')
    op = validar_opcion('Opción: ',1,3)
    return op
