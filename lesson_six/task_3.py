"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать,
что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""

with open('users.txt', 'w', encoding='utf-8') as f:
    f.write('Иванов, Иван, Иванович\nПетров, Петр, Петрович\n')

with open('hobby.txt', 'w', encoding='utf-8') as f:
    f.write('скалолазание, охота\nгорные лыжи\n')

with open('users.txt', 'r', encoding='utf-8') as f1, open('hobby.txt', 'r', encoding='utf-8') as f2:
    lines = f1.read().splitlines()
    lines_1 = f2.read().splitlines()
    dic = {}
    for line in lines:
        first = line
        dic.setdefault(first, lines_1[0:])
    print(dic)
    # with open('text.txt', 'w', encoding='utf-8') as file:
    #     file.write(dic)

# ks = dic.keys()
# for k in sorted(ks):
#     print(k, dic[k])