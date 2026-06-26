# Operaciones de Conjuntos: Union, Interseccion y Diferencia

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: Elementos en cualquiera de los conjuntos
union_set = set_a | set_b
print('Union:', union_set)  # Salidas: Union: {1, 2, 3, 4, 5, 6}

# Interseccion: Elementos en ambos conjuntos
intersection_set = set_a & set_b
print('Intersection:', intersection_set)  # Interseccion: {3, 4}

# Diferencia: Elementos en `set_a` pero no en `set_b`
difference_set = set_a - set_b
print('Difference:', difference_set)  # Diferencia: {1, 2}

# Diferencia simetrica: Elementos en uno de los conjuntos, pero no en ambos
symmetric_difference_set = set_a ^ set_b
print('Symmetric Difference:', symmetric_difference_set)  # Salida: Diferencia Simetrica: {1, 2, 5, 6}
