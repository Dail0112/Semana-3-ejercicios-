#Fecha: Miercoles 09 de abril del 2025
#Autora: Claudia Sofia Vargas Ayerdis
"""
 Ejercicio #3
Paquete de algoritmos de búsqueda
Desarrollar un programa para organizar diferentes algoritmos de búsqueda en un paquete
estructurado. Los estudiantes deberán crear al menos dos módulos que contengan
implementaciones de búsqueda lineal y búsqueda binaria, configurando adecuadamente el
archivo init.py. Posteriormente, desde un script principal, se utilizarán estas funciones para
localizar elementos específicos en una colección de datos, resaltando la importancia de la
organización en proyectos de mayor envergadura. 
"""

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

coleccion = [1, 3, 5, 7, 9, 11]
print("Búsqueda lineal del 5:", busqueda_lineal(coleccion, 5))
print("Búsqueda binaria del 7:", busqueda_binaria(coleccion, 7))
