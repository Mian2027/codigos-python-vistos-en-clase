# Desempaquetado de pares dentro de tuplas

nested_tuple = ((1, 2), (3, 4), (5, 6))

# Desempaquetado de tuplas con parametros
(first_a, first_b), (second_a, second_b), (third_a, third_b) = nested_tuple
print('First pair:', first_a, ',', first_b)  # Salida: Pares primero: (1, 2)
print('Second pair:', second_a, ',', second_b)  # Salida: Pares segundo: (3, 4)
print('Third pair:', third_a, ',', third_b)  # Salida: Tercer par: 5, 6
