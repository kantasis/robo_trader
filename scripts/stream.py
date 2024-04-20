#!/usr/local/bin/python3

# Imports
from os import environ
from alpaca.data.live import StockDataStream

# Parameters
alpaca_endpoint_str = environ['ALPACA_ENDPOINT']
alpaca_key_str = environ['ALPACA_KEY']
alpaca_secret_str = environ['ALPACA_SECRET']

ticker_name="SPY"

# Main

stream = StockDataStream (
   alpaca_key_str,
   alpaca_secret_str,
)

async def handle_trade(data):
   print(data)

stream.subscribe_trades(handle_trade, ticker_name)
stream.run()
