from os import getenv
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

E_CLOUD_HOST = getenv("E_CLOUD_HOST")
E_CLOUD_USER = getenv("E_CLOUD_USER")
E_CLOUD_PSWD = getenv("E_CLOUD_PSWD")