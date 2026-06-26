# Version de Python: Combinar y rebanar listas ha sido soportado desde Python 1.0 (enero 1994).

# Combinar y Rebanar Arreglos (Listas)
# Python te permite combinar y rebanar listas facilmente.

# Listas de ejemplo
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Combinando listas usando concatenacion (+)
combined_list = list1 + list2
print('Lista combinada:', combined_list)  # Salida (output): Lista combinada: [1, 2, 3, 4, 5, 6]

# Rebanando una lista para obtener un subconjunto
subset_list = combined_list[2:5]  # Obtiene elementos del indice 2 al 4 (5 no es incluido)
print('Lista rebanada:', subset_list)  # Salida (output): Lista rebanada: [3, 4, 5]

# Nota: El operador + concatena dos listas.
# Rebanar te permite extraer una porcion de la lista especificando un indice de inicio y fin.
