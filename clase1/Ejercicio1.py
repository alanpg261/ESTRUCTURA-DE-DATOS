'''
#Variables que permiten almacenar un unico valor
edad = 12
altura = 1.75
nombre = "Juan"
#Creación de lista por asignación 
Lista2 = ["manzana", "banana", "cereza"]    #Lista de cadenas
Lista3 = [1.20, 2.34, 3.45]                 #Lista de flotantes
Lista4 = [1, "dos", 3.0, True]              #Lista mixta

marcas = ["Toyota", "Ford", "BMW", "Audi", "Honda"]

Lista1 = [1, 2, 3, 4, 5]
suma = 0
for numero in Lista1:  #Recorriendo cada elemento de la lista
    suma += numero     #Acumulando la suma de los elementos
print("La suma de los elementos de Lista1 es:", suma) #imprimir el resultado


meses = ["Enero", "Febrero", "Marzo", "Abril"]
print(meses[0])  # Imprime "Enero"
print(meses[3])  # Imprime "Abril"



Alumno = ["Ana", 3.5, 4.0]
suma = 0
suma += Alumno[1]  # Sumar la calificación 3.5
suma += Alumno[2]  # Sumar la calificación 4.0
promedio = suma / 2  # Calcular el promedio dividiendo la suma entre el número de calificaciones
print("El promedio de las calificaciones de", Alumno[0], "es:", promedio)  # Imprime el resultado del promedio


lista = [103,1231,300,400,102,10,50,300,450]
x = 0
for numero in lista:
    if numero > 100:
        x = x + 1
print(f"La cantidad de numeros superiores a 100 es: {x}")

x = 0 #Variable contador 
enteros = [20, 10, 6, 7, 3, 1] #Definir la lista de elementos 
for numero in enteros: #Recorrer la lista 
    if numero >= 7: #validar si el numero es mayor o igual a 7
        x = x + 1  #Sumar 1 al contador 
        print(numero) #Imprimir el numero 
print(f"La cantidad de numeros superiores o iguales a 7 es: {x}")


cont = 0
nombres = ["Maria", "Ana", "Pedro", "Carlos", "Uriel"]
for nombre in nombres:
    if len(nombre) >= 5:
        cont += 1
print(f"La cantidad de nombres con 5 o más caracteres es: {cont}")

lista = [] 

while True:
    numero = int(input("Ingrese un numero entero, si desea finalizar el ingreso de elementos ingrese 0:"))
    if numero == 0:
        break
    else:
        lista.append(numero)

for numero in lista:
    print(numero)

print(f"El tamaño total de la lista es: {len(lista)}")
'''


"""
EJERCICIO 1: Búsqueda del número mayor y filtrado de productos
==============================================================
Este programa realiza dos tareas principales:
1. Lee 5 números enteros del usuario y encuentra el mayor
2. Lee información de 5 productos (nombre y precio) y filtra los que superan 10000


# ==================== PRIMERA TAREA: ENCONTRAR EL NÚMERO MAYOR ====================
print("=== BÚSQUEDA DEL NÚMERO MAYOR ===")

# Crear una lista vacía para almacenar los números ingresados por el usuario
lista = []

# Ciclo para ingresar 5 números enteros
# El usuario será solicitado 5 veces para ingresar valores
for i in range(5):
    numero = int(input("Ingrese un numero entero: "))
    lista.append(numero)  # Agregar el número a la lista

# Inicializar la variable 'mayor' con el primer elemento de la lista
# Esta será la variable que almacenará el número mayor encontrado
mayor = lista[0]

# Recorrer cada elemento de la lista para comparar con el mayor actual
for i in lista:
    # Si el elemento actual es mayor al número guardado en 'mayor', actualizarlo
    if i > mayor:
        mayor = i

# Mostrar el resultado: el número mayor encontrado
print(f"El numero mayor de la lista es: {mayor}")


# ==================== SEGUNDA TAREA: FILTRADO DE PRODUCTOS ====================
print("\n=== INGRESO Y FILTRADO DE PRODUCTOS ===")

# Crear listas vacías para almacenar los nombres y precios de los productos
nombres = []      # Lista que almacenará los nombres de los productos
precios = []      # Lista que almacenará los precios de los productos

# Ciclo para ingresar información de 5 productos
for i in range(5):
    # Solicitar al usuario el nombre del producto
    nombre = input("Ingrese el nombre del producto: ")
    # Solicitar al usuario el precio del producto (convertir a float para decimales)
    precio = float(input("Ingrese el precio del producto: "))
    # Agregar el nombre a la lista de nombres
    nombres.append(nombre)
    # Agregar el precio a la lista de precios
    precios.append(precio)

# Mostrar encabezado para los productos filtrados
print("\nProductos con precio mayor a 10000:")

# Recorrer todas las posiciones de los productos (0 a 4)
for i in range(5):
    # Validar si el precio en la posición actual es mayor a 10000
    if precios[i] > 10000:
        # Mostrar el nombre del producto y su precio
        print(f"  - {nombres[i]}: ${precios[i]}")
"""
print("\n=== INGRESO Y FILTRADO DE ESTUDIANTES ===")

alumnos = []  # Lista para almacenar los nombres de los alumnos
notas = []    # Lista para almacenar las notas de los alumnos
evaluacion = [] 
for i in range(5):
    nombre = input("Ingrese el nombre del alumno: ")
    nota = float(input("Ingrese la nota del alumno: "))
    alumnos.append(nombre)  # Agregar el nombre del alumno a la lista
    notas.append(nota)      # Agregar la nota del alumno a la lista

cantidad = 0                                        # Variable para contar la cantidad de alumnos con nota "Muy bueno"
for i in range(5):
    if notas[i] >= 4.5:
        evaluacion.append("Muy bueno")              # Agregar "Muy bueno" a la lista de evaluación
        cantidad += 1
    elif notas[i] >= 3.5 and notas[i] < 4.5:
        evaluacion.append("Bueno")                  # Agregar "Bueno" a la lista de evaluación
    elif notas[i] < 3.5:
        evaluacion.append("Insuficiente")           # Agregar "Insuficiente" a la lista de evaluación
 
print("Evaluación de alumnos:")
for i in range(5):
    print(f"Alumno: {alumnos[i]}, Nota: {notas[i]}, Evaluación: {evaluacion[i]}")
print(f"Cantidad de alumnos con una nota muy buena: {cantidad}")