# juego piedra papel o tijera
import random

bot = ""
user = ""
puntos_usuario = 0
puntos_bot = 0
rondas = 0

opciones = ["piedra", "papel", "tijera"]
reglas = {
    "piedra": "tijera",
    "papel": "piedra",
    "tijera": "papel"
}

while True:
    user = input("""\n>>>_Elige; piedra, papel o tijera\n>>>_Usa 'salir' para salir del juego:-->  """).lower().strip()
    
    if user == "salir":
        print("\nSaliendo...")
        print(f"\n_-PUNTUACION:-_\nPuntos del usuario: {puntos_usuario}\nPuntos del bot: {puntos_bot}\nRondas: {rondas}\n") 
        break
    elif user not in opciones:
        print("\n==|||--> OPCION INVALIDA <--|||==")
        print()
        print("\nELIGE UNA OPCION VALIDA")
        continue
        
    bot = random.choice(opciones)
    if bot == user:
        print(f"\nEmpate: Bot {bot} | Tu {user}")
    
    elif reglas[bot] == user:
        print(f"\nperdistes: Bot {bot} | Tu {user}")
        puntos_bot += 10
    else:
        print(f"\nGanaste: Tu {user} | Bot {bot}")
        puntos_usuario += 10
        
    rondas += 1
    
    print(f"\n>>>Resultados:<<<\nPuntos del usuario: {puntos_usuario}\nPuntos del bot: {puntos_bot}\nRondas: {rondas}")
    
    
