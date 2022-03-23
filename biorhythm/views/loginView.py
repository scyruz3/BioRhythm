from biorhythm import app
from flask import render_template, redirect, request
from biorhythm.manager import loginManager
from biorhythm.utils.LoginForm import LoginForm


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        if loginManager.login(username=form.username.data, password=form.password.data):
            return redirect("/")
        else:
            # some error
            print("nope")
    return render_template("login.html", form=form)
