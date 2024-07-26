#!/usr/bin/env python3.12
from flask import Flask, make_response, jsonify
from flask_cors import CORS

from database import db
from models import get_doctors


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
@app.route('/login', strict_slashes=False)
def login():
    return "Login"

@app.route('/logout', strict_slashes=False)
def logout():
    return "Logout"

@app.route('/signup', strict_slashes=False)
def signup():
    return "Signup"

@app.get('/doctors', strict_slashes=False)
@app.get('/doctors/<int:id>', strict_slashes=False)
def doctor(id=None):
    """
    Returns a list of doctors if id is not specified, else
    returns doctor with specified id
    """
    result = get_doctors(id)
    return jsonify({
        "message": f"queried user with id {id}",
        "result": result
    })

@app.errorhandler(404)
def not_found(error):
    """ 404 error """
    return make_response(jsonify({"error":"Not found"}), 404)

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
