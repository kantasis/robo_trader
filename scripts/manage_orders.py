#!/usr/local/bin/python3

# Imports
from os import environ
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, QueryOrderStatus

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

request_params = GetOrdersRequest(
   status = QueryOrderStatus.OPEN,
)

# # # Cancel open orders
# orders = trading_client.get_orders(request_params)
# # print(orders)
# for order in orders:
#    print(f"Canceling: {order.id}")
#    trading_client.cancel_order_by_id(order.id)

positions = trading_client.get_all_positions()

print(positions)


