from flask import redirect
from biorhythm import app
from biorhythm.manager import loginManager
from biorhythm.middleware.authMiddleware import protectedRoute


@app.route("/logout")
@protectedRoute
def logoutView(current_user):
    if loginManager.logout():
        return redirect("/login")
    return redirect("/")
