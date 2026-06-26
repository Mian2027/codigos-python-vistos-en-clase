# Uso simple de Tupla: Cambiando variables

# Valores iniciales
x, y = 10, 20
# Salidas: Antes de cambiar los valores: x = 10, y = 20
print('Before swapping: x =', x, ', y =', y)

# Cambiando valores usando desempaquetado de tuplas
x, y = y, x
# Salida: Despues de intercambiar: x = 20, y = 10
print('After swapping: x =', x, ', y =', y)
