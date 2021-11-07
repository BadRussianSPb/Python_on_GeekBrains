__author__ = 'Pavlov_Egor'

import requests
import time
from bs4 import BeautifulSoup
from decimal import Decimal
from datetime import datetime as dt


def cureency_rates_str(ticker_str):
    """
    Request for a currency exchange rate in the Central Bank of the Russian Federation
    string methods
    :param ticker_str: currency ticker
    :return: response as a list of elements
    """
    response = requests.api.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)

    ticker_str = str(ticker_str.upper())
    list_of_answer = []
    if ticker_str in content:

        date_of_char = dt.date(dt.strptime(content[content.find('Date') + 6:content.find('Date') + 16:], '%d.%m.%Y'))
        char_code_ind = content.find(ticker_str)  # нашел обозначение валюты
        nominal_first_ind = content.find('Nominal', char_code_ind,)  # нашел номинал после обозначения
        nominal_last_ind = content.find('<', nominal_first_ind,)
        nominal = float(content[nominal_first_ind + 8:nominal_last_ind:])  # записал номинал на всякий дальнейший случай
        value_ind = content.find('Value', nominal_last_ind, )  # нашел метку курса после номинала
        first_ind = value_ind + 6  # первый индекс курса
        second_ind = content.find('<', first_ind, )  # последний индекс курса
        value_of_char = Decimal(content[first_ind:second_ind:].replace(',', '.'))
        list_of_answer.extend(['На', date_of_char, 'за', nominal, ticker_str, value_of_char, 'RUB'])
        return list_of_answer
    else:
        return None


def cureency_rates_bs4(ticker_bs4):
    """
    Request for a currency exchange rate in the Central Bank of the Russian Federation
    BeautifulSoup4 methods
    :param ticker_bs4: currency ticker
    :return: response as a list of elements
    """
    response = requests.api.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    ticker_bs4 = str(ticker_bs4.upper())
    if ticker_bs4 in content:
        content_of_bs = BeautifulSoup(content, features="html.parser")
        ticker_bs4 = str(ticker_bs4.upper())
        list_of_answer = []
        list_of_ticker = []
        list_of_values = []
        list_of_nominals = []
        dict_of_values = {}
        dict_of_nominals = {}
        for tickers, values, nominals in zip(content_of_bs.find_all('charcode'),
                                             content_of_bs.find_all('value'),
                                             content_of_bs.find_all('nominal')):
            list_of_ticker.append(tickers.text)  # наполнил список тикеров
            list_of_values.append(Decimal(values.text.replace(',', '.')))  # наполнил список курсов
            list_of_nominals.append(float(nominals.text))  # наполнил список номиналов
        for key, value, value2 in zip(list_of_ticker, list_of_values, list_of_nominals):
            dict_of_values.setdefault(key, []).append(value)    # наполнил справочник курсов
            dict_of_nominals.setdefault(key, []).append(value2)  # наполнил справочник номиналов. dict in dict никак
        date_of_char = dt.date(dt.strptime(content_of_bs.find('valcurs').get('date'), '%d.%m.%Y'))  # нашел дату
        value_of_char = dict_of_values.get(ticker_bs4)
        value_of_nominal = dict_of_nominals.get(ticker_bs4)
        list_of_answer.extend(['На', date_of_char, 'за', *value_of_nominal, ticker_bs4, *value_of_char, 'RUB'])
        return list_of_answer
    else:
        return None


if __name__ == '__main__':
    start_time = time.time()
    ticker = 'гне'
    print(cureency_rates_str(ticker))
    print(cureency_rates_bs4(ticker))
    print((time.time() - start_time), "s")
