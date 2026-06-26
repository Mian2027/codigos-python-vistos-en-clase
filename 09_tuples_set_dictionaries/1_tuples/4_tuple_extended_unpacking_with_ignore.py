
# Descomposicion extendida con ignorar (usando *_)

numbers_tuple = (1, 2, 3, 4, 5)

# Descomposicion extendida con ignorar - ignorando todos los elementos entre b y el ultimo
a, b, *_, last = numbers_tuple
print('a:', a, ', b:', b, ', last:', last)  # Salidas: a: 1, b: 2, ultimo: 5

# Nota: *_ captura todas las entradas intermedias, efectivamente ignorandolas.
