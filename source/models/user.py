from sqlalchemy import Integer, String
from ..extensions import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String(50), unique=True)
    last_name = db.Column(String(50), unique=True)
    father_name = db.Column(String(50), unique=True)
    email = db.Column(String(50), unique=True)

    orders = db.relationship('Order', back_populates='user')


