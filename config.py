import dotenv
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s - %(lineno)d")

try:
    config_env = dotenv.dotenv_values(".env")
except Exception as e:
    logging.error("An error occurred while loading .env file : %s", str(e))

mongodb_uri = config_env['MONGODB_URI']
openai_api_key = config_env['OPENAI_API_KEY']

rapid_api_key = config_env['RAPID_API_KEY']
rapid_api_host = "linkedin-jobs-search.p.rapidapi.com"
rapid_api_url = "https://linkedin-jobs-search.p.rapidapi.com/"
page_count=2
