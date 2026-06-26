# Desempaquetado de Tuplas con *args en Definiciones de Funciones

def print_all(*args):
    # args es una tupla que contiene todos los argumentos pasados a la funcion.
    for arg in args:
        print(arg)


# Llamar a la funcion con multiples argumentos
print_all(1, 2, 3, 4)
# {output}
# 1
# 2
# 3
# 4

# Llamar a la funcion con un argumento de tupla unico
print_all((5, 6))
# {output}
# (5, 6)
