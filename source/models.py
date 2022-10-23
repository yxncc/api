from sqlalchemy import Column, Integer, String
from .extensions import db


class User(db.Model):
    tablename = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    posts = db.relationship('Post', back_populates='user')

    def init(self, name=None, email=None):
        self.name = name
        self.email = email

    def repr(self):
        return '<User %r>' % self.name


class Post(db.Model):
    tablename = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = db.Column('user_id', db.ForeignKey('users.id'), nullable=True)
    content = db.Column(String)

    user = db.relationship('User')
