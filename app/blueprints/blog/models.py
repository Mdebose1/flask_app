from enum import unique
import uuid
from datetime import datetime as dt
from app import db


class Post(db.Model):
    # _all = []
    # def __init__(self, body, author):
    id = db.Column(db.String(32), primary_key=True)
    body = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    author = db.Column(db.ForeignKey('user.id'))
    # _all.append(self)

    def to_dict(self):
        return{
            'id':self.id, 
            'body': self.body,
            'date_created': self.date_created,
            'author': User.query.get(self.author)
        }
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id=uuid.uuid4().hex

    # @classmethod
    # def all(cls):
    #     return cls._all

    def __repr__(self):
        return f'<Post: {self.body[30]}...>'


class User(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    email=db.Column(db.String(50), unique=True)
    password=db.Column(db.String(300))
    post=db.relationship('Post', backref='posts', cascade='all, delete-orphan')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id=uuid.uuid4().hex

    def __repr__(self):
        return f'<User: {self.email}>'
