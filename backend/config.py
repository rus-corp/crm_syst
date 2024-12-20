from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()


DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')



DB_PORT_TEST = os.getenv('DB_PORT_TEST')
DB_NAME_TEST = os.getenv('DB_NAME_TEST')
DB_HOST_TEST = os.getenv('DB_HOST_TEST')

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

super_user_email = os.getenv('SUPER_ADMIN').split(',')


BASE_DIR = Path(__file__).resolve().parent