import requests
from deep_translator import GoogleTranslator

def fetch_news_from_cryptocompare(api_key, limit=10):
    url = f"https://min-api.cryptocompare.com/data/v2/news/?lang=EN&limit={limit}"
    headers = {'authorization': f'Apikey {api_key}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()['Data']
    else:
        print(f"Error: {response.status_code}")
        return None

def translate_to_russian(text):
    try:
        translator = GoogleTranslator(source='auto', target='ru')
        return translator.translate(text)
    except Exception as e:
        print(f"Error during translation: {e}")
        return text