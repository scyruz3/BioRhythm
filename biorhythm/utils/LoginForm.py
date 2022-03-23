from asyncio import wait_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField(
        label="Username", validators=[DataRequired(), Length(min=3, max=20)]
    )
    password = PasswordField(
        label="Password", validators={DataRequired(), Length(min=6, max=24)}
    )
    login = SubmitField(label="Login")
