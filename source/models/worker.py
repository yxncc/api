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
    post_id = db.Column('post_id', db.ForeignKey('posts.id'))

    post = db.relationship('Post', back_populates='workers')
    zakaz = db.relationship('Zakaz', back_populates='worker')


