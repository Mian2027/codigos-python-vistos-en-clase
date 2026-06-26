# Comprehesion de Diccionarios con Condicionales

person = {"nombre": "Alice", "edad": 31, "ciudad": "Nueva York"}

# Crear un nuevo diccionario filtrando los elementos
filtered_dict = {k: v for k, v in person.items() if k != "ciudad"}
print('Filtered dictionary:', filtered_dict)  # Salida: Diccionario filtrado: {'nombre': 'Alice', 'edad': 31}
