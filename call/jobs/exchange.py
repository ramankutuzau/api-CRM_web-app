from calculation.models import ExchangeRates
import requests
from bs4 import BeautifulSoup


def update_exchange_rate(name, value):
    try:
        value = round(value, 4)
        exchange_rate = ExchangeRates.objects.get(name=name)
        auto = exchange_rate.auto
        if auto:
            exchange_rate.value = value

        add_percent = exchange_rate.add_percent
        if add_percent:
            value_percent = exchange_rate.value_percent
            exchange_rate.value = exchange_rate.value + (exchange_rate.value / 100 * value_percent)

        exchange_rate.save()
    except ExchangeRates.DoesNotExist:
        ExchangeRates.objects.create(name=name, value=value, auto=True, add_percent=True)


def parse_exchange_rates():
    url = 'https://www.nbrb.by/statistics/rates/ratesdaily.asp'
    try:
        response = requests.get(url)
    except:
        pass
    soup = BeautifulSoup(response.text, 'lxml')
    data = []
    table = soup.find('table', attrs={'class': 'currencyTable'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    for row in data:
        value = float(row[2].replace(',', '.'))

        if row[0] == 'Доллар США':
            update_exchange_rate('USD', value)

        elif row[0] == 'Российский рубль':
            value = value / 100
            update_exchange_rate('RUB', value)

        elif row[0] == 'Евро':
            update_exchange_rate('EUR', value)
