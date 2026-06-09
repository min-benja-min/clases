

productosDicc = { 
    1 : {"Nombre": "Maracuya", "Precio": 1500},
    2 : {"Nombre": "Sandia", "Precio": 3000},
    3 : {"Nombre": "Naranja", "Precio": 2000}
}


def mostrarProd():
    print("-"*20)
    c = 1
    for clave in productosDicc:
        print(f"{c}.-{productosDicc[clave]["Nombre"]}, {productosDicc[clave]["Precio"]}")
        c += 1
    print("-"*20)

def actualizaProducto():
    mostrarProd()
    opc = int(input("Seleccione una opcion para actualizar: "))
    nuevoProd = input("Ingrese el producto: ")
    nuevoPrec = int(input("Ingrese el precio: "))

    productosDicc[opc] = {"Nombre": nuevoProd, "Precio": nuevoPrec}

    print(f"Producto actualizado a: {productosDicc[opc]}")

def comprarProd():
    mostrarProd()
    carrito = []
    cant = int(input("Cuántos productos desea comprar?: "))
    for compra in range(cant):
        comp = int(input("Ingrese el producto que quiera comprar: "))
        carrito.append(productosDicc[comp])
        print(f"Su carrito actual es: {carrito}")
    print(f"\nSu carrito final es: {carrito}")

def crearBoleta():
    
    for p in carrito:
    print("El total de su boleta es: ")


def feria():
    while True:
        print("---FERIA---")
        print("1.- Agregar Producto")
        print("2.- Eliminar Producto")
        print("3.- Actualizar Producto")
        print("4.- Mostrar Producto")
        print("5.- Comprar Productos")
        print("6.- Crear Boleta (calcula IVA) y Salir")

        op = int(input("Seleccione una opcion: "))
        match op:
            case 1:
                mostrarProd()
            case 2:
                print("")
            case 3:
                actualizaProducto()
            case 4:
                mostrarProd()
            case 5:
                comprarProd()
            case 6:
                crearBoleta()
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")

feria() 























#Desafio

pokemons = {
    1: {"Nombre": "Eevee",
        "Nivel": 14,
        "HP": 32,
        "Ataque": [20,40] 
       }
}