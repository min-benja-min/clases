# Uso y explicacion de random
import random

# num = random.randint(1,10)
# print(num)

# for i in range(num):
#     print(f"{num} x {i+1} = {num*(i+1)}")

#--------------------------------------------------------------


# personas = 3

# p1 = random.randint(60,190)
# p2 = random.randint(60,190)
# p3 = random.randint(60,190)


# for turno in range(personas):
#     if turno == 0:
#         print("Jugador 1")
#         print(f"El golpe fue de {p1} metros.")
#         turno +=1
        
#     elif turno == 1:
#         print("Jugador 2")
#         print(f"El golpe fue de {p2} metros.")
#         turno +=1
        
#     else:
#         print("Jugador 3")
#         print(f"El golpe fue de {p3} metros.")
#         turno = 0
        
# print("\GANADOR")

# if p1 > p2 and p1 > p3:
#     print("El jugador 1 ha ganado.")
# elif p2 > p3:
#     print("El jugador 2 ha ganado.")
# else:
#     print("El jugador 3 ha ganado.")

#-------------------------------------------------------

num = random.randint(1,100)
i = 0

while i < 5:
    n = int(input("Adivine un numero del 1 al 100: "))

    if n < num:
        print("El numero a adivinar es mayor.")
        i += 1
    elif n > num:
        print("Te pasaste")
        i += 1
    else:
        print("HAS ADIVINADO!")
        i = 5 #break
print(f"Se te han agotado los intentos, el numero era el {num}")