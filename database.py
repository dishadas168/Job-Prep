import pymongo
import uuid
import config
from pathlib import Path
from utils import *
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s - %(lineno)d")

class Database:
    def __init__(self):
        try:
            self.client = pymongo.MongoClient(config.mongodb_uri)
            self.db = self.client["job-prep"]
            self.resume_collection = self.db["resumes"]
            self.raw_jobs_collection = self.db["raw_jobs"]
            self.processed_jobs_collection = self.db["processed_jobs"]
            self.search_collection = self.db["search"]
        except Exception as e:
            logging.error("An error occurred while fetching MongoDB client: %s", str(e))
    
    def get_client(self):
        return self.db

    def store_search_id(self, search_id, positions, location):
        try:
            self.search_collection.insert_one({
                "_id" : search_id,
                "positions" : positions,
                "location"  : location
            })
        except Exception as e:
            logging.error("An error occurred while inserting search data: %s", str(e))

    #TODO: Modify to store unique values only
    def store_raw(self, jsonlist):
        try:
            self.raw_jobs_collection.delete_many({})
            self.raw_jobs_collection.insert_many(jsonlist)
        except Exception as e:
            logging.error("An error occurred while inserting raw data: %s", str(e))


    def store_processed(self, jsonlist):
        try:
            self.processed_jobs_collection.delete_many({})
            self.processed_jobs_collection.insert_many(jsonlist)
        except Exception as e:
            logging.error("An error occurred while inserting processed data: %s", str(e))


    def check_if_resume_exists(self):
        if self.resume_collection.count_documents({"type": "resume"}) > 0:
            return True
        else:
            return False

            
    def store_resume(self, pdf):

        if self.check_if_resume_exists():
            self.resume_collection.delete_one({"type": "resume"})

        chunks=get_text_from_pdf(pdf)
        self.resume_collection.insert_one({
            "type": "resume", 
            "filename": pdf.name, 
            "content": chunks})


    def get_resume(self):
        if self.check_if_resume_exists():
            return self.resume_collection.find_one({"type": "resume"})
        else:
            return None

    def get_raw(self):
        return list(self.raw_jobs_collection.find({}))

    def get_processed(self, applied=False):
        if applied:
            return list(self.processed_jobs_collection.find({"applied": True})) 
        else:
            return list(self.processed_jobs_collection.find({}))

    def update(self, df):
        for item in df:
            query = { "_id": item["_id"] }
            newvalue = { "$set": { "applied": item["applied"] } }
            self.processed_jobs_collection.update_one(query, newvalue)

