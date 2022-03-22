from biorhythm import app
from flask import redirect, render_template, request, session
from biorhythm.manager import friendManager


@app.route("/users/find", methods=["GET"])
def find_users():
    query = request.args.get("query")
    results = friendManager.find_users_by_username(query)
    return render_template(
        "findUsers.html",
        query=query,
        results=results
    )
