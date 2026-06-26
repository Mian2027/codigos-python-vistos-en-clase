# Desempaquetar claves especificas de un diccionario con ** para una funcion matematica
def calculate_force(mass, acceleration):
    return mass * acceleration

data = {'masa': 60, 'aceleracion': 9.8, 'friccion': 0.3}

# Crear un nuevo diccionario con solo las claves necesarias
physics_data = {key: data[key] for key in ['masa', 'aceleracion']}

# Desempaquetando el diccionario filtrado
force = calculate_force(**physics_data)
print('Force:', force)  # Force: 588.0
