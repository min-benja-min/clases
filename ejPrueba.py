
# Productos enlatados

peso = int(input("Ingrese el peso del producto (en gramos): ")) #solo valores positivos
while 0 >= peso:
    print("Solo valores positivos, ingrese nuevamente: ")
    peso = int(input("Ingrese el peso del producto (en gramos): "))

sodio = int(input("Ingrese el porcentaje de sodio del producto (1/100): ")) #valores del 1 al 100
while sodio not in range(1,100):
    print("Solo valores entre 1 y 100, ingrese nuevamente: ")
    sodio = int(input("Ingrese el porcentaje de sodio del producto (1/100): "))

pais = int(input("Ingrese su tipo de venta (1.- Nacional /  2.- Internacional): ")) # 1 o 2
while pais < 1 or pais > 2:
    print("El valor debe ser 1 o 2 según su tipo de venta, intente nuevamente")
    pais = int(input("Ingrese su tipo de venta (1.- Nacional /  2.- Internacional): "))


if peso <= 500:
    peso = "Lata normal"
elif 501 <= peso <= 1500:
    peso = "Lata mediana"
else:
    peso = "Lata grande"
if sodio < 5:
    peso = peso
elif 5 <= sodio <= 8:
    sodio = "Lata especial"
    peso = ""
else:
    sodio = "Lata acorazada"
    peso = ""
if pais == 2:
    pais = "con sticker sanitario"
else:
    pais = ""

print(f"{peso} {sodio} {pais}\n")

