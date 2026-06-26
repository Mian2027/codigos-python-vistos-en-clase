# Un `nested for loop` (bucle for anidado) ocurre cuando colocas un bucle `for` dentro de otro bucle `for`.
# Esto es util para iterar sobre multiples iterables (iterables) simultaneamente o cuando necesitas realizar iteraciones complejas.
# Sintaxis:
#     for <variable1> in <iterable1>:
#         for <variable2> in <iterable2>:
#             <codigo a ejecutar>

# Ejemplo 1: Comparando dos listas de productos para encontrar elementos comunes
products_in_stock = ["laptop", "tablet", "monitor"]
requested_products = ["smartphone", "tablet", "laptop"]
for stock_product in products_in_stock:
    for requested_product in requested_products:
        if stock_product == requested_product:
            print(requested_product, 'esta disponible en stock.')


###############################################


# Ejemplo 2: Creando una lista de combinaciones de dos iterables diferentes
# (por ejemplo, colores y tamanos)
colors = ["red", "blue", "green"]
sizes = ["small", "medium", "large"]
combinations = []
for color in colors:
    for size in sizes:
        combinations.append("{} - {}".format(color, size))
print("Combinaciones disponibles:", combinations)
