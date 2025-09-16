import requests
from config import EXCHANGERATE_API_KEY
import time

def get_all_supported_currencies():
    """Ottiene tutti i codici valuta supportati da ExchangeRate-API"""
    
    # Endpoint per ottenere tutti i tassi di cambio
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGERATE_API_KEY}/latest/USD"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if 'conversion_rates' in data:
            currencies = list(data['conversion_rates'].keys())
            return currencies
        else:
            print("Errore: nessun dato trovato")
            return []
            
    except Exception as e:
        print(f"Errore nell'ottenere i dati: {e}")
        return []

def filter_commodities(currencies):
    """Filtra le commodities dai codici valuta"""
    
    # Codici comuni per commodities e metalli preziosi
    commodity_codes = {
        'XAU': 'Oro',
        'XAG': 'Argento', 
        'XPT': 'Platino',
        'XPD': 'Palladio',
        'XCU': 'Rame',
        'XOI': 'Petrolio',
        'XNG': 'Gas Naturale',
        'XWH': 'Grano',
        'XCO': 'Mais',
        'XSO': 'Soia',
        'XSU': 'Zucchero',
        'XCF': 'Caffè',
        'XCC': 'Cacao'
    }
    
    found_commodities = {}
    
    for code in currencies:
        if code in commodity_codes:
            found_commodities[code] = commodity_codes[code]
    
    return found_commodities

if __name__ == "__main__":
    print("\nOttenendo tutti i codici valuta supportati da ExchangeRate-API...")
    print("=" * 60)
    
    # Ottieni tutti i codici supportati
    currencies = get_all_supported_currencies()
    
    if currencies:
        print(f"\nTotale codici valuta supportati: {len(currencies)}")
        print("\nPrimi 20 codici:")
        for i, currency in enumerate(currencies[:20]):
            print(f"  {currency}")
        
        print("\n" + "=" * 60)
        print("Ricerca commodities...")
        
        # Filtra le commodities
        commodities = filter_commodities(currencies)
        
        if commodities:
            print(f"\nCommodities trovate ({len(commodities)}):")
            for code, name in commodities.items():
                print(f"  {code}: {name}")
        else:
            print("\nNessuna commodity trovata nei codici standard.")
            
        print("\n" + "=" * 60)
        print("Tutti i codici supportati:")
        for currency in currencies:
            print(f"  {currency}")
            
    else:
        print("Impossibile ottenere i dati dall'API.")