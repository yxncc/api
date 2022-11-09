from sqlalchemy import Integer
from ..extensions import db

OrderProduct = db.Table('orders_products',
                        db.Column('id', Integer, primary_key=True),
                        db.Column('product_id', Integer, db.ForeignKey('products.id')),
                        db.Column('order_id', Integer, db.ForeignKey('orders.id')))


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(Integer, primary_key=True)
    worker_id = db.Column(Integer, db.ForeignKey('workers.id'))
    user_id = db.Column(Integer, db.ForeignKey('users.id'))

    worker = db.relationship('Worker', back_populates='orders')
    user = db.relationship('User', back_populates='orders')
    products = db.relationship('Product', secondary=OrderProduct, backref='Order')
