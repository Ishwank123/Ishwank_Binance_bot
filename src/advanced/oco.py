    

def place_oco_order(client: Client, symbol: str, quantity: float, price: float, stop_price: float, stop_limit_price: float):
    try:
        order = client.futures_create_oco_order(
            symbol=symbol,
            side='SELL',
            quantity=quantity,
            price=str(price),
            stopPrice=str(stop_price),
            stopLimitPrice=str(stop_limit_price),
            stopLimitTimeInForce='GTC'
        )
        logger.info(f"OCO order placed: {order}")
        return order
    except Exception as e:
        logger.error(f"Failed to place OCO order: {e}")
        return None

