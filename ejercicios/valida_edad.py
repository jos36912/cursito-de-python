entrada = input("Cual es tu edad?: ").strip()

if entrada.isdigit():
    edad = int(entrada)
    if edad >= 18:
        print()
        print("eres mayor de edad")
    else:
        print()
        print("eres menor de edad")
else:
    print("Por favor, ingresa solo números.")
