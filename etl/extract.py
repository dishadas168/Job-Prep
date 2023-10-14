import requests
import config
from database import Database

db = Database()

url = config.rapid_api_url

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": config.rapid_api_key,
    "X-RapidAPI-Host": config.rapid_api_host
}

def extract(positions, location):
    
    for page in range(1, config.page_count+1):
        payload = {
            "search_terms": str(positions),
            "location": str(location),
            "page": str(page)
        }
        response = requests.post(url, json=payload, headers=headers)
        db.push_to_db(response.json())
    
