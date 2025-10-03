# Ishwank_Binance_bot
# This is command-line crypto trading bot for BINANCE USDT-M features, supporting MArket,Limit,OCO,TWAP and more advanced order types.All actions are logged, inputs are validated and the code base is modular for maintainability.

#dependencies : Python_Binance,pandas,python-dotenv

# Explanation: 
# market-order is simple buy/sell at the current price. If the current price is above the buy price the function would sell the coin if the price is below it will buy the coin.
# limit-order places a order at a specified price 
# oco(one cancels the other) it places a take-profit and stop loss simultaneously,if one executes the other stops
# twap(Time - weighhted average price) splits a large trade into smaller market orders.
