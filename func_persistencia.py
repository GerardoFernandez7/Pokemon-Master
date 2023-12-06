import csv
from collections import Counter
archivo = 'Temario A.csv'

# Opcion 1: Modificar el valor de la columna Tipo 2 en algun pokemon
def modificar_tipo2():
    filas = []
    columna_modificar = 3

    # Leer el archivo CSV y almacenar las filas en una lista
    with open('Temario A.csv', mode='r+', newline='') as pokes:
        leer = csv.reader(pokes)
        for fila in leer:
            filas.append(fila)

    fila_modificar= int(input('Ingrese el numero de la fila en la cual desea modificar el valor del Tipo 2: '))
    nuevo_tipo2 = input('Ingrese el nuevo valor para Tipo 2: ')

    # Modificar el valor de la celda específica
    filas[fila_modificar][columna_modificar] = nuevo_tipo2

    # Escribir las filas modificadas en el archivo CSV
    with open('Temario A.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(filas)
    print("El tipo 2 de su Pokémon ha sido cambiado exitosamente! ")

# Opcion 2: Modificar el valor de la columna Generación en algun pokemon
def modificar_generacion():
    columna_modificar = 8
    filas = []

    # Leer el archivo CSV y almacenar las filas en una lista
    with open('Temario A.csv', mode='r+', newline='') as pokes:
        leer = csv.reader(pokes)
        for fila in leer:
            filas.append(fila)

    fila_modificar= int(input('Ingrese el numero de la fila en la cual desea modificar la Generacion: '))

    print("")
    print("1. Primera")
    print("2. Segunda")
    print("3. Tercera")
    print("4. Cuarta")
    print("5. Quinta")
    print("")
    nueva_generacion = input('Ingrese la Generacion deseada: ')

    if nueva_generacion.isdigit() == False:
                print("Seleccione un tipo de valor válido")
    else:
        nueva_generacion = int(nueva_generacion)

        if nueva_generacion == 1:
            nueva_generacion = 'Primera'
            print("Ha seleccionado Primera generacion")
            
        elif nueva_generacion == 2:
            nueva_generacion = 'Segunda'
            print("Ha seleccionado Segunda generacion")
   
        elif nueva_generacion == 3:
            nueva_generacion = 'Tercera'
            print("Ha seleccionado Tercera generacion")
       
        elif nueva_generacion == 4:
            nueva_generacion = 'Cuarta'
            print("Ha seleccionado Cuarta generacion")
        
        elif nueva_generacion == 5:
            nueva_generacion = 'Quinta'
            print("Ha seleccionado Quinta generacion")

        else:
            print("Seleccione un dígito válido.")

    # Modificar el valor de la celda específica
    filas[fila_modificar][columna_modificar] = nueva_generacion

        # Escribir las filas modificadas en el archivo CSV
    with open('Temario A.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(filas)
    print("La generación de su Pokémon ha sido cambiada exitosamente! ")

# Opcion 3: Agregar un nuevo pokemon
def agregar_pokemon():

    # Leer el archivo CSV y almacenar las filas en una lista
     with open('Temario A.csv', mode='r') as pokes:
        leer = csv.DictReader(pokes)
        fieldnames = leer.fieldnames

     new_poke = {
    'Numero' : int(input("Ingrese el numero del pokemon: ")),
    'Nombre' : input("Ingrese el nombre del pokemon: "),
    'Tipo 1' : input("Ingrese el tipo 1 de su pokemon: "),
    'Tipo 2' : input("Ingrese el tipo 2 de su pokemon: "),
    'HP' : int(input("Ingrese la cantidad de HP que tiene su pokemon: ")),
    'Ataque' : int(input("Ingrese la cantidad de ataque de su pokemon: ")),
    'Defensa' : int(input("Ingrese la cantidad de defensa de su pokemon: ")),
    'Velocidad' : int(input("Ingrese la cantidad de Velocidad de su pokemon: "))
    }
     
     
     while True:
        generacion = input("Ingrese la generacion de su pokemon (1-5): ")
        if generacion.isdigit() == False:
                print("Seleccione un tipo de valor válido")
        else:
         generacion = int(generacion)

        if generacion >= 1 and generacion <= 5:
            # Asignar el valor correspondiente a la llave 'Generacion'
            if generacion == 1:
                new_poke['Generacion'] = 'Primera'
            elif generacion == 2:
                new_poke['Generacion'] = 'Segunda'
            elif generacion == 3:
                new_poke['Generacion'] = 'Tercera'
            elif generacion == 4:
                new_poke['Generacion'] = 'Cuarta'
            else:
                new_poke['Generacion'] = 'Quinta'
            break
        else:
            print("Seleccione un dígito válido.")
     
    # Escribir la fila nueva en el archivo CSV
     with open('Temario A.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(new_poke)
     print("Su Pokémon ha sido añadido exitosamente!")

# Opcion 5: Ver reporte
def reporte(archivo):

    # Variables para almacenar la información del reporte
    max_hp = 0
    pokemon_max_hp = ''
    generaciones = []
    tipos = []
    max_velocidad = 0
    pokemon_max_velocidad = ''

    # Leer el contenido del archivo CSV
    with open('Temario A.csv', 'r') as file:
        leer = csv.DictReader(file)
        for fila in leer:
            
            # Calcular el Pokémon con mayor HP
            hp = int(fila['HP'])
            if hp > max_hp:
                max_hp = hp
                pokemon_max_hp = fila['Nombre']

            # Almacenar las generaciones y los tipos de Pokémon
            generaciones.append(fila['Generacion'])
            tipos.append(fila['Tipo 1'])

            # Calcular el Pokémon más rápido
            velocidad = int(fila['Velocidad'])
            if velocidad > max_velocidad:
                max_velocidad = velocidad
                pokemon_max_velocidad = fila['Nombre']

    # Calcular la generación con más Pokémon
    generacion_mas_pokemon = Counter(generaciones).most_common(1)[0][0]

    # Calcular el tipo de Pokémon favorito
    tipo_favorito = Counter(tipos).most_common(1)[0][0]

    # Mostrar el reporte al usuario
    print('Pokémon con mayor HP:', pokemon_max_hp)
    print('Generación con más Pokémon:', generacion_mas_pokemon)
    print('Tipo de Pokémon favorito:', tipo_favorito)
    print('Pokémon más rápido:', pokemon_max_velocidad)