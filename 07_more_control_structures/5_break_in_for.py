# La sentencia `break` se usa para salir del bucle (loop) prematuramente, deteniendo las iteraciones restantes.
# Cuando se encuentra `break` dentro de un bucle (loop), el bucle se termina inmediatamente.
# Sintaxis:
#     for <variable> in <iterable>:
#         if <condition>:
#             break
#         <codigo a ejecutar>

# Ejemplo 1: Buscar un producto especifico y detenerse cuando se encuentra
products = ["laptop", "tablet", "smartphone", "monitor"]
for product in products:
    if product == "smartphone":
        print(product, 'encontrado en stock!')
        break  # Detenerse una vez que se encuentra el producto
    print('Aun revisando:', product)


###############################################


# Ejemplo 2: Buscar el primer numero grande en una lista
numbers = [10, 15, 25, 35, 50]
for num in numbers:
    if num > 30:
        print('Se encontro un numero grande:', num)
        break
    print(num, 'no es lo suficientemente grande.')
