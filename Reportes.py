#Fecha: Miercoles 09 de abril del 2025
#Autora: Claudia Sofia Vargas Ayerdis
"""
 Ejercicio #5
Facturación y reportes de ventas
Crear una clase Factura que simule el proceso de facturación de una venta. Los estudiantes
deberán encapsular los datos internos de la factura (como los detalles de los productos,
cantidades, precios y descuentos) y proveer métodos para calcular el total de la venta,
generar reportes simples y validar la integridad de la información. Este ejercicio enfatiza la
importancia de ocultar la implementación interna y de diseñar interfaces claras y seguras
para la gestión de transacciones comerciales. 
"""

class Factura:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad, descuento):
        self.productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
            "descuento": descuento
        })

    def calcular_total(self):
        total = 0
        for p in self.productos:
            subtotal = p["precio"] * p["cantidad"]
            descuento = subtotal * (p["descuento"] / 100)
            total += subtotal - descuento
        return total

factura = Factura()
factura.agregar_producto("Camisa", 20, 2, 10)
factura.agregar_producto("Pantalón", 30, 1, 0)

print(f"Total de la factura: {factura.calcular_total()}")
