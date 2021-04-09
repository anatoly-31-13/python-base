"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения
извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError.
Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
"""

import re

emails = 'someone@geekbrains.ru'
email_adress = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z-9-]+\.[a-zA-Z0-9-.]+)", emails)

dictionary = {}
for mail in email_adress:
    mail = ' '.join(emails.strip().split("@"))
    name = ('username', 'domain')
    dictionary = dict.fromkeys(name, mail)
    print(dictionary)