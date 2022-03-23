from flask import redirect
from biorhythm import app
from biorhythm.manager import loginManager


@app.route("/logout")
def logoutView():
    if loginManager.logout():
        return redirect("/login")
    return redirect("/")
