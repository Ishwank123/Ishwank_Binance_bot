def place_buy_order_symbol(client, symbol, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side='BUY',
            type='MARKET',
            quantity=quantity
        )
        logger.info(f"Buy market order placed for {symbol} quantity {quantity}: {order}")
        return order
    except Exception as e:
        logger.error(f"Error placing buy order: {e}")
        return None

def place_sell_order_symbol(client, symbol, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side='SELL',
            type='MARKET',
            quantity=quantity
        )
        logger.info(f"Sell market order placed for {symbol} quantity {quantity}: {order}")
        return order
    except Exception as e:
        logger.error(f"Error placing sell order: {e}")
        return None
