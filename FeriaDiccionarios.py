

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

# def actualizarFruta():
#     muestraFruta()
#     opc = int(input("Seleccione el numero de la fruta a actualizar: "))
#     nuevaF = input("Ingrese la nueva fruta: ")

#     frutas[opc-1] = nuevaF

actualizaProducto()

#Desafio

pokemons = {
    1: {"Nombre": "Eevee",
        "Nivel": 14,
        "HP": 32,
        "Ataque": [20,40] 
       }
}