temperaturas = {
    "lunes": 15,
    "martes": 18,
    "miercoles": 14,
    "jueves": 9,
    "viernes": 19,
}

list = []

for dia, maxi in temperaturas.items():
    print(dia, maxi)
    list.append(maxi)

list.sort()

print(f"La temperatura minima es {list[0]} y la maxima es {list[-1]}")

# maximos

maximos = []
for dia, maxi in temperaturas.items():
    maximos.append(maxi)
print("La temperatura maxuima fue", max(maximos))