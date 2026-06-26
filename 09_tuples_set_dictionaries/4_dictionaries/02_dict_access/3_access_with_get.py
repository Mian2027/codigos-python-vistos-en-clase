# Acceso a claves con el metodo get().

person = {"nombre": "Alice", "edad": 30}

# Acceder a una clave existente.
age = person.get("edad")
print('Edad:', age)  # Salida: Edad: 30

# Acceder a una clave no existente con valor predeterminado.
salary = person.get("salario", "No especificado")
print('Salario:', salary)  # Salida: Salario: No especificado

# Acceder a una clave no existente sin valor predeterminado.
gender = person.get("genero")
print('Genero:', gender)  # Salida: Genero: None

# Acceder a una clave en un diccionario anidado con valor predeterminado.
person = {
    "nombre": "Alice",
    "edad": 30,
    "direccion": {
        "ciudad": "Olimpo",
        "zip": "12345"
    }
}
zip_code = person.get("direccion", {}).get("zip", "No se encontro ZIP")
print('Codigo ZIP:', zip_code)  # Salida: Codigo ZIP: 12345

# Manejo de claves anidadas faltantes.
country = person.get("direccion", {}).get("pais", "Pais no especificado")
print('Pais:', country)  # Salida: Pais: Pais no especificado
