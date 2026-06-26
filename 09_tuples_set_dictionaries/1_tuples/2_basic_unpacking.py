# Creacion de tuplas y desempaquetado basico.

# Crear una tupla simple.
numbers_tuple = (1, 2, 3)
print('Tupla de numeros:', numbers_tuple)  # Salida: Tupla de numeros: (1, 2, 3)

# Desempaquetado basico.
a, b, c = numbers_tuple
print('a:', a, ', b:', b, ', c:', c)  # Salida: a: 1, b: 2, c: 3

# Desempaquetado con cantidad incorrecta de elementos.
# Quitar el comentario de la siguiente linea genera un ValueError.
# a, b = numbers_tuple  # ValueError: demasiados valores para desempaquetar (se esperaban 2)
