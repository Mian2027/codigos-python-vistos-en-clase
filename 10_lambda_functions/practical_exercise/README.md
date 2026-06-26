# Ejercicio practico: lambdas para productos

## Instrucciones

Completa `exercise.py`.

El programa debe usar funciones lambda para trabajar con productos y precios.

Debes:

1. crear una lambda sin parametros que devuelva `"Reporte de productos"`;
2. crear una lambda que calcule el cuadrado de un numero;
3. crear una lambda que calcule el subtotal de un producto usando precio y cantidad;
4. crear una lambda que aplique 10% de descuento a un precio;
5. crear una lambda que diga si un precio es `"Caro"` o `"Economico"`;
6. crear una lista de precios;
7. crear una lambda que reciba una lista y devuelva solo los precios mayores o iguales a 100;
8. crear una lambda que reciba una lista y devuelva los precios con descuento;
9. crear una lista de productos como tuplas `(nombre, precio)`;
10. ordenar los productos por precio usando `sorted()` y `key=lambda`;
11. obtener el producto mas caro usando `max()` y `key=lambda`;
12. mostrar todos los resultados.

Debes utilizar:

- `lambda`;
- lambdas con cero, uno y varios parametros;
- condicional dentro de una lambda;
- list comprehension dentro de una lambda;
- `sorted()` con `key=lambda`;
- `max()` con `key=lambda`.

## Ejemplo de salida

```text
Titulo: Reporte de productos
Cuadrado de 5: 25
Subtotal: 60
Precio con descuento: 90.0
Categoria de precio: Caro
Precios altos: [120, 250, 100]
Precios con descuento: [45.0, 108.0, 225.0, 72.0, 90.0]
Productos ordenados: [('mouse', 50), ('teclado', 80), ('monitor', 650), ('laptop', 2500)]
Producto mas caro: ('laptop', 2500)
```
