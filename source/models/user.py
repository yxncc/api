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

    def update(self, data):
        self.first_name = data.first_name
        self.last_name = data.last_name
        self.father_name = data.father_name
        self.email = data.email
