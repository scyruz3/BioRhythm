from biorhythm import app
from flask import render_template, session
from biorhythm.manager import biorhythmManager


@app.route("/dashboard", methods=["GET"])
def get_dashboard():
    biorhythm = biorhythmManager.getBioRhythm("622d0e529523a13ef2ad42f8")
    session["userId"] = 1234
    print(session["userId"])
    return render_template("index.html", biorhythm=biorhythm)
