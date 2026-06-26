# Crea un diccionario desde claves y valores.

keys = ["nombre", "edad", "salario"]
values = ["Alice", 31, 70000]

# Crea el diccionario usando zip
person_dict = dict(zip(keys, values))
# Salida: Diccionario a partir de claves y valores: {'nombre': 'Alice', 'edad': 31,
# 'salario': 70000}
print('Dictionary from keys and values:', person_dict)
