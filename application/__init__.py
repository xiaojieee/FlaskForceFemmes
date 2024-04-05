from flask import Flask
import os
from application import routes

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY



# from application import errors
