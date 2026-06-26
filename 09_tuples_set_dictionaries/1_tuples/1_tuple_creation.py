# Version de Python: Las tuplas han sido parte del lenguaje desde la version 1.0.
# (enero de 1994)

# Creado una tupla en Python
# Las tuplas son secuencias inmutables tipicamente usadas para almacenar colecciones de
# datos heterogeneos.

# Crear una tupla simple
numbers_tuple = (1, 2, 3, 4, 5)
# Salida: Tupla de numeros: (1, 2, 3, 4, 5)
print('Numbers tuple:', numbers_tuple)

# Las tuplas pueden contener tipos de datos diferentes
mixed_tuple = (1, "dos", 3.0, True)
# Salida: Tupla mixta: (1, 'dos', 3.0, True)
print('Mixed tuple:', mixed_tuple)

# Crea una tupla sin parentesis.
implicit_tuple = 1, 2, 3
# Salida: Tuple implicito: (1, 2, 3)
print('Implicit tuple:', implicit_tuple)

# Crea una tupla usando la funcion tuple().
tuple_from_list = tuple([1, 2, 3, 4])
# Salida: Tuple from list using tuple(): (1, 2, 3, 4)
print('Tuple from list using tuple():', tuple_from_list)

# Toma nota: Los tuplas son inmutables, lo que significa que sus elementos no pueden ser modificados.
# despues de la creacion.
