from biorhythm import app
from flask import render_template
from flask_login import Login
from biorhythm.forms import LoginForm, SignUpForm

# @app.route("/")
# def hello_world():
#     return render_template("index.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)


@app.route('/log-in', methods = ['GET', 'POST'])
def log_in():
    form = LoginForm
    if form.validate_on_submit():
        user = form.get('username')
        password = form.get('password')

        