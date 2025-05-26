from pydantic_settings import BaseSettings
from pathlib import Path
from typing import ClassVar

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    DB_PORT_TEST: str
    DB_NAME_TEST: str
    DB_HOST_TEST: str

    SECRET_KEY: str
    ALGORITHM: str
    SUPER_ADMIN: str
    BASE_DIR: ClassVar[Path] = Path(__file__).resolve().parent
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()






# from dotenv import load_dotenv
# import os

# load_dotenv()


# DB_USER = os.getenv('DB_USER')
# DB_PASSWORD = os.getenv('DB_PASSWORD')
# DB_HOST = os.getenv('DB_HOST')
# DB_PORT = os.getenv('DB_PORT')
# DB_NAME = os.getenv('DB_NAME')



# DB_PORT_TEST = os.getenv('DB_PORT_TEST')
# DB_NAME_TEST = os.getenv('DB_NAME_TEST')
# DB_HOST_TEST = os.getenv('DB_HOST_TEST')

# SECRET_KEY = os.getenv('SECRET_KEY')
# ALGORITHM = os.getenv('ALGORITHM')

# super_user_email = os.getenv('SUPER_ADMIN').split(',')


