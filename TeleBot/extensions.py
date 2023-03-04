import requests
import json
from config import keys


class ConvertionException(Exception):
    pass

class APIException:
    @staticmethod
    def convert(to: str, base: str, amount: str):
        if to == base:
            raise APIException('Невозможно перевести одинаковые валюты. Введите значение по формуле <имя валюты> <в какую валюту перевести> <количество переводимой валюты>')

        try:
            to_ticker = keys[to]
        except KeyError:
            raise APIException(f'Данная валюта не обрабатывается: {to}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Данная валюта не обрабатывается: {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Неверное количество: {amount}')

        headers = {"apikey": "u1Aa9zTGMxSFBWaUR8KxyVA90FTIDuJV"}

        r = requests.get(f'https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={to_ticker}&amount={amount}',
                         headers=headers)
        total_base = json.loads(r.content)["result"]

        return total_base