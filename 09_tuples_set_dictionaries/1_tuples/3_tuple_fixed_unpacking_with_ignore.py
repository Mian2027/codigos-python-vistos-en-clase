# Desempaquetado fijo con ignorar (_)

numbers_tuple = (1, 2, 3, 4)

# Desempaquetado fijo con ignorar - ignorando el tercer elemento
a, b, _, d = numbers_tuple
print('a:', a, ', b:', b, ', d:', d)  # Salida: a: 1, b: 2, d: 4

# Nota: Solo se ignora un elemento (en este caso, el tercer)
