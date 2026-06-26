# Introduccion a diferentes metodos de formato de cadenas (string formatting).
# Contexto historico (historical context):
# - El formato antiguo (old-style formatting) con '%' existe desde Python 1.x.
# - El metodo str.format() fue introducido en Python 2.7 (July 2010) y Python 3.0 (December 2008).
# - Las cadenas con formato nombrado se pueden construir con str.format().
# Explicación: formatear es aplicar una funcion F(plantilla, valores) -> cadena final.


# 1. Formato antiguo

# Este metodo es similar al formato tipo printf (printf-style formatting) de C.
# '%s' se usa como marcador (placeholder) para strings y '%d' para enteros.
# Explicación: la plantilla recibe el par ordenado (name, age) y produce un string.
name = "Marco"
age = 30
print("Hola, %s. Tienes %d años." % (name, age))
# Salida: Hola, Marco. Tienes 30 años.

# 2. Sintaxis con format()

# Este metodo es mas potente y flexible que el operador '%'.
# Usa llaves {} como marcadores (placeholders), que se reemplazan con los argumentos de format().
# Explicación: format(name, age) sustituye posiciones: {}_1 = name y {}_2 = age.
print("Hola, {}. Tienes {} años.".format(name, age))
# Salida: Hola, Marco. Tienes 30 años.

# 3. format() con argumentos nombrados

# str.format() tambien permite usar nombres dentro de la plantilla.
# Esto ayuda a que la cadena sea clara cuando hay varios valores.
# Explicación: format(name=name, age=age) sustituye {name} y {age}.
print("Hola, {name}. Tienes {age} años.".format(name=name, age=age))
# Salida: Hola, Marco. Tienes 30 años.

# 4. print() con multiples objetos

# La documentacion representa estos argumentos posicionales como *objects.
# print() puede recibir varios objetos separados por comas.
# Por defecto, agrega un espacio entre cada argumento y convierte los valores a texto.
# No es necesario convertir manualmente age con str().
# Explicación: print(a, b, c) muestra str(a) + " " + str(b) + " " + str(c).
print("Hola,", name + ".", "Tienes", age, "años.")
# Salida: Hola, Marco. Tienes 30 años.

# Nota: str.format() es util cuando quieres construir una cadena usando una plantilla.
