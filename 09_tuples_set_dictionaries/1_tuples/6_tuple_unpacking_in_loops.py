# Desempaquetado de Tuplas en Ciclos

pairs = [(1, 2), (3, 4), (5, 6)]

# Desempaquetado en un Ciclo para For
for a, b in pairs:
    print('a:', a, ', b:', b)  # Salidas: a: 1, b: 2 (y asi por cada par)

# Desempaquetado Nestado en Ciclos
nested_pairs = [((1, 2), (3, 4)), ((5, 6), (7, 8))]
for (a, b), (c, d) in nested_pairs:
    # Salida: a: 1, b: 2, c: 3, d: 4 (and so on)
    print('a:', a, ', b:', b, ', c:', c, ', d:', d)
