import requests
from config import SYMBOL_MAPPING, AVAILABLE_TICKERS, COMMODITIES_API_KEY
import time

def get_current_price(symbol):
    ticker = SYMBOL_MAPPING.get(symbol.lower())
    
    if ticker is None:
        raise ValueError(f"Symbol {symbol} not found in mapping. Available symbols: {AVAILABLE_TICKERS}")
    
    # Usa Commodities-API per metalli preziosi e commodities
    if ticker == 'gold':
        commodity = 'XAU'
    elif ticker == 'silver':
        commodity = 'XAG'
    else:
        raise ValueError(f"No API available for {symbol}")
    
    url = f"https://commodities-api.com/api/latest?access_key={COMMODITIES_API_KEY}&symbols={commodity}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if 'data' in data and 'rates' in data['data'] and commodity in data['data']['rates']:
            # Commodities-API restituisce USD per oncia troy
            usd_per_oz = 1 / data['data']['rates'][commodity]
            usd_per_gram = usd_per_oz / 31.1035
            return round(usd_per_gram, 2)
        else:
            raise ValueError(f"No real price data available for {symbol}")
            
    except Exception as e:
        raise ValueError(f"Failed to fetch price for {symbol}: {str(e)}")

def get_available_symbols():
    """Return list of available symbols"""
    return AVAILABLE_TICKERS.copy()

def add_symbol_mapping(symbol, ticker):
    """Add new symbol mapping at runtime"""
    SYMBOL_MAPPING[symbol.lower()] = ticker
    if symbol.lower() not in AVAILABLE_TICKERS:
        AVAILABLE_TICKERS.append(symbol.lower())