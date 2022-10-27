from sqlalchemy import Integer
from ..extensions import db

ZakazTovar = db.Table('ZakazTovar',
                      db.Column('id', Integer, primary_key=True),
                      db.Column('id_tovar', Integer, db.ForeignKey('Tovar')),
                      db.Column('id_zakaz', Integer, db.ForeignKey('Zakaz')))


class Zakaz(db.Model):
    tablename = 'zakaz'
    id = db.Column(Integer, primary_key=True)
    id_worker = db.Column(Integer, primary_key=True)
    id_user = db.Column(Integer, primary_key=True)
    user = db.relationship('User', back_populates='zakaz')
    tovars = db.relationship('Tovar', secondary=ZakazTovar, backref='Zakaz')


