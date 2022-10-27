from sqlalchemy import Integer, String

from .zakaz import ZakazTovar
from ..extensions import db


class Tovars(db.Model):
    __tablename__ = 'tovar'
    id = db.Column(Integer, primary_key=True)
    id_provider = db.Column(String(50), unique=True)

    provider = db.relationship('Provider', back_populates='tovars')
    zakaz = db.relationship('Zakaz', secondary=ZakazTovar, backref='Tovar')
