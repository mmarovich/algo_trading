from dotenv import load_dotenv
import os

load_dotenv()

exchange_list = [
    {
        'name': 'Binance US',
        'id': 'binanceus',
        'key': os.getenv('BINANCE_API_KEY'),
        'secret': os.getenv('BINANCE_API_SECRET')  
    },
    {
        'name': 'Phemex',
        'id': 'phemex',
        'key': os.getenv('PHEMEX_API_ID'),
        'secret': os.getenv('PHEMEX_API_SECRET')
    },
    {
        'name': 'MEXC Global',
        'id': 'mexc',
        'key': os.getenv('MEXC_API_KEY'),
        'secret': os.getenv('MEXC_API_SECRET')
    },
    {
        'name': 'Kraken',
        'id': 'kraken',
        'key': os.getenv('KRAKEN_API_KEY'),
        'secret': os.getenv('KRAKEN_API_SECRET')
    },
    {
        'name': 'KuCoin',
        'id': 'kucoin',
        'key': os.getenv('KUCOIN_API_KEY'),
        'secret': os.getenv('KUCOIN_API_SECRET'),
        'password': os.getenv('KUCOIN_API_PASSPHRASE')
    }
    
]