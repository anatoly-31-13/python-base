"""
Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
Код валюты может быть в произвольном регистре.
Функция должна возвращать результат числового типа, например float.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
http://www.cbr.ru/scripts/XML_daily.asp.
Выведите на экран курсы для доллара и евро, используя написанную функцию.
Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере,
посмотреть содержимое ответа.
"""

import requests
from bs4 import BeautifulSoup



dollar_rub = 'https://www.google.ru/search?newwindow=1&source=hp&ei=sWZLYLCuBMrF5OUPsZu52AI&iflsig=' \
             'AINFCbYAAAAAYEt0wYgsMxtob9lw9Jgqy4Ixm6KibC-p&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0' \
             '%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%' \
             'D1%81&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCAAQRhCCAjICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIA' \
             'DoKCAAQ6gIQtAIQQzoICAAQxwEQrwE6AgguOggIABDHARCjAlCfSljsaGDNeGgDcAB4AYABnAeIAYAgkgEHMS41LT' \
             'QuMpgBAKABAaoBB2d3cy13aXqwAQo&sclient=gws-wiz'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50'}


def get_currency_rate():
    full_page = requests.get(dollar_rub, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll('span', {'class': "DFlfde", 'class': 'SwHCTb', 'data-precision': 2})
    print("Сейчас курс 1 доллар = ", convert[0].text)


get_currency_rate()