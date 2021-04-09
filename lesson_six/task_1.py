"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
bsodj = BeautifulSoup(html.read())
print(bsodj)


# reg = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
# reg_1 = r'\[a-zA-Z]+'
# ip_list = re.findall(reg, bsodj)
# text = re.findall(reg_1, bsodj)
# print(ip_list, text)s