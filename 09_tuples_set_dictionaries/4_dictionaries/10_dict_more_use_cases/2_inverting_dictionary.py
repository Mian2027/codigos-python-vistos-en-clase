# Dinvertir un Diccionario (Las Claves Pasan a Ser Valores y Los Valores Pasan a Ser Claves)

original_dict = {"nombre": "Alice", "profesion": "Ingeniero"}

# Invertiendo el diccionario
inverted_dict = {v: k for k, v in original_dict.items()}
# Salida: Diccionario invertido: {'Alice': 'nombre', 'Engineer': 'profesion'}
print('Inverted dictionary:', inverted_dict)
