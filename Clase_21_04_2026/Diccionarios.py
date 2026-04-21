'''
def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])

paises = {"Colombia": "Bogotá", "Perú": "Lima", "Argentina": "Buenos Aires"}
imprimir(paises)

def Cargar():
    personas = {}
    for i in range(5):
        nombre = input("Ingrese el nombre de la persona: ")
        documento = int(input("Ingrese el documento de la persona: "))
        personas[documento] = nombre
    return personas

def Imprimir(personas):
    for clave in personas:
        print(clave, personas[clave])

def consultar(personas):
    documento = int(input("Ingrese el documento a consultar: "))
    for clave in personas:
        if clave == documento:
            print("El nombre de la persona es: ", personas[clave])
            return
    print("Documento no encontrado.")

personas = Cargar()
Imprimir(personas)
consultar(personas)

#Desarrolar una agenda. Utilizar cuya clave sea la fecha. Permitir almacenar distintas actividades para la misma fecha (se ingresa la hora y la actividad)
#implemntar las siguientes funciones:
#1. Cargar la agenda
#2. Listado completo de la agenda
#3. Consultar por fecha

def cargar_agenda():
    agenda = {}
    while True:
        fecha = input("Ingrese la fecha (dd/mm/yyyy) o 'salir' para terminar: ")
        if fecha.lower() == 'salir':
            break
        hora = input("Ingrese la hora (hh:mm): ")
        actividad = input("Ingrese la descripción de la actividad: ")
        if fecha not in agenda:
            agenda[fecha] = []
        agenda[fecha].append([hora, actividad])
    return agenda

def imprimir_agenda(agenda):
    print("AGENDA DE ACTIVIDADES:")
    print("----------------------")
    for fecha in agenda:
        print(f"Fecha: {fecha}")
        for hora, actividad in agenda[fecha]:
            print(f"  Hora: {hora}, Actividad: {actividad}")

def consultar_agenda(agenda):
    fecha = input("Ingrese la fecha a consultar (dd/mm/yyyy): ")
    if fecha in agenda:
        print(f"Actividades para la fecha {fecha}:")
        for hora, actividad in agenda[fecha]:
            print(f"  Hora: {hora}, Actividad: {actividad}")
    else:
        print("No hay actividades para esa fecha.")

agenda = cargar_agenda()
imprimir_agenda(agenda)
consultar_agenda(agenda)
'''
#Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el numero de documento del alumno.
#Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota. Crear las siguientes funciones:
#1. Cargar los datos de los alumnos(por cada alumno se ingresa el numero de documento, luego se ingresan las materias y sus notas, se finaliza el ingreso de materias con la palabra "salir")
#2. Listar los datos de los alumnos
#3. Consultar por numero de documento

def cargar_alumnos():
    alumnos = {}
    for i in range(3):
        documento = int(input("Ingrese el número de documento del alumno: "))
        materias = []
        while True:
            materia = input("Ingrese el nombre de la materia (o 'salir' para finalizar): ")
            if materia.lower() == 'salir':
                break
            nota = float(input("Ingrese la nota de la materia: "))
            materias.append((materia, nota))
        alumnos[documento] = materias
    return alumnos

def listar_alumnos(alumnos):
    print("DATOS DE LOS ALUMNOS:")
    print("---------------------")
    for documento in alumnos:
        print(f"Documento: {documento}")
        for materia, nota in alumnos[documento]:
            print(f"  Materia: {materia}, Nota: {nota}")

def consultar_alumno(alumnos):
    documento = int(input("Ingrese el número de documento a consultar: "))
    if documento in alumnos:
        print(f"Datos del alumno con documento {documento}:")
        for materia, nota in alumnos[documento]:
            print(f"  Materia: {materia}, Nota: {nota}")
    else:
        print("Alumno no encontrado.")

alumnos = cargar_alumnos()
listar_alumnos(alumnos)
consultar_alumno(alumnos)