from crypt import methods
from biorhythm import app
from flask import redirect, render_template, request, Response
from biorhythm.manager import biorhythmManager, eventManager

@app.route("/newEvent", methods=["GET","POST"])
def get_newEvent():
    biorhythm = biorhythmManager.getBioRhythm("622d0e529523a13ef2ad42f8")
    if request.method == 'POST':
        newEvent = {
                'creator': '622d0e529523a13ef2ad42f8',
                'title': request.form['title'],
                'description': 'This is the description',
                'biorhythmType': biorhythmManager.getBioRhythmTypeForEvent('622d0e529523a13ef2ad42f8', request.form['eDate']),
                'confirmedUsers': [],
                'eventDate': request.form['eDate'],
                'invitedUsers': []
            }

        eventManager.postEvent(newEvent, '20:35')

    return render_template(
        "createEvent.html",
        biorhythm=biorhythm        
    )
