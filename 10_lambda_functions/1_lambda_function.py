# Introduccion a las Funciones Lambda

# Ejemplo 1: Funcion lambda sin parametros
# Las funciones lambda pueden definirse sin parametros y siempre devuelven el mismo valor.
# Esto es util para crear funciones simples, reutilizables y constantes.

no_param = lambda: "Hola, Mundo!"
print('Message from no_param lambda:', no_param())

##########################################################

# Ejemplo 2: Funcion lambda con un solo parametro
# Las funciones lambda pueden tomar un unico parametro, lo que las hace utiles para realizar transformaciones rapidas.
# Aqui definimos una funcion lambda para elevar al cuadrado un numero.

square = lambda x: x ** 2
print('Square of 4 using lambda:', square(4))

##########################################################

# Funcion lambda con multiples parametros
# Las funciones lambda pueden tomar multiples parametros para realizar operaciones sobre ellos.
# Este ejemplo muestra una funcion lambda que multiplica dos numeros.

multiply = lambda x, y: x * y
print('Result of multiplying 3 and 4 using lambda:', multiply(3, 4))

##########################################################

# Ejemplo 4: Lambda retornando multiples outputs
# Aunque las funciones lambda estan limitadas a una expresion unica, pueden devolver multiples valores usando tuplas o listas. Esto hace que sean versatiles incluso en escenarios sencillos.
# Al igual que las funciones lambda, los metodos tambien pueden ser definidos como closures.

multiple_outputs = lambda x: (x, x**2, x**3)
print('Multiple outputs from lambda:', multiple_outputs(2))
