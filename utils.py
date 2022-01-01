import requests
import datetime


def curency_rate(user_valute):
    responce = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = responce.content.decode(encoding=responce.encoding)
    date_content = content.split('Date="')[1][:10]
    date_string = '/'.join(date_content.split('.'))
    date = datetime.datetime.strptime(date_string, '%d/%m/%Y').date()
    valute = {}
    for el in content.split('<Valute ID='):
        if el.find('<CharCode>') != -1:
            key = el.split('<CharCode>')[1][:3]
            value = round(float('.'.join(el.split('<Value>')[1][:7].split(','))), 2)
            valute[key] = value
    if valute.get(user_valute.upper()):
        print(f'{date} курс {user_valute.upper()} равен {valute[user_valute.upper()]} р')
    else:
        print(valute.get(user_valute))


if __name__ == '__main__':
    curency_rate('gbp')
    curency_rate('USD')
    curency_rate('eur')
    curency_rate('RUB')
