from database import db
from datetime import datetime

class BaseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


class Doctor(BaseModel, db.Model):
    email = db.Column(db.String(128), nullable=False, unique=True) # email
    first = db.Column(db.String(128), nullable=False)  # first name
    last = db.Column(db.String(128), nullable=False)  # last name
    specialty = db.Column(db.String(128), nullable=False) # specialty
    hospital = db.Column(db.String(128), nullable=False)  # hospital where employed
    city = db.Column(db.String(128), nullable=False)  # location of hospital
    rank = db.Column(db.String(128), default='active')  # can only pick rank from this set
    phone = db.Column(db.String(128), nullable=False)  # phone number
    password = db.Column(db.String(128), nullable=False)  # hashed password
    dp = db.Column(db.String(128), default="default-dp.jgp")  # default profile picture for init

print(Doctor)
