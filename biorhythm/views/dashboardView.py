from biorhythm import app
from flask import redirect, render_template, session
from biorhythm.manager import biorhythmManager, eventManager
from biorhythm.middleware.authMiddleware import protectedRoute


@app.route("/", methods=["GET"])
@protectedRoute
def redirect_dashboard(current_user):
    return redirect("/dashboard")


@app.route("/dashboard", methods=["GET"])
@protectedRoute
def get_dashboard(current_user):
    biorhythm = biorhythmManager.getBioRhythm(current_user["userId"])
    createdEvents = eventManager.getEventsCreatedByUser(current_user["userId"])
    confirmedEvents = eventManager.getConfirmedEventsByUser(current_user["userId"])
    pendingEvents = eventManager.getPendingEventsByUser(current_user["userId"])
    return render_template(
        "dashboard.html",
        biorhythm=biorhythm,
        createdEvents=createdEvents,
        confirmedEvents=confirmedEvents,
        pendingEvents=pendingEvents,
    )
