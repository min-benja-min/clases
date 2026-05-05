import random

cant = random.randint(10,20)
lata = 0
plancha = 0

for i in range(cant):
    pez = random.randint(1,1600)
    if pez < 800:
        print("En lata")
        lata += 1
    else:
        print("A la plancha")
        plancha += 1

print(f"Has capturado {lata+plancha} peces, {lata} peces pequeños y {plancha} peces grandes")