## DATOS COMPUESTOS

# tipo de dato son las listas se pueden modificar
lista = ["jeyson jarquin", "soy jeyson", True, 1.70]

# tuplas es similar a las listas solo que no se pueden modificar
tupla = ("jeyson jarquin", "soy jeyson", True, 1.70)

# esto es valido 
lista [3] = "maquinola"

# esto no
# tupla [3] = "maquinola"

# creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)
# muestra los datos de manera desordenada
conjunto = {"jeyson jarquin", "soy jeyson", True, 1.70}

# print(conjunto [2]) #--> no puede acceder al elemento

# creando un diccionario (dict) (la estructura es key : value y sepramos con comas)
diccionario = {
    'nombre' : "jeyson jarquin",
    'edad' : "19",
    'esta_listo' : True,
    'altura' : 1.70,
    'dato_duplicado' : "jeyson jarquin" 
}

# print(diccionario ['altura'])
print(lista [0])