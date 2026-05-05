import random
import time

c = 0
n1 = random.randint(1,9)
n2 = random.randint(1,9)
n3 = random.randint(1,9)
t1 = False
t2 = False
t3 = False

print(f"Los numeros generados son: {n1} {n2} {n3}")

while not t1 or not t2 or not t3:
    n = random.randint(1,9)
    print(f"El numero es: {n}")
    time.sleep(0.5)
    if n == n1:
        t1 = True
    if n == n2:
        t2 = True
    if n == n3:
        t3 = True
    c += 1

print(f"Ganaste el {c} intentos")