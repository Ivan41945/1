import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote:str, base:str, amount:str):

        if quote == base:
            raise ConvertionException(f'Невозможен перевод одинаковой валюты - {base}.')

        try:
            quote_tkr = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_tkr = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tkr}&tsyms={base_tkr}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base