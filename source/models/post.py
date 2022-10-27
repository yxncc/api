from sqlalchemy import Integer, String
from ..extensions import db


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50), unique=True)

    workers = db.relationship('Worker', back_populates='post')
