"""
Спросить у пользователя три числа, напечатать какое число больше других.
Вывести фразу с номером большего числа. Если три числа равны вывести "все числа равны".
Если два наибольших числа равны между собой вывести их номера, например "первое и второе".
Например, если пользователь ввел: 11, 23, 23 - напечатать "второе и третье"
"""

a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))
c = int(input("Введите число 3: "))

if a > b and a > c:
    print("первое")
elif b > a and b > c:
    print("второе")
elif c > a and c > b:
    print("третье")
elif a > c and b > c:
    print("первое и второе")
elif b > a and c > a:
    print("второе и третье")
elif a > b and c > b:
    print("первое и третье")
else:
    print("числа равны")