# Importaciones necesarias para el sistema
import datetime

# Estructuras de datos principales para almacenar la información
productos = []  # Lista para almacenar los productos del inventario
ventas = []     # Lista para almacenar el historial de ventas
empleados = []  # Lista para almacenar la información de empleados

# Diccionario que define los rangos de comisión para los empleados
RANGOS_COMISION = {
    1: 0.08,  # 8% de comisión para el rango 1
    2: 0.20,  # 20% de comisión para el rango 2
    3: 0.35,  # 35% de comisión para el rango 3
    4: 0.50   # 50% de comisión para el rango 4
}

# Función para generar IDs únicos para productos
def generarIdProducto():
    return len(productos) + 1

# Función para generar IDs únicos para empleados
def generarIdEmpleado():
    return len(empleados) + 1

# Función para agregar un nuevo producto al inventario
def agregarProducto():
    print("\n Agregar Nuevo Producto")
    nombre = input("Nombre del producto: ")
    categoria = input("Categoria ej:(Mujer, Hombre, Niños): ")
    
    try:
        precio = float(input("Precio $: "))
        stock = int(input("Cantidad en stock: ")) 
 
    except ValueError:
        print("Precio o cantidad invalidos. intenta de nuevo\n")
        return

    # Crear diccionario con la información del producto
    producto = {
        "id" : generarIdProducto(),
        "nombre" : nombre,
        "precio" : precio,
        "stock" : stock,
        "categoria" : categoria        
    }
    # Agregar el producto a la lista de productos
    productos.append(producto)
    print(f"Producto '{nombre}' agregado correctamente .... \n")
    
# Función para mostrar todos los productos en el inventario
def listarProductos():
    if not productos:
        print("\n no hay productos registrados")
        return 
    
    print("\n Inventario de Productos: ")
    for i in productos:
        print(f"ID: {i['id']} - {i['nombre']} - ${i['precio']:.2f} - {i['stock']} - {i['categoria']}")
    print()

# Función para buscar productos por nombre
def buscarProductos():
    criterio = input(" \n Ingresa nombre o parte del nombre del producto a buscar: ")
    # Buscar productos que coincidan con el criterio de búsqueda
    resultados = [i for i in productos if criterio in i['nombre'].lower()]
    if resultados:
        print("\n Productos encontrados: ")
        for i in resultados:
            print(f"ID: {i['id']} - {i['nombre']} - ${i['precio']:.2f} - {i['stock']} - {i['categoria']}")
        print()
    else:
        print("no se econtraron coincidencias \n")
        
#VENTAS--------------------------------- Registro de ventas

def realizarVentas():
    listarProductos()
    try:
        idProducto = int(input("Ingrese el id a vender: "))
        cantidad = int(input("cantidad a vender: "))
        cliente = input("Ingrese el nombre del cliente: ")
        idEmpleado = int(input("Ingrese el ID del empleado que realiza la venta: "))
    except ValueError:
        print("entrada invalida. Use numeros para id y cantidad \n")
        return
    #buscar producto por id
    producto = next((p for p in productos if p['id'] == idProducto), None)
    empleado = next((e for e in empleados if e['id'] == idEmpleado), None)
    
    if not producto:
        print("producto no encontrado \n")
        return
    if not empleado:
        print("empleado no encontrado \n")
        return
    if producto['stock'] < cantidad:
        print(f" stock insuficiente. solo quedan {producto['stock']} unidades ")
        return
    
    #calcular el total de la venta y actualizar el inventario
    total = cantidad * producto['precio']
    producto['stock'] -= cantidad
    
    # Calcular comisión según rango del empleado
    comision = total * RANGOS_COMISION[empleado['rango']]
    
    venta = {
        "cliente" : cliente,
        "producto" : producto['nombre'],
        "cantidad" : cantidad,
        "total" : total,
        "fecha" : datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        "empleado_id" : idEmpleado,
        "comision" : comision
    }
    #agragegar a la lista ventas
    ventas.append(venta)
    print(f"venta registrada con exito. Total: ${total:.2f}")
    print(f"Comisión del empleado: ${comision:.2f}\n")
    
    
def verHistorialVentas():
    print("\n HISTORIAL DE VENTAS CALZADO \n")
    if len(ventas) == 0:
        print("No hay ventas para mostrar")
    else:
        for i, vent in enumerate(ventas, 1):
            empleado = next((e for e in empleados if e['id'] == vent['empleado_id']), None)
            nombre_empleado = empleado['nombre'] if empleado else "Empleado no encontrado"
            print(f"{i}. {vent['cliente']} - {vent['producto']} - {vent['cantidad']} - ${vent['total']:.2f} - {vent['fecha']} - Vendedor: {nombre_empleado} - Comisión: ${vent['comision']:.2f}")
    
# Funciones para gestión de empleados y nómina
def agregarEmpleado():
    print("\n Agregar Nuevo Empleado")
    nombre = input("Nombre del empleado: ")
    cargo = input("Cargo del empleado: ")
    
    try:
        salario_base = float(input("Salario base $: "))
        rango = int(input("Rango de comisión (1-4): "))
        
        if rango not in RANGOS_COMISION:
            print("Rango inválido. Debe ser entre 1 y 4\n")
            return
            
    except ValueError:
        print("Valores inválidos. Intente de nuevo\n")
        return
        
    empleado = {
        "id": generarIdEmpleado(),
        "nombre": nombre,
        "cargo": cargo,
        "salario_base": salario_base,
        "rango": rango,
        "comisiones_mes": 0.0
    }
    
    empleados.append(empleado)
    print(f"Empleado '{nombre}' agregado correctamente\n")

def listarEmpleados():
    if not empleados:
        print("\nNo hay empleados registrados")
        return
        
    print("\n Nómina de Empleados: ")
    for e in empleados:
        print(f"ID: {e['id']} - {e['nombre']} - {e['cargo']} - Salario Base: ${e['salario_base']:.2f} - Rango: {e['rango']} ({RANGOS_COMISION[e['rango']]*100}%)")
    print()

def calcularNominaMensual():
    if not empleados:
        print("\nNo hay empleados registrados")
        return
        
    print("\n Nómina Mensual: ")
    for e in empleados:
        # Obtener ventas del mes actual para este empleado
        mes_actual = datetime.datetime.now().month
        ventas_mes = [v for v in ventas if v['empleado_id'] == e['id'] and 
                    datetime.datetime.strptime(v['fecha'], "%d/%m/%Y, %H:%M:%S").month == mes_actual]
        
        # Calcular comisiones del mes
        comisiones_mes = sum(v['comision'] for v in ventas_mes)
        
        # Calcular salario total
        salario_total = e['salario_base'] + comisiones_mes
        
        print(f"\nEmpleado: {e['nombre']}")
        print(f"Cargo: {e['cargo']}")
        print(f"Salario Base: ${e['salario_base']:.2f}")
        print(f"Comisiones del mes: ${comisiones_mes:.2f}")
        print(f"Salario Total: ${salario_total:.2f}")
        print("-" * 50)

def mostrarMenu():
    print("\n TIENDA DE CALZADO")
    print("\nMenu de opciones CALZADO")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Realizar venta")
    print("5. Ver historial de ventas")
    print("6. Gestión de Empleados")
    print("7. Calcular Nómina Mensual")
    print("8. Salir")

def menuEmpleados():
    while True:
        print("\n GESTIÓN DE EMPLEADOS")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            agregarEmpleado()
        elif opcion == "2":
            listarEmpleados()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")

def ejecutarPrograma():
    while True:
        mostrarMenu()
        try:
            opcion = int(input(f"ingrese una opcion del (1-8): "))

            if opcion == 1:
                agregarProducto()
            elif opcion == 2:
                listarProductos()
            elif opcion == 3:
                buscarProductos()
            elif opcion == 4:
                realizarVentas()
            elif opcion == 5:
                verHistorialVentas()
            elif opcion == 6:
                menuEmpleados()
            elif opcion == 7:
                calcularNominaMensual()
            elif opcion == 8:
                print("Saliendo de la aplicacion")
                break
            else:
                print("opcion invalida, intente de nuevo")
        except ValueError:
            print("Por favor ingrese un número válido")

ejecutarPrograma()
