from biorhythm import app
from flask import redirect, render_template, request, session
from biorhythm.manager import friendManager
from biorhythm.middleware.authMiddleware import protectedRoute


@app.route("/users/find", methods=["GET"])
@protectedRoute
def find_users(current_user):
    query = request.args.get("query")
    results = friendManager.find_users_by_username(query)
    return render_template("findUsers.html", query=query, results=results)
