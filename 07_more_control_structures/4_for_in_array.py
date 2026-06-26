# El bucle `for-in` se usa comunmente para iterar directamente sobre los elementos de un iterable (como una lista, tupla o cadena (string)).
# Esto es mas conciso que usar un indice para acceder a cada elemento en el iterable.
# Sintaxis:
#     for <variable> in <iterable>:
#         <codigo a ejecutar>

# Ejemplo 1: Iterar a traves de una lista de nombres de clientes e imprimir un saludo
customers = ["Alice", "Bob", "Charlie", "Dana"]
for customer in customers:
    print('Hola,', customer, '! Bienvenido a nuestra tienda.')


###############################################


# Ejemplo 2: Modificar una lista de nombres de empleados para agregar sus titulos de trabajo
employees = ["Alice", "Bob", "Charlie"]
titled_employees = []
for employee in employees:
    titled_employees.append("{} - Ingeniero de Software".format(employee))
print("Empleados con Titulos:", titled_employees)
