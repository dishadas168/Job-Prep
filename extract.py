import requests
import config
from database import Database
import uuid

db = Database()

url = config.rapid_api_url

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": config.rapid_api_key,
    "X-RapidAPI-Host": config.rapid_api_host
}

def extract_data(positions, location):
    
    jobs_jsonlist = []
    for page in range(1, config.page_count+1):
        payload = {
            "search_terms": str(positions),
            "location": str(location),
            "page": str(page)
        }
        response = requests.post(url, json=payload, headers=headers)
        jobs_jsonlist.extend(response.json())

    #TODO: Check if search already exists. If yes, add unique records only
    search_id = str(uuid.uuid4())
    db.store_search_id(search_id, positions, location)

    for jobs in jobs_jsonlist:
        jobs["search_id"] = search_id
    db.store_raw(jobs_jsonlist)

    
