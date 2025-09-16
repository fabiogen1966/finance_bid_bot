# Configuration file for finance symbols mapping

SYMBOL_MAPPING = {
    'oro': 'gold',
    'argento': 'silver'
}

# Units for each symbol
SYMBOL_UNITS = {
    'oro': 'USD/g',
    'argento': 'USD/g'
}

# Alpha Vantage API Configuration
ALPHA_VANTAGE_API_KEY = 'ILOSTKEZ9LL3O0AY'

# ExchangeRate-API Configuration (1500 richieste/mese gratis)
EXCHANGERATE_API_KEY = '27540f5cbbbd77bd87abcd70'

# Commodities-API Configuration
# <-- INSERISCI QUI LA TUA CHIAVE COMMODITIES
COMMODITIES_API_KEY = '27540f5cbbbd77bd87abcd70'

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