import requests

currency = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
print(currency)

