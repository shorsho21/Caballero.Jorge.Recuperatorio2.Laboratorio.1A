import os
import csv
import json
import random
# import csv

# def cargar_datos_desde_archivo(archivo: str) -> str:
#     lista = []
#     try:
#         with open(archivo, 'r', encoding="utf-8") as archivo_csv:
#             contenido = archivo_csv.readlines()[1:]     #leo todas las lineas a partir de la 2da linea
#             for linea in contenido:
#                 fila = linea.strip().split(',')   #dividido por las comas y elimnino el \n con el strip
#                 lista.append(fila)
#         return lista
#     except FileNotFoundError:   #si no encuentra el archivo retorna false
#         return False

# lista = cargar_datos_desde_archivo(r"Programacion\Primer parcial\insumos.csv")

# /////////////////////////////////CARGAR DATOS DEL ARCHIVO CSV A UNA LISTA DE DICCIONARIO//////////////////////////////////////////////////////////////
def agregar_stock(producto):
    producto["stock"] = random.randint(0, 10)
    return producto

def generar_id(lista:list)->str:
    id_mayor = 0
    for id in lista:
        if int(id["id"]) > id_mayor:
            id_mayor = int(id["id"])
    
    nuevo_id = str(int(id_mayor) + 1)
    return nuevo_id
    


def pedir_nombre_archivo()->str:
    nombre_archivo = input("Ingrese el nombre del archivo a cargar: ")
    return nombre_archivo


def cargar_datos_archivo(archivo: str) -> list:
    """Recibe el path de insumos.csv y lo carga en una lista y lo retorna

    Args:
        archivo (str): path del archivo csv

    Returns:
        list: lista de diccionario de los datos del archivo csv
    """
    try:
        with open(archivo, "r", encoding="utf-8") as archivo_csv:
            contenido = archivo_csv.readlines()[1:]
            lista = []
            for linea in contenido:
                filas = linea.strip().split(',')
                insumos = {
                    'id': filas[0],
                    'producto': filas[1],
                    'marca': filas[2],
                    'precio': filas[3].replace("$", ""),
                    'caracteristicas': filas[4].split('~')
                }
                lista.append(insumos)
        print("Los datos han sido cargados...")
    except FileNotFoundError:
        input("Nombre invalido...volviendo al menu...")
        return False
    
    lista_con_stock = list(map(agregar_stock, lista))


    




    return lista_con_stock


# lista = cargar_datos_archivo(r"insumos.csv")
# print(lista)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# //////////////////////////////////////LISTAR LA CANTIDAD DE PRODUCTOS POR MARCA/////////////////////////////////////////////////////////////////////////////////////////////

# Listar cantidad por marca: Muestra todas las marcas y la cantidad
# de insumos correspondientes a cada una.


def listar_cantidad_por_marca(lista: list) -> None:
    """recibe una lista de diccionarios con los insumos y retorna todas las marcas con la cantidad de productos del mismo

    Args:
        lista (list): lista de insumos
    """
    lista_marcas = []
    contador = 0
    for value in lista:
        lista_marcas.append(value["marca"])
    lista_marcas = set(lista_marcas)

    print("Cantidad de productos por marca")
    for marcas in lista_marcas:
        for value in lista:
            if marcas in value["marca"]:
                contador = contador + 1

        print(f"{marcas:30s} {contador:5d}")

# listar_cantidad_por_marca(lista)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////LISTAR INSUMOS POR MARCA//////////////////////////////////////////////////////////////////////////////////////

# 3. Listar insumos por marca: Muestra, para cada marca, el nombre y
# precio de los insumos correspondientes.


def listar_insumos_por_marca(lista:list)->None:
    """Recibe una lista y muestra las marcas y sus productos

    Args:
        lista (list): La lista de insumos
    """
    lista_marcas = []
    for value in lista:
        lista_marcas.append(value["marca"])
    lista_marcas = set(lista_marcas)

    for marcas in lista_marcas:
        print(f"Productos de {marcas} :")
        for value in lista:
            if marcas in value["marca"]:
                print(f"{value['producto']:30s}  precio: {value['precio']}")
        print("\n\n\n")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ///////////////////////////////////////////////////BUSCAR INSUMO POR CARACTERISTICA///////////////////////////////////////////////////////////////////

# Buscar insumo por característica: El usuario ingresa una
# característica (por ejemplo, "Sin Granos") y se listarán todos los
# insumos que poseen dicha característica.

def buscar_insumo_por_caracteristica(lista:list)->None:
    """Recibe una lista, pide al usuario una caracteristica y se imprime los insumos con esa caracteristica

    Args:
        lista (list): la lista de insumos

    Returns:
        _type_: none
    """
    lista_caracteristicas = []

    for value in lista:

        for caracteristicas in value["caracteristicas"]:
            lista_caracteristicas.append(caracteristicas)

    lista_caracteristicas = set(lista_caracteristicas)

    buscar_caracteristica = input("Ingrese una caracteristica: ")

    if not buscar_caracteristica in lista_caracteristicas:
        print("La caracteristica es invalida...")
        input("Intente con una caracteristica valida...")
        return False
    else:
        for value in lista:
            for caracteristica in value["caracteristicas"]:
                if buscar_caracteristica in caracteristica:
                    print(f"{value['producto']}")


# Ideal para perros de pelo largo

# buscar_insumo_por_caracteristica(lista)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# /////////////////////////////////////////LISTAR INSUMOS ORDENADOS///////////////////////////////////////////////////////////////////////////////////////
# 5. Listar insumos ordenados: Muestra el ID, descripción, precio, marca
# y la primera característica de todos los productos, ordenados por
# marca de forma ascendente (A-Z) y, ante marcas iguales, por precio
# descendente.


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


def listar_insumos_ordenados(lista:list)->None:
    """Recibe una lista e imprime los insumos de forma ordenada  por marca(A-Z)

    Args:
        lista (list): lista de insumos
    """

    ordenar_lista_dict_doble_criterio(lista, "marca", "precio")
    print(f"ID       PRODUCTO                                MARCA                             PRECIO                   CARACTERISTICAS")
    for value in lista:

        print(f"{value['id']:2s}   {value['producto']:40s}  {value['marca']:35s} {value['precio']:20s}  {value['caracteristicas'][0]}")

# listar_insumos_ordenados(lista)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////REALIZAR COMPRAS///////////////////////////////////////////////////////////////////////////

# 6. Realizar compras: Permite realizar compras de productos. El usuario
# ingresa una marca y se muestran todos los productos disponibles de
# esa marca. Luego, el usuario elige un producto y la cantidad deseada.
# Esta acción se repite hasta que el usuario decida finalizar la compra.
# Al finalizar, se muestra el total de la compra y se genera un archivo
# TXT con la factura de la compra, incluyendo cantidad, producto,
# subtotal y el total de la compra.

def realizar_compras(lista: list)->None:
    """Recibe una lista, muestra las marcas, elegis una marca, elegis los productos de esa marca, se crea un ticket de compra.

    Args:
        lista (list): lista de insumos

    Returns:
        _type_: None
    """
    lista_marcas = []
    producto = {"producto": None, "cantidad": 0, "precio": None, "id": None}
    lista_productos = []
    id = 0
    for value in lista:
        lista_marcas.append(value["marca"])
    lista_marcas = set(lista_marcas)

    print("Lista de marcas")
    for marcas in lista_marcas:
        print(marcas)
    opcion = input("Ingrese una marca:  ")
    os.system("cls")

    if not opcion in lista_marcas:
        print("Opcion invalida...ingrese una marca valida...")
        input("Precione cualquier tecla para continuar...")
        return False

    for value in lista:
        if opcion == value["marca"]:
            id = id + 1
            producto = {
                "producto": value['producto'], "cantidad": 0, "precio": value['precio'], "id": id, "stock":value['stock']}
            lista_productos.append(producto)
            print(
                f"id: {producto['id']}  {producto['producto']:25s}  precio: {producto['precio']}  stock:{producto['stock']}")

    entrada = True
    while entrada:
        try:
            compra_id = int(input("Ingrese el ID del producto a comprar: "))
        except ValueError:
            input("El id ingresado no es valido...")
            return -1

        flag_id = False
        for value in lista_productos:
            if compra_id == value['id']:
                flag_id = True
        if flag_id == False:
            print("El id ingresado es invalido...Ingrese un id valido")
            input("Preciona una tecla para continuar...")
            break
        try:
            compra_cantidad = int(
                input("Ingrese la cantidad que quiere comprar: "))
        except ValueError:
            input("El valor ingresado es invalido....")
            return -1
        for value in lista_productos:
            if compra_id == value['id']:
                if value['stock'] == 0:
                    input("No hay stock...")
                    return -1
                while value['stock'] < compra_cantidad:
                    compra_cantidad= int(input("No hay suficiente stock...Ingrese una cantidad valida: "))




        for value in range(len(lista_productos)):
            if compra_id == lista_productos[value]["id"]:
                lista_productos[value]["cantidad"] += compra_cantidad

        print("Seguir comprando[1]     Salir[2]")
        comprando = input("")
        while comprando != "2" and comprando != "1":
            comprando = input("Error, ingrese una opcion valida...")
        if comprando == "2":
            entrada = False

    with open(r"ticket.txt", "w") as archivo:
        precio_total = 0
        sub_total = 0
        print(f"PRODUCTO                              PRECIO     CANTIDAD     SUBTOTAL")
        archivo.write(
            f"PRODUCTO                              PRECIO     CANTIDAD     SUBTOTAL\n")
        for productos in lista_productos:

            sub_total = float(productos['precio']) * productos['cantidad']
            precio_total = precio_total + sub_total
            if productos['cantidad'] != 0:
                archivo.write(
                    f"{productos['producto']:35s}  ${productos['precio']:5s}      {productos['cantidad']}            ${sub_total:3.2f}\n")
                print(
                    f"{productos['producto']:35s}  ${productos['precio']:5s}      {productos['cantidad']}            ${sub_total:3.2f}")

        archivo.write(f"\nTotal: ${precio_total:.2f}")
        print(f"Total: ${precio_total:.2f}")


# realizar_compras(lista)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////GUARDAR EN FORMATO JSON////////////////////////////////////////////////////////////////////////////////

# 7. Guardar en formato JSON: Genera un archivo JSON con todos los
# productos cuyo nombre contiene la palabra "Alimento".


def guardar_formato_json(lista:list)->None:
    """Recibe una lista y guarda los insumos tipo Alimento a un archivo json

    Args:
        lista (list): Lista de insumos
    """
    productos_alimentos = []
    for productos in lista:
        if "Alimento" in productos['producto']:
            productos_alimentos.append(productos)

    with open(r"alimentos.json", "w") as file:
        json.dump(productos_alimentos, file, indent=4)

    print("Se guardaron los productos tipo Alimento en formato json")


# guardar_formato_json(lista)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////


# /////////////////////////////////////LEER DESDE FORMATO JSON////////////////////////////////////////////////////////////////////
# r"Programacion\Primer parcial\alimentos.json"
def leer_formato_json(archivo: str)->None:
    """Recibe la direccion del archivo json de alimentos y lo muestra en pantalla

    Args:
        archivo (str): Direccion del archivo alimentos.json
    """

    with open(archivo, "r") as file:
        archivo = file.read()

    lista_alimentos = json.loads(archivo)
    print(f"ID       PRODUCTO                                MARCA                             PRECIO                   CARACTERISTICAS")
    for value in lista_alimentos:

        print(f"{value['id']:2s}   {value['producto']:40s}  {value['marca']:35s} {value['precio']:20s}  {value['caracteristicas'][0]}")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////ACTUALIZAR PRECIOS//////////////////////////////////////////////////////////////////////////////////////
# 9. Actualizar precios: Aplica un aumento del 8.4% a todos los
# productos, utilizando la función map. Los productos actualizados se
# guardan en el archivo "Insumos.csv".

def aumentar_precio(lista:list)->list:
    """Recibe una lista, actualiza los precios, retorna la lista con precios actualizados

    Args:
        lista (list): lista de insumos

    Returns:
        _type_: lista con precios actualizados
    """
    lista['precio'] = round(float(lista['precio']) * 1.084, 2)
    return lista


def actualizar_precios(lista:list)->None:
    """Recibe la lista, actualiza los precios en 8.4% y lo guarda en un archivo csv

    Args:
        lista (list): lista de insumos
    """

    lista_precios_actualizados = list(map(aumentar_precio, lista))

    with open(r"insumos(precios_actualizados).csv", "w") as file:
        file.write("ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS\n")
        for value in range(len(lista_precios_actualizados)):
            id = lista_precios_actualizados[value]["id"]
            producto = lista_precios_actualizados[value]["producto"]
            marca = lista_precios_actualizados[value]["marca"]
            precio = str(lista_precios_actualizados[value]["precio"])
            caracteristicas = lista_precios_actualizados[value]["caracteristicas"]

            file.write(id)
            file.write(",")
            file.write(producto)
            file.write(",")
            file.write(marca)
            file.write(",")
            file.write(precio)
            file.write(",")
            for value in lista_precios_actualizados[value]["caracteristicas"]:
                file.write("~")
                file.write(value)
            file.write("\n")
            # file.write(caracteristicas)
    print("se actualizaron los precios")


def imprimir_menu():
    print("""
    _________________MENU_________________
    1. Cargar datos de insumos
    2. Listar cantidad de productos por marca
    3. Mostrar insumos por marca
    4. Buscar insumo por característica
    5. Mostrar insumos ordenados (A-Z)
    6. Realizar compras
    7. Guardar los alimentos en formato JSON
    8. Leer los alimentos desde archivo JSON
    9. Actualizar los precios 8.4%
    10. Agregar un nuevo producto
    11. Guardar cambios[csv][json]
    12. Salir del programa
    13. Mostrar stock por Marca
    14. Imprimir bajo stock
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
    """Aplicacion principal del programa, muestra menu, pide la opcion y ejecuta los programas.
    """
    flag_archivos_cargados = False
    flag_alimentos = False
    while True:
        os.system("cls")
        imprimir_menu()
        opcion = mostrar_opciones()

        os.system("cls")

        match opcion:
            case 1:
                os.system("cls")
                lista = cargar_datos_archivo(pedir_nombre_archivo())
                if lista != False:
                    flag_archivos_cargados = True
                input("precione caulquier tecla...")
                os.system("cls")
            case 2:
                if flag_archivos_cargados:
                    os.system("cls")
                    listar_cantidad_por_marca(lista)
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero...")
                    os.system("cls")
            case 3:
                if flag_archivos_cargados:
                    os.system("cls")
                    listar_insumos_por_marca(lista)
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero...")
                    os.system("cls")
            case 4:
                if flag_archivos_cargados:
                    os.system("cls")
                    buscar_insumo_por_caracteristica(lista)
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero...")
                    os.system("cls")
            case 5:
                if flag_archivos_cargados:
                    os.system("cls")
                    listar_insumos_ordenados(lista)
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero...")
                    os.system("cls")
            case 6:
                if flag_archivos_cargados:
                    os.system("cls")
                    realizar_compras(lista)
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero...")
                    os.system("cls")
            case 7:
                if flag_archivos_cargados:
                    os.system("cls")
                    guardar_formato_json(lista)
                    flag_alimentos = True
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero...")
                    os.system("cls")

            case 8:
                if flag_archivos_cargados and flag_alimentos:
                    os.system("cls")
                    leer_formato_json(
                        r"alimentos.json")
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input(
                        "Necesitas cargar los datos primero o guardar los datos en tipo json...")
                    os.system("cls")
            case 9:
                if flag_archivos_cargados:
                    os.system("cls")
                    actualizar_precios(lista)
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero...")
                    os.system("cls")
            case 10:
                if flag_archivos_cargados:
                    os.system("cls")
                    agregar_nuevo_producto(lista)
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero...")
                    os.system("cls")
            case 11:
                if flag_archivos_cargados:
                    os.system("cls")
                    guardar_csv_json(lista)
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero...")
                    os.system("cls")
            case 12:
                os.system("cls")
                input("Saliendo precione caulquier tecla...")
                break
            case 13:
                if flag_archivos_cargados:
                    os.system("cls")
                    mostrar_stock_por_marca(lista)
                    input("Saliendo precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero...")
                    os.system("cls")
            case 14:
                if flag_archivos_cargados:
                    os.system("cls")
                    imprimir_bajo_stock(lista)
                    input("precione caulquier tecla...")
                    os.system("cls")
                else:
                    os.system("cls")
                    input("Necesitas cargar los datos primero...")
                    os.system("cls")

            case _:
                input("Valor no valido...precione caulquier tecla para continuar")


def agregar_nuevo_producto(lista: list):
    """Agrega un nuevo producto a la lista de insumos

    Args:
        lista (list): lista de insumos
    """

    print("Ingresando nuevo producto")
    nuevo_producto = {
        "id": generar_id(lista),
        "producto": input("Ingrese nombre del producto ")
    }
    while True:
        try:
            nuevo_producto['precio'] = float(input("Ingrese un precio: "))
            nuevo_producto['precio'] = str(nuevo_producto['precio'])
            break
        except ValueError:
            input("El precio ingresado es invalido.... ")

    agregar_stock(nuevo_producto)



    with open(r"marcas.txt", "r", encoding="utf-8") as file:
        contenido = file.readlines()
        for marcas in range(len(contenido)):
            contenido[marcas] = contenido[marcas].replace("\n", "")

        for marcas in contenido:
            print(marcas)

        nuevo_producto['marca'] = input("Ingrese una marca: ")
        while not nuevo_producto['marca'] in contenido:
            nuevo_producto['marca'] = input("Ingrese una marca valida...")

    caracteristica = []
    print("Cuantas caracteristicas quiere ingresar?[1-3] ")
    cantidad_caracteristicas = int(input(""))
    while cantidad_caracteristicas < 1 or cantidad_caracteristicas > 3:
        cantidad_caracteristicas = int(
            input("Ingrese una cantidad valida... "))

    match cantidad_caracteristicas:
        case 1:
            caracteristica.append(
                str(input("Ingrese la primera caracteristica ")))
        case 2:
            caracteristica.append(
                str(input("Ingrese la primera caracteristica ")))
            caracteristica.append(
                str(input("Ingrese la segunda caracteristica ")))
        case 3:
            caracteristica.append(
                str(input("Ingrese la primera caracteristica ")))
            caracteristica.append(
                str(input("Ingrese la segunda caracteristica ")))
            caracteristica.append(
                str(input("Ingrese la tercera caracteristica ")))
        case _:
            print("Opcion no valida")

    nuevo_producto['caracteristicas'] = caracteristica

    lista.append(nuevo_producto)


# agregar_nuevo_producto(lista)


def guardar_csv_json(lista:list)->None:
    """Pide al usuario guardar la lista de insumos en formato csv o json

    Args:
        lista (list): lista de insumos

    Returns:
        : none
    """

    opcion = input("Ingrese el formato [csv] o [json]").lower()
    while opcion != "csv" and opcion != "json":
        opcion = input("Ingresa un formato valido [csv] o [json]: ")

    nombre_archivo = input("Ingrese el nombre del archivo: ")
    nombre_archivo += "."+opcion
    print(nombre_archivo)
    if opcion == "csv":
        with open(nombre_archivo, "w", encoding="utf-8") as file:
            file.write("ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS")

            for item in lista:
                file.write(
                    f"\n{item['id']},{item['producto']},{item['marca']},{item['precio']},")
                for value in item['caracteristicas']:
                    file.write("~")
                    file.write(value)

    if opcion == "json":
        with open(nombre_archivo, "w", encoding="utf-8") as file:
            json.dump(lista, file, indent=4)



#///////////////////////////////////////////////////////
def mostrar_stock_por_marca(lista:list):
    """Recibe una lista, pide al usuario una marca y muestra el stock de esa marca

    Args:
        lista (list): lista de insumos

    Returns:
        _type_: none
    """
    stock_total = 0
    lista_marcas = []
    for value in lista:
        lista_marcas.append(value["marca"])
    lista_marcas = set(lista_marcas)
    lista_marcas = list(lista_marcas)

    print("LISTA DE MARCAS")
    for marcas in lista_marcas:
        print(marcas)

    opcion = input("INGRESE UNA MARCA PARA MOSTRAR SU STOCK: ")
    flag_producto = False


    for marcas in lista_marcas:
        if opcion == marcas:
            flag_producto = True
            print(f"___________________{marcas}___________________")
            for value in lista:
                if marcas in value["marca"]:
                    print(f"{value['producto']:30s}       stock: {value['stock']}\n")
                    stock_total += value['stock']
            print(f"Stock total: {stock_total}")

    if flag_producto == False:
        input("La marca ingresada no es valida")
        return -1


# D. Agregar opción imprimir bajo stock. Que imprima en un archivo de 
# texto en formato csv. Un listado con el nombre de producto y el stock de 
# aquellos productos que tengan 2 o menos unidades de stock. 



def imprimir_bajo_stock(lista:list):
    """Recibe lista, imprime por pantalla y por archivo csv los productos con bajo stock 2 o menos

    Args:
        lista (list): lista de insumos
    """

    lista_productos_stock = []

    for productos in lista:
        if productos['stock'] < 3:
            lista_productos_stock.append(productos)

    with open ("lista_productos_stock.csv", "w",) as file:
            
            print("NOMBRE                                STOCK")
            file.write("NOMBRE                                STOCK\n")
            for productos in lista_productos_stock:
                print(f"{productos['producto']:35s}     {productos['stock']}")

                file.write(f"{productos['producto']:35}     {productos['stock']}\n")
