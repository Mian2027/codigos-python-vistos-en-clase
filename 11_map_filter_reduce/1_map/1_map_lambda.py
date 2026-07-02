# Ejemplo: Utilizar `map` para sumar 1 a cada elemento en una lista.
numbers = [1, 2, 3, 4, 5]
add_one = list(map(lambda x: x + 1, numbers))
print('Adding 1 to each element:', add_one)


# Ejemplo: Utilizar `map` con una funcion nombrada para elevar al cuadrado cada elemento en una lista.
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print('Squaring each element:', squared_numbers)
