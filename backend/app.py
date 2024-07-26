#!/usr/bin/env python3.12
from flask import Flask
from flask_cors import CORS

from database import db
from models import Doctor


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///intron.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize SQLAlchemy with flask app
db.init_app(app)

def create_db():
    """ create db with app context """
    with app.app_context():
        db.create_all()

CORS(app)


@app.route('/')
def home():
    return {'message': 'Hello World!'}

""" auth routes """
@app.route('/login')
def login():
    return "Login"

@app.route('/logout')
def logout():
    return "Logout"

@app.route('/signup')
def signup():
    return "Signup"

@app.get('/doctors')
def doctor():
    """
    Returns a list of doctors if email is not specified, else
    returns doctor with specified email
    """
    result = Doctor.query.first()
    print(result.first)
    return(result.first)

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
