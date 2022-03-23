from biorhythm import app
from flask import render_template, redirect, request
from biorhythm.utils.SignUpForm import SignUpForm
from biorhythm.manager import registerManager

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = SignUpForm(request.form)
    if request.method == "POST":
        registerManager.registerUser(form)
    return render_template('register.html', title = 'Register', form = form)
