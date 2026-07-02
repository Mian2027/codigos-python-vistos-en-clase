# Ejemplo: Utilizar map con multiples iterables para sumar elementos de dos listas
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
sum_numbers = list(map(lambda x, y: x + y, numbers1, numbers2))
print('Sum of elements from two lists:', sum_numbers)
