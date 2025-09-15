import yfinance as yf
from config import SYMBOL_MAPPING, AVAILABLE_TICKERS

def get_current_price(symbol):
    # Get the Yahoo Finance ticker for the symbol
    ticker = SYMBOL_MAPPING.get(symbol.lower())
    
    if ticker is None:
        raise ValueError(f"Symbol {symbol} not found in mapping. Available symbols: {AVAILABLE_TICKERS}")
        
    # Get ticker info from Yahoo Finance
    yf_ticker = yf.Ticker(ticker)
    
    # Get current price (last closing price)
    current_price = yf_ticker.info['regularMarketPrice']
    
    return current_price

def get_available_symbols():
    """Return list of available symbols"""
    return AVAILABLE_TICKERS.copy()

def add_symbol_mapping(symbol, ticker):
    """Add new symbol mapping at runtime"""
    SYMBOL_MAPPING[symbol.lower()] = ticker
    if symbol.lower() not in AVAILABLE_TICKERS:
        AVAILABLE_TICKERS.append(symbol.lower())