import requests
import config
from database import Database
import uuid
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s - %(lineno)d")

db = Database()

url = config.rapid_api_url

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": config.rapid_api_key,
    "X-RapidAPI-Host": config.rapid_api_host
}

def extract_data(positions, location):
    logging.info("Fetching data...")

    jobs_jsonlist = []
    for page in range(1, config.page_count+1):
        try:
            payload = {
                "search_terms": str(positions),
                "location": str(location),
                "page": str(page)
            }
            response = requests.post(url, json=payload, headers=headers)

            if len(response.json()) != 0:
                jobs_jsonlist.extend(response.json())
            else:
                logging.warning("No jobs found for page %d", page)

        except Exception as e:
            logging.error(
                "An error occurred while fetching jobs for page %d: %s", page, str(e)
            )
        
    logging.info("Storing raw data in database...")

    #TODO: Check if search already exists. If yes, add unique records only
    search_id = str(uuid.uuid4())
    db.store_search_id(search_id, positions, location)

    for jobs in jobs_jsonlist:
        jobs["search_id"] = search_id
    db.store_raw(jobs_jsonlist)


    
