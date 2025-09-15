import requests

BOT_TOKEN = '<YOUR_BOT_TOKEN>'

def send_chat_id_to_user():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    response = requests.get(url)
    data = response.json()
    
    if data['ok'] and data['result']:
        for update in data['result']:
            if 'message' in update:
                chat_id = update['message']['chat']['id']
                message = f"Il tuo Chat ID è: {chat_id}"
                
                send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                send_data = {
                    'chat_id': chat_id,
                    'text': message
                }
                requests.post(send_url, data=send_data)
                print(f"Chat ID {chat_id} inviato all'utente")

if __name__ == "__main__":
    send_chat_id_to_user()