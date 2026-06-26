# Desempaquetado de tuplas con **kwargs en definiciones de funciones

def print_details(**kwargs):
    # kwargs es un diccionario que contiene todas las argumentos por clave
    for key, value in kwargs.items():
        print(key, ':', value)


# Llamando la funcion con argumentos por clave
print_details(name="Alice", age=30, profession="Ingeniero")
# {output}
# nombre: Alice
# edad: 30
# profesion: Ingeniero

# Nota: La sintaxis de **kwargs permite a la funcion aceptar un numero arbitrario de argumentos de palabra clave.
# Los metodos como `append`, `remove`, y `pop` pueden modificar el objeto original, mientras que los metodos como `insert` y `extend` no lo hacen.
