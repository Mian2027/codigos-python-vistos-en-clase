# Removiendo el Ultimo Puesto Ingresado con popitem()

person = {"nombre": "Alice", "edad": 31, "ciudad": "Nueva York"}

# Removiendo la ultima pares clave-valor insertado usando popitem()
last_item = person.popitem()
print('Updated dictionary:', person)  # Salida: Diccionario actualizado: {'nombre': 'Alice', 'edad': 31}
print('Removed item:', last_item)  # Salida: Eliminado el elemento: ('ciudad', 'Nueva York')
