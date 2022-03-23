from biorhythm import app
from flask import render_template, redirect, request
from biorhythm.utils.SignUpForm import SignUpForm
from biorhythm.manager import registerManager
from werkzeug.utils import secure_filename


@app.route("/register", methods=["POST", "GET"])
def register():
    form = SignUpForm()
    if request.method == "POST" and form.validate_on_submit():
        registerManager.registerUser(form)
        return redirect("login")
    return render_template("register.html", title="Register", form=form)
