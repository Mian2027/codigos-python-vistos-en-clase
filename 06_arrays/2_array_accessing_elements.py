# Version de Python (Python Version): el acceso a elementos en listas existe desde Python 1.0 (January 1994).

# Accediendo a elementos en un arreglo (lista)
# Los elementos en una lista (list) pueden ser accedidos por su indice, siendo el primer elemento el de indice 0.

# Ejemplo de lista
fruits = ["apple", "banana", "cherry"]

# Accediendo al primer elemento
first_fruit = fruits[0]
print('Primera fruta:', first_fruit)  # Salida (output): Primera fruta: apple

# Accediendo al ultimo elemento usando indexado negativo
last_fruit = fruits[-1]
print('Ultima fruta:', last_fruit)  # Salida (output): Ultima fruta: cherry

# Accediendo a un rango de elementos (slicing / rebanado)
some_fruits = fruits[0:2]  # Obtiene elementos del indice 0 al 1 (el 2 no se incluye)
print('Algunas frutas:', some_fruits)  # Salida (output): Algunas frutas: ['apple', 'banana']

# Nota: Python soporta tanto indexado positivo como negativo. Los indices negativos cuentan desde el final de la lista (list).
# El rebanado (slicing) te permite acceder a un subconjunto de la lista (list) especificando un indice de inicio y fin.
