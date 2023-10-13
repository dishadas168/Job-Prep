import pymongo
import uuid
import config
from pathlib import Path
from utils import *

class Database:
    def __init__(self):
        self.client = pymongo.MongoClient(config.mongodb_uri)
        self.db = self.client["job-prep"]
        self.resume_collection = self.db["resumes"]


    def store_resumes(self, pdf):
        for filename in pdf:
            chunks=get_pdf_text(filename)
            self.resume_collection.insert_one({"filename": filename.name, "page_content": chunks})
    
