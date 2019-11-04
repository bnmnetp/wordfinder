from flask import Flask
from flask_wtf.csrf import CsrfProtect

csrf = CsrfProtect()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'row the boat'

csrf.init_app(app)

from . import controller
