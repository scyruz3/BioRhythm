from biorhythm import app
from flask import render_template, session


@app.route("/dashboard")
def get_dashboard():
    # getBioRhythm(userId)
    session["userId"] = 1234
    print(session["userId"])
    return render_template("index.html")
