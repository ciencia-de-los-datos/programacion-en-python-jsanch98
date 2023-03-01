import csv

"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def leer_csv(archivo: str):
   archivo = open(archivo, 'r')
   datos = csv.reader(archivo, delimiter='\t')
   return datos


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    datos: list = list(leer_csv('data.csv'))
    suma_col_b: int = 0
    for registro in datos:
        suma_col_b += int(registro[1])
    return suma_col_b


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    datos: list = list(leer_csv('data.csv'))
    resultado: dict = dict()
    for registro in datos:
        try:
            resultado[registro[0]] += 1
        except KeyError :
            resultado[registro[0]] = 1
    return sorted(resultado.items())


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    datos: list = list(leer_csv('data.csv'))
    resultado: dict = dict()
    for registro in datos:
        try:
            resultado[registro[0]] += int(registro[1])
        except KeyError :
            resultado[registro[0]] = int(registro[1])
    return sorted(resultado.items())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    datos: list = list(leer_csv('data.csv'))
    resultado: dict = dict()
    for registro in datos:
        mes = registro[2].split('-')[1]
        try:
            resultado[mes] += 1
        except KeyError :
            resultado[mes] = 1
    return sorted(resultado.items())


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    datos: list = list(leer_csv('data.csv'))
    valores_por_letra: dict = dict()
    resultado: list = []
    for registro in datos:
        try:
            valores_por_letra[registro[0]].append(int(registro[1]))
        except:
            valores_por_letra[registro[0]] = [int(registro[1])]
    for k,v in valores_por_letra.items():
        resultado.append((k, max(v), min(v)))
    return sorted(resultado)


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    datos: list = list(leer_csv('data.csv'))
    diccionarios_registros: list = []
    diccionarios_agrupados: dict = dict()
    resultado: list = []

    for registro in datos:
        col_5 = registro[4].split(',')
        lista_de_tuplas = list(map(lambda par: tuple(par.split(':')), col_5))
        diccionarios_registros.append(dict(lista_de_tuplas))

    for diccionario in diccionarios_registros:
        for k,v in diccionario.items():
            try:
                diccionarios_agrupados[k].append(int(v))
            except:
                diccionarios_agrupados[k] = [int(v)]

    for k,v in diccionarios_agrupados.items():
        resultado.append((k, min(v), max(v)))

    return sorted(resultado)


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    datos: list = list(leer_csv('data.csv'))
    resultado: dict = dict()
    for registro in datos:
        try:
            resultado[int(registro[1])].append(registro[0])
        except KeyError :
            resultado[int(registro[1])] = [registro[0]]
    return sorted(resultado.items())


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    datos: list = list(leer_csv('data.csv'))
    resultado: dict = dict()
    for registro in datos:
        try:
            if registro[0] not in resultado[int(registro[1])]:
                resultado[int(registro[1])].append(registro[0])
        except KeyError :
            resultado[int(registro[1])] = [registro[0]]
        finally:
            resultado[int(registro[1])] = sorted(resultado[int(registro[1])])

    return sorted(resultado.items())


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    datos: list = list(leer_csv('data.csv'))
    diccionarios_registros: list = []
    diccionarios_agrupados: dict = dict()

    for registro in datos:
        col_5 = registro[4].split(',')
        lista_de_tuplas = list(map(lambda par: tuple(par.split(':')), col_5))
        diccionarios_registros.append(dict(lista_de_tuplas))

    for diccionario in diccionarios_registros:
        for k,v in diccionario.items():
            try:
                    diccionarios_agrupados[k] += 1
            except:
                    diccionarios_agrupados[k] = 1

    return dict(sorted(diccionarios_agrupados.items()))


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    datos: list = list(leer_csv('data.csv'))
    return list(map(lambda reg: (reg[0], len(reg[3].split(',')), len(reg[4].split(','))), datos))


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    datos: list = list(leer_csv('data.csv'))
    resultado: dict = dict()

    for registro in datos:
        valores_col_4 = registro[3].split(',')
        valores_col_4 = list(map(lambda val: (val, int(registro[1])), valores_col_4))
        for valor in valores_col_4:
            try:
                resultado[valor[0]] += valor[1]
            except KeyError as exception:
                resultado[valor[0]] = valor[1]
    return dict(sorted(resultado.items()))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    datos: list = list(leer_csv('data.csv'))
    resultado: dict = dict()

    datos_mapeados = list(map(lambda reg: (reg[0], reg[4].replace(':',',').split(',')[1::2]),datos))

    for tupla in datos_mapeados:
        suma_valores_numericos: int = sum(list(map(lambda val: int(val) ,tupla[1])))
        try:
            resultado[tupla[0]] += suma_valores_numericos
        except:
            resultado[tupla[0]] = suma_valores_numericos
    return dict(sorted(resultado.items()))
