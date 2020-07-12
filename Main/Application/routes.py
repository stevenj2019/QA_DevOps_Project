from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from Application import app, db, login_manager, crypt
from Application.forms import UserForm, TopUpForm
from Application.models import User
import requests

@app.route('/')
@app.route('/register', methods=['GET', 'POST']) #write functionality
def register():
    form = UserForm()
    if request.method == 'POST': 
        if form.validate_on_submit():
            db.session.add(User(email=form.email.data, password=crypt.generate_password_hash(form.password.data)))
            db.session.commit
            return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UserForm()
    if request.method =='POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and crypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                if request.args.get('next'):
                    return redirect(request.args.get('next'))
                else:
                    return redirect(url_for('home'))
    return render_template('login.html', title='login', form=form)

@app.route('/home', methods=['GET'])
@login_required
def home():
    return render_template('home.html', title='home')


@app.route('/topup', methods=['GET', 'POST'])
@login_required
def topup():
    form = TopUpForm()
    if form.validate_on_submit():
        current_user.balance = current_user.balance + int(form.cash.data)
        db.session.commit()
    return render_template('topup.html', title='Top-Up account', form = form)

@app.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    user = User.query.filter_by(id=current_user.id).first()
    logout_user()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('register'))


@app.route('/slots', methods=['GET'])
@login_required
def slots():
    user = User.query.filter_by(id=current_user.id).first()
    slot_data = requests.get('http://api_1:5001/get/slot').json['machine']
    multi_request = requests.get('http://api_2:5002/get/multi').json['multiply']
    slot_value = requests.post('http://api_3:5003/get/total', json={'slot':slot_data, 'multiple':multi_data}).get_json()['TOTAL'] # is an int
    win = (slot_value != 0)
    if win == False:
        user.balance = user.balance - 1
    else:
        user.balance = user.balance + slot_value
    db.session.commit()
    return render_template('slots.html', machine = slot_data, multi = multi_data, balance = user.balance, win = win)   


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
