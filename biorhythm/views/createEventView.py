from crypt import methods
from biorhythm import app
from flask import redirect, render_template, request, session, url_for
from biorhythm.manager import biorhythmManager, eventManager

@app.route("/newEvent", methods=["GET","POST"])
def newEvent():
    session['userId'] = '622d0e529523a13ef2ad42f8'
    if request.method == 'POST':
        newEvent = {
                'creator': session['userId'],
                'title': request.form['title'],
                'description': request.form['description'],
                'biorhythmType': biorhythmManager.getBioRhythmTypeForEvent(session['userId'], request.form['eDate']),
                'confirmedUsers': [],
                'eventDate': request.form['eDate'],
                'eventTime': request.form['etime'],
                'invitedUsers': []
            }
        session['eventId'] = eventManager.postEvent(newEvent)
        return redirect(url_for('inviteFriends'))
        
    else:
        return render_template(
            "createEvent.html",
        )


@app.route("/inviteFriends", methods=["GET", "POST"])
def inviteFriends():
    if request.method == 'POST':
        if('friendId' in request.form):
            eventManager.inviteFriendToEvent(session['eventId'], request.form['friendId'])
        else:
            eventManager.inviteAllFriends(session['eventId'], session['friendsToInvite'])

    session['friendsToInvite'] = biorhythmManager.getFriendsToInviteByBioRhythm(session['eventId'])
    return render_template(
        "inviteFriends.html",
        friends=session['friendsToInvite']
    )

@app.route("/modifyEvent",  methods=["GET", "POST"])
def modifyEvent():
    if request.method == 'POST':
        if('friendId' in request.form):
            eventManager.uninviteFriendFromEvent(request.args.get('event'), request.form['friendId'])     
        else:
            eventManager.updateEvent(session['eventId'], {
                'title': request.form['title'],
                'description': request.form['description'],
                'biorhythmType': biorhythmManager.getBioRhythmTypeForEvent(session['userId'], request.form['eventDate']),
                'eventDate': request.form['eventDate'],
                'eventTime': request.form['eventTime'],
            })
    biorhythm = biorhythmManager.getBioRhythm(session['userId'])
    eventValues = eventManager.getEvent(request.args.get('event'))
    return render_template(
    "modifyEvent.html",
    biorhythm=biorhythm,
    eventTitle=eventValues['title'],
    eventDescription=eventValues['description'],
    eventDate=eventValues['eventDate'],
    eventTime=eventValues['eventTime'],
    invitedUsers=eventValues['invitedUsers']
    )     

