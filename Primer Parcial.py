import json
import re
import csv
import os


def clearconsole():
    """
    La función "clearconsole" borra la pantalla de la consola y espera a que continúe la entrada del
    usuario.
    """
  
    _= input('Presione enter para continuar...')
    os.system('cls')

def imprimir_menu():
    """
    Esta función imprime un menú con 21 opciones para un programa de estadísticas de baloncesto.
    """

    print("Menú de opciones:")
    print("1. Mostrar la lista de todos los jugadores del Dream Team")
    print("2. Seleccionar un jugador por su índice y mostrar sus estadísticas completas")
    print("3. Mostrar estadisticas de un jugador y guardarlas en un archivo CSV")
    print("4. Buscar un jugador por su nombre y mostrar sus logros")
    print("5. Mostrar el promedio de puntos por partido del Dream Team (ordenado por nombre ascendente) ")
    print("6. Buscar jugador en el Salón de la Fama del Baloncesto")
    print("7. Mostrar el jugador con la mayor cantidad de rebotes totales")
    print("8. Mostrar el jugador con el mayor porcentaje de tiros de campo")
    print("9. Mostrar el jugador con la mayor cantidad de asistencias totales")
    print("10. Buscar y mostrar los jugadores que han promediado más puntos por partido")
    print("11. Buscar y mostrar los jugadores que han promediado más rebotes por partido")
    print("12. Buscar y mostrar los jugadores que han promediado más asistencias por partido ")
    print("13. Mostrar el jugador con la mayor cantidad de robos totales")   
    print("14. Mostrar el jugador con la mayor cantidad de bloqueos totales")
    print("15. Buscar y mostrar los jugadores que hayan tenido un porcentaje de tiros libres")
    print("16. Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos")
    print("17. Mostrar el jugador con la mayor cantidad de logros obtenidos")
    print("18. Buscar y mostrar los jugadores que hayan tenido un porcentaje de tiros triples ")    
    print("19. Mostrar el jugador con la mayor cantidad de temporadas jugadas")
    print("20. Buscar y mostrar los jugadores, ordenados por posición en la cancha, segun porcentaje de tiros de campo ")   
    print("21. Salir")

def validar_menu_principal():
    """
    Esta función valida la entrada del usuario para la opción del menú principal comprobando si es un
    número.
    :return: ya sea la entrada del usuario (si es un entero válido) o -1 (si la entrada no es un entero
    válido).
    """
    
    imprimir_menu()

    opcion = input("\nIngrese la opción deseada: ")
    validacion = r'([0-9]+)'

    if re.search(validacion,opcion):
        return opcion
    else:
        return -1

def cargar_menu_principal(lista:list):
    """
    Esta función contiene un menú con varias opciones que realizan diferentes operaciones en una lista
    dada.
    
    :param lista: El parámetro "lista" es una lista de jugadores de baloncesto, cada uno representado
    como un diccionario con claves como "nombre" (nombre), "edad" (edad), "equipo" (equipo) y varias
    estadísticas como "puntos_por_partido" (puntos por juego) y "rebotes_totales", etc.
    :type lista: list
    """

    while True:        
        opcion = validar_menu_principal()
    
        if opcion == "1":
            mostrar_jugador(lista)
        
        elif opcion == "2":
            print(mostrar_estadisticas(lista))
            
        elif opcion == "3":
            guardar_csv_jugador(lista)

        elif opcion == "4":
            print(buscar_jugador_nombre(lista)) 

        elif opcion == "5":
            print(calcular_ordenar_por_promedio_puntos_partido(lista))

        elif opcion == "6":
            print(buscar_miembro_salon_fama(lista))

        elif opcion == "7":
            calcular_mayor_estadistica(lista,"rebotes_totales")
        
        elif opcion == "8":
            calcular_mayor_estadistica(lista,"porcentaje_tiros_de_campo")
            
        elif opcion == "9":
            calcular_mayor_estadistica(lista,"asistencias_totales")

        elif opcion == "10":
            print(mostrar_jugador_mayor_al_promedio(lista,"promedio_puntos_por_partido"))

        elif opcion == "11":
            print(mostrar_jugador_mayor_al_promedio(lista,"promedio_rebotes_por_partido"))

        elif opcion == "12":
            print(mostrar_jugador_mayor_al_promedio(lista,"promedio_asistencias_por_partido"))

        elif opcion == "13":
            calcular_mayor_estadistica(lista,"robos_totales")
        
        elif opcion == "14":
            calcular_mayor_estadistica(lista,"bloqueos_totales")
            
        elif opcion == "15":
            print(mostrar_jugador_mayor_al_promedio(lista,"porcentaje_tiros_libres"))

        elif opcion == "16":
            print(calcular_promedio_excluyente(lista))

        elif opcion == "17":
            calcular_mayor_logros(lista)

        elif opcion == "18":
            print(mostrar_jugador_mayor_al_promedio(lista,"porcentaje_tiros_triples"))

        elif opcion == "19":
            calcular_mayor_estadistica(lista,"temporadas")

        elif opcion == "20":
            ordenar_por_posicion_tiros_de_campo(lista)

        elif opcion == "21":
            break

        else:
            print("Opción inválida. Intente de nuevo.")

        clearconsole()

def abrir_json(archivo_json):
    """
    Esta función lee un archivo JSON y devuelve su contenido como un diccionario.
    
    :param archivo_json: El parámetro "archivo_json" es una cadena que representa la ruta del archivo
    JSON que queremos abrir y leer
    :return: un objeto de diccionario que se obtiene al leer un archivo JSON.
    """

    # Leer el archivo JSON -> load devuelve un diccionario
    with open(archivo_json) as harry_potter_personajes:
        data = json.load(harry_potter_personajes)
    return data

def guardar_archivo_csv(string:str,formato:dict):
    """
    Esta función guarda un diccionario en formato CSV con un nombre de archivo determinado.
    
    :param string: Una cadena que representa el nombre del archivo que se va a crear
    :type string: str
    :param formato: El parámetro "formato" es un diccionario que contiene los datos que se escribirán en
    el archivo CSV. Las claves del diccionario representan los encabezados de las columnas y los valores
    representan los datos de cada columna
    :type formato: dict
    :return: un valor booleano, ya sea True o False, según si el archivo se creó correctamente o no.
    """
   
    nombre_archivo = "{0}.csv".format(string)

    with open(nombre_archivo, "w+") as file:
        escritor_csv = csv.writer(file)

        escritor_csv.writerow(formato.keys())

        escritor_csv.writerow(formato.values())

    if escritor_csv != None:
        print("Se creó el archivo: archivo.csv")
        return True
    else:
        print("‘Error al crear el archivo: archivo.csv")
        return False


dict_equipo = abrir_json(r'C:\Users\usuario\Documents\Programacion I\EXAMEN\dt.json')

lista_nba = dict_equipo["jugadores"]


def mostrar_jugador(lista:list):
    """
    La función "mostrar_jugador" toma una lista de diccionarios que contienen información del jugador e
    imprime su nombre y posición.
    
    :param lista: El parámetro "lista" es una lista de diccionarios, donde cada diccionario representa a
    un jugador y contiene información sobre su nombre y posición
    :type lista: list
    """

    for jugador in lista:
        if len(lista) >= 1:
            mensaje = ("{0} - Posicion: {1}".format(jugador["nombre"],jugador["posicion"]))
            print(mensaje)

def mostrar_estadisticas(lista:list):
    """
    Esta función toma una lista de jugadores de la NBA y una característica específica, solicita al
    usuario que seleccione un jugador de la lista y devuelve el valor de la característica elegida por
    el jugador seleccionado.
    
    :param lista: La lista de jugadores de la NBA y sus estadísticas
    :type lista: list
    :param caracteristica: El parámetro "caracteristica" es una cadena que representa la estadística o
    característica específica de un jugador de baloncesto que el usuario quiere ver. Por ejemplo, podría
    ser "puntos por partido", "rebotes por partido", "asistencias por partido", etc
    :type caracteristica: str
    :return: ya sea el valor de la característica especificada del jugador elegido o un mensaje de error
    si el índice elegido no es válido.
    """
    
    
    indice = -1
    validacion = r'([0-9]+)'
    mensaje_error = "Error, el indice indicado no es correcto."

    for jugador in lista_nba:
        if len(lista) >= 1:
            indice += 1
            print("{0} {1}".format(indice,jugador["nombre"]))

    opcion = input("Ingrese el indice del jugador para mostrar sus caracteristicas: ")

    if opcion.isdigit():
        if re.match(validacion,opcion):
            opcion_elegida = int(opcion)
            if opcion_elegida < len(lista) and len(lista) >= 1:
                for jugador in lista:
                    dict_jugador_elegido = lista[opcion_elegida]["estadisticas"]
                    dict_jugador_elegido["nombre"] = lista[opcion_elegida]["nombre"]
                    dict_jugador_elegido["posicion"] = lista[opcion_elegida]["posicion"]
                    return dict_jugador_elegido
            else:
                return mensaje_error
    else:
        return mensaje_error

def guardar_csv_jugador(lista:list):
    """
    Esta función guarda las estadísticas de un jugador elegido de una lista de jugadores en un archivo
    CSV.
    
    :param lista: una lista de diccionarios, donde cada diccionario representa un jugador y sus
    estadísticas
    :type lista: list
    """
    
    dict_jugador_elegido = mostrar_estadisticas(lista)
    for jugador in lista:
        if dict_jugador_elegido == jugador["estadisticas"]:
            nombre_jugador = jugador["nombre"]
            guardar_archivo_csv("estadisticas_{0}".format(nombre_jugador),dict_jugador_elegido)
        else:
            continue

def buscar_jugador_nombre(lista:list):
    """
    Esta función toma una lista de jugadores y solicita al usuario que ingrese el nombre de un jugador,
    luego devuelve el nombre y los logros del jugador o un mensaje de error si el nombre no es válido o
    no se encuentra.
    
    :param lista: El parámetro "lista" es una lista de diccionarios, donde cada diccionario representa
    un jugador y sus logros
    :type lista: list
    :return: ya sea una cadena con el nombre y los logros del jugador cuyo nombre ingresó el usuario, o
    un mensaje de error si el nombre ingresado no es válido o el jugador no se encuentra en la lista.
    """
    
    ingreso = input("Ingrese el nombre del jugador para ver sus logros: ")
    validacion = r'^[a-zA-Z]+([A-Za-z]+)*$'
    mensaje_error = "Error, el nombre ingresado no es válido o no se encontró el jugador."

    for jugador in lista:
        if re.search(validacion,ingreso):
                if re.search(ingreso,jugador["nombre"],re.IGNORECASE):
                    jugador = "{0}\n{1}".format(jugador["nombre"],jugador["logros"])
                    return jugador

    return mensaje_error
                
def calcular_ordenar_por_promedio_puntos_partido(lista:list):
    """
    Esta función calcula el promedio de puntos por juego para una lista de jugadores de la NBA y los
    ordena por su promedio de puntos por juego en orden ascendente, devolviendo una lista de sus
    nombres.
    
    :param lista: El parámetro de entrada es una lista de diccionarios, donde cada diccionario
    representa un jugador de baloncesto y sus estadísticas
    :type lista: list
    :return: una lista ordenada de nombres de jugadores de la lista de entrada, ordenados por su
    promedio de puntos por juego, y también imprimiendo el total de puntos promedio por juego del
    equipo.
    """
  
    
    suma = 0
    rango_a = len(lista)
    flag_swap = True
    nombres_ordenados = []
        
    for i in range(rango_a):
        suma += lista_nba[i]["estadisticas"]["promedio_puntos_por_partido"]

    total_promedio = suma / rango_a

    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1
        for indice_A in range(rango_a):
                if  lista[indice_A]["estadisticas"]["promedio_puntos_por_partido"] > lista[indice_A+1]["estadisticas"]["promedio_puntos_por_partido"]:
                    lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]                    
                    flag_swap = True

    for jugadores in lista:
        nombres_ordenados.append(jugadores['nombre'])
        nombres_ordenados.sort()
    
    print("El promedio de puntos del Dream Team es: {0}".format(total_promedio))
    return nombres_ordenados

def buscar_miembro_salon_fama(lista:list):
    """
    Esta función busca el nombre de un jugador de baloncesto en una lista de logros y devuelve un
    mensaje que indica si es o no miembro del Basketball Hall of Fame.
    
    :param lista: El parámetro "lista" es una lista de diccionarios que contienen información sobre
    jugadores de baloncesto, incluido su nombre y logros
    :type lista: list
    :return: ya sea una cadena con un mensaje de éxito que indica que el jugador ingresado es miembro
    del Salón de la Fama del Baloncesto, o una cadena con un mensaje de error que indica que el nombre
    ingresado no es válido, no se encontró al jugador o el jugador no es un miembro del Salón de la
    Fama.
    """
   

    ingreso = input("Ingrese el nombre del jugador para ver sus logros: ")
    mensaje_error = "Este jugador no pertenece al Salon de la Fama del Baloncesto."
    error = "Error, el nombre ingresado no es válido, no se encontró el jugador."
    mensaje_exito = "Este jugador pertenece al Salon de la Fama del Baloncesto"
    logro_buscado = "Miembro del Salon de la Fama del Baloncesto"
    validacion = r'^[a-zA-Z]+([A-Za-z]+)*$'

    for jugador in lista:
        if re.search(validacion,ingreso):
                if re.search(ingreso,jugador["nombre"],re.IGNORECASE):
                    if logro_buscado in jugador["logros"]:
                        informe = ("{0}, {1}".format(jugador["nombre"],mensaje_exito))
                        return informe
                    else:
                        informe = ("{0}, {1}".format(jugador["nombre"],mensaje_error))
                        return informe
                    
    return error

def calcular_mayor_estadistica(lista:list,estadistica:str):
    """
    La función calcula el jugador con el valor más alto de una estadística dada de una lista de
    jugadores y sus estadísticas.
    
    :param lista: una lista de diccionarios, donde cada diccionario representa a un jugador y sus
    estadísticas
    :type lista: list
    :param estadistica: El parámetro "estadistica" es una cadena que representa la estadística
    específica para la que queremos calcular el valor máximo. Se utiliza para acceder al valor
    correspondiente en el diccionario de "estadísticas" de cada jugador en la lista de entrada
    :type estadistica: str
    """

    estadistica_maxima = lista[0]["estadisticas"][estadistica]
    nombre_jugador_maximo = [lista[0]["nombre"]]

    for indice in range(len(lista)):
        if lista[indice]["estadisticas"][estadistica] > estadistica_maxima:
            estadistica_maxima = lista[indice]["estadisticas"][estadistica]
            nombre_jugador_maximo = [lista[indice]["nombre"]]
        elif lista[indice]["estadisticas"][estadistica] == estadistica_maxima:
            nombre_jugador_maximo.append(lista[indice]["nombre"])
            
    if len(nombre_jugador_maximo) == 1:
        print("El jugador con mayor cantidad de {2} totales es {0} y tiene {1}".format(nombre_jugador_maximo[0],estadistica_maxima,estadistica))
    else:
        print("El jugador con mayor cantidad de {2} totales son {0} y tienen {1}".format(nombre_jugador_maximo,estadistica_maxima,estadistica))

def mostrar_jugador_mayor_al_promedio(lista:list,estadistica:str):
    """
    Esta función toma una lista de jugadores y una estadística, solicita al usuario un valor y devuelve
    una lista de jugadores cuya estadística es mayor o igual que el valor de entrada.
    
    :param lista: Una lista de diccionarios que representan a los jugadores y sus estadísticas
    :type lista: list
    :param estadistica: una cadena que representa una estadística para un jugador (por ejemplo,
    "puntuaciones", "rebotes", "asistencias")
    :type estadistica: str
    :return: una lista de diccionarios que contienen información sobre jugadores cuyas estadísticas para
    una categoría determinada son mayores o iguales que un valor ingresado por el usuario. Si no hay
    jugadores que cumplan con este criterio, se devuelve una lista vacía.
    """

    ingreso = input("Ingrese un numero entero para mostrar los jugadores que tengan un {0} mayor: ".format(estadistica))
    lista_jugadores_maximos = []

    if ingreso.isdigit():
        valor_a_superar = float(ingreso)
        if valor_a_superar > 0:
            for indice in range(len(lista)):
                if lista[indice]["estadisticas"][estadistica] >= valor_a_superar:
                    lista_jugadores_maximos.append(lista[indice])

    if len(lista_jugadores_maximos) >= 1:
        return lista_jugadores_maximos
    else:
        print("No hay jugadores que tengan un promedio de {0} mayor al valor ingresado o se ingreso un caracter invalido".format(estadistica))
        return mostrar_jugador_mayor_al_promedio(lista,estadistica)

def calcular_jugador_minimo_promedio(lista:list):
    """
    Esta función calcula el jugador con la media mínima de puntos por partido a partir de una lista de
    estadísticas de jugadores.
    
    :param lista: una lista de diccionarios, donde cada diccionario representa un jugador y sus
    estadísticas. Cada diccionario tiene una clave "estadisticas" que contiene otro diccionario con
    claves "promedio_puntos_por_partido" (promedio de puntos por partido) y otras estadísticas. La
    función está destinada a calcular y devolver el
    :type lista: list
    :return: un diccionario que representa al jugador con el promedio de puntos más bajo por juego de
    una lista dada de jugadores.
    """

    for i in range(len(lista)):
        dict_minimo = lista[0]["estadisticas"]["promedio_puntos_por_partido"]
        if dict_minimo < lista[i]["estadisticas"]["promedio_puntos_por_partido"]:
            continue
        elif dict_minimo > lista[i]["estadisticas"]["promedio_puntos_por_partido"]:
            dict_minimo = lista[i]

    return dict_minimo

def calcular_promedio_excluyente(lista:list):
    """
    Esta función calcula el promedio de puntos por partido de un equipo, excluyendo al jugador con el
    promedio más bajo.
    
    :param lista: El parámetro "lista" es una lista de diccionarios, donde cada diccionario representa a
    un jugador de un equipo de baloncesto. Cada diccionario de jugadores contiene información sobre el
    nombre, la posición y las estadísticas del jugador, como puntos por juego, rebotes por juego, etc
    :type lista: list
    """

    jugador_minimo_promedio = calcular_jugador_minimo_promedio(lista)
    suma_total = 0
    lista_menos_uno = len(lista) - 1

    for jugador in lista:
        if jugador != jugador_minimo_promedio:
            suma_total += jugador["estadisticas"]["promedio_puntos_por_partido"]
        elif jugador == jugador_minimo_promedio:
            continue

    promedio_total_sin_uno = suma_total / lista_menos_uno
    mensaje_retorno = "El promedio del equipo Dream Team, sin sumar a {0} con el menor promedio, es: {1}".format(jugador_minimo_promedio["nombre"],promedio_total_sin_uno)

    return mensaje_retorno

def calcular_mayor_logros(lista:list):
    """
    La función calcula el jugador con el mayor número de logros en una lista de jugadores.
    
    :param lista: Una lista de diccionarios, donde cada diccionario representa a un jugador y sus
    logros. Cada diccionario tiene una tecla "nombre" con el nombre del jugador como valor de cadena y
    una tecla "logros" con una lista de logros como valor
    :type lista: list
    """

    cantidad_logros_maximo = len(lista[0]["logros"])
    nombre_jugador_maximo = lista[0]["nombre"]


    for indice in range(len(lista)):
        if len(lista[indice]["logros"]) > cantidad_logros_maximo:
            cantidad_logros_maximo = len(lista[indice]["logros"])
            nombre_jugador_maximo = lista[indice]["nombre"]

    print("El jugador con mayor cantidad de logros totales es {0} y tiene {1}".format(nombre_jugador_maximo,cantidad_logros_maximo))

def ordenar_por_posicion_tiros_de_campo(lista:list):
    """
    Esta función ordena una lista de jugadores de baloncesto por su posición, según su porcentaje de
    tiros de campo.
    
    :param lista: El parámetro "lista" es una lista de diccionarios que representan a jugadores de
    baloncesto, donde cada diccionario contiene información sobre un jugador, como su nombre, posición y
    estadísticas de tiro
    :type lista: list
    :return: ya sea una lista impresa de jugadores ordenados por su posición, o una cadena que indica
    que no hay jugadores con un porcentaje de tiros de campo más alto que el valor de entrada.
    """

    lista_maximos = mostrar_jugador_mayor_al_promedio(lista,"porcentaje_tiros_de_campo")
    rango_a = len(lista_maximos)
    flag_swap = True

    if rango_a > 1:
        while(flag_swap):
            flag_swap = False
            rango_a = rango_a - 1

            for indice_A in range(rango_a):
                if  lista_maximos[indice_A]["posicion"] > lista_maximos[indice_A+1]["posicion"]:
                    lista_maximos[indice_A],lista_maximos[indice_A+1] = lista_maximos[indice_A+1],lista_maximos[indice_A]
                    flag_swap = True

        for jugador in lista_maximos:
            print("{0} : {1}".format(jugador["nombre"],jugador["posicion"]))
    
    elif rango_a == 1:
        for jugador in lista_maximos:
            print("{0} : {1}".format(jugador["nombre"],jugador["posicion"]))
            
    elif rango_a == 0:
        return ("No hay jugadores que tengan un promedio de porcentaje_tiros_de_campo mayor al valor ingresado")

cargar_menu_principal(lista_nba)

