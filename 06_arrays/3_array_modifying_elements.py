# Python Version: Modificar elementos en listas es compatible desde Python 1.0 (enero de 1994).

# Modificar Elementos en un Arreglo (Lista)
# Las listas en Python son mutables, lo que significa que sus elementos pueden cambiarse despues de su creacion.

# Lista de ejemplo
colors = ["red", "green", "blue"]

# Modificar un elemento por indice
colors[1] = "yellow"
print('Colores modificados:', colors)  # Salida: Colores modificados: ['red', 'yellow', 'blue']

# Modificar un rango de elementos (slicing)
colors[0:2] = ["purple", "orange"]
print('Colores modificados con slicing:', colors)  # Salida: Colores modificados con slicing: ['purple', 'orange', 'blue']

# Nota: Como las listas son mutables, puedes cambiar directamente sus elementos usando indexacion.
# El slicing permite la modificacion en bloque de varios elementos a la vez.
