#!/usr/local/bin/python3

# Imports
from os import environ
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

# Parameters
alpaca_endpoint_str = environ['ALPACA_ENDPOINT']
alpaca_key_str = environ['ALPACA_KEY']
alpaca_secret_str = environ['ALPACA_SECRET']

ticker_name="SPY"

# Main

trading_client = TradingClient(
   alpaca_key_str,
   alpaca_secret_str,
)

# # Regular Order
# market_order_data = MarketOrderRequest(
#    symbol=ticker_name,
#    qty=1,
#    side=OrderSide.BUY,
#    time_in_force=TimeInForce.DAY,
# )
# market_order = trading_client.submit_order(market_order_data)
# print(f"Market Order: {market_order}")


# Limit Order
limit_order_data = LimitOrderRequest(
   symbol=ticker_name,
   qty=1,
   side=OrderSide.BUY,
   time_in_force=TimeInForce.DAY,
   limit_price=490.00
)
limit_order = trading_client.submit_order(limit_order_data)

print(f"Limit Order: {limit_order}")







