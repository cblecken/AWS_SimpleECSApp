import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class AWSConfig(Config):
    ENV = "devAWS"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymsql://databasedemo.catpojzm0jag.us-west-2.rds.amazonaws.com:3306/product'
    print(SQLALCHEMY_DATABASE_URI)


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@cproduct_dbase:3306/product'
    print(SQLALCHEMY_DATABASE_URI)
