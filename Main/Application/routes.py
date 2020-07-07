from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from Application import app, db, login_manager, crypt
from Application.forms import RegisterForm
from Application.models import User

@app.route('/')
def main():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST']) #write functionality
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        DATA=User(email=form.email.data, password=crypt.generate_password_hash(form.password.data))
        db.session.add(DATA)
        db.session.commit
        return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and crypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            if request.args.get('next'):
                return redirect(request.args.get('next'))
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='login', form=form)

@login_required
@app.route('/home', methods=['GET'])
def home()

@login_required
@app.route('/edit/user', methods=['GET', 'POST'])
def edit():
    return render_template('')

@login_required
@app.route('/slots', methods=['GET'])
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

@login_required
@app.route('/logout')
def logout():