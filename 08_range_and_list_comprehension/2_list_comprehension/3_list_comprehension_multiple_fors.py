# Ejemplo 1: Multiples bucles for en comprension de lista (list comprehension)

# Esta comprension de lista (list comprehension) crea una lista de tuplas (tuples) que representan pares (x, y)
# donde x es de la primera lista e y es de la segunda lista.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# El orden es:
# 1. for x in list1: Itera sobre cada elemento de list1.
# 2. for y in list2: Itera sobre cada elemento de list2 por cada elemento de list1.
# 3. (x, y): Incluye la tupla (x, y) en la nueva lista.
pairs = [(x, y) for x in list1 for y in list2]
print('Pares:', pairs)  # Salida (output): Pares: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]


# Ejemplo 2: Multiples bucles for con condiciones

# Esta comprension de lista (list comprehension) crea una lista de tuplas (tuples) que representan pares (x, y)
# donde x es par, e y es una vocal.

list1 = [1, 2, 3, 4]
list2 = ['a', 'e', 'i', 'o', 'u']

# El orden es:
# 1. for x in list1: Itera sobre cada elemento de list1.
# 2. if x % 2 == 0: Verifica si x es par.
# 3. for y in list2: Itera sobre cada elemento de list2 si x es par.
# 4. (x, y): Incluye la tupla (x, y) en la nueva lista.
pairs = [(x, y) for x in list1 if x % 2 == 0 for y in list2]
print('Pares:', pairs)  # Salida (output): Pares: [(2, 'a'), (2, 'e'), (2, 'i'), (2, 'o'), (2, 'u'), (4, 'a'), (4, 'e'), (4, 'i'), (4, 'o'), (4, 'u')]
