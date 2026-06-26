# Conjuntos de comprension

# Crear un conjunto de cuadrados
squares_set = {x ** 2 for x in range(6)}
print('Squares set:', squares_set)  # Salida: Conjunto de cuadrados: {0, 1, 4, 9, 16, 25}

# Crear un conjunto de caracteres unicos
unique_chars_set = {char for char in "Hola mundo"}
print('Unique characters set:', unique_chars_set)  # Salida: Conjunto de caracteres unicos: {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}

# Nota: Las comprensiones de conjuntos proporcionan una forma concisa de crear conjuntos, similar a las comprensiones de listas.
