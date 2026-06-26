# En Python, las funciones lambda estan restringidas a una expresion unica,
# lo que significa que los loops tradicionales multi-linea 'for' no pueden usarse directamente.
# Sin embargo, puedes usar list comprehensions o expresiones generadoras dentro de las funciones lambda para lograr comportamientos similares.
# Despues, esta seccion trata el codigo basico del modulo numero.

# Ejemplo 1: Filtrar numeros pares usando una funcion lambda con expresiones de lista.
# Las expresiones de lista proporcionan una manera de incluir ciclos dentro de las expresiones lambda.
# En este caso, se filtran los numeros pares de una lista.

filter_evens = lambda lst: [x for x in lst if x % 2 == 0]
print('Even numbers in [1, 2, 3, 4, 5, 6]:', filter_evens([1, 2, 3, 4, 5, 6]))

##########################################################

# Ejemplo 2: Crear una lista de cuadrados
# De manera similar, las comprensiones de lista pueden usarse para transformar una lista dentro de una funcion lambda.
# Esta funcion lambda genera el cuadrado de cada numero en una lista.

square_numbers = lambda lst: [x**2 for x in lst]
print('Squares of [1, 2, 3, 4]:', square_numbers([1, 2, 3, 4]))
