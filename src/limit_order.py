from binance.client import Client
from src.logger import logger
from src.utils import validate_symbol, validate_quantity

def place_limit_order(client: Client, symbol: str, quantity: float, price: float, side: str):
    if not validate_symbol(client, symbol) or not validate_quantity(quantity) or price <= 0:
        logger.error("Invalid limit order parameters")
        return None
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            timeInForce='GTC',
            quantity=quantity,
            price=str(price)
        )
        logger.info(f"Limit order placed: {order}")
        return order
    except Exception as e:
        logger.error(f"Failed to place limit order: {e}")
        return None
