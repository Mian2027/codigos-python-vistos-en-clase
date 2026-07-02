# Ejemplo: Usando `filter` para obtener numeros pares de una lista
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print('Even numbers:', evens)


# Ejemplo: Usando `filter` con una funcion nombrada para filtrar numeros positivos
def is_positive(x):
    return x > 0

numbers = [-5, 3, -1, 101, 0]
positive_numbers = list(filter(is_positive, numbers))
print('Positive numbers:', positive_numbers)
