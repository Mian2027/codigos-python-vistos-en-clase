# Ejercicio practico: inventario con listas

## Instrucciones

Completa `exercise.py`.

El programa debe representar un inventario de productos usando una lista.

Debes:

1. crear una lista inicial con `"lapiz"`, `"cuaderno"`, `"borrador"` y `"regla"`;
2. mostrar el inventario inicial;
3. obtener el primer producto usando indice positivo;
4. obtener el ultimo producto usando indice negativo;
5. obtener los productos centrales usando slicing;
6. modificar `"cuaderno"` por `"agenda"`;
7. agregar `"mochila"` al final con `append()`;
8. insertar `"plumon"` en la posicion 2 con `insert()`;
9. agregar `"colores"` y `"tijera"` con `extend()`;
10. eliminar `"borrador"` con `remove()`;
11. mostrar el inventario actualizado;
12. vender el primer producto usando `pop(0)`;
13. comprobar si `"regla"` existe en el inventario;
14. obtener el indice de `"regla"`;
15. obtener la cantidad de productos con `len()`;
16. obtener los primeros tres productos y los ultimos dos usando slicing;
17. mostrar los productos finales usando `for` y `enumerate()`.

Debes utilizar:

- una lista;
- indices positivos y negativos;
- slicing;
- `append()`;
- `insert()`;
- `extend()`;
- `remove()`;
- `pop()`;
- `in`;
- `index()`;
- `len()`;
- `for`;
- `enumerate()`.

## Ejemplo de salida

```text
Inventario inicial: ['lapiz', 'cuaderno', 'borrador', 'regla']
Primer producto: lapiz
Ultimo producto: regla
Productos centrales: ['cuaderno', 'borrador']
Inventario actualizado: ['lapiz', 'agenda', 'plumon', 'regla', 'mochila', 'colores', 'tijera']
Producto vendido: lapiz
Inventario final: ['agenda', 'plumon', 'regla', 'mochila', 'colores', 'tijera']
Hay regla: True
Indice de regla: 2
Cantidad de productos: 6
Primeros tres: ['agenda', 'plumon', 'regla']
Ultimos dos: ['colores', 'tijera']
Productos enumerados:
1. agenda
2. plumon
3. regla
4. mochila
5. colores
6. tijera
```
