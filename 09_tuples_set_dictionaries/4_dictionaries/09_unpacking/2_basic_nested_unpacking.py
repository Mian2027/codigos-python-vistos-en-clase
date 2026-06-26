# Ejemplo de desempaquetado de diccionarios anidados para una funcion matematica
def calculate_volume(length, width, height):
    return length * width * height

box = {
    'materiales': 'carton',
    'dimensiones': {
        'longitud': 10,
        'ancho': 5,
        'altura': 4
    }
}

# Desempaquetando la diccionario 'dimensiones'
volume = calculate_volume(**box['dimensiones'])
print('Volume:', volume)  # Salida: Volumen: 200
