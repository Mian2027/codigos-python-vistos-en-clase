# Un bucle `for` puede incluir opcionalmente un bloque `else`.
# El bloque `else` se ejecuta despues de que el bucle termina,
# salvo que el bucle se interrumpa con `break`.
# Sintaxis:
#     for <variable> in <iterable>:
#         <codigo>
#     else:
#         <codigo a ejecutar si el bucle termina sin break>

# Ejemplo 1: verificar la disponibilidad de un producto en una lista.
products = ["laptop", "tableta", "smartphone", "monitor"]
for product in products:
    print('Verificando disponibilidad de', product, '...')
else:
    print("Todos los productos fueron revisados.")


###############################################


# Ejemplo 2: detener la busqueda cuando se encuentra un producto especifico.
search_item = "tableta"
for product in products:
    if product == search_item:
        print(search_item, 'encontrado!')
        break  # Detiene la busqueda cuando se encuentra el item.
else:
    print(search_item, 'no encontrado.')
