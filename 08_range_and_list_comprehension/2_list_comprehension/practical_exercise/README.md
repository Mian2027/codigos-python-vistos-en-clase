# Ejercicio practico: list comprehensions

## Instrucciones

Completa `exercise.py`.

El programa debe crear nuevas listas usando list comprehensions.

Debes:

1. crear una lista de numeros del 1 al 10;
2. crear una lista con los cuadrados de esos numeros;
3. crear una lista solo con los numeros pares;
4. crear una lista solo con los numeros mayores que 5;
5. crear una lista de etiquetas `"Par"` o `"Impar"`;
6. crear una lista donde los pares se dupliquen y los impares se conviertan en `0`;
7. crear una lista de nombres en mayusculas;
8. crear una lista de nombres que tengan mas de 4 caracteres;
9. crear pares `(numero, letra)` combinando numeros y letras con varios `for`;
10. crear pares solo con numeros pares y vocales `"a"` y `"e"`;
11. mostrar todos los resultados.

Debes utilizar:

- list comprehensions simples;
- list comprehensions con `if`;
- list comprehensions con `if/else`;
- metodos de strings dentro de una comprehension;
- multiples `for` dentro de una comprehension.

## Ejemplo de salida

```text
Numeros: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Cuadrados: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Pares: [2, 4, 6, 8, 10]
Mayores que 5: [6, 7, 8, 9, 10]
Etiquetas: ['Impar', 'Par', 'Impar', 'Par', 'Impar', 'Par', 'Impar', 'Par', 'Impar', 'Par']
Pares duplicados e impares en cero: [0, 4, 0, 8, 0, 12, 0, 16, 0, 20]
Nombres en mayusculas: ['ANA', 'LUIS', 'MARCELA', 'JOSE']
Nombres largos: ['Marcela']
Pares numero-letra: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
Pares filtrados: [(2, 'a'), (2, 'e'), (4, 'a'), (4, 'e')]
```
