# Version de Python: Eliminar elementos de listas ha sido soportado desde Python 1.0 (Enero 1994).

# Eliminando Elementos de un Arreglo (List)
# Python proporciona varias formas de eliminar elementos de una lista.

# Lista de ejemplo
fruits = ["apple", "banana", "cherry", "date"]

# Eliminando un elemento por valor usando remove()
fruits.remove("banana")
print('Despues de remove:', fruits)  # Salida (output): Despues de remove: ['apple', 'cherry', 'date']

# Eliminando un elemento por indice usando pop()
popped_fruit = fruits.pop(1)
print('Despues de pop:', fruits, ', Fruta eliminada:', popped_fruit)  # Salida (output): Despues de pop: ['apple', 'date'], Fruta eliminada: cherry

# Eliminando el ultimo elemento usando pop() sin un indice
last_fruit = fruits.pop()
print('Despues de pop sin indice:', fruits, ', Ultima fruta:', last_fruit)  # Salida (output): Despues de pop sin indice: ['apple'], Ultima fruta: date

# Limpiando todos los elementos de la lista usando clear()
fruits.clear()
print('Despues de clear:', fruits)  # Salida (output): Despues de clear: []

# Nota: El metodo remove() elimina la primera ocurrencia de un valor.
# El metodo pop() elimina y devuelve el elemento en el indice especificado, o el ultimo elemento si no se proporciona un indice.
# El metodo clear() elimina todos los elementos de la lista.
