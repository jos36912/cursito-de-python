print()
print("=|||= Ejecuntando el programa mini-bot =|||=")

print()
nombre = input("Cual es tu nombre?: ").strip()

if nombre.isalpha():
    print()
    print(f"Encantado de conocerte {nombre}")
else:
    print("ingresa solo letras")

edad = input("Cual es tu edad?: ").strip()
bot_edad = 3

if edad.isdigit():
    edad = int(edad)
    print()
    print(f"{nombre} tienes {edad} años, yo solo tengo {bot_edad} años")
else:
    print("ingresa solo numeros")