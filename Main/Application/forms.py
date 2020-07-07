from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
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

class TopUpForm(FlaskForm):
    cash = IntegerField('£', validators=[DataRequired()])
    submit = SubmitField('add to account')
