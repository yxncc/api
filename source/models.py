from sqlalchemy import Column, Integer, String
from .extensions import db


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    posts = db.relationship('Post', back_populates='user')

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user = db.relationship('User')
    content = db.Column(String)