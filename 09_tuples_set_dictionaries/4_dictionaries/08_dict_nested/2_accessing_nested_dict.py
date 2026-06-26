# Accediendo a un Diccionario Nestado

company = {
    "employee_1": {"nombre": "Alice", "edad": 31, "salario": 70000},
    "employee_2": {"nombre": "Bob", "edad": 28, "salario": 60000},
}

# Acceso a elementos nestados
employee_1_name = company["employee_1"]["nombre"]
print("Employee 1's name:", employee_1_name)  # Salidas: Nombre del empleado 1: Alice
