from crypt import methods
from biorhythm import app
from flask import redirect, render_template, session
from biorhythm.manager import biorhythmManager, eventManager


@app.route("/", methods=["GET"])
def redirect_dashboard():
    return redirect("/dashboard")


@app.route("/dashboard", methods=["GET"])
def get_dashboard():
    biorhythm = biorhythmManager.getBioRhythm("622d0e529523a13ef2ad42f8")
    createdEvents = eventManager.getEventsCreatedByUser("622d0e529523a13ef2ad42f8")
    print(createdEvents)
    session["userId"] = 1234
    print(session["userId"])
    return render_template(
        "index.html", biorhythm=biorhythm, createdEvents=createdEvents
    )
