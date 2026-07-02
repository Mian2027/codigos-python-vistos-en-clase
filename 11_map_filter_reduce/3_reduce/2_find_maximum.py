# Ejemplo: Utilizar reduce para encontrar el elemento maximo en una lista
from functools import reduce

numbers = [1, 2, 3, 4, 5]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print('Maximum value:', max_value)
