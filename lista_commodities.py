import requests
from config import COMMODITIES_API_KEY
import time

def get_all_supported_commodities():
    """Ottiene tutte le commodities supportate da Commodities-API"""
    
    # Endpoint per ottenere tutti i simboli supportati
    url = f"https://commodities-api.com/api/symbols?access_key={COMMODITIES_API_KEY}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        print(f"Debug response: {data}")
        
        if 'data' in data:
            return data['data']
        else:
            print("Errore: nessun dato trovato")
            return {}
            
    except Exception as e:
        print(f"Errore nell'ottenere i dati: {e}")
        return {}

def get_latest_rates():
    """Ottiene i tassi più recenti per tutte le commodities"""
    
    url = f"https://commodities-api.com/api/latest?access_key={COMMODITIES_API_KEY}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        print(f"Debug rates: {data}")
        
        if 'data' in data and 'rates' in data['data']:
            return data['data']['rates']
        else:
            return {}
            
    except Exception as e:
        print(f"Errore nell'ottenere i tassi: {e}")
        return {}

if __name__ == "__main__":
    print("\nOttenendo tutte le commodities supportate da Commodities-API...")
    print("=" * 60)
    
    # Ottieni tutti i simboli supportati
    symbols = get_all_supported_commodities()
    
    if symbols:
        print(f"\nCommodities supportate ({len(symbols)}):")
        for code, info in symbols.items():
            print(f"  {code}: {info}")
    else:
        print("Nessun simbolo trovato o errore API")
    
    print("\n" + "=" * 60)
    print("Ottenendo tassi attuali...")
    
    # Ottieni i tassi attuali
    rates = get_latest_rates()
    
    if rates:
        print(f"\nTassi attuali ({len(rates)}):")
        for commodity, rate in rates.items():
            print(f"  {commodity}: {rate}")
    else:
        print("Nessun tasso trovato o errore API")