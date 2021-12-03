import logging

from flask import Flask, request, jsonify

from app.models import Product
import datetime
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app = Flask(__name__)

items = []


@app.route('/', methods=['GET'])
def get_root():
    logger.error("get_root")
    response = jsonify({'results': 'root context'})
    return response


@app.route('/api/products', methods=['GET'])
def products():
    global items
    logger.info(request)
    logger.error("products")
    res = []
    for row in items:
        res.append(row.to_json())

    response = jsonify({'results': res})
    return response


@app.route('/api/product/create', methods=['POST'])
def post_create():
    global items
    item = None
    try:
        logger.info(request)
        logger.error("post_create")
        logger.info(request.data)
        obj = json.loads(request.data)
        # for key, value in request.form.items():
        #     logger.info(key, ':', value)
        # productId = request.form['productId']
        # type = request.form['type']
        # price = request.form['price'].strip('\n')
        # currencyCode = request.form['currencyCode']
        logger.info(obj["productId"])

        item = Product()
        item.productId = obj["productId"]
        item.type = obj["type"]
        item.price = obj["price"]
        item.currencyCode = obj["currencyCode"]
        item.createdOn = datetime.datetime.utcnow()

        items.append(item)

    except Exception as e:
        logger.error("ERROROR in create", e)
    if item:
        response = jsonify({'message': 'Product added', 'product': item.to_json()})
    else:
        response = "Could not add product"
    return response


@app.route('/data', methods=['GET'])
def get_query_string():
    logger.info("get_query_string")
    return request.query_string


@app.route('/api/product/<productId>', methods=['GET'])
def product(productId):
    logger.error("product")
    global items
    item = None
    for i in items:
        if i.productId == productId:
            item = i
            break
    if item is not None:
        response = jsonify({'result': item.to_json()})
    else:
        response = jsonify({'message': 'Cannot find product'}), 404
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
