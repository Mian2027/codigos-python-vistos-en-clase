# Version de Python: La iteracion sobre listas ha sido soportada desde Python 1.0 (Enero 1994).

# Iterando Sobre Elementos en un Arreglo (Lista)
# Python te permite iterar sobre los elementos de una lista usando un ciclo for.

# Lista de ejemplo
colors = ["rojo", "verde", "azul"]

# 1. Iterando usando un ciclo for
# Esta es la forma mas directa de iterar sobre los elementos de una lista.
for color in colors:
    print('Color:', color)  # Salida: Color: rojo, Color: verde, Color: azul

# 2. Iterando con indice usando enumerate()
# La funcion enumerate() anade un contador a la iteracion, permitiendote acceder tanto al indice como al valor.
for index, color in enumerate(colors):
    print('Indice', index, ':', color)  # Salida: Indice 0: rojo, Indice 1: verde, Indice 2: azul

# Nota: El ciclo for de Python es una herramienta poderosa para iterar sobre listas.
# La funcion enumerate() anade un contador a la iteracion, permitiendote acceder tanto al indice como al valor.

# 3. Iterando Usando un Ciclo `while` (Menos Comun)
# Un ciclo `while` puede ser usado para iterar sobre una lista si necesitas mas control sobre el flujo del ciclo.
index = 0
while index < len(colors):
    print('Indice', index, ':', colors[index])
    index += 1  # Salida: Indice 0: rojo, Indice 1: verde, Indice 2: azul

# 4. Iterando Sobre Multiples Listas Simultaneamente con `zip()`
# `zip()` empareja elementos de cada lista juntos, permitiendo iteracion paralela.
shades = ["claro", "oscuro", "medio"]
for color, shade in zip(colors, shades):
    print(shade.capitalize(), color)  # Salida: Claro rojo, Oscuro verde, Medio azul

# 5. Iterando en Orden Inverso Usando `reversed()`
# La funcion `reversed()` te permite iterar sobre la lista en orden inverso.
for color in reversed(colors):
    print('Color:', color)  # Salida: Color: azul, Color: verde, Color: rojo
