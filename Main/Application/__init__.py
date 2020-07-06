from flask import Flask, render_template, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

import os 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('PROD_DB_URI'))
app.config['SECRET_KEY'] = str(os.getenv('PROD_SKEY'))

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'main'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = (db.String, nullable = False)
    balance = (db.Integer, nullable = False)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class LoginForm(FlaskForm):
    email = StringField('Email Address', 
        validators=[
            DataRequired()
            Email()
        ]
    )
    submit = SubmitField('play')

@app.route('/')
def main():
    form = LoginForm()
    if form.validate_on_submit():
        db.session.add(User(email=form.email.data, balance=0))
        login_user(user)
        return redirect(url_for('slots'))
    return render_template('auth.html', form = form)

@app.route('/slots')
def slots():
    user = User.query.filter_by(id=current_user.id).first()
    slot_data = self.client.get('http://api_1/get/slot').get_json()['machine'] # is a list
    multi_data = self.client.get('http://api_2/get/multi').get_json()['multiply'] # is a string
    slot_value = self.client.post('http://api_3/get/total', json={'slot':slot_data, 'multiple':multi_data}).get_json()['TOTAL'] # is an int
    win = (slot_value != 0)
    if win == False:
        user.balance = user.balance - 1
    else:
        user.balance = user.balance + slot_value
    db.session.commit()
    return render_template('slots.html', machine = slot_data, multi = multi_data, balance = user.balance, win = win)   