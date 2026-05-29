
productos = [
    ["Xbox Series S", 300000],
    ["Sony PS5", 600000],
    ["LGTV 60 Pulgadas", 450000]
]

# opc = 1
# for prod, precio in productos:
#     print(f"{opc}.- Producto: {prod} Precio: ${precio}")
#     opc += 1

def menuProd():
    opc = 1
    for p in productos:
        print(f"{opc}.- Producto: {p[0]} Precio: ${p[1]}")
        opc += 1

def menuPrincipal():
    print("1.- Menu Admin ")
    print("2.- Menu Cliente ")
    print("3.- Salir ")



def selectProd():

    op = 0
    total = 0
    menuProd()
    while op != 4:
        menuPrincipal()
        print("4.- Salir")
        op = int(input("Seleccione un opcion: "))

        match op:

            case 1:
                print("El valor a pagar", 250000*1.19)
                total += 250000*1.19
            case 2:
                print("El valor a pagar", 500000*1.19)
                total += 500000*1.19
            case 3:
                print("El valor a pagar", 600000*1.19)
                total += 600000*1.19
            case 4:
                print(f"El total a pagar es {total}")
                print("Vuelva pronto!!")
            case _:
                print("Opcion invalida")


def selectAdmin():
    while True:
        print("1.- Agregar producto")
        print("2.- Eliminar producto")
        print("3.- Actualizar producto")
        print("4.- Mostrar producto")
        print("5.- Salir")

        op = int(input("Seleccione una opcion: "))
        match op:
            case 1:
                nuevoProd = input("Ingrese el producto a ingresar: ")
                precioProd = int(input("Ingrese el precio del producto: "))
                productos.append([nuevoProd, precioProd])
            case 2:
                nuevoProd = input("Ingrese el producto a eliminar: ")
                precioProd = int(input("Ingrese el precio del producto: "))
                productos.remove([nuevoProd, precioProd])
            case 3:
                print("act")
            case 4:
                print(productos)
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")

def selectPrin():
    while True:
        menuPrincipal()
        op = int(input("Seleccione una opcion: "))
        match op:
            case 1:
                print("---Menu Admin---")
                selectAdmin()
            case 2:
                print("---Menu Productos---")
                selectProd()
            case 3:
                print("Salir")
                break
            case _:
                print("Opcion invalida")

selectPrin()



