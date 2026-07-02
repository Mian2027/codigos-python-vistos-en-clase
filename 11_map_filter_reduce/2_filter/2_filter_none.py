# Ejemplo: Filtrar valores nulos de una lista
mixed_list = [1, None, "Hola", 0, None, 5]
filtered_list = list(filter(None, mixed_list))
print('List after removing None values:', filtered_list)
