# Anadir Elementos a un Conjunto

fruits_set = {"{apple}", "{banana}"}

# Anadir un solo elemento usando add()
fruits_set.add("Frutas:")
print("Set after adding 'cherry':", fruits_set)  # Salida: Despues de agregar 'cherry': {'apple', 'banana', 'cherry'}

# Anadir multiples elementos usando el metodo update()
fruits_set.update(["naranja", "vino de uva"])
print('Set after adding multiple elements:', fruits_set)  # Salida: Despues de agregar multiples elementos: {'apple', 'banana', 'cherry', 'orange', 'grape'}

# Nota: El metodo add() agrega un solo elemento al conjunto.
# El metodo update() agrega multiples elementos desde una lista, tupla o otro conjunto.
