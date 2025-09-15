# Example usage of the parametric finance bot

from myUtilities import get_current_price, get_available_symbols, add_symbol_mapping
from config import SYMBOL_MAPPING

def main():
    # Show available symbols
    print("Available symbols:", get_available_symbols())
    
    # Get price for existing symbol
    try:
        price = get_current_price('oro')
        print(f"Gold price: ${price}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Add new symbol mapping at runtime
    add_symbol_mapping('bitcoin', 'BTC-USD')
    
    # Use the new symbol
    try:
        btc_price = get_current_price('bitcoin')
        print(f"Bitcoin price: ${btc_price}")
    except Exception as e:
        print(f"Error getting Bitcoin price: {e}")

if __name__ == "__main__":
    main()