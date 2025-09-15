import myUtilities as mu
from config import SYMBOL_MAPPING, SYMBOL_UNITS

if __name__ == "__main__":
    print("\nFetching current prices for various commodities...") 
    print("=" * 50)
    print("\n")

    for symbol in SYMBOL_MAPPING.keys():
        price = mu.get_current_price(symbol)
        unit = SYMBOL_UNITS.get(symbol, 'USD')
        print(f"The current price of {symbol} is: {price} {unit}")
    
    print("\n")