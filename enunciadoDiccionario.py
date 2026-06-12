# Crear un gestor de estacionamiento
# Un estacionamiento tiene cuatro pisos
# y cada piso tiene veinte espacios.
# Cuando entra un vehiculo preguntar qué tipo
# de vehiculo es (ligero 2000, mediano 3000, pesado 3500), luego acomodarlo en algun piso
# disponible. El menú debe tener las siguientes 
# alternativas.

'''1.- Ingresar vehiculo
"2.- Contar ganancias
3.- Contar vehiculos'''

#Use listas o diccionarios según le acomode más.

vehiculos = [
    {"liviano": 2000},
    {"mediano": 3000},
    {"pesado": 3500}
]

pisos = [
    {1: 20},
    {2: 20},
    {3: 20},
    {4: 20}
]



ganancias = 0
ingresados = 0

def mostrar():
    
    print("-"* 30)
    c = 1
    for i in vehiculos:
        print(f"{c}.- {i} ")
        c += 1
    print("-"* 30)

while True:
    try: 
        print(''' --- Gestor de estacionamiento ---
    1.- Ingresar vehiculo
    2.- Contar ganancias
    3.- Contar vehiculos
    4.- Salir''')
        
        op = int(input("Ingrese una opcion: "))
    
        match op:
            case 1:
                print("--INGRESAR VEHICULOS--\n")
                # print(" YO creo que hay que hacer algo mas por acási...en eso estamos, no veo que avancen-...XD>:c")
                mostrar()
                clase = int(input(f"Ingrese su clase de vehiculo: "))

                # if pisos[0][1] <= 20:
                #     print("Vehiculo ingresado al piso 1")
                #     pisos[0][1] -= 1
                #     print(pisos[0][1])
                # elif pisos[0][2] <= 20:
                #     print("Vehiculo ingresado al piso 2")
                #     pisos[0][2] -= 1
                # elif pisos[0][3] <= 20:
                #     print("Vehiculo ingresado al piso 3")
                #     pisos[0][3] -= 1
                # else:
                #     print("No hay espacio disponible")
                #     break


                if clase == 1:
                    ganancias += 2000
                    ingresados += 1

                elif clase == 2:
                    ganancias += 3000
                    ingresados += 1
                else:
                    ganancias += 3500
                    ingresados += 1

            case 2:
                print("--CONTAR GANANCIAS")
                print(f"Ganancias totales: {ganancias}")
            case 3:
                print("--CONTAR VEHICULOS--\n")
                print(f"Vehiculos ingresados: {ingresados}")
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida, intente nuevamente")
    except ValueError:
        print("Valor invalido, intente nuevamente")

print(pisos[0][1])