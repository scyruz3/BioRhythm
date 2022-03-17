#from crypt import methods
from biorhythm import app
from flask import render_template, url_for, redirect 
from biorhythm.forms import SignUpForm

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)