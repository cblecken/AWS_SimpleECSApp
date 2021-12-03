import logging

from . import product_api_blueprint
from .. import db
from ..models import Product
from flask import jsonify, request

logger = logging.Logger("__name__")


@product_api_blueprint.route('/', methods=['GET'])
def get_products():
    logger.info(request)
    logger.error("get_products")
    response = jsonify({'results': 'No Products'})
    return response


@product_api_blueprint.route('/health-check', methods=['GET'])
def get_health():
    logger.info(request)
    logger.error("get_health")
    response = jsonify({'results': 'NooProducts'})
    return response


@product_api_blueprint.route('/api/products', methods=['GET'])
def products():
    logger.info(request)
    logger.error("products")
    items = []
    for row in Product.query.all():
        items.append(row.to_json())

    response = jsonify({'results': items})
    return response


@product_api_blueprint.route('/api/product/create', methods=['POST'])
def post_create():
    logger.info(request)
    logger.error("post_create")
    productId = request.form['productId']
    type = request.form['type']
    price = request.form['price']
    currencyCode = request.form['currencyCode']

    item = Product()
    item.productId = productId
    item.type = type
    item.price = price
    item.currencyCode = currencyCode

    db.session.add(item)
    db.session.commit()

    response = jsonify({'message': 'Product added', 'product': item.to_json()})
    return response


@product_api_blueprint.route('/api/product/<productId>', methods=['GET'])
def product(productId):
    logger.error("product")
    item = Product.query.filter_by(productId=productId).first()
    if item is not None:
        response = jsonify({'result': item.to_json()})
    else:
        response = jsonify({'message': 'Cannot find product'}), 404
    return response
