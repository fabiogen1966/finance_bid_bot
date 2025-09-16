import requests
from config import SYMBOL_MAPPING, AVAILABLE_TICKERS, ALPHA_VANTAGE_API_KEY
import time

def get_current_price(symbol):
    ticker = SYMBOL_MAPPING.get(symbol.lower())
    
    if ticker is None:
        raise ValueError(f"Symbol {symbol} not found in mapping. Available symbols: {AVAILABLE_TICKERS}")
    
    if ticker in ['XAU', 'XAG']:
        # Usa ETF per metalli preziosi
        etf_symbol = 'GLD' if ticker == 'XAU' else 'SLV'  # ETF per oro e argento
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={etf_symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if 'Global Quote' in data and '05. price' in data['Global Quote']:
            price = float(data['Global Quote']['05. price'])
            # Converti da prezzo ETF a prezzo per oncia
            if ticker == 'XAU':
                price = price * 10  # GLD rappresenta circa 1/10 di oncia d'oro
            else:
                price = price  # SLV prezzo diretto
            return round(price, 2)
        elif 'Error Message' in data:
            raise ValueError(f"API Error for {symbol}: {data['Error Message']}")
        else:
            raise ValueError(f"No real price data available for {symbol}")
    
    elif ticker in ['WTI', 'COPPER']:
        # Per commodities usa TIME_SERIES_DAILY per ETF correlati
        etf_symbol = 'USO' if ticker == 'WTI' else 'CPER'  # ETF per petrolio e rame
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={etf_symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if 'Global Quote' in data and '05. price' in data['Global Quote']:
            price = float(data['Global Quote']['05. price'])
            # Converti da prezzo ETF a prezzo commodity
            if ticker == 'WTI':
                price = price * 2.5  # USO conversione approssimativa
            else:
                price = price * 0.14  # CPER conversione per rame
            return round(price, 2)
        elif 'Error Message' in data:
            raise ValueError(f"API Error for {symbol}: {data['Error Message']}")
        else:
            raise ValueError(f"No real price data available for {symbol}")
    
    else:
        raise ValueError(f"No API endpoint available for {symbol}")

def get_available_symbols():
    """Return list of available symbols"""
    return AVAILABLE_TICKERS.copy()

def add_symbol_mapping(symbol, ticker):
    """Add new symbol mapping at runtime"""
    SYMBOL_MAPPING[symbol.lower()] = ticker
    if symbol.lower() not in AVAILABLE_TICKERS:
        AVAILABLE_TICKERS.append(symbol.lower())