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
