from sqlalchemy import Integer, String
from ..extensions import db


class Worker(db.Model):
    __tablename__ = 'workers'
    id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String(50))
    last_name = db.Column(String(50))
    father_name = db.Column(String(50))
    email = db.Column(String(50), unique=True)
    birthday = db.Column(String(50))
    position_id = db.Column('position_id', db.ForeignKey('positions.id'))

    position = db.relationship('Position', back_populates='workers')
    orders = db.relationship('Order', back_populates='worker')

    def update(self, data):
        self.first_name = data.first_name
        self.last_name = data.last_name
        self.father_name = data.father_name
        self.email = data.email
        self.birthday = data.birthday
        self.position_id = data.position_id

