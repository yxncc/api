from sqlalchemy import Integer, String

from .order import OrderProduct
from ..extensions import db


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(Integer, primary_key=True)
    provider_id = db.Column(
        Integer,
        db.ForeignKey('providers.id'),
        unique=True
    )

    provider = db.relationship('Provider', back_populates='products')
    orders = db.relationship('Order', secondary=OrderProduct, backref='Product')