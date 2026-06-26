# Desempaquetado de tuplas en argumentos de funciones

def calculate_sum(a, b, c):
    return a + b + c


# Tupla a desempacar
values = (1, 2, 3)

# Desempaquetando tupla para pasarle a los argumentos de la funcion
result = calculate_sum(*values)
print('Sum:', result)  # Salida: Suma: 6
