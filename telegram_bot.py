import time
import requests
import myUtilities as mu
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, POLLING_INTERVAL, PRICE_THRESHOLDS, SYMBOL_UNITS

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    requests.post(url, data=data)

def check_prices():
    for symbol, threshold in PRICE_THRESHOLDS.items():
        try:
            current_price = mu.get_current_price(symbol)
            unit = SYMBOL_UNITS.get(symbol, 'USD')
            
            if current_price < threshold:
                message = f"🚨 ALERT: {symbol.upper()} price dropped below threshold!\n"
                message += f"Current: {current_price} {unit}\n"
                message += f"Threshold: {threshold} {unit}"
                send_telegram_message(message)
                print(f"Alert sent for {symbol}: {current_price} < {threshold}")
        except Exception as e:
            print(f"Error checking {symbol}: {e}")

def main():
    print(f"Starting price monitoring bot...")
    print(f"Polling interval: {POLLING_INTERVAL} seconds")
    
    while True:
        check_prices()
        time.sleep(POLLING_INTERVAL)

if __name__ == "__main__":
    main()