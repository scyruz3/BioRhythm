from crypt import methods
from biorhythm import app
from flask import redirect, render_template, session
from biorhythm.manager import biorhythmManager, eventManager

@app.route("/inviteFriends")
def get_inviteFriends():
    biorhythm = biorhythmManager.getBioRhythm("622d0e529523a13ef2ad42f8")
    return render_template(
        "inviteFriends.html",
        biorhythm=biorhythm,
    )
