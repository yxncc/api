from sqlalchemy import Integer, String
from ..extensions import db


class Position(db.Model):
    __tablename__ = 'positions'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50), unique=True)

    workers = db.relationship('Worker', back_populates='position')
