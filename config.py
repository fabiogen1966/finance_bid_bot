# Configuration file for finance symbols mapping

SYMBOL_MAPPING = {
    'oro': 'GC=F',      # Gold Futures
    'argento': 'SI=F',  # Silver Futures
    'petrolio': 'CL=F', # Crude Oil Futures
    'rame': 'HG=F'     # Copper Futures
}

# Units for each symbol
SYMBOL_UNITS = {
    'oro': 'USD/OZ', 
    'argento': 'USD/OZ',
    'petrolio': 'USD/BBL',
    'rame': 'USD/LB'
}

# List of available tickers for easy reference
AVAILABLE_TICKERS = list(SYMBOL_MAPPING.keys())