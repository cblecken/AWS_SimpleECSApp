from app import create_app, db
from flask import jsonify, Flask
from app import models
from flask_migrate import Migrate
import logging
from http.client import HTTPConnection

HTTPConnection.debuglevel = 1

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("__name__")

# app = create_app()
app = Flask(__name__)
migrate = Migrate(app, db)

items = []


@app.route('/')
def root():
    logger.info("root context")
    return "No Response"


@app.route('/api/product')
def product():
    response = jsonify(items[0])
    return response


@app.route('/api/products')
def products():
    response = jsonify({'results': items})
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
