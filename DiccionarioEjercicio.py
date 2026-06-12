
vegetales={
   1:"Maracuyá",
   2:"Pera",
   3:"Cebolla",
   7:"Papa"
}

# print(len(vegetales))

def agregaVegetal():
    nombreF=input("Ingrese el nombre del Vegetal: ")
    vegetales[list(vegetales.items())[-1][0]+1]=nombreF
def muestraVegetal():
    for key, value in vegetales.items():
        print(key, ".-" , value)
    print("-"*30)
def eliminaVegetal():
    muestraVegetal()
    borra=int(input("Cual desea eliminar?: "))
    del vegetales[borra]
def actualiazaVegetal():
    muestraVegetal()
    actualiza=int(input("Cual desea actualizar?: "))
    nuevo_vegetal=input("Cual es el nombre nuevo?: ")
    vegetales[actualiza]=nuevo_vegetal
def vegetalesMenu():
    while True:
        try:
            print("1.- Agregar Vegetal")
            print("2.- Eliminar Vegetal")
            print("3.- Actualizar Vegetal")
            print("4.- Mostrar Vegetal")
            print("5.- Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agregaVegetal()
                case 2:
                    eliminaVegetal()
                case 3:
                    actualiazaVegetal()
                case 4:
                    muestraVegetal()
                case 5:
                    print("Salir")
                    break
                case _:
                    print("Opcion invalida")  
        except Exception as e:
            print("Error :", e)

# vegetalesMenu()


productosDicc={
   1:{"nombre": "Maracuyá", "precio": 3000},
   2:{"nombre": "Pera", "precio": 1500},
   3:{"nombre": "Cebolla", "precio": 1200}
}


# print(productosDicc[2]["precio"])  # precio de la pera
# print(productosDicc[3]["nombre"])  # precio de la pera

# productosList=[
#    {"nombre": "Maracuyá", "precio": 3000},
#    {"nombre": "Pera", "precio": 1500},
#    {"nombre": "Cebolla", "precio": 1200}
# ]

# print(productosList[2]["precio"]) #precio de la cebolla
# print(productosList[0]["nombre"]) #precio de la cebolla
pokemons={
    1:{"nombre": "Eevee",
       "nlv": 14,
       "hp": 32,
       "atk": [20,40] }
}

productosDicc={
   1:{"nombre": "Maracuyá", "precio": 3000},
   2:{"nombre": "Pera", "precio": 1500},
   3:{"nombre": "Cebolla", "precio": 1200}
}
productosDicc[4]={"nombre": "Tomate", "precio": 1500} 


# print(productosDicc.keys())
# print(productosDicc.values())
# print(productosDicc.items())
# listadeKeys=list(productosDicc.keys())

# print(list(productosDicc.keys())[-1])

carrito=[]
def agregaProducto():
    nombreP=input("Ingrese el nombre del Producto: ")
    precioP=int(input("Ingrese el precio del Producto: "))
    productosDicc[list(productosDicc.keys())[-1]+1]={"nombre": nombreP, "precio": precioP} 
def muestraProducto():
    print("-"*30)
    for nombre, precio in productosDicc.items():
        print(f"{nombre} .-  {precio}")
    print("-"*30)
def eliminaProducto():
    muestraProducto()
    borra=int(input("Cual desea eliminar?: "))
    del productosDicc[borra]
def actualiazaProducto():
    muestraProducto()
    actualiza=int(input("Cual producto desea actualizar?: "))
    nuevonombre=input("ingrese el nuevo nombre") 
    nuevoPRECIO=input("ingrese el nuevo precio") 
    productosDicc[actualiza]={"nombre":nuevonombre , "precio": nuevoPRECIO}

def comprar():
    while True:
        muestraProducto()
        try:
            comprar=int(input("Cual producto desea comprar? o presione 0 para salir: "))
            if comprar == 0:
                break
            if comprar in productosDicc:
                print(f"Usted ha comprado {productosDicc[comprar]['nombre']} por un valor de {productosDicc[comprar]['precio']}")
                carrito.append(productosDicc[comprar])
        
            else:
                print("Producto no existe")
        except ValueError:
            print("Debe ingresar un número válido")

def boleta():
    total=0
    for p in carrito:
        try:
            total+=int(p["precio"])
            
        except (ValueError, TypeError):
            print(f"Precio inválido para {p.get('nombre','?')}, contando como 0")
    iva=total*0.19
    print(f"El total de su compra es {total} y el IVA es {iva}")
    print(f"El total a pagar es  {total+iva} ")
def productosMenu():
    while True:
        try:
            print("1.- Agregar Producto")
            print("2.- Eliminar Producto")
            print("3.- Actualizar Producto")
            print("4.- Mostrar Producto")
            print("5.- Comprar Productos")
            print("6.- Crear Boleta (calcula IVA) y Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agregaProducto()
                case 2:
                    eliminaProducto()
                case 3:
                    actualiazaProducto()
                case 4:
                    muestraProducto()
                case 5:
                    comprar()
                case 6:
                    boleta()
                    print("Salir")
                    break
                case _:
                    print("Opcion invalida")  
        except Exception as e:
            print("Error :", e)


productosMenu()


