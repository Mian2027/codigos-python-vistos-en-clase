# Actualizando un diccionario anidado

company = {
    "employee_1": {"nombre": "Alice", "edad": 31, "salario": 70000},
    "employee_2": {"nombre": "Bob", "edad": 28, "salario": 60000},
}

# Actualizar un diccionario anidado
company["employee_1"]["salario"] = 75000
print('Updated company dictionary:', company)
