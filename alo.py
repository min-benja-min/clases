
notas = [4.6, 6.8, 4.1]

cantNotas = 0
notasIngresadas = []



def agregarNotas():

    print("")
    nota = float(input("Ingrese la nota: "))
    notas.append(nota)


def muestraNotas():

    print("-"*20)
    c = 1
    for f in notas:
        print(f"{c}.- {f}")
        c += 1
    print("-"*20)

def muestraCantidadNotas():
    len(notas)

def promedioNotas():
    print("")
    tot = 0
    for n in notas:
        tot += n
    prom = tot / len(notas)
    print(f"El promedio de notas es: {prom}")


while True:
    try:
        print('''
            # 1.- Agregar las notas a la lista
            # 2.- Muestre por pantalla todas las notas.
            # 3.- Muestre la cantidad de notas.
            # 4.- Obtenga el promedio de las notas
            # 5.- Salir
            ''')
        op = int(input("Ingrese una opcion: "))

    except ValueError as e:
        print("Error", e)
    
    match op:

        case 1:
            agregarNotas()
        case 2:
            muestraNotas()
        case 3:
            muestraCantidadNotas()
        case 4:
            promedioNotas()
        case 5:
            print("Saliendo...")
        case _:
            print("Opcion invalida")    
