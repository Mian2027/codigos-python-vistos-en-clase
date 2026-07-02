# Ejemplo: Utilizar reduce para concatenar una lista de strings
from functools import reduce

strings = ["{apple}", "{banana}", "Frutas:"]
concatenated_string = reduce(lambda x, y: x + y, strings)
print('Concatenated string:', concatenated_string)
