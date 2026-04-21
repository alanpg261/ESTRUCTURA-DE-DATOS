'''
def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])

paises = {"Colombia": "Bogotá", "Perú": "Lima", "Argentina": "Buenos Aires"}
imprimir(paises)
'''
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