import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import Database

@pytest.fixture
def db():
    return Database()

def test_init(db):
    client = db.get_client()
    collection_names = client.list_collection_names()
    assert "resumes" in collection_names
    assert "raw_jobs" in collection_names
    assert "processed_jobs" in collection_names
    assert "search" in collection_names

def test_store_search_id(db):
    client = db.get_client()

    db.store_search_id("1234", "software engineer, data engineer", "united states, florida")
    result= client["search"].find_one({"_id" : "1234"})

    assert client["search"].count_documents({"_id" : "1234"}, limit = 1) != 0
    assert result["positions"] == "software engineer, data engineer"
    assert result["location"] == "united states, florida"

    client["search"].delete_one({"_id" : "1234"})


def test_store_raw(db):
    client = db.get_client()
    jsonlist = [
        {"_id": "1", "company_name": "microsoft", "job_title": "software developer", "search_id": "1"},
        {"_id": "2", "company_name": "amazon", "job_title": "sde 2", "search_id": "1"},
        {"_id": "3", "company_name": "microsoft", "job_title": "data scientist", "search_id": "1"}
    ]
    db.store_raw(jsonlist)
    result = list(client["raw_jobs"].find({"search_id": "1"}))

    assert len(result) == 3
    assert result[0] == jsonlist[0]
    assert result[1] == jsonlist[1]
    assert result[2] == jsonlist[2]

    client["raw_jobs"].delete_many({"search_id": "1"})


def test_store_processed(db):
    client = db.get_client()
    jsonlist = [
        {"_id": "1", "company_name": "microsoft", "job_title": "software developer", "search_id": "1"},
        {"_id": "2", "company_name": "amazon", "job_title": "sde 2", "search_id": "1"},
        {"_id": "3", "company_name": "microsoft", "job_title": "data scientist", "search_id": "1"}
    ]
    db.store_processed(jsonlist)
    result = list(client["processed_jobs"].find({"search_id": "1"}))

    assert len(result) == 3
    assert result[0] == jsonlist[0]
    assert result[1] == jsonlist[1]
    assert result[2] == jsonlist[2]

    client["processed_jobs"].delete_many({"search_id": "1"})

