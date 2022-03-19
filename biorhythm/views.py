#from crypt import methods
import email
from unicodedata import category
from biorhythm import app, mongo
from flask import render_template, url_for, redirect, flash
from biorhythm.forms import SignUpForm
from biorhythm.dao.userDAO import createUser

db = mongo.db

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        user = createUser(
            username = form.username.data, 
            birthdate = form.birthdate.data,
            email = form.email.data,
            password = form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash (f'Account created successfully for{form.username.data}', category = 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)