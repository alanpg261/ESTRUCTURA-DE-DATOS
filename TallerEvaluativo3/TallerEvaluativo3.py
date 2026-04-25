#SISTEMA DE VALORACIÓN DE  INVENTARIO DE INVENTARIO DE HARDWARE

#Entrada de datos
def CargarProductos():
    cantidad = 0
    productos = {}
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de productos que desea ingresar: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
        
    for i in range(cantidad):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        id_producto = input("Ingrese el ID del producto: ")
        productos[id_producto] = (nombre, precio)

    return productos

def ListarProductos(productos):
    print("Listado de productos:")
    for id_producto, (nombre, precio) in productos.items():
        print(f"ID: {id_producto}\n Nombre: {nombre}\n Precio: {precio}\n")


# REQUERIMIENTO 2: Control de Pedidos por Cliente
#Función que captura clientes y sus artículos adquiridos con validación y precios
def entrada_datos_clientes(productos):
    
    clientes_pedidos = {}
    
    while True:
        try:
            cantidad_clientes = int(input("\n¿Cuántos clientes se atenderán? "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    for i in range(cantidad_clientes):
        nombre_cliente = input(f"\nIngrese el nombre del cliente {i+1}: ")
        
        while True:
            try:
                cantidad_articulos = int(input(f"¿Cuántos artículos adquirió {nombre_cliente}? "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        articulos = []
        for j in range(cantidad_articulos):
            while True:
                nombre_producto = input(f"Ingrese el nombre del producto {j+1}: ")
                
                # Validar que el producto exista en el catálogo y obtener su precio
                precio_encontrado = None
                for i, (nombre_prod, precio_prod) in productos.items():
                    if nombre_prod.lower() == nombre_producto.lower():
                        precio_encontrado = precio_prod
                        break
                
                if precio_encontrado is not None:
                    articulo = {
                        "nombre": nombre_producto,
                        "precio": precio_encontrado
                    }
                    articulos.append(articulo)
                    break
                else:
                    print(f"El producto '{nombre_producto}' no existe en el catálogo. Intente de nuevo.")
        
        clientes_pedidos[nombre_cliente] = articulos
    
    return clientes_pedidos

#Función que imprime el resumen de despacho con precios
def visualizacion_despacho(clientes_pedidos):
    
    print("\n" + "="*80)
    print("RESUMEN DE DESPACHO")
    print("="*80)
    print(f"{'CLIENTE':<25} {'ARTÍCULOS':<30} {'PRECIO UNITARIO':<15} {'TOTAL VENTA':<15}")
    print("-"*80)
    
    for cliente, articulos in clientes_pedidos.items():
        total_venta = sum(articulo["precio"] for articulo in articulos)
        
        if articulos:
            # Mostrar primer artículo con cliente
            primer_articulo = articulos[0]
            print(f"{cliente:<25} {primer_articulo['nombre']:<30} ${primer_articulo['precio']:<14.2f} ${total_venta:<14.2f}")
            
            # Mostrar resto de artículos
            for articulo in articulos[1:]:
                print(f"{'':25} {articulo['nombre']:<30} ${articulo['precio']:<14.2f}")
        else:
            print(f"{cliente:<25} {'(sin artículos)':30}")
    
    print("="*80)

# REQUERIMIENTO 3: Registro de bitacora geográfica
#Función que captura ubicaciones geográficas
def entrada_datos_geograficos():
    while True:
        opcion = input("\n¿Desea ingresar una ubicación geográfica? (s/n): ").lower()
        if opcion == "s":
            ubicaciones = []
            while True:
                nombre_ubicacion = input("\nIngrese el nombre de la ubicación geográfica (o 'salir' para finalizar): ")
                if nombre_ubicacion.lower() == 'salir':
                    break
                while True:
                    try:
                        latitud = float(input("Ingrese la latitud de la ubicación: "))
                        longitud = float(input("Ingrese la longitud de la ubicación: "))
                        break
                    except ValueError:
                        print("Por favor, ingrese números válidos para las coordenadas.")
                
                ubicacion = {
                    "sitio": nombre_ubicacion,
                    "coordenadas": (latitud, longitud)
                }
                ubicaciones.append(ubicacion)
            return ubicaciones
        elif opcion == "n":
            return []
        else:
            print("Por favor, ingrese 's' para sí o 'n' para no.")

#Función que imprime una tabla visual de ubicaciones geográficas
def visualizacion_ubicaciones(ubicaciones):
    print("\n" + "="*80)
    print("TABLA DE UBICACIONES GEOGRÁFICAS")
    print("="*80)
    print(f"{'SITIO':<30} {'LATITUD':<25} {'LONGITUD':<25}")
    print("-"*80)
    
    for ubicacion in ubicaciones:
        sitio = ubicacion["sitio"]
        latitud, longitud = ubicacion["coordenadas"]
        print(f"{sitio:<30} {latitud:<25.6f} {longitud:<25.6f}")
    
    print("="*80)

# Función principal para ejecutar el programa
def main():
    print("SISTEMA DE VALORACIÓN DE INVENTARIO DE HARDWARE")
    print("="*50)
    
    # Requerimiento 1: Inventario de Hardware
    productos = CargarProductos()
    ListarProductos(productos)
    
    # Requerimiento 2: Control de Pedidos por Cliente
    clientes_pedidos = entrada_datos_clientes(productos)
    visualizacion_despacho(clientes_pedidos)
    
    # Requerimiento 3: Registro de bitacora geográfica
    ubicaciones = entrada_datos_geograficos()
    visualizacion_ubicaciones(ubicaciones)

if __name__ == "__main__":
    main()