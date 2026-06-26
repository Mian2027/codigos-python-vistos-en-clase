# El bucle (loop) `for` se utiliza para iterar sobre un iterable (como una lista, tupla, cadena (string), diccionario o conjunto (set)).
# Permite ejecutar un bloque de codigo varias veces, una vez por cada elemento en el iterable.
# Sintaxis:
#     for <variable> in <iterable>:
#         <codigo a ejecutar> (code to execute)
# El bucle se detendra despues de que el ultimo elemento del iterable haya sido procesado.

# Ejemplo 1: Procesando una lista de precios y aplicando un descuento a cada uno
prices = [100, 200, 300, 400]
discounted_prices = []
for price in prices:
    discounted_price = price * 0.9  # Aplicar 10% de descuento
    discounted_prices.append(discounted_price)
print("Precios Descontados:", discounted_prices)


###############################################


# Ejemplo 2: Recolectando edades validas de una lista (edad debe ser >= 18)
ages = [15, 22, 17, 19, 34]
valid_ages = []
for age in ages:
    if age >= 18:
        valid_ages.append(age)
print("Edades Validas:", valid_ages)
