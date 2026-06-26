# Copiando un Diccionario con copy()

person = {"nombre": "Alice", "edad": 31, "ciudad": "Nueva York"}

# Primero, asignemos la diccionario original a una nueva variable sin usar copy()
person_copy = person

# En este punto, 'person' y 'person_copy' se refieren al mismo objeto de diccionario en memoria.
# Modificar uno afectara el otro porque no son independientes entre si.

# Vamos a modificar 'persona_copia'
person_copy["edad"] = 32

# Ahora, vamos a verificar ambos diccionarios
print('Original dictionary after modification:', person)  # Salida: Diccionario original despues de la modificacion: {'nombre': 'Alice', 'edad': 32, 'ciudad': 'Nueva York'}
print("Modified 'person_copy' dictionary:", person_copy)  # Salida: Diccionario 'persona_copia' modificado: {'nombre': 'Alice', 'edad': 32, 'ciudad': 'Nueva York'}

# Nota que tanto 'persona' como 'persona_copia' han sido modificados.
# Esto porque ambos apuntan a la misma objeto de diccionario.

# Ahora, veamos como usar el metodo copy() evita este problema.

# Restablezca el 'persona' diccionario
person = {"nombre": "Alice", "edad": 31, "ciudad": "Nueva York"}

# Crea una copia verdadera del diccionario utilizando el metodo copy()
person_copy = person.copy()

# Con `copy()`, 'person_copy' ahora referencia un objeto diferente de diccionario.
# Modificando 'person_copy' no afectara el diccionario original 'person'.

# Modifica el diccionario copiado
person_copy["edad"] = 32

# Verifica ambos diccionarios de nuevo.
print('Original dictionary after using copy():', person)  # Salida: Diccionario original despues de usar copia(): {'name': 'Alice', 'age': 31, 'city': 'New York'}
print('Copied and modified dictionary:', person_copy)  # Salida: Diccionario copiado y modificado: {'name': 'Alice', 'age': 32, 'city': 'New York'}

# Ahora, el diccionario original permanece inmutable porque 'person_copy' es una copia independiente.
