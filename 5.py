#Реализуйте алгоритм перемешивания списка.

import random

some_list = list(map(int, input('Заполните список, вводя числа через запятую: ').split(',')))
print(f'Список до перемешевания: {some_list}')
random.shuffle(some_list)
print(f'Список после перемешивания: {some_list}')