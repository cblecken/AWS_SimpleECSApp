import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.util import _collections, langhelpers
# from sqlalchemy.engine import url
# from sqlalchemy.dialects import mysql
# import pymysql

host = "127.0.0.1"
user = "root"
passwd = "123456"
database = "product"

# Database connection
# db_one = pymysql.connect(
#         host=host,
#         user=user,
#         passwd=passwd,
#         db=database,
#         port=3306,
#         autocommit=True)

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    environment_configuration = os.environ.get('CONFIGURATION_SETUP', 'config.DevelopmentConfig')

    app.config.from_object(environment_configuration)

    db.init_app(app)

    # with app.app_context():
    #     from .product_api import product_api_blueprint
    #     app.register_blueprint(product_api_blueprint)
    #     return app