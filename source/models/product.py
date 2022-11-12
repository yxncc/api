from sqlalchemy import Integer, String

from .order import OrderProduct
from ..extensions import db


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String, nullable=False)
    provider_id = db.Column(
        Integer,
        db.ForeignKey('providers.id')
    )

    provider = db.relationship('Provider', back_populates='products')
    orders = db.relationship('Order', secondary='orders_products', back_populates='products')

    def update(self, data):
        self.name = data.name
