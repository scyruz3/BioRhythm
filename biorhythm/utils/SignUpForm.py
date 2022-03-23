from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed


class SignUpForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min = 3, max = 20)])
    photo = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    birthdate= DateField(label = 'DD/MM/YYYY', validators={DataRequired()})
    email = StringField(label='Email', validators={DataRequired(), Email()})
    password = PasswordField(label='Password', validators={DataRequired(), Length(min=6, max =24)})
    confirm_password = PasswordField(label= 'Confirm Password', validators={DataRequired(), EqualTo('password')})
    sign_up = SubmitField(label='Create Account!')
