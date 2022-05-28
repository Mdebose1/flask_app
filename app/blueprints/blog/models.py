from enum import unique
import uuid
from datetime import datetime as dt
from app import db
import werkzeug
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


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


class User(db.Model, UserMixin):
    id = db.Column(db.String(32), primary_key=True)
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    email=db.Column(db.String(50), unique=True)
    password=db.Column(db.String(300))
    post=db.relationship('Post', backref='posts', cascade='all, delete-orphan')

    def generate_password(self, password_from_form):
        self.password = generate_password_hash(password_from_form)

    def check_password(self, password_from_from):
        return check_password_hash(self.password, password_from_from)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id=uuid.uuid4().hex

    def __repr__(self):
        return f'<User: {self.email}>'

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)    
