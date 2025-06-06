import customtkinter as ctk
import datetime
from tkinter import messagebox

class TiendaCustomTkinter:
    def __init__(self):
        self.productos = []
        self.ventas = []
        self.empleados = []
        
        # Configuración de la ventana principal
        self.root = ctk.CTk()
        self.root.title("Tienda de Calzado Luna")
        self.root.geometry("1000x600")
        
        # Rangos de comisión
        self.RANGOS_COMISION = {
            1: {"ventas_min": 1, "ventas_max": 1000000, "porcentaje": 0.08},
            2: {"ventas_min": 1000001, "ventas_max": 3000000, "porcentaje": 0.20},
            3: {"ventas_min": 3000001, "ventas_max": 6000000, "porcentaje": 0.35},
            4: {"ventas_min": 6000001, "ventas_max": float('inf'), "porcentaje": 0.50}
        }
        
        # Categorías de calzado
        self.CATEGORIAS = {
            1: "Tennis",
            2: "Running",
            3: "Workout",
            4: "Casual",
            5: "Fútbol",
            6: "Rugby",
            7: "Golf"
        }
        
        # Configurar el tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Crear pestañas
        self.tabview = ctk.CTkTabview(self.root)
        self.tabview.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Agregar pestañas
        self.tab_productos = self.tabview.add("Productos")
        self.tab_ventas = self.tabview.add("Ventas")
        self.tab_empleados = self.tabview.add("Empleados")
        self.tab_reportes = self.tabview.add("Reportes")
        
        # Configurar cada pestaña
        self.setup_productos_tab()
        self.setup_ventas_tab()
        self.setup_empleados_tab()
        self.setup_reportes_tab()

    def setup_productos_tab(self):
        """Configura la pestaña de productos con formulario y lista de inventario"""
        # Frame para el formulario
        form_frame = ctk.CTkFrame(self.tab_productos)
        form_frame.pack(padx=20, pady=20, fill="x")
        
        # Título
        ctk.CTkLabel(form_frame, text="Agregar Producto", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Campos del formulario
        ctk.CTkLabel(form_frame, text="Nombre:").pack()
        self.nombre_producto = ctk.CTkEntry(form_frame)
        self.nombre_producto.pack(pady=5)
        
        ctk.CTkLabel(form_frame, text="Categoría:").pack()
        self.categoria_producto = ctk.CTkComboBox(form_frame, values=list(self.CATEGORIAS.values()))
        self.categoria_producto.pack(pady=5)
        
        ctk.CTkLabel(form_frame, text="Precio:").pack()
        self.precio_producto = ctk.CTkEntry(form_frame)
        self.precio_producto.pack(pady=5)
        
        ctk.CTkLabel(form_frame, text="Stock:").pack()
        self.stock_producto = ctk.CTkEntry(form_frame)
        self.stock_producto.pack(pady=5)
        
        # Botón para agregar
        ctk.CTkButton(form_frame, text="Agregar Producto", command=self.agregar_producto).pack(pady=20)
        
        # Frame para la lista de productos
        list_frame = ctk.CTkFrame(self.tab_productos)
        list_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Título de la lista
        ctk.CTkLabel(list_frame, text="Inventario", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Lista de productos
        self.lista_productos = ctk.CTkTextbox(list_frame, height=200)
        self.lista_productos.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Botón para actualizar lista
        ctk.CTkButton(list_frame, text="Actualizar Lista", command=self.actualizar_lista_productos).pack(pady=10)

    def setup_ventas_tab(self):
        """Configura la pestaña de ventas con formulario y lista de ventas"""
        # Frame para el formulario de venta
        form_frame = ctk.CTkFrame(self.tab_ventas)
        form_frame.pack(padx=20, pady=20, fill="x")
        
        # Título
        ctk.CTkLabel(form_frame, text="Realizar Venta", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Campos del formulario
        ctk.CTkLabel(form_frame, text="ID Producto:").pack()
        self.id_venta_producto = ctk.CTkEntry(form_frame)
        self.id_venta_producto.pack(pady=5)
        
        ctk.CTkLabel(form_frame, text="Cantidad:").pack()
        self.cantidad_venta = ctk.CTkEntry(form_frame)
        self.cantidad_venta.pack(pady=5)
        
        ctk.CTkLabel(form_frame, text="Cliente:").pack()
        self.cliente_venta = ctk.CTkEntry(form_frame)
        self.cliente_venta.pack(pady=5)
        
        # Botón para realizar venta
        ctk.CTkButton(form_frame, text="Realizar Venta", command=self.realizar_venta).pack(pady=20)
        
        # Frame para la lista de ventas
        list_frame = ctk.CTkFrame(self.tab_ventas)
        list_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Título de la lista
        ctk.CTkLabel(list_frame, text="Historial de Ventas", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Lista de ventas
        self.lista_ventas = ctk.CTkTextbox(list_frame, height=200)
        self.lista_ventas.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Botón para actualizar lista
        ctk.CTkButton(list_frame, text="Actualizar Lista", command=self.actualizar_lista_ventas).pack(pady=10)

    def setup_empleados_tab(self):
        """Configura la pestaña de empleados con formulario y lista de empleados"""
        # Frame para el formulario
        form_frame = ctk.CTkFrame(self.tab_empleados)
        form_frame.pack(padx=20, pady=20, fill="x")
        
        # Título
        ctk.CTkLabel(form_frame, text="Agregar Empleado", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Campos del formulario
        ctk.CTkLabel(form_frame, text="Nombre:").pack()
        self.nombre_empleado = ctk.CTkEntry(form_frame)
        self.nombre_empleado.pack(pady=5)
        
        ctk.CTkLabel(form_frame, text="Cargo:").pack()
        self.cargo_empleado = ctk.CTkEntry(form_frame)
        self.cargo_empleado.pack(pady=5)
        
        ctk.CTkLabel(form_frame, text="Salario Base:").pack()
        self.salario_empleado = ctk.CTkEntry(form_frame)
        self.salario_empleado.pack(pady=5)
        
        # Botón para agregar
        ctk.CTkButton(form_frame, text="Agregar Empleado", command=self.agregar_empleado).pack(pady=20)
        
        # Frame para la lista de empleados
        list_frame = ctk.CTkFrame(self.tab_empleados)
        list_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Título de la lista
        ctk.CTkLabel(list_frame, text="Lista de Empleados", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Lista de empleados
        self.lista_empleados = ctk.CTkTextbox(list_frame, height=200)
        self.lista_empleados.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Botón para actualizar lista
        ctk.CTkButton(list_frame, text="Actualizar Lista", command=self.actualizar_lista_empleados).pack(pady=10)

    def setup_reportes_tab(self):
        """Configura la pestaña de reportes con botones y área de visualización"""
        # Frame para reportes
        report_frame = ctk.CTkFrame(self.tab_reportes)
        report_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Título
        ctk.CTkLabel(report_frame, text="Reportes", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Botones para diferentes reportes
        ctk.CTkButton(report_frame, text="Ver Historial de Ventas", 
                    command=self.mostrar_historial_ventas).pack(pady=10)
        ctk.CTkButton(report_frame, text="Ver Productos con Bajo Stock", 
                    command=self.mostrar_bajo_stock).pack(pady=10)
        
        # Área de visualización de reportes
        self.area_reportes = ctk.CTkTextbox(report_frame, height=300)
        self.area_reportes.pack(padx=10, pady=10, fill="both", expand=True)

    def agregar_producto(self):
        """Agrega un nuevo producto al inventario"""
        try:
            nombre = self.nombre_producto.get()
            categoria = self.categoria_producto.get()
            precio = float(self.precio_producto.get())
            stock = int(self.stock_producto.get())
            
            producto = {
                "id": len(self.productos) + 1,
                "nombre": nombre,
                "categoria": categoria,
                "precio": precio,
                "stock": stock
            }
            
            self.productos.append(producto)
            self.actualizar_lista_productos()
            
            # Limpiar campos
            self.nombre_producto.delete(0, 'end')
            self.precio_producto.delete(0, 'end')
            self.stock_producto.delete(0, 'end')
            
            messagebox.showinfo("Éxito", "Producto agregado exitosamente!")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos")

    def actualizar_lista_productos(self):
        """Actualiza la lista de productos en la interfaz"""
        self.lista_productos.delete("1.0", "end")
        if not self.productos:
            self.lista_productos.insert("end", "No hay productos en el inventario\n")
        else:
            for p in self.productos:
                self.lista_productos.insert("end", 
                    f"ID: {p['id']}\n"
                    f"Nombre: {p['nombre']}\n"
                    f"Categoría: {p['categoria']}\n"
                    f"Precio: ${p['precio']:.2f}\n"
                    f"Stock: {p['stock']}\n"
                    f"{'='*30}\n"
                )

    def realizar_venta(self):
        """Procesa una nueva venta"""
        try:
            id_producto = int(self.id_venta_producto.get())
            cantidad = int(self.cantidad_venta.get())
            cliente = self.cliente_venta.get()
            
            producto = next((p for p in self.productos if p['id'] == id_producto), None)
            if not producto:
                messagebox.showerror("Error", "Producto no encontrado")
                return
            
            if producto['stock'] < cantidad:
                messagebox.showerror("Error", f"Stock insuficiente. Solo quedan {producto['stock']} unidades")
                return
            
            total = cantidad * producto['precio']
            producto['stock'] -= cantidad
            
            venta = {
                "id": len(self.ventas) + 1,
                "cliente": cliente,
                "producto": producto['nombre'],
                "cantidad": cantidad,
                "total": total,
                "fecha": datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            }
            
            self.ventas.append(venta)
            self.actualizar_lista_ventas()
            self.actualizar_lista_productos()
            
            # Limpiar campos
            self.id_venta_producto.delete(0, 'end')
            self.cantidad_venta.delete(0, 'end')
            self.cliente_venta.delete(0, 'end')
            
            messagebox.showinfo("Éxito", f"Venta realizada exitosamente!\nTotal: ${total:.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos")

    def actualizar_lista_ventas(self):
        """Actualiza la lista de ventas en la interfaz"""
        self.lista_ventas.delete("1.0", "end")
        if not self.ventas:
            self.lista_ventas.insert("end", "No hay ventas registradas\n")
        else:
            for v in self.ventas:
                self.lista_ventas.insert("end",
                    f"ID: {v['id']}\n"
                    f"Cliente: {v['cliente']}\n"
                    f"Producto: {v['producto']}\n"
                    f"Cantidad: {v['cantidad']}\n"
                    f"Total: ${v['total']:.2f}\n"
                    f"Fecha: {v['fecha']}\n"
                    f"{'='*30}\n"
                )

    def agregar_empleado(self):
        """Agrega un nuevo empleado al sistema"""
        try:
            nombre = self.nombre_empleado.get()
            cargo = self.cargo_empleado.get()
            salario = float(self.salario_empleado.get())
            
            empleado = {
                "id": len(self.empleados) + 1,
                "nombre": nombre,
                "cargo": cargo,
                "salario_base": salario
            }
            
            self.empleados.append(empleado)
            self.actualizar_lista_empleados()
            
            # Limpiar campos
            self.nombre_empleado.delete(0, 'end')
            self.cargo_empleado.delete(0, 'end')
            self.salario_empleado.delete(0, 'end')
            
            messagebox.showinfo("Éxito", "Empleado agregado exitosamente!")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos")

    def actualizar_lista_empleados(self):
        """Actualiza la lista de empleados en la interfaz"""
        self.lista_empleados.delete("1.0", "end")
        if not self.empleados:
            self.lista_empleados.insert("end", "No hay empleados registrados\n")
        else:
            for e in self.empleados:
                self.lista_empleados.insert("end",
                    f"ID: {e['id']}\n"
                    f"Nombre: {e['nombre']}\n"
                    f"Cargo: {e['cargo']}\n"
                    f"Salario Base: ${e['salario_base']:.2f}\n"
                    f"{'='*30}\n"
                )

    def mostrar_historial_ventas(self):
        """Muestra el historial completo de ventas"""
        self.area_reportes.delete("1.0", "end")
        if not self.ventas:
            self.area_reportes.insert("end", "No hay ventas registradas\n")
        else:
            self.area_reportes.insert("end", "HISTORIAL DE VENTAS\n" + "="*30 + "\n\n")
            for v in self.ventas:
                self.area_reportes.insert("end",
                    f"ID: {v['id']}\n"
                    f"Cliente: {v['cliente']}\n"
                    f"Producto: {v['producto']}\n"
                    f"Cantidad: {v['cantidad']}\n"
                    f"Total: ${v['total']:.2f}\n"
                    f"Fecha: {v['fecha']}\n"
                    f"{'='*30}\n"
                )

    def mostrar_bajo_stock(self):
        """Muestra los productos con stock bajo (menos de 5 unidades)"""
        self.area_reportes.delete("1.0", "end")
        productos_bajo_stock = [p for p in self.productos if p['stock'] < 5]
        
        if not productos_bajo_stock:
            self.area_reportes.insert("end", "No hay productos con bajo stock\n")
        else:
            self.area_reportes.insert("end", "PRODUCTOS CON BAJO STOCK\n" + "="*30 + "\n\n")
            for p in productos_bajo_stock:
                self.area_reportes.insert("end",
                    f"ID: {p['id']}\n"
                    f"Nombre: {p['nombre']}\n"
                    f"Categoría: {p['categoria']}\n"
                    f"Stock: {p['stock']}\n"
                    f"{'='*30}\n"
                )

    def run(self):
        """Inicia la aplicación"""
        self.root.mainloop()

if __name__ == "__main__":
    tienda = TiendaCustomTkinter()
    tienda.run() 
