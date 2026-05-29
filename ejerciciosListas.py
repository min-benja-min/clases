frutas = ["Maracuya", "banana", "Pera"]

def muestraFruta():
    print("-"*20)
    c = 1
    for f in frutas:
        print(f"{c}.- {f}")
        c += 1
    print("-"*20)

def agregarFruta():
    nuevaF = input("Ingrese el fruta a ingresar: ")
    frutas.append(nuevaF)

def eliminarFruta():
    muestraFruta()
    elim = input("Seleccione el numero de la fruta a eliminar: ")
    frutas.pop(elim-1)

    # O usando remove()
    # nuevaF = input("Ingrese el fruta a eliminar: ")
    # frutas.remove(nuevaF)

def actualizarFruta():
    muestraFruta()
    opc = int(input("Seleccione el numero de la fruta a actualizar: "))
    nuevaF = input("Ingrese la nueva fruta: ")

    frutas[opc-1] = nuevaF


def feria():
    while True:
        print("---FERIA---")
        print("1.- Agregar fruta")
        print("2.- Eliminar fruta")
        print("3.- Actualizar fruta")
        print("4.- Mostrar frutas")
        print("5.- Salir")

        op = int(input("Seleccione una opcion: "))
        match op:
            case 1:
                agregarFruta()
            case 2:
                eliminarFruta()
            case 3:
                actualizarFruta()
            case 4:
                muestraFruta()
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")

feria() 