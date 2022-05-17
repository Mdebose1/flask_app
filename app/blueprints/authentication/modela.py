from enum import unique
import uuid
from datetime import datetime as dt
from app import db

class Signup(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    email=db.Column(db.String(50), unique=True)
    password=db.Column(db.String(300))
    date_created = db.Column(db.DateTime, default=dt.utcnow)
