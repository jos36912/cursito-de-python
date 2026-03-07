entrada = 0

while True:
    entrada = input("\nIngresa 'salir' para salir del programa.\nCual es tu edad?: ").strip()
    if entrada.lower() == "salir":
        print("\nSaliendo...")
        break
    if entrada.isdigit():
        entrada = int(entrada)
        if entrada >= 18:
            print(f"\nTienes {entrada} años, Eres mayor de edad")
        else:
            print(f"\nTienes {entrada} años, Eres menor de edad")
    else:
        print("Por favor, ingresa solo números.")
        break
