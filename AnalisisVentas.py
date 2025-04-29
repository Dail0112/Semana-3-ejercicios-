#Fecha: Miercoles 09 de abril del 2025
#Autora: Claudia Sofia Vargas Ayerdis
"""
 Ejercicio #1
Análisis de datos de ventas
Desarrollar un programa que procese un conjunto de registros de ventas (por ejemplo, listas
de diccionarios) para extraer información relevante. Los estudiantes deberán aplicar
funciones internas como map, filter y reduce para transformar y filtrar los datos, calculando
totales y promedios. Este ejercicio busca que los estudiantes identifiquen y aprovechen las
funcionalidades nativas de Python para la manipulación eficiente de estructuras de datos.
"""

ventas = [
    {"producto": "camisa", "precio": 20, "cantidad": 2},
    {"producto": "pantalón", "precio": 25, "cantidad": 1},
    {"producto": "gorra", "precio": 10, "cantidad": 3}
]

suma_total = 0
for venta in ventas:
    total = venta["precio"] * venta["cantidad"]
    suma_total += total
    print(f"Producto: {venta['producto']}, Total: {total}")

promedio = suma_total / len(ventas)
print(f"Total general: {suma_total}")
print(f"Promedio por producto: {promedio}")
