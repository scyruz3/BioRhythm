from email.message import EmailMessage
from tkinter import Label
from flask_wtf import Flaskform
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class SignUpForm(Flaskform):
    username = StringField(label='Username', validators=[DataRequired(), Length(min = 3, max = 20)])
    photo 
    birthdate
    email = StringField(label='Email', validators={DataRequired(), EmailMessage()})
    password = PasswordField(label='Password', validators={DataRequired(), Length(min=6, max =24)})
    confirm_password = PasswordField(label= 'Confirm Password', validators={DataRequired(), EqualTo('password')})
    sign_up = SubmitField(label='Sign up')
