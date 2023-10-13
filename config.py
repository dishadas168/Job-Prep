import dotenv

config_env = dotenv.dotenv_values(".env")
mongodb_uri = config_env['MONGODB_URI']
openai_api_key = config_env['OPENAI_API_KEY']