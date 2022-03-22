#from crypt import methods
from unicodedata import category
from biorhythm import app
from flask import render_template, url_for, redirect, flash
from biorhythm.forms.forms import SignUpForm
from biorhythm.dao.userDAO import createUser

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
        flash (f'Account created successfully for{form.username.data}', category = 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)