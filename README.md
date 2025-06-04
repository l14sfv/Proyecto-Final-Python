# Sistema de Gestión de Tienda

Este es un sistema de gestión de tienda desarrollado en Python que permite manejar productos, ventas y nómina de empleados utilizando estructuras de datos en memoria.

## Características

- Gestión de productos (inventario)
- Sistema de ventas
- Gestión de nómina de empleados
- Almacenamiento en memoria usando estructuras de datos de Python

## Requisitos

- Python 3.6 o superior
- Dependencias de Python (ver requirements.txt)

## Instalación

1. Clonar o descargar el repositorio
2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Ejecutar el programa:
```bash
python sistema_tienda.py
```

2. Seguir las instrucciones del menú principal:
   - Gestión de Productos
   - Gestión de Ventas
   - Gestión de Nómina
   - Ver Historial de Ventas

## Estructura del Proyecto

- `sistema_tienda.py`: Archivo principal del sistema
- `requirements.txt`: Dependencias del proyecto

## Funcionalidades

### Gestión de Productos
- Agregar nuevos productos
- Ver inventario actual
- Control de stock

### Gestión de Ventas
- Realizar ventas
- Ver inventario antes de vender
- Registro automático de ventas
- Historial de ventas

### Gestión de Nómina
- Agregar empleados
- Ver lista de empleados
- Control de salarios

## Estructuras de Datos Utilizadas

- Listas para almacenar productos, empleados y ventas
- Clases para modelar entidades (Producto, Empleado, Venta, DetalleVenta)
- Manejo de fechas y horas para el registro de ventas 