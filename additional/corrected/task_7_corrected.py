"""
Спросить у пользователя число.
Вывести на экран это число и квадрат (вторую степень) этого числа.
Например, если пользователь ввел "13", то напечатать "13^2 = 169".
Продолжить спрашивать числа у пользователя пока он не введет "0".
Когда пользователь введет "0" - вывести результат и остановиться.
"""

first = int(input("Введите число: "))
i = 0
if first == 0:
    print("end")
else:
    while first != 0:
        print(first, first ** 2)
        i += 1
        first = int(input("Введите число: "))
        if first == 0:
            print(first, first ** 2)