from sqlalchemy import Integer, String
from ..extensions import db


class Worker(db.Model):
    __tablename__ = 'workers'
    id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String(50), unique=True)
    last_name = db.Column(String(50), unique=True)
    father_name = db.Column(String(50), unique=True)
    email = db.Column(String(50), unique=True)
    birthday = db.Column(String(50), unique=True)
    position_id = db.Column('position_id', db.ForeignKey('positions.id'))

    position = db.relationship('Position', back_populates='workers')
    orders = db.relationship('Order', back_populates='worker')


