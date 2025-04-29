#Fecha: Miercoles 09 de abril del 2025
#Autora: Claudia Sofia Vargas Ayerdis
"""
 Ejercicio #4
Gestión de productos e inventario
Diseñar una clase Producto que incluya atributos como código, nombre, precio y cantidad
en stock. Además, los estudiantes deberán implementar una clase Inventario que administre
una colección de objetos Producto, incorporando métodos para agregar, buscar, actualizar
y eliminar productos. Este ejercicio permite modelar situaciones reales de gestión de ventas
y refuerza el concepto de encapsulación y manejo de colecciones en programación orientada
a objetos
"""

class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def buscar(self, codigo):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar(self, codigo, cantidad):
        producto = self.buscar(codigo)
        if producto:
            producto.cantidad = cantidad

    def eliminar(self, codigo):
        self.productos = [p for p in self.productos if p.codigo != codigo]

inventario = Inventario()
inventario.agregar(Producto("001", "Camisa", 20, 5))
inventario.agregar(Producto("002", "Pantalón", 25, 3))

p = inventario.buscar("001")
if p:
    print(f"Producto encontrado: {p.nombre}, Cantidad: {p.cantidad}")

