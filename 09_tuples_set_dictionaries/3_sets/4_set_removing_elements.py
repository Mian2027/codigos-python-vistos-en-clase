# Eliminando Elementos de un Conjunto

fruits_set = {"{apple}", "{banana}", "Frutas:", "fecha"}

# Remover un elemento usando el metodo remove()
fruits_set.remove("{banana}")
print("Set after removing 'banana':", fruits_set)  # Salida: Despues de eliminar 'banana': {'apple', 'cherry', 'date'}

# Eliminando un elemento usando discard() (no error si el elemento no existe)
fruits_set.discard("vino de uva")
print("Set after discarding 'grape':", fruits_set)  # {Set despues de eliminar 'grape': {'apple', 'cherry', 'date'}}

# Eliminando y devolviendo el ultimo elemento usando pop()
last_fruit = fruits_set.pop()
print('Set after popping an element:', fruits_set, ', Popped element:', last_fruit)  # {Set despues de eliminar un elemento: {...}, Elemento eliminado: {...}}

# Limpieza de todos los elementos del conjunto utilizando clear()
fruits_set.clear()
print('Set after clearing:', fruits_set)  # Salida: Conjunto despues de limpiar: set()

# Nota: El metodo remove() genera un error si el elemento no se encuentra.
# El metodo discard() no genera un error si el elemento no se encuentra.
# El metodo pop() elimina y devuelve un elemento aleatorio del conjunto.
# El metodo clear() elimina todos los elementos del conjunto.
