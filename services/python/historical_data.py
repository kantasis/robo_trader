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

data_client = StockHistoricalDataClient(
   alpaca_key_str,
   alpaca_secret_str,
)

requestParams_dict = {
   "symbol_or_symbols":ticker_name,
   "start":datetime(2024, 4, 18, 14, 00),
   "end":datetime(2024, 4, 18, 14, 30),
}

requestParams_obj = StockTradesRequest( **requestParams_dict )
trades_obj = data_client.get_stock_trades(requestParams_obj)

# print(trades_obj)

for trade in trades_obj.data[ticker_name]:
   print(trade)
   break

