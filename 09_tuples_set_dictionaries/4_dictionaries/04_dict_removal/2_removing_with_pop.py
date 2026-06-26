# Remover una Pares de Clave-Valor con pop()

person = {"nombre": "Alice", "edad": 31, "ciudad": "Nueva York"}

# Removiendo un par de clave-valor usando pop()
city = person.pop("ciudad")
print('Updated dictionary:', person)  # Salida: Diccionario actualizado: {'nombre': 'Alice', 'edad': 31}
print('Removed city:', city)  # Removed ciudad: Nueva York
