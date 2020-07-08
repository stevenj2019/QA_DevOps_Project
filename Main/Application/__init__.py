from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('PROD_DB_URI'))
app.config['SECRET_KEY'] = str(os.getenv('PROD_SKEY'))

db = SQLAlchemy(app)
login_manager = LoginManager(app)
crypt = Bcrypt(app)
login_manager.login_view = 'login'

from Application import routes 