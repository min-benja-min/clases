clave = input("Ingrese una clave: ")

if (clave.upper()) == "SHAZAM":
    print("Clave correcta!")
else:
    print("Clave incorrecta.")


#-------------------------------------------

nom = input("Ingrese un nombre de usuario que tenga de 4 a 10 caracteres: ")

if 4 <= len(nom) <= 10:
    print("Largo correcto.")
else:
    print("Largo incorrecto.")

# #-------------------------------------------

pin = int(input("Ingrese un pin: "))

if len(str(pin)) == 4:
    print("pin valido.")
else:
    print("pin invalido.")

