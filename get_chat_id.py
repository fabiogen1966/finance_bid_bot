import requests

# Sostituisci con il tuo bot token
BOT_TOKEN = '8416801496:AAHIU5uWJnF1mmWKRrxqPZZWacARCFwHnvM'

def get_chat_id():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    response = requests.get(url)
    data = response.json()
    
    if data['ok'] and data['result']:
        for update in data['result']:
            if 'message' in update:
                chat_id = update['message']['chat']['id']
                chat_type = update['message']['chat']['type']
                print(f"Chat ID: {chat_id}")
                print(f"Chat Type: {chat_type}")
                if 'username' in update['message']['chat']:
                    print(f"Username: @{update['message']['chat']['username']}")
                print("---")
    else:
        print("Nessun messaggio trovato. Invia un messaggio al bot prima.")

if __name__ == "__main__":
    get_chat_id()