# Funciones Lambda con Logica Condicional

# Ejemplo 1: Verifica si un numero es par o impar
# La logica condicional permite que las funciones lambdas hagan decisiones basadas en el input.
# Esta funcion lambda verifica si un numero es par o impar.

check_even_odd = lambda x: "Pares" if x % 2 == 0 else "Impares"
print('The number 7 is:', check_even_odd(7))

##########################################################

# Ejemplo 2: Determinar si un numero es positivo, negativo o cero
# Las funciones lambda pueden manejar condicionales anidados para producir multiples resultados.

check_sign = lambda x: "Positivo" if x > 0 else ("Negativo" if x < 0 else "Cero")
print('The number -5 is:', check_sign(-5))

##########################################################

# Ejemplo 3: Categorizar longitud de cadena
# Utilice funciones lambda para clasificar cadenas segun su longitud.
# Este ejemplo categoriza una cadena como 'Corta', 'Media' o 'Larga'.

check_string_length = lambda s: "Corta" if len(s) < 5 else ("Media" if len(s) < 10 else "Long")
print("The string 'hello' is:", check_string_length('Hola'))

##########################################################

# Ejemplo 4: Categorizar el grupo de edad
# Esta funcion categoriza la edad de una persona en 'Nino', 'Adolescente' o 'Adulto'.

categorize_age = lambda age: "Nino" if age < 13 else ("Adolescente" if age < 18 else "Adulto")
print('The age 16 is categorized as:', categorize_age(16))
