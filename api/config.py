from os import getenv

from dotenv import load_dotenv


class Config:
    load_dotenv()

    ENVIRONMENT = getenv('ENVIRONMENT')
    DEBUG = getenv('DEBUG')
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{getenv("SQLALCHEMY_DATABASE_USER")}:'
        f'{getenv("SQLALCHEMY_DATABASE_PASSWORD")}@'
        f'{getenv("SQLALCHEMY_DATABASE_HOST")}:'
        f'{getenv("SQLALCHEMY_DATABASE_PORT")}/'
        f'{getenv("SQLALCHEMY_DATABASE_NAME")}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
