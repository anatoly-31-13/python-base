"""
Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран
отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
"""
n = 0
for n in range(1, 101):
    if n % 10 == 1 and n != 11:
        print(n, "процент")
    if 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        print(n, "процента")
    else:
        print(n, "процентов")

