import time
# Assumes logger and client are already set up

def place_twap_order(client, symbol, total_quantity, slices, interval_sec, side):
    logger.info(f"TWAP: Placing {slices} market orders for {symbol}, total_quantity={total_quantity}, interval={interval_sec}s")
    quantity_per_slice = total_quantity / slices
    for i in range(slices):
        try:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,  # 'BUY' or 'SELL'
                type='MARKET',
                quantity=quantity_per_slice
            )
            logger.info(f"TWAP slice {i+1}/{slices}: Order placed: {order}")
        except Exception as e:
            logger.error(f"TWAP slice {i+1}/{slices}: Error placing order: {e}")
        if i < slices - 1:
            time.sleep(interval_sec)

