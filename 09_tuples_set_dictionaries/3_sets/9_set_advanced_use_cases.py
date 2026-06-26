# Operaciones Avanzadas de Conjuntos y Casos de Uso

# Prueba del Membresia de Conjuntos con Subconjuntos
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

# Verifica si set_a es un subconjunto de set_b
is_subset = set_a.issubset(set_b)
print('Is set_a a subset of set_b?', is_subset)  # Salida: set_a es un subconjunto de set_b? True

# Verifica si set_b es un superconjunto de set_a.
is_superset = set_b.issuperset(set_a)
print('Is set_b a superset of set_a?', is_superset)  # {True}

# Conjuntos disjuntos: Sin elementos en comun.
set_c = {6, 7, 8}
are_disjoint = set_a.isdisjoint(set_c)
print('Are set_a and set_c disjoint?', are_disjoint)  # {True}
