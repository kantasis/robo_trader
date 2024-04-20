#!/usr/local/bin/python3

# Imports
from os import environ
# from alpaca.trading.client import TradingClient
from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from datetime import datetime

# Parameters
alpaca_endpoint_str = environ['ALPACA_ENDPOINT']
alpaca_key_str = environ['ALPACA_KEY']
alpaca_secret_str = environ['ALPACA_SECRET']

ticker_name="GE"

# Main

trading_client = TradingClient(
   alpaca_key_str,
   alpaca_secret_str,
)

print(trading_client.get_account().account_number)
print(trading_client.get_account().buying_power)






