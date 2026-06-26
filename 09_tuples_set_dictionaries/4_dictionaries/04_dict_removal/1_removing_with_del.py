# Eliminar una Pares de Clave-Valor con `del`

person = {"nombre": "Alice", "edad": 31, "ciudad": "Nueva York"}

# Eliminar un par clave-valor usando `del`
del person["ciudad"]
# Salida: Diccionario actualizado: {'nombre': 'Alice', 'edad': 31}
print('Updated dictionary:', person)
