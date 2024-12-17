
# Sistema de Gesitón de Inventario

Este *sistema de gestión de inventario* permite a los usuarios **registrar, actualizar, eliminar, buscar y listar productos** en una base de datos *SQLite*. También incluye *funcionalidades* para **generar reportes de productos con bajo stock y vaciar el inventario completo**. El sistema está *diseñado para ser ejecutado* en la *terminal*, con una interfaz de usuario *interactiva y sencilla*.

## Requisitos

+ Python 3.x;
+ Librería *colorama* para la coloración del texto en la terminal;
+ Base de datos SQLite3 (automáticamente creada en el directorio de ejecución).

## Instalación

*Pasos requeridos*:

+ pip install python
+ pip install colorama
+ git clone https://example.com
+ cd ../ruta/al/archivo
+ python inventario.py

## Funcionalidades

- **Registrar Producto**: Permite ingresar un nuevo producto al inventario, solicitando el código, nombre, precio, cantidad en stock y categoría. Se verifica que los datos sean válidos y que el código del producto no esté duplicado.

- **Actualizar producto**: Permite actualizar los detalles de un producto existente en el inventario. Se puede modificar el nombre, precio, cantidad en stock y categoría del producto seleccionado mediante su código.

- **Eliminar producto**: Permite eliminar un producto del inventario utilizando su código. Si el producto no existe, se muestra un mensaje de error.

- **Mostrar producto**: Muestra todos los productos almacenados en el inventario, incluyendo su código, nombre, precio, cantidad en stock y categoría.

- **Buscar producto**: Permite buscar productos por su código o nombre. Se muestran los productos que coincidan con la búsqueda.

- **Generar Reporte de Stock Bajo**: Permite generar un reporte de productos cuyo stock sea inferior a una cantidad mínima especificada por el usuario.

- **Vaciar Inventario**: Permite eliminar todos los productos del inventario de forma irreversible. Se solicita confirmación antes de realizar esta acción.

- **Salir**: Cierra el sistema de gestión de inventario.

## Estructura de la Base de Datos

La base de datos SQLite se crea **automáticamente** al ejecutar el *script* y contiene una tabla llamada *productos* con la siguiente estructura:

| Columna   | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| codigo    | `TEXT`   | Código único del producto  |
| nombre    | `TEXT`   | Nombre del producto        |
| precio    | `REAL`   | Precio del producto        |
| cantidad  | `INTEGER`| Cantidad del producto      |
| categoria | `TEXT`   | Cateogoría del producto    |


## Tecnologías

**Backend**: Python

**Almacenamiento**: SQLite3