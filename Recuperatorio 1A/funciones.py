import os
import csv
import json
import random



def cargar_archivos()->list:
    nombre_archivo = input("Ingrese el nombre del archivo a cargar: ")

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo_csv:
            contenido = archivo_csv.readlines()[1:]
            lista = []
            for linea in contenido:
                filas = linea.strip().split(',')
                peliculas = {
                    'id_peli': filas[0],
                    'titulo': filas[1],
                    'genero': filas[2],
                    'duracion': str(filas[3])
                }
                lista.append(peliculas)
        print("Los datos han sido cargados...")
    except FileNotFoundError:
        input("Nombre invalido...volviendo al menu...")
        return 0
    
    return lista
    

def Imprimir_lista(lista:list):
    if lista == 0:
        input("La lista esta vacia....")
        return False
    
    
    for peliculas in lista:
        print(f"ID:{peliculas['id_peli']:2s}  Titulo:{peliculas['titulo']:30s}  Genero:{peliculas['genero']:15s}  Duracion:{peliculas['duracion']}")




def generar_duracion(pelicula):
    pelicula["duracion"] = random.randint(100, 240)
    return pelicula


def asignar_tiempo(lista):
    if lista == 0:
        input("La lista esta vacia....")
        return False


    lista_peliculas_con_duracion = list(map(generar_duracion, lista))
    for peliculas in lista_peliculas_con_duracion:
        print(f"Titulo:{peliculas['titulo']:30s}   Duracion:{peliculas['duracion']:6d}")


    return lista_peliculas_con_duracion


def filtrar_por_tipo(lista):
    if lista == 0:
        input("La lista esta vacia....")
        return False
    
    genero_pelicula = input("Ingrese el tipo de genero que quiere filtrar: ")
    flag_genero = False
    for generos in lista:
        if genero_pelicula == generos["genero"]:
            flag_genero = True

    if flag_genero == False:
        input("El genero ingresado no existe")
        return False

    with open(r"movies_filtradas.csv", "w") as file:
        file.write("id_peli,titulo,genero,duracion\n")

        for peliculas in lista:
            if genero_pelicula in peliculas["genero"]:
                file.write(peliculas["id_peli"])
                file.write(",")
                file.write(peliculas["titulo"])
                file.write(",")
                file.write(peliculas["genero"])
                file.write(",")
                file.write(str(peliculas["duracion"]))
                file.write("\n")


    print("Se filtro y genero un archivo")






def ordenar_lista_dict_doble_criterio(lista: list, key1: str, key2: str)->None:
    """Ordenamientos burbuja de diccionarios doble criterio

    Args:
        lista (list): lista de insumos
        key1 (str): primer criterio
        key2 (str): segundo criterio
    """
    tam = len(lista)
    for i in range(tam-1):
        for j in range(i+1, tam):
            if ((lista[i][key1] == lista[j][key1]) and (lista[i][key2] < lista[j][key2])) or (lista[i][key1] > lista[j][key1]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux



def mostrar_duraciones(lista):
    if lista == 0:
        input("La lista esta vacia....")
        return False
    
    lista_ordenada = ordenar_lista_dict_doble_criterio(lista,"genero","duracion")

    for peliculas in lista:
        print(f"ID:{peliculas['id_peli']:2s}  Titulo:{peliculas['titulo']:30s}  Genero:{peliculas['genero']:15s}  Duracion:{peliculas['duracion']:6d}")


    return lista



def guardar_peliculas(lista):
    if lista == 0:
        input("La lista esta vacia...")
        return False

    with open(r"peliculas_ordenadas_por_genero.txt", "w") as archivo:
        archivo.write("id_peli,titulo,genero,duracion\n")
        for peliculas in lista:
            archivo.write(peliculas["id_peli"])
            archivo.write(",")
            archivo.write(peliculas["titulo"])
            archivo.write(",")
            archivo.write(peliculas["genero"])
            archivo.write(",")
            archivo.write(str(peliculas["duracion"]))
            archivo.write("\n")



def imprimir_menu():
    print("""
    _________________MENU_________________
    1. Cargar datos de peliculas
    2. imprimir lista
    3. Asignar tiempos
    4. Filtrar por tipo
    5. Mostrar y ordenar por genero y duracion
    6. Guardar Peliculas
    7. Salir
    """)


def mostrar_opciones():
    """Pide que ingrese una opcion al usuario

    Returns:
        _type_: none
    """
    try:
        opcion = input("ingrese una opcion: ")
        return int(opcion)
    except ValueError:
        return -1



def app_principal():
    flag_archivos = False
    flag_ordenada_por_genero = False
    lista = []
    while True:
        os.system("cls")
        imprimir_menu()
        opcion = mostrar_opciones()

        os.system("cls")
        
        
        match opcion:
            case 1:
                os.system("cls")
                lista = cargar_archivos()
                if lista != False:
                    flag_archivos = True
                input("precione caulquier tecla...")
                os.system("cls")


            case 2:
                if flag_archivos == True:
                    os.system("cls")
                    Imprimir_lista(lista)
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero...")
                    os.system("cls")

            case 3:
                if flag_archivos:
                    os.system("cls")
                    asignar_tiempo(lista)
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero...")
                    os.system("cls")

            case 4:
                if flag_archivos:
                    os.system("cls")
                    filtrar_por_tipo(lista)
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero...")
                    os.system("cls")

            case 5:
                if flag_archivos:
                    os.system("cls")
                    mostrar_duraciones(lista)
                    flag_ordenada_por_genero = True
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero...")
                    os.system("cls")

            case 6:
                if flag_archivos == True and flag_ordenada_por_genero == True:
                    os.system("cls")
                    guardar_peliculas(lista)
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero y mostrar las duraciones...")
                    os.system("cls")

            case 7:
                os.system("cls")
                input("Saliendo precione caulquier tecla...")
                break

            case _:
                input("Valor no valido...precione caulquier tecla para continuar")





