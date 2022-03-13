from biorhythm import app
from flask import render_template, url_for, redirect 
from forms import SignUpForm

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/register', method=['POST', 'GET'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        return redirect(url_for('homepage'))
    return render_template('register.html', title = 'Register', form = form)