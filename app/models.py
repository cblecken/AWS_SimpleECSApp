from . import db
from datetime import datetime


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.String(255), unique=True, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    currencyCode = db.Column(db.String(50), nullable=False)
    createdOn = db.Column(db.DateTime, default=datetime.utcnow)
    updatedOn = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.productId,
            'type': self.type,
            'price': self.price,
            'currencyCode': self.currencyCode,
            'createdOn': self.createdOn,
            'updatedOn': self.updatedOn
        }
