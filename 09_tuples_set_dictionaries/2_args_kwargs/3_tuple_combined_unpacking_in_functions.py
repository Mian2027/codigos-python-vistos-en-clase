# Combiniendo *args y **kwargs en las Definiciones de Funciones

def process_data(a, b, *args, **kwargs):
    print('a:', a, ', b:', b)
    print('Additional positional arguments:', args)
    print('Keyword arguments:', kwargs)


# Llamar la funcion con ambos argumentos posicionales y clave-valor
process_data(1, 2, 3, 4, x=10, y=20)
# {output}
# a: 1, b: 2
# Argumentos Posicionales Adicionales: (3, 4)
# Argumentos de palabras clave: {'x': 10, 'y': 20}

# Nota: Esta funcion puede manejar tanto argumentos fijos como poscionales adicionales (...).
# y argumentos de clave-valor (**kwargs) simultaneamente.
