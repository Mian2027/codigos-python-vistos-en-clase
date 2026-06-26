# Conjunto inmutable: Un conjunto inmutable.

# Creando un conjunto inmutable
immutable_set = frozenset([1, 2, 3, 3, 4])
print('Immutable set:', immutable_set)  # Salida: Conjunto inmutable: frozenset({1, 2, 3, 4})

# Utilizando un conjunto inmutable como clave en una diccionario (ya que es inmutable)
my_dict = {frozenset([1, 2, 3]): "Primero"}
print('Dictionary with frozenset key:', my_dict)  # Salida: Diccionario con clave fija: {'frozenset({1, 2, 3}): 'first'}

# Nota: Los frozensets son como los sets pero inmutables, lo que significa que sus elementos no pueden modificarse despues de su creacion.
