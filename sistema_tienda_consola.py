# Importaciones necesarias para el sistema
from datetime import datetime
from tabulate import tabulate
import os

# Clase para representar un producto en el sistema
class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id          # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio unitario
        self.cantidad = cantidad  # Cantidad en inventario

# Clase para representar un empleado en el sistema
class Empleado:
    def __init__(self, id, nombre, cargo, salario):
        self.id = id          # Identificador único del empleado
        self.nombre = nombre  # Nombre del empleado
        self.cargo = cargo    # Cargo del empleado
        self.salario = salario  # Salario mensual

# Clase para representar una venta en el sistema
class Venta:
    def __init__(self, id, fecha, total):
        self.id = id          # Identificador único de la venta
        self.fecha = fecha    # Fecha y hora de la venta
        self.total = total    # Monto total de la venta
        self.detalles = []    # Lista para almacenar los detalles de la venta

# Clase para representar el detalle de una venta
class DetalleVenta:
    def __init__(self, producto_id, cantidad, precio_unitario):
        self.producto_id = producto_id        # ID del producto vendido
        self.cantidad = cantidad              # Cantidad vendida
        self.precio_unitario = precio_unitario  # Precio unitario al momento de la venta

# Clase principal que maneja la lógica del negocio
class SistemaTienda:
    def __init__(self):
        # Inicialización de las estructuras de datos principales
        self.productos = []  # Lista para almacenar productos
        self.empleados = []  # Lista para almacenar empleados
        self.ventas = []     # Lista para almacenar ventas
        
        # Contadores para generar IDs únicos
        self.contador_productos = 1
        self.contador_empleados = 1
        self.contador_ventas = 1

    # Método para agregar un nuevo producto al sistema
    def agregar_producto(self, nombre, precio, cantidad):
        try:
            # Crear nuevo producto y agregarlo a la lista
            producto = Producto(self.contador_productos, nombre, precio, cantidad)
            self.productos.append(producto)
            self.contador_productos += 1
            return True, "Producto agregado exitosamente"
        except Exception as e:
            return False, f"Error al agregar producto: {e}"

    # Método para realizar una venta de productos
    def vender_producto(self, producto_id, cantidad):
        try:
            # Buscar el producto por ID
            producto = next((p for p in self.productos if p.id == producto_id), None)
            
            # Validar que el producto exista
            if not producto:
                return False, "Producto no encontrado"
            
            # Validar stock suficiente
            if producto.cantidad < cantidad:
                return False, "Stock insuficiente"

            # Actualizar el stock
            producto.cantidad -= cantidad
            
            # Crear la venta
            total = producto.precio * cantidad
            venta = Venta(self.contador_ventas, datetime.now(), total)
            
            # Agregar detalle de la venta
            detalle = DetalleVenta(producto_id, cantidad, producto.precio)
            venta.detalles.append(detalle)
            
            # Guardar la venta
            self.ventas.append(venta)
            self.contador_ventas += 1
            
            return True, f"Venta realizada exitosamente. Total: ${total:.2f}"
        except Exception as e:
            return False, f"Error al realizar la venta: {e}"

    # Método para mostrar el inventario actual
    def mostrar_inventario(self):
        try:
            if not self.productos:
                print("\nNo hay productos en el inventario")
                return
                
            # Formatear y mostrar los datos en una tabla
            datos = [[p.id, p.nombre, f"${p.precio:.2f}", p.cantidad] for p in self.productos]
            headers = ["ID", "Nombre", "Precio", "Cantidad"]
            print("\n=== INVENTARIO ===")
            print(tabulate(datos, headers=headers, tablefmt="grid"))
        except Exception as e:
            print(f"\nError al mostrar inventario: {e}")

    # Método para agregar un nuevo empleado al sistema
    def agregar_empleado(self, nombre, cargo, salario):
        try:
            # Crear nuevo empleado y agregarlo a la lista
            empleado = Empleado(self.contador_empleados, nombre, cargo, salario)
            self.empleados.append(empleado)
            self.contador_empleados += 1
            return True, "Empleado agregado exitosamente"
        except Exception as e:
            return False, f"Error al agregar empleado: {e}"

    # Método para mostrar la nómina actual
    def mostrar_nomina(self):
        try:
            if not self.empleados:
                print("\nNo hay empleados registrados")
                return
                
            # Formatear y mostrar los datos en una tabla
            datos = [[e.id, e.nombre, e.cargo, f"${e.salario:.2f}"] for e in self.empleados]
            headers = ["ID", "Nombre", "Cargo", "Salario"]
            print("\n=== NÓMINA ===")
            print(tabulate(datos, headers=headers, tablefmt="grid"))
        except Exception as e:
            print(f"\nError al mostrar nómina: {e}")

    # Método para mostrar el historial de ventas
    def mostrar_ventas(self):
        try:
            if not self.ventas:
                print("\nNo hay ventas registradas")
                return
                
            # Formatear y mostrar los datos en una tabla
            datos = [[v.id, v.fecha.strftime("%Y-%m-%d %H:%M:%S"), f"${v.total:.2f}"] for v in self.ventas]
            headers = ["ID", "Fecha", "Total"]
            print("\n=== HISTORIAL DE VENTAS ===")
            print(tabulate(datos, headers=headers, tablefmt="grid"))
        except Exception as e:
            print(f"\nError al mostrar ventas: {e}")

# Clase para manejar la interfaz de consola
class SistemaTiendaConsola:
    def __init__(self):
        self.sistema = SistemaTienda()

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_menu_principal(self):
        self.limpiar_pantalla()
        print("\n=== SISTEMA DE GESTIÓN ===")
        print("1. Gestión de Productos")
        print("2. Gestión de Ventas")
        print("3. Gestión de Nómina")
        print("4. Ver Historial de Ventas")
        print("5. Salir")
        return input("\nSeleccione una opción: ")

    def menu_productos(self):
        while True:
            self.limpiar_pantalla()
            print("\n=== GESTIÓN DE PRODUCTOS ===")
            print("1. Ver Inventario")
            print("2. Agregar Producto")
            print("3. Volver al Menú Principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.sistema.mostrar_inventario()
                input("\nPresione Enter para continuar...")
            elif opcion == "2":
                self.agregar_producto()
            elif opcion == "3":
                break
            else:
                print("\nOpción no válida")
                input("\nPresione Enter para continuar...")

    def menu_ventas(self):
        while True:
            self.limpiar_pantalla()
            print("\n=== GESTIÓN DE VENTAS ===")
            print("1. Ver Inventario")
            print("2. Realizar Venta")
            print("3. Volver al Menú Principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.sistema.mostrar_inventario()
                input("\nPresione Enter para continuar...")
            elif opcion == "2":
                self.realizar_venta()
            elif opcion == "3":
                break
            else:
                print("\nOpción no válida")
                input("\nPresione Enter para continuar...")

    def menu_nomina(self):
        while True:
            self.limpiar_pantalla()
            print("\n=== GESTIÓN DE NÓMINA ===")
            print("1. Ver Nómina")
            print("2. Agregar Empleado")
            print("3. Volver al Menú Principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.sistema.mostrar_nomina()
                input("\nPresione Enter para continuar...")
            elif opcion == "2":
                self.agregar_empleado()
            elif opcion == "3":
                break
            else:
                print("\nOpción no válida")
                input("\nPresione Enter para continuar...")

    def agregar_producto(self):
        self.limpiar_pantalla()
        print("\n=== AGREGAR PRODUCTO ===")
        
        try:
            nombre = input("\nNombre del producto: ")
            precio = float(input("Precio: $"))
            cantidad = int(input("Cantidad: "))

            if not nombre or precio <= 0 or cantidad <= 0:
                print("\nError: Por favor ingrese valores válidos")
                input("\nPresione Enter para continuar...")
                return

            success, message = self.sistema.agregar_producto(nombre, precio, cantidad)
            print(f"\n{message}")
            input("\nPresione Enter para continuar...")
        except ValueError:
            print("\nError: Por favor ingrese valores numéricos válidos")
            input("\nPresione Enter para continuar...")

    def realizar_venta(self):
        self.limpiar_pantalla()
        print("\n=== REALIZAR VENTA ===")
        
        try:
            self.sistema.mostrar_inventario()
            producto_id = int(input("\nID del producto: "))
            cantidad = int(input("Cantidad: "))

            if cantidad <= 0:
                print("\nError: La cantidad debe ser mayor a 0")
                input("\nPresione Enter para continuar...")
                return

            success, message = self.sistema.vender_producto(producto_id, cantidad)
            print(f"\n{message}")
            input("\nPresione Enter para continuar...")
        except ValueError:
            print("\nError: Por favor ingrese valores numéricos válidos")
            input("\nPresione Enter para continuar...")

    def agregar_empleado(self):
        self.limpiar_pantalla()
        print("\n=== AGREGAR EMPLEADO ===")
        
        try:
            nombre = input("\nNombre del empleado: ")
            cargo = input("Cargo: ")
            salario = float(input("Salario: $"))

            if not nombre or not cargo or salario <= 0:
                print("\nError: Por favor ingrese valores válidos")
                input("\nPresione Enter para continuar...")
                return

            success, message = self.sistema.agregar_empleado(nombre, cargo, salario)
            print(f"\n{message}")
            input("\nPresione Enter para continuar...")
        except ValueError:
            print("\nError: Por favor ingrese valores numéricos válidos")
            input("\nPresione Enter para continuar...")

    def ejecutar(self):
        while True:
            opcion = self.mostrar_menu_principal()
            
            if opcion == "1":
                self.menu_productos()
            elif opcion == "2":
                self.menu_ventas()
            elif opcion == "3":
                self.menu_nomina()
            elif opcion == "4":
                self.sistema.mostrar_ventas()
                input("\nPresione Enter para continuar...")
            elif opcion == "5":
                print("\n¡Gracias por usar el sistema!")
                break
            else:
                print("\nOpción no válida")
                input("\nPresione Enter para continuar...")

# Punto de entrada del programa
if __name__ == "__main__":
    app = SistemaTiendaConsola()
    app.ejecutar() 