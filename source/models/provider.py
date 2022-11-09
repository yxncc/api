from sqlalchemy import Integer, String
from ..extensions import db


class Provider(db.Model):
    __tablename__ = 'providers'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50), unique=True)

    products = db.relationship('Product', back_populates='provider', lazy=True)
