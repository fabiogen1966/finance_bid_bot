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

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = '<YOUR_BOT_TOKEN>'
TELEGRAM_CHAT_ID = '<YOUR_CHAT_ID>'

# Polling interval in seconds
POLLING_INTERVAL = 300  # 5 minutes

# Price thresholds for alerts
PRICE_THRESHOLDS = {
    'oro': 2000.0,
    'argento': 25.0,
    'petrolio': 70.0,
    'rame': 4.0
}

# List of available tickers for easy reference
AVAILABLE_TICKERS = list(SYMBOL_MAPPING.keys())