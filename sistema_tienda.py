# Importaciones necesarias para el sistema
import tkinter as tk  # Para la interfaz gráfica
from tkinter import ttk, messagebox  # Componentes adicionales de tkinter
from datetime import datetime  # Para manejar fechas y horas
from tabulate import tabulate  # Para formatear tablas en consola

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
                print("No hay productos en el inventario")
                return
                
            # Formatear y mostrar los datos en una tabla
            datos = [[p.id, p.nombre, p.precio, p.cantidad] for p in self.productos]
            headers = ["ID", "Nombre", "Precio", "Cantidad"]
            print(tabulate(datos, headers=headers, tablefmt="grid"))
        except Exception as e:
            print(f"Error al mostrar inventario: {e}")

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
                print("No hay empleados registrados")
                return
                
            # Formatear y mostrar los datos en una tabla
            datos = [[e.id, e.nombre, e.cargo, e.salario] for e in self.empleados]
            headers = ["ID", "Nombre", "Cargo", "Salario"]
            print(tabulate(datos, headers=headers, tablefmt="grid"))
        except Exception as e:
            print(f"Error al mostrar nómina: {e}")

    # Método para mostrar el historial de ventas
    def mostrar_ventas(self):
        try:
            if not self.ventas:
                print("No hay ventas registradas")
                return
                
            # Formatear y mostrar los datos en una tabla
            datos = [[v.id, v.fecha.strftime("%Y-%m-%d %H:%M:%S"), v.total] for v in self.ventas]
            headers = ["ID", "Fecha", "Total"]
            print(tabulate(datos, headers=headers, tablefmt="grid"))
        except Exception as e:
            print(f"Error al mostrar ventas: {e}")

# Clase que maneja la interfaz gráfica del sistema
class SistemaTiendaGUI:
    def __init__(self):
        # Inicializar el sistema y la ventana principal
        self.sistema = SistemaTienda()
        self.root = tk.Tk()
        self.root.title("Sistema de Gestión")
        self.root.geometry("800x600")
        
        # Configurar estilos de la interfaz
        style = ttk.Style()
        style.configure("TNotebook", background="#f0f0f0")
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0")
        style.configure("TButton", padding=5)
        
        # Configurar la interfaz
        self.setup_gui()

    # Método para configurar la interfaz gráfica
    def setup_gui(self):
        # Crear notebook (pestañas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=5)

        # Configurar cada pestaña
        self.tab_productos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_productos, text='Productos')
        self.setup_productos_tab()

        self.tab_ventas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_ventas, text='Ventas')
        self.setup_ventas_tab()

        self.tab_nomina = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_nomina, text='Nómina')
        self.setup_nomina_tab()

        self.tab_historial = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_historial, text='Historial de Ventas')
        self.setup_historial_tab()

    # Método para configurar la pestaña de productos
    def setup_productos_tab(self):
        # Frame para agregar productos
        frame_agregar = ttk.LabelFrame(self.tab_productos, text="Agregar Producto")
        frame_agregar.pack(fill='x', padx=5, pady=5)

        # Campos del formulario
        ttk.Label(frame_agregar, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_producto = ttk.Entry(frame_agregar)
        self.nombre_producto.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_agregar, text="Precio:").grid(row=1, column=0, padx=5, pady=5)
        self.precio_producto = ttk.Entry(frame_agregar)
        self.precio_producto.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_agregar, text="Cantidad:").grid(row=2, column=0, padx=5, pady=5)
        self.cantidad_producto = ttk.Entry(frame_agregar)
        self.cantidad_producto.grid(row=2, column=1, padx=5, pady=5)

        # Botón para agregar producto
        ttk.Button(frame_agregar, text="Agregar", command=self.agregar_producto).grid(row=3, column=0, columnspan=2, pady=10)

        # Frame para mostrar productos
        frame_lista = ttk.LabelFrame(self.tab_productos, text="Inventario")
        frame_lista.pack(fill='both', expand=True, padx=5, pady=5)

        # Tabla de productos
        self.tree_productos = ttk.Treeview(frame_lista, columns=('ID', 'Nombre', 'Precio', 'Cantidad'), show='headings')
        self.tree_productos.heading('ID', text='ID')
        self.tree_productos.heading('Nombre', text='Nombre')
        self.tree_productos.heading('Precio', text='Precio')
        self.tree_productos.heading('Cantidad', text='Cantidad')
        self.tree_productos.pack(fill='both', expand=True)

    # Método para configurar la pestaña de ventas
    def setup_ventas_tab(self):
        # Frame para realizar ventas
        frame_venta = ttk.LabelFrame(self.tab_ventas, text="Realizar Venta")
        frame_venta.pack(fill='x', padx=5, pady=5)

        # Campos del formulario
        ttk.Label(frame_venta, text="ID Producto:").grid(row=0, column=0, padx=5, pady=5)
        self.id_venta = ttk.Entry(frame_venta)
        self.id_venta.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_venta, text="Cantidad:").grid(row=1, column=0, padx=5, pady=5)
        self.cantidad_venta = ttk.Entry(frame_venta)
        self.cantidad_venta.grid(row=1, column=1, padx=5, pady=5)

        # Botón para realizar venta
        ttk.Button(frame_venta, text="Vender", command=self.realizar_venta).grid(row=2, column=0, columnspan=2, pady=10)

        # Frame para mostrar inventario
        frame_inventario = ttk.LabelFrame(self.tab_ventas, text="Inventario Disponible")
        frame_inventario.pack(fill='both', expand=True, padx=5, pady=5)

        # Tabla de inventario
        self.tree_ventas = ttk.Treeview(frame_inventario, columns=('ID', 'Nombre', 'Precio', 'Cantidad'), show='headings')
        self.tree_ventas.heading('ID', text='ID')
        self.tree_ventas.heading('Nombre', text='Nombre')
        self.tree_ventas.heading('Precio', text='Precio')
        self.tree_ventas.heading('Cantidad', text='Cantidad')
        self.tree_ventas.pack(fill='both', expand=True)

    # Método para configurar la pestaña de nómina
    def setup_nomina_tab(self):
        # Frame para agregar empleados
        frame_agregar = ttk.LabelFrame(self.tab_nomina, text="Agregar Empleado")
        frame_agregar.pack(fill='x', padx=5, pady=5)

        # Campos del formulario
        ttk.Label(frame_agregar, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_empleado = ttk.Entry(frame_agregar)
        self.nombre_empleado.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_agregar, text="Cargo:").grid(row=1, column=0, padx=5, pady=5)
        self.cargo_empleado = ttk.Entry(frame_agregar)
        self.cargo_empleado.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_agregar, text="Salario:").grid(row=2, column=0, padx=5, pady=5)
        self.salario_empleado = ttk.Entry(frame_agregar)
        self.salario_empleado.grid(row=2, column=1, padx=5, pady=5)

        # Botón para agregar empleado
        ttk.Button(frame_agregar, text="Agregar", command=self.agregar_empleado).grid(row=3, column=0, columnspan=2, pady=10)

        # Frame para mostrar empleados
        frame_lista = ttk.LabelFrame(self.tab_nomina, text="Nómina")
        frame_lista.pack(fill='both', expand=True, padx=5, pady=5)

        # Tabla de empleados
        self.tree_empleados = ttk.Treeview(frame_lista, columns=('ID', 'Nombre', 'Cargo', 'Salario'), show='headings')
        self.tree_empleados.heading('ID', text='ID')
        self.tree_empleados.heading('Nombre', text='Nombre')
        self.tree_empleados.heading('Cargo', text='Cargo')
        self.tree_empleados.heading('Salario', text='Salario')
        self.tree_empleados.pack(fill='both', expand=True)

    # Método para configurar la pestaña de historial
    def setup_historial_tab(self):
        # Frame para mostrar historial de ventas
        frame_historial = ttk.LabelFrame(self.tab_historial, text="Historial de Ventas")
        frame_historial.pack(fill='both', expand=True, padx=5, pady=5)

        # Tabla de historial
        self.tree_historial = ttk.Treeview(frame_historial, columns=('ID', 'Fecha', 'Total'), show='headings')
        self.tree_historial.heading('ID', text='ID')
        self.tree_historial.heading('Fecha', text='Fecha')
        self.tree_historial.heading('Total', text='Total')
        self.tree_historial.pack(fill='both', expand=True)

    # Método para agregar un producto desde la interfaz
    def agregar_producto(self):
        try:
            # Obtener y validar datos del formulario
            nombre = self.nombre_producto.get()
            precio = float(self.precio_producto.get())
            cantidad = int(self.cantidad_producto.get())

            # Validar datos
            if not nombre or precio <= 0 or cantidad <= 0:
                messagebox.showerror("Error", "Por favor ingrese valores válidos")
                return

            # Intentar agregar el producto
            success, message = self.sistema.agregar_producto(nombre, precio, cantidad)
            if success:
                messagebox.showinfo("Éxito", message)
                self.actualizar_lista_productos()
                self.limpiar_campos_producto()
            else:
                messagebox.showerror("Error", message)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

    # Método para realizar una venta desde la interfaz
    def realizar_venta(self):
        try:
            # Obtener y validar datos del formulario
            producto_id = int(self.id_venta.get())
            cantidad = int(self.cantidad_venta.get())

            # Validar cantidad
            if cantidad <= 0:
                messagebox.showerror("Error", "La cantidad debe ser mayor a 0")
                return

            # Intentar realizar la venta
            success, message = self.sistema.vender_producto(producto_id, cantidad)
            if success:
                messagebox.showinfo("Éxito", message)
                self.actualizar_lista_productos()
                self.actualizar_historial_ventas()
                self.limpiar_campos_venta()
            else:
                messagebox.showerror("Error", message)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

    # Método para agregar un empleado desde la interfaz
    def agregar_empleado(self):
        try:
            # Obtener y validar datos del formulario
            nombre = self.nombre_empleado.get()
            cargo = self.cargo_empleado.get()
            salario = float(self.salario_empleado.get())

            # Validar datos
            if not nombre or not cargo or salario <= 0:
                messagebox.showerror("Error", "Por favor ingrese valores válidos")
                return

            # Intentar agregar el empleado
            success, message = self.sistema.agregar_empleado(nombre, cargo, salario)
            if success:
                messagebox.showinfo("Éxito", message)
                self.actualizar_lista_empleados()
                self.limpiar_campos_empleado()
            else:
                messagebox.showerror("Error", message)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

    # Método para actualizar la lista de productos en la interfaz
    def actualizar_lista_productos(self):
        # Limpiar lista actual
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)
        
        # Agregar productos actualizados
        for producto in self.sistema.productos:
            self.tree_productos.insert('', 'end', values=(
                producto.id, 
                producto.nombre, 
                f"${producto.precio:.2f}", 
                producto.cantidad
            ))

    # Método para actualizar la lista de empleados en la interfaz
    def actualizar_lista_empleados(self):
        # Limpiar lista actual
        for item in self.tree_empleados.get_children():
            self.tree_empleados.delete(item)
        
        # Agregar empleados actualizados
        for empleado in self.sistema.empleados:
            self.tree_empleados.insert('', 'end', values=(
                empleado.id, 
                empleado.nombre, 
                empleado.cargo, 
                f"${empleado.salario:.2f}"
            ))

    # Método para actualizar el historial de ventas en la interfaz
    def actualizar_historial_ventas(self):
        # Limpiar lista actual
        for item in self.tree_historial.get_children():
            self.tree_historial.delete(item)
        
        # Agregar ventas actualizadas
        for venta in self.sistema.ventas:
            self.tree_historial.insert('', 'end', values=(
                venta.id, 
                venta.fecha.strftime("%Y-%m-%d %H:%M:%S"), 
                f"${venta.total:.2f}"
            ))

    # Método para limpiar los campos del formulario de productos
    def limpiar_campos_producto(self):
        self.nombre_producto.delete(0, tk.END)
        self.precio_producto.delete(0, tk.END)
        self.cantidad_producto.delete(0, tk.END)

    # Método para limpiar los campos del formulario de ventas
    def limpiar_campos_venta(self):
        self.id_venta.delete(0, tk.END)
        self.cantidad_venta.delete(0, tk.END)

    # Método para limpiar los campos del formulario de empleados
    def limpiar_campos_empleado(self):
        self.nombre_empleado.delete(0, tk.END)
        self.cargo_empleado.delete(0, tk.END)
        self.salario_empleado.delete(0, tk.END)

    # Método para iniciar la aplicación
    def run(self):
        self.root.mainloop()

# Punto de entrada del programa
if __name__ == "__main__":
    app = SistemaTiendaGUI()
    app.run() 