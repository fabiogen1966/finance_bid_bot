# Configuration file for finance symbols mapping

SYMBOL_MAPPING = {
    'oro': 'XAU',         # Gold
    'argento': 'XAG',     # Silver
    'petrolio': 'WTI',    # West Texas Intermediate
    'rame': 'COPPER'      # Copper
}

# Units for each symbol
SYMBOL_UNITS = {
    'oro': 'USD/OZ', 
    'argento': 'USD/OZ',
    'petrolio': 'USD/BBL',
    'rame': 'USD/LB'
}

# Alpha Vantage API Configuration
# <-- INSERISCI QUI LA TUA CHIAVE API
ALPHA_VANTAGE_API_KEY = 'ILOSTKEZ9LL3O0AY'

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = '8416801496:AAHIU5uWJnF1mmWKRrxqPZZWacARCFwHnvM'
TELEGRAM_CHAT_ID = '268510781'

# Polling interval in seconds
POLLING_INTERVAL = 15  # 5 minutes

# Price thresholds for alerts
PRICE_THRESHOLDS = {
    'oro': 3810.0,
    'argento': 41.0,
    'petrolio': 61.0,
    'rame': 4.0
}

# List of available tickers for easy reference
AVAILABLE_TICKERS = list(SYMBOL_MAPPING.keys())