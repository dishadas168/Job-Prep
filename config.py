import dotenv

config_env = dotenv.dotenv_values(".env")

mongodb_uri = config_env['MONGODB_URI']
openai_api_key = config_env['OPENAI_API_KEY']

rapid_api_key = config_env['RAPID_API_KEY']
rapid_api_host = config_env['RAPID_API_HOST']
rapid_api_url = config_env['RAPID_API_URL']
page_count=2