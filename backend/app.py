#!/usr/bin/env python3.12
from flask import Flask, make_response, jsonify, request, session
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

from config import ApplicationConfig
from database import db
from models import Doctor, get_doctors


app = Flask(__name__)
app.config.from_object(ApplicationConfig)
server_session = Session(app)

# initialize SQLAlchemy with flask app
db.init_app(app)

def create_db():
    """ create db with app context """
    with app.app_context():
        db.create_all()

CORS(app, support_credentials=True)


@app.route('/')
def home():
    return {'message': 'Hello World!'}

""" auth routes """
@app.route('/login', methods=["GET", "POST"], strict_slashes=False)
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
    user = Doctor.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"error": "username or password incorrect"}), 401
    if not check_password_hash(password, user.password):
        return jsonify({"error": "username or password incorrect"}), 401
    
    session["user_id"] = user.id
    return jsonify({
        "id": user.id,
        "email": user.email
    })

@app.route('/logout', strict_slashes=False)
def logout():
    session.pop("user_id")
    return "200"

@app.route('/signup', strict_slashes=False)
def signup():
    """ sign up a new user """
    user_exists = Doctor.query.filter_by(email=request.email).first()

    if user_exists:
        return jsonify({"error": "User exists"}), 409
    
    new_user = Doctor(
        email = request.email,
        first = request.first_name,
        last = request.last_name,
        specialty = request.specialty,
        hospital = request.hospital,
        city = request.city,
        rank = request.ranking,
        phone = request.phone,
        password = generate_password_hash(request.password)
    )
    return new_user.register_doctor()

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
