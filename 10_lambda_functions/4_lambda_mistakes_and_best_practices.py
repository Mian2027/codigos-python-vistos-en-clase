# Mismesas Comunes y Practicas con Funciones Lambda

# Error 1: Suponer que la funcion lambda tiene un retorno implicito
# Las funciones lambda devuelven el resultado de la expresion, pero es importante recordar que esta expresion es el unico resultado que pueden devolver.

no_return = lambda x: x + 1
print('No return lambda with 4:', no_return(4))

##########################################################

# Error 2: Intentar usar sentencias multiples en una funcion lambda
# Las funciones lambda en Python solo pueden contener una expresion, por lo que intentar incluir logica multilinea resultara en un error.

# Descomentando el siguiente codigo causara un error de sintaxis.
# multi_line = lambda x: (y = x + 1; z = y + 2)

##########################################################

# Error 3: Usar funciones lambda para logica compleja
# Las funciones lambda son las mejores para operaciones simples. Para logica compleja o procesos multi-estep, es mejor definir una funcion regular por claridad y mantenibilidad.
# Hay que evitar la logica compleja en las funciones lambda (la practica recomendada es evitar la logica compleja).

# Manejar excepciones en funciones lambda (la practica recomendada es evitar la logica compleja)
safe_divide = lambda x, y: x / y if y != 0 else "Undefined"
print('Safe division:', safe_divide(10, 2), 'and', safe_divide(10, 0))

##########################################################

# Practica de la mejor practica: Utilice funciones lambda para operaciones simples y enlazadas unicamente.
# Si su funcion lambda comienza a ser demasiado compleja, es un indicio de que deberia usar una funcion regular en su lugar.
