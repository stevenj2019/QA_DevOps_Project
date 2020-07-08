from Application import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(30), nullable = False)
    password = db.Column(db.String(500), nullable = False)
    balance = db.Column(db.Integer, nullable = False, default = 5)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))