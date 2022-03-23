from functools import wraps
from flask import redirect, session
from biorhythm import app

# custom decorator for route protection
# all views must include 'current_user' as the first
# parameter
def protectedRoute(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # check if the user id is in the session
        if "userId" in session:
            current_user = {
                "userId": session.get("userId"),
                "username": session.get("username"),
            }
        # if the user id is not in the session, redirect
        else:
            return redirect("/login")

        return f(current_user, *args, **kwargs)

    return decorated


# allows all views access to the user object
@app.context_processor
def inject_user():
    current_user = {
        "userId": session.get("userId"),
        "username": session.get("username"),
    }
    return dict(current_user=current_user)
