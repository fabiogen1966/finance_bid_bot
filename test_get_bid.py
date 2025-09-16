import myUtilities as mu
from config import SYMBOL_MAPPING, SYMBOL_UNITS
import time

if __name__ == "__main__":
    print("\nFetching current prices for various commodities...") 
    print("=" * 50)
    print("\n")

    for symbol in SYMBOL_MAPPING.keys():
        try:
            price = mu.get_current_price(symbol)
            unit = SYMBOL_UNITS.get(symbol, 'USD')
            print(f"The current price of {symbol} is: {price} {unit}")
        except Exception as e:
            print(f"Error fetching price for {symbol}: {e}")
        
        # Wait 2 seconds between requests to avoid rate limiting
        time.sleep(2)
    
    print("\n")