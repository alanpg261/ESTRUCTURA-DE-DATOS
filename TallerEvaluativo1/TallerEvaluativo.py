#CREACIÓN Y REGISTRO DE DATOS PARA DROGUERÍA

def registrarProducto():
    nombres = []
    precios = []
    cantidades = []
    fechasVencimiento = []
    presentaciones = []
    proveedores = []

    while True:
        try:     #LEER LOS DATOS INGRESADOS Y VALIDAR QUE SEAN NÚMEROS VÁLIDOS
            cantProductos = int(input("Ingrese la cantidad de medicamentos a registrar: "))
            if cantProductos <= 0:
                print("Debe ser un número positivo.\n")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número válido, sin letras.\n")

    for i in range(cantProductos):
        print(f"\n--- Ingrese datos del medicamento {i+1} ---")
        nombre = input("Nombre del medicamento: ")
        
        while True:
            try:
                precio = float(input("Precio del medicamento: "))
                if precio <= 0:
                    print("El precio debe ser mayor a 0.\n")
                    continue
                break
            except ValueError:
                print("Error: Ingrese un número válido, sin letras.\n")
        
        while True:
            try:
                cantidad = int(input("Cantidad en stock: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0.\n")
                    continue
                break
            except ValueError:
                print("Error: Ingrese un número válido, sin letras.\n")
        
        fechaVencimiento = input("Fecha de vencimiento (DD/MM/YYYY): ")
        presentacion = input("Presentación (ej: tabletas, jarabe, crema, cápsulas): ")
        proveedor = input("Proveedor del medicamento: ")
        #AGREGAR LOS DATOS INGRESADOS A LAS LISTAS CORRESPONDIENTES
        nombres.append(nombre)
        precios.append(precio)
        cantidades.append(cantidad)
        fechasVencimiento.append(fechaVencimiento)
        presentaciones.append(presentacion)
        proveedores.append(proveedor)
    return nombres, precios, cantidades, fechasVencimiento, presentaciones, proveedores, cantProductos

#CALCULAR EL VALOR TOTAL DEL INVENTARIO DE MEDICAMENTOS
def calcularValorInventario(precios, cantidades, cantProductos):
    #VALIDAR LA EXISTENCIA DE MEDICAMENTOS EN EL INVENTARIO
    if cantProductos == None or cantProductos == 0:
        print("No hay medicamentos registrados en el inventario.")
        return
    
    totalInventario = 0
    for i in range(cantProductos):
        totalInventario += precios[i] * cantidades[i]
    print(f"El valor total del inventario de medicamentos es: ${totalInventario:.2f}")

#FUNCIÓN PARA CALCULAR EL PRODUCTO CON EL MAYOR PRECIO EN EL INVENTARIO
def calcularMayorPrecio(precios, nombres, cantProductos):
    if cantProductos == None or cantProductos == 0:
        print("No hay medicamentos registrados en el inventario.")
        return
    
    indice_mayor = 0
    mayor = precios[0]
    for i in range(cantProductos):
        if precios[i] > mayor:
            mayor = precios[i]
            indice_mayor = i
    print(f"El medicamento con el mayor precio es: {nombres[indice_mayor]} - ${mayor:.2f}")

#IMPRIMIR INVENTARIO DE MEDICAMENTOS
def imprimirInventario(nombres, precios, cantidades, fechasVencimiento, presentaciones, proveedores, cantProductos):
    if cantProductos == None or cantProductos == 0:
        print("No hay medicamentos registrados en el inventario.")
        return
    
    print("=" * 80)
    print("INVENTARIO DE MEDICAMENTOS DE LA DROGUERÍA")
    print("=" * 80)
    for i in range(cantProductos):
        print(f"\nMedicamento {i+1}:")
        print(f"  Nombre: {nombres[i]}")
        print(f"  Precio: ${precios[i]:.2f}")
        print(f"  Cantidad en stock: {cantidades[i]}")
        if cantidades[i] < 5:
            print(f"  ⚠️  ALERTA: Stock crítico - Cantidad muy baja")
        print(f"  Fecha de vencimiento: {fechasVencimiento[i]}")
        print(f"  Presentación: {presentaciones[i]}")
        print(f"  Proveedor: {proveedores[i]}")
        print(f"\n {'-' * 80}")

#FUNCION PARA EDITAR LOS DATOS DE UN MEDICAMENTO EXISTENTE EN EL INVENTARIO     
def editarProducto(nombres, precios, cantidades, fechasVencimiento, presentaciones, proveedores, cantProductos):
    if cantProductos == None or cantProductos == 0:
        print("No hay medicamentos registrados en el inventario.")
        return
    #SE MUESTRA EL INVENTARIO PARA SELECCIONAR EL MEDICAMENTO A EDITAR;
    #CON VALIDACIONES DE ENTRADA PARA SELECCIONAR UN NÚMERO VÁLIDO
    while True: 
        imprimirInventario(nombres, precios, cantidades, fechasVencimiento, presentaciones, proveedores, cantProductos)
        try:
            indice = int(input(f"Ingrese el número del medicamento a editar (1-{cantProductos}): ")) - 1
            if indice < 0 or indice >= cantProductos:
                print(f"Error: Ingrese un número entre 1 y {cantProductos}.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número válido, sin letras.")
    #SE PRESENTA UN MENÚ PARA SELECCIONAR EL DATO A EDITAR DEL MEDICAMENTO SELECCIONADO, CON VALIDACIONES DE ENTRADA PARA CADA CAMPO
    while True:
        print(f"\n--- Editar datos del medicamento: {nombres[indice]} ---")
        print("1. Cambiar nombre")
        print("2. Cambiar precio")
        print("3. Cambiar cantidad en stock")
        print("4. Cambiar fecha de vencimiento")
        print("5. Cambiar presentación")
        print("6. Cambiar proveedor")
        print("7. Salir de edición")
        #VALIDAR QUE LA OPCIÓN SELECCIONADA SEA UN NÚMERO VÁLIDO ENTRE 1 Y 7
        try:
            opcion = int(input("Seleccione el dato a editar (1-7): "))
            if opcion < 1 or opcion > 7:
                print("Opción no válida.")
                continue
        except ValueError:
            print("Error: Ingrese un número válido.")
            continue
        
        if opcion == 1:
            nombres[indice] = input("Nuevo nombre del medicamento: ")
            print("✓ Nombre actualizado.")
        #VALIDAR QUE EL NUEVO PRECIO INGRESADO SEA UN NÚMERO VÁLIDO Y MAYOR A 0
        elif opcion == 2:
            while True:
                try:
                    precios[indice] = float(input("Nuevo precio del medicamento: "))
                    if precios[indice] <= 0:
                        print("El precio debe ser mayor a 0.\n")
                        continue
                    print("✓ Precio actualizado.")
                    break
                except ValueError:
                    print("Error: Ingrese un número válido, sin letras.\n")
        #VALIDAR QUE LA NUEVA CANTIDAD EN STOCK INGRESADA SEA UN NÚMERO VÁLIDO Y MAYOR A 0
        elif opcion == 3:
            while True:
                try:
                    cantidades[indice] = int(input("Nueva cantidad en stock: "))
                    if cantidades[indice] <= 0:
                        print("La cantidad debe ser mayor a 0.\n")
                        continue
                    print("✓ Cantidad actualizada.")
                    break
                except ValueError:
                    print("Error: Ingrese un número válido, sin letras.\n")
        #VALIDAR QUE LA NUEVA FECHA DE VENCIMIENTO INGRESADA TENGA EL FORMATO CORRECTO (DD/MM/YYYY)
        elif opcion == 4:
            fechasVencimiento[indice] = input("Nueva fecha de vencimiento (DD/MM/YYYY): ")
            print("✓ Fecha de vencimiento actualizada.")
        #VALIDAR QUE LA NUEVA PRESENTACIÓN INGRESADA NO ESTÉ VACÍA
        elif opcion == 5:
            presentaciones[indice] = input("Nueva presentación (ej: tabletas, jarabe, crema, cápsulas): ")
            print("✓ Presentación actualizada.")
        #VALIDAR QUE EL NUEVO PROVEEDOR INGRESADO NO ESTÉ VACÍO
        elif opcion == 6:
            proveedores[indice] = input("Nuevo proveedor del medicamento: ")
            print("✓ Proveedor actualizado.")
        #VALIDAR QUE LA OPCIÓN DE SALIR DE EDICIÓN SEA 7 Y MOSTRAR UN MENSAJE DE CONFIRMACIÓN ANTES DE SALIR
        elif opcion == 7:
            print("✓ Edición completada.")
            break


        
#INTERFAZ DE USUARIO/MAIN

def main():
    
    nombres = None
    precios = None
    cantidades = None
    fechasVencimiento = None
    presentaciones = None
    proveedores = None
    cantProductos = 0
    #SE MUESTRA UN MENÚ PRINCIPAL PARA SELECCIONAR LAS DIFERENTES FUNCIONES DEL SISTEMA DE GESTIÓN DE DROGUERÍA;
    #CON VALIDACIONES DE ENTRADA PARA SELECCIONAR UNA OPCIÓN VÁLIDA
    while True:
        print("\n" + "=" * 50)
        print("SISTEMA DE GESTIÓN DE DROGUERÍA")
        print("=" * 50)
        print("1. Registrar medicamentos")
        print("2. Ver inventario")
        print("3. Editar medicamento")
        print("4. Calcular valor total del inventario")
        print("5. Ver medicamento con mayor precio")
        print("6. Salir")
        print("=" * 50)
    
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            if opcion < 1 or opcion > 6:
                print("Opción no válida. Ingrese un número entre 1 y 6.")
                continue
        except ValueError:
            print("Error: Ingrese un número válido, sin letras.")
            continue
        #SE EJECUTA LA FUNCION CORRESPONDIENTE SEGÚN LA OPCIÓN ELEGIDA; 
        #CON VALIDACIONES PARA VERIFICAR QUE HAYA MEDICAMENTOS REGISTRADOS ANTES DE REALIZAR ACCIONES QUE REQUIERAN DATOS EN EL INVENTARIO
        match opcion:
            case 1:
                nombres, precios, cantidades, fechasVencimiento, presentaciones, proveedores, cantProductos = registrarProducto()
                print("\n✓ Medicamentos registrados exitosamente.")
            case 2:
                imprimirInventario(nombres, precios, cantidades, fechasVencimiento, presentaciones, proveedores, cantProductos)
            case 3:
                editarProducto(nombres, precios, cantidades, fechasVencimiento, presentaciones, proveedores, cantProductos)
            case 4:
                calcularValorInventario(precios, cantidades, cantProductos)
            case 5:
                calcularMayorPrecio(precios, nombres, cantProductos)
            case 6:
                print("¡Gracias por usar el sistema de droguería!")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")
        
#EJECUTAR PROGRAMA        
main()
            