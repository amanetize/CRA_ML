from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("GEOLOC")
url = f'https://geocode.maps.co/search?q={{}}&api_key={api_key}'

def getloc(query):
    try:
        response = requests.get(url.format(query)).json()[0]
    except:
        return 'NaN'
    response = {"lat" : response['lat'], "lon" : response['lon']}
    
    return response