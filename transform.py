import config
from database import Database
import urllib.request
from bs4 import BeautifulSoup
import time
import re
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s - %(lineno)d")

db = Database()

def modify_fields(data):

    fields_to_delete = ['job_url', 'company_name', 'company_url']
    key_rename_dict = {
        "linkedin_job_url_cleaned" : "job_url",
        "linkedin_company_url_cleaned" : "company_url",
        "normalized_company_name" : "company_name"
    }

    for job in data:
        for key in fields_to_delete: job.pop(key, None)
        for old_key in key_rename_dict: job[key_rename_dict[old_key]] = job.pop(old_key)
        job["applied"] = False

    return data


def extract_description(data):

    for job in data:
        job_url = job.get("job_url")
        if job_url:
            try:
                html = urllib.request.urlopen(job_url).read()
                soup = BeautifulSoup(html, features="html.parser")

                for script in soup(["script", "style"]):
                    script.extract() 

                text = soup.get_text()
                lines = (line.strip() for line in text.splitlines())
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                text = "\n".join(chunk for chunk in chunks if chunk)
                job["description"] = text
            except Exception as e:
                job["description"] = ""
                logging.error("An error occurred while scraping %s: %s", job_url, str(e))
        else:
            job["description"] = ""
        time.sleep(0.5)

    return data


def extract_salaries(data):

    for job in data:

        description = job["description"]

        salary_pattern_1 = r"\$([\d,]+)(?:\.(\d{2}))?"
        salary_pattern_2 = r"\$([\d\.]+)(K)"
        salary_pattern_3 = (
            r"\$(?!401K)([\d,]+)(?:\.(\d{2}))?\s*(K)?\s*-"
            r"\s*\$(?!401K)([\d,]+)(?:\.(\d{2}))?(K)?"
        )

        hourly_pattern = r"\$([\d\.]+)\s*to\s*\$([\d\.]+)\/hour"
        million_pattern = r"\b\d+M\b"

        # Search for patterns
        match1 = re.search(salary_pattern_1, description)
        match2 = re.search(salary_pattern_2, description)
        match3 = re.search(salary_pattern_3, description)
        match4 = re.search(hourly_pattern, description)
        match5 = re.search(million_pattern, description)

        salary_low, salary_high = None, None

        if match3:
            salary_low = (
                float(match3.group(1).replace(",", "")) * 1000
                if match3.group(3) == "K"
                else float(match3.group(1).replace(",", ""))
            )
            salary_high = (
                float(match3.group(4).replace(",", "")) * 1000
                if match3.group(6) == "K"
                else float(match3.group(4).replace(",", ""))
            )

        elif match2:
            salary_low = salary_high = float(match2.group(1).replace(",", "")) * 1000

        elif match1:
            salary_low = salary_high = (
                float(match1.group(1).replace(",", "") + "." + match1.group(2))
                if match1.group(2)
                else float(match1.group(1).replace(",", ""))
            )

        elif match4:
            salary_low = float(match4.group(2)) * 40 * 52
            salary_high = float(match4.group(3)) * 40 * 52

        elif match5:
            return (None, None)

        if salary_low is not None and salary_low < 100:
            salary_low *= 1000
        if salary_high is not None and salary_high < 100:
            salary_high *= 1000

        job["salary_low"] = float(salary_low) if salary_low is not None else None
        job["salary_high"] = float(salary_high) if salary_high is not None else None
    
    return data


def process_data():

    data = db.get_raw()

    if data is not None:

        logging.info("Modifying fields...")
        data = modify_fields(data)

        logging.info("Extracting descriptions...")
        data = extract_description(data)

        logging.info("Extracting salaries...")
        data = extract_salaries(data)

        logging.info("Storing processed data...")
        db.store_processed(data)

        logging.info("Processing data finished.")

    else:
        logging.warning("No data was processed.")

