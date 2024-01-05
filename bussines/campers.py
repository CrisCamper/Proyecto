from commons.utils import save_to_json, limpiar_pantalla

def crear_camper (): # Funcion para crear un nuevo camper
    lista_campers = []
    while True:        
        try:
            name = input('Ingrese nombre del Camper: ')
            last_names = input('Ingrese apellidos del camper: ')
            id = int(input('Ingrese Numero de identificacion: '))
            direction = input('Ingrese direccion del camper: ')
            attendant = input('Ingrese nombre del acudiente: ')
            contact = int(input('Numero de contacto: '))
            permanent_contact = int(input('Numero de telefono fijo [Puede ser el mismo de contacto]: '))
            state = input('Ingrese el estado del camper: ')

            camper = { # Creamos un diccionario con la informacion del camper
                'Nombre': name,
                'Apellidos': last_names,
                'Identificacion': id,
                'Direccion': direction,
                'Acudiente': attendant,
                'Numero de contacto': contact,
                'Telefono fijo': permanent_contact,
                'Estado del camper': state
            }

            lista_campers.append(camper)  # Agregamos el camper a la lista
            save_to_json(lista_campers)  # Guardamos la lista en JSON

            while True:
                limpiar_pantalla() # Limpiamos la pantalla
                another_entry = input("¿Desea agregar otro camper? (y/n): ")
                if another_entry.lower() == 'y':
                    print('Guardando...')
                    # Rompemos el bucle interno para entrar al principal
                    break
                elif another_entry.lower() == 'n':
                    print('Guardando...')
                    print('Campers guardados exitosamente!')
                    limpiar_pantalla() # limpiamos pantalla antes de pasar al menú principal
                    return camper
                else:
                    print('Opcion no reconocida :(')

        except ValueError as e:  # Capturamos la excepción específica para errores de valor
            print(f"Error: {e}. Asegúrese de ingresar números en los campos que lo requieren.")