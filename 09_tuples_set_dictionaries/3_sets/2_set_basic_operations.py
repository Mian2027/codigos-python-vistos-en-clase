# Operaciones de conjuntos basicas: pertenencia y longitud

# Ejemplo conjunto
fruits_set = {"{apple}", "{banana}", "Frutas:"}

# Verificacion de pertenencia
is_apple_in_set = "{apple}" in fruits_set
print("Is 'apple' in set:", is_apple_in_set)  # Salida: {'apple'} esta en el conjunto: True

# Verificacion de no membresia
is_grape_in_set = "vino de uva" not in fruits_set
print("Is 'grape' not in set:", is_grape_in_set)  # Salida: No esta 'grape' en el conjunto: True

# Obtener el largo de un conjunto
set_length = len(fruits_set)
print('Number of elements in set:', set_length)  # Salida: Cantidad de elementos en el conjunto: 3
