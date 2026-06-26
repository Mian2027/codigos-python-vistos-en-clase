# Version de Python: Buscar elementos en listas ha sido soportado desde Python 1.0 (enero de 1994).

# Buscando Elementos en un Arreglo (Lista)
# Python provee metodos para buscar elementos dentro de una lista.

# Lista de ejemplo
animals = ["dog", "cat", "bird", "fish"]

# Verificando si un elemento existe usando 'in'
is_dog_present = "dog" in animals
print("Esta 'dog' presente:", is_dog_present)  # Salida (output): Esta 'dog' presente: True

# Encontrando el indice de un elemento usando index()
cat_index = animals.index("cat")
print("Indice de 'cat':", cat_index)  # Salida (output): Indice de 'cat': 1

# Encontrando el conteo de un elemento usando count()
fish_count = animals.count("fish")
print("Conteo de 'fish':", fish_count)  # Salida (output): Conteo de 'fish': 1

# Nota: La palabra clave 'in' se usa para verificar la existencia de un elemento en una lista.
# El metodo index() retorna el indice de la primera ocurrencia de un valor.
# El metodo count() retorna el numero de ocurrencias de un valor en la lista.
