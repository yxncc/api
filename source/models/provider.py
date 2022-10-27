from sqlalchemy import Integer, String
from ..extensions import db


class Provider(db.Model):
    __tablename__ = 'provider'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50), unique=True)

    tovars = db.relationship('Tovar', back_populates='provider')
