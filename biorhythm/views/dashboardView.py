from biorhythm import app
from flask import redirect, render_template, session
from biorhythm.manager import biorhythmManager, eventManager
from biorhythm.middleware.authMiddleware import protectedRoute


@app.route("/", methods=["GET"])
def redirect_dashboard():
    return redirect("/dashboard")


@app.route("/dashboard", methods=["GET"])
@protectedRoute
def get_dashboard(current_user_id):
    biorhythm = biorhythmManager.getBioRhythm("622d0e529523a13ef2ad42f8")
    createdEvents = eventManager.getEventsCreatedByUser("622d0e529523a13ef2ad42f8")
    confirmedEvents = eventManager.getConfirmedEventsByUser("622d0e529523a13ef2ad42f8")
    pendingEvents = eventManager.getPendingEventsByUser("622d0e529523a13ef2ad42f8")
    # session["userId"] = 1234
    return render_template(
        "dashboard.html",
        biorhythm=biorhythm,
        createdEvents=createdEvents,
        confirmedEvents=confirmedEvents,
        pendingEvents=pendingEvents,
    )
