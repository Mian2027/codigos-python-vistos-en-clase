# Version de Python: Las list comprehensions se introdujeron en Python 2.0 (octubre de 2000).

# La list comprehension es una forma concisa de crear listas. 
# Permite generar una nueva lista aplicando una expresion a cada elemento de una lista o iterable existente.

# Creando una lista de numeros del 1 al 10
numbers = list(range(1, 11))
print('Numeros originales:', numbers)  # Salida (output): Numeros originales: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Creando una lista de cuadrados usando list comprehension
squares = [x**2 for x in numbers]
print('Cuadrados:', squares)  # Salida (output): Cuadrados: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

##################################

# Ejemplo 1: Filtrando numeros pares

# Esta list comprehension crea una nueva lista que contiene solo los numeros pares de la lista original.

# El orden es:
# 1. `for x in numbers`: Itera sobre cada numero en la lista `numbers`.
# 2. `if x % 2 == 0`: Verifica si el numero actual `x` es par.
# 3. `x`: Incluye el numero `x` en la nueva lista `evens` si la condicion es True.
evens = [x for x in numbers if x % 2 == 0]
print('Pares:', evens)  # Salida (output): Pares: [2, 4, 6, 8, 10]


# Ejemplo 2: Filtrando numeros pares con variable explicita

# Esta list comprehension crea una nueva lista de numeros pares.

# El orden es:
# 1. `for number in numbers`: Itera sobre cada numero en la lista `numbers`.
# 2. `if number % 2 == 0`: Verifica si el numero actual `number` es par.
# 3. `number`: Incluye el numero `number` en la nueva lista `evens` si la condicion es True.
evens = [number for number in numbers if number % 2 == 0]
print('Pares:', evens)  # Salida (output): Pares: [2, 4, 6, 8, 10]



##################################

# Nuevos ejemplos con if y else dentro de list comprehensions

# Ejemplo 3: Creando una lista de etiquetas pares e impares

# Esta list comprehension crea una nueva lista donde los numeros pares se etiquetan como 'Par' 
# y los numeros impares se etiquetan como 'Impar'.

# El orden es:
# 1. for x in numbers: Itera sobre cada numero en la lista numbers.
# 2. if x % 2 == 0: Verifica si el numero actual x es par.
# 3. 'Par' si la condicion es True, en caso contrario 'Impar': Incluye la etiqueta apropiada en la nueva lista.
labels = ['Par' if x % 2 == 0 else 'Impar' for x in numbers]
print('Etiquetas:', labels)  # Salida (output): Etiquetas: ['Impar', 'Par', 'Impar', 'Par', 'Impar', 'Par', 'Impar', 'Par', 'Impar', 'Par']

# Ejemplo 4: Duplicando numeros pares, dividiendo a la mitad los impares

# Esta list comprehension crea una nueva lista donde los numeros pares se duplican,
# y los numeros impares se dividen a la mitad.

# El orden es:
# 1. for x in numbers: Itera sobre cada numero en la lista numbers.
# 2. if x % 2 == 0: Verifica si el numero actual x es par.
# 3. x * 2 si la condicion es True, en caso contrario x / 2: Realiza la operacion apropiada sobre x y lo incluye en la nueva lista.
modified_numbers = [x * 2 if x % 2 == 0 else x / 2 for x in numbers]
print('Numeros modificados:', modified_numbers)  # Salida (output): Numeros modificados: [0.5, 4, 1.5, 8, 2.5, 12, 3.5, 16, 4.5, 20]

# Ejemplo 5: Categorizando numeros

# Esta list comprehension crea una nueva lista que categoriza los numeros en 'Pequeno', 'Mediano' o 'Grande'.

# El orden es:
# 1. for x in numbers: Itera sobre cada numero en la lista numbers.
# 2. if x <= 3: Verifica si el numero actual x es menor o igual a 3.
# 3. if x <= 7: Verifica si el numero actual x es menor o igual a 7.
# 4. 'Pequeno', 'Mediano' o 'Grande': Incluye la etiqueta apropiada en la nueva lista.
categories = ['Pequeno' if x <= 3 else 'Mediano' if x <= 7 else 'Grande' for x in numbers]
print('Categorias:', categories)  # Salida (output): Categorias: ['Pequeno', 'Pequeno', 'Pequeno', 'Mediano', 'Mediano', 'Mediano', 'Mediano', 'Grande', 'Grande', 'Grande']
