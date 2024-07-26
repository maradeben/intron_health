from database import db
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from flask import make_response, jsonify
import json

class BaseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


class Doctor(BaseModel, db.Model):
    email = db.Column(db.String(128), nullable=False, unique=True) # id
    first = db.Column(db.String(128), nullable=False)  # first name
    last = db.Column(db.String(128), nullable=False)  # last name
    specialty = db.Column(db.String(128), nullable=False) # specialty
    hospital = db.Column(db.String(128), nullable=False)  # hospital where employed
    city = db.Column(db.String(128), nullable=False)  # location of hospital
    rank = db.Column(db.String(128), default='active')  # can only pick rank from this set
    phone = db.Column(db.String(128), nullable=False)  # phone number
    password = db.Column(db.String(128), nullable=False)  # hashed password
    dp = db.Column(db.String(128), default="default-dp.jgp")  # default profile picture for init

    def register_doctor(self):
        """ register a new doctor """
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print("user already exists")
            return jsonify({
                "message":"User already exists"
                })
        else:
            print("user added")
        return jsonify({
            "message": "registered successfully",
            "user": self
            })

    def to_dict(self):
        """ serialize object """
        doc_json = json.dumps({ self.id:
            {
            'id': self.id,
            'first': self.first,
            'last': self.last,
            'email': self.email,
            'phone': self.phone,
            'hospital': self.hospital,
            'city': self.city,
            'rank': self.rank,
            'specialty': self.specialty,
            'dp': self.dp,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)}
        })
        return doc_json

# print(Doctor)

""" database query operations """
def get_doctors(id: int=None):
    if id:
        result = Doctor.query.filter_by(id=id).first()
        return result.to_dict()
    else:
        result = Doctor.query.all()
        all_docs = []
        for doc in result:
            all_docs.append(doc.to_dict())
        result = all_docs
    return result
