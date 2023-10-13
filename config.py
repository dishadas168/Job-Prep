import dotenv

config_env = dotenv.dotenv_values(".env")
mongodb_uri = config_env['MONGODB_URI']