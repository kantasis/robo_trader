#!/usr/local/bin/python3

from os import environ
from alpaca.trading.client import TradingClient

alpaca_endpoint_str = environ['ALPACA_ENDPOINT']
alpaca_key_str = environ['ALPACA_KEY']
alpaca_secret_str = environ['ALPACA_SECRET']

trading_client = TradingClient(
   alpaca_key_str,
   alpaca_secret_str,
)

print(trading_client.get_account().account_number)






