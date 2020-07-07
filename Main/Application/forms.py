from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from Application.models import User
from flask_login import current_user

class RegisterForm(FlaskForm):
    email = StringField('Email Address', 
        validators=[
            DataRequired(), 
            Email()
        ]
    )
    password = PasswordField('Email Address', 
        validators=[
            DataRequired(), 
            Length(min=5, max=15)
        ]
    )
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('Email Address', 
        validators=[
            DataRequired(),
            Email()
        ]
    )
    submit = SubmitField('play')