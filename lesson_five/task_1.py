"""
Написать функцию-генератор rand_nums, генерирующую N случайных целых чисел в диапазоне 1 до 100
(включительно). Количество чисел N, которое выдаст генератор передается в функцию через параметр:

#>>> rand15 = rand_nums(15)
#>>> next(rand15) # 1-й вызов
#11
#>>> next(rand15) # 2-й вызов
#38
#...
#>>> next(rand15) # 15-й вызов
#7
#>>> next(rand15) # 16-й вызов
#...StopIteration...
"""

import random


def rand_nums(*args):
    for i in range(random.randint(1, 100)):
        args = yield random.randint(1, 100)
    print(i)
    rand_nums(args)


rand_15 = rand_nums(15)
rand_15 = iter(rand_15)
print(next(rand_15))
print(next(rand_15))
print(next(rand_15))
print(next(rand_15))
print(next(rand_15))
print(next(rand_15))
print(next(rand_15))
print(next(rand_15))
print(next(rand_15))
print(next(rand_15))
print(next(rand_15))
print(next(rand_15))
print(next(rand_15))
print(next(rand_15))
print(next(rand_15))
# print(next(rand_15))

