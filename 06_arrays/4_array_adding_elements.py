# Version de Python: Agregar elementos a listas ha sido soportado desde Python 1.0 (Enero 1994).

# Agregando Elementos a un Arreglo (Lista)
# Python provee varias formas de agregar elementos a una lista.

# Lista de ejemplo
numbers = [1, 2, 3]

# Agregando un elemento al final usando append()
numbers.append(4)
print('Despues de append:', numbers)  # Salida (output): Despues de append: [1, 2, 3, 4]

# Agregando multiples elementos al final usando extend()
numbers.extend([5, 6])
print('Despues de extend:', numbers)  # Salida (output): Despues de extend: [1, 2, 3, 4, 5, 6]

# Agregando un elemento en un indice especifico usando insert()
numbers.insert(2, "two-and-a-half")
print('Despues de insert:', numbers)  # Salida (output): Despues de insert: [1, 2, 'two-and-a-half', 3, 4, 5, 6]

# Nota: El metodo append() agrega un solo elemento al final de la lista.
# El metodo extend() agrega multiples elementos al final de la lista.
# El metodo insert() te permite agregar un elemento en un indice especifico.
