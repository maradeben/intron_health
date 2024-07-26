""" authentication module """
from flask import Blueprint
from database import db
import app

# auth = Blueprint('auth', __name__)

@app.route('/login')
def login():
    return 'Login'

@app.route('/signup')
def signup():
    return 'Signup'

@app.route('/logout')
def logout():
    return 'Logout'
