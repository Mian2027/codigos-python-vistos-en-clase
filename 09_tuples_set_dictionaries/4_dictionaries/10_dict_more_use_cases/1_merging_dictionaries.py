# Juntar dos diccionarios

dict_a = {"nombre": "Alice", "edad": 31}
dict_b = {"profesion": "Ingeniero", "salario": 70000}

# Juntar dos diccionarios (Python 3.9+)
merged_dict = dict_a | dict_b
# Salida: Diccionario juntado: {'name': 'Alice', 'age': 31, 'profession':
# 'Engineer', 'salary': 70000}
print('Merged dictionary:', merged_dict)
