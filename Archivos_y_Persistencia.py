# Gerardo Andre Fernandez Cruz
# Este es un programa en cual te podras convertir en el mejor maestro pokemon, ya que almacenaremos tus pokemones e incluso
# guardaremos sus estadisticas para que sepas cuales son las debilidades de cada uno mas facilmente 

# Importar modulos
import csv
import func_persistencia

# Declarar variables
seguir_en_programa = True
filas = []
archivo = 'Temario A.csv'

# Leer el archivo CSV
with open('Temario A.csv', mode='r') as pokes:
    leer = csv.reader(pokes)

# Programa principal
while seguir_en_programa == True:

    print("")
    print("### BIENVENIDO ###")
    print("¿Qué desea hacer?")
    print("1. Modificar el valor de la columna Tipo 2 en algun pokemon")
    print("2. Modificar el valor de la columna Generación en algun pokemon")
    print("3. Agregar un nuevo pokemon")
    print("4. Mostrar todos los elementos dentro del archivo")
    print("5. Ver reporte")
    print("6. Salir")
    print("")
    
    opcion = input("Seleccione una opción válida ")

    # Hacer que la opción elegida sea un dígito, y si no lo es, volver a ejecutar el menú
    if opcion.isdigit() == False:
        print("Seleccione un tipo de valor válido")
    else:
        opcion = int(opcion)
    
    # Opcion 1: Modificar el valor de la columna Tipo 2 en algun pokemon
    if opcion == 1:
        func_persistencia.modificar_tipo2()

    # Opcion 2: Modificar el valor de la columna Generación en algun pokemon
    if opcion == 2:
        func_persistencia.modificar_generacion()

    # Opcion 3: Agregar un nuevo pokemon
    if opcion == 3:
        func_persistencia.agregar_pokemon()
    
    # Opcion 4: Mostrar todos los elementos dentro del archivo
    if opcion == 4:
        with open('Temario A.csv', mode='r') as pokes:
            leer = csv.reader(pokes)
            for fila in leer:
                filas.append(fila)

    # Calcular el ancho máximo de cada columna
    column_widths = [max(len(cell) for cell in column) for column in zip(*filas)]

    # Crear una cadena de formato para alinear los datos en columnas
    column_format = ' | '.join('{{:<{}}}'.format(width) for width in column_widths)

    # Mostrar el contenido del archivo CSV en una tabla
    for fila in filas:
        print(column_format.format(*fila))

    # Opcion 5: Ver reporte
    if opcion == 5:
        func_persistencia.reporte(archivo)

    # Opcion 6: Salir
    if opcion == 6:
        seguir_en_programa = False
        print("Eso ha sido todo, vuelva pronto!")

    else:
        print("Seleccione una opción válida.")