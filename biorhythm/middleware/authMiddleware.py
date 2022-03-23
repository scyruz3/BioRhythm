from functools import wraps
from flask import redirect, session


def protectedRoute(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # check if the user id is in the session
        if "userId" in session:
            current_user_id = session.get("userId")
        # if the user id is not in the session, redirect
        else:
            return redirect("/login")

        return f(current_user_id, *args, **kwargs)

    return decorated
