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
        return redirect(url_for('inviteFriends', event = session['eventId']))
        
    else:
        return render_template(
            "createEvent.html",
        )


@app.route("/inviteFriends", methods=["GET", "POST"])
def inviteFriends():
    session['userId'] = '622d0e529523a13ef2ad42f8'
    session['eventId'] = request.args.get('event')
    if request.method == 'POST':
        if('friendId' in request.form):
            eventManager.inviteFriendToEvent(session['eventId'], request.form['friendId'])
        elif('list' in request.form):
            friendsToInvite = biorhythmManager.getFriendsToInviteByBioRhythm(session['eventId'])
            eventManager.inviteAllFriends(session['eventId'], friendsToInvite)
            
    friendsToInvite = biorhythmManager.getFriendsToInviteByBioRhythm(request.args.get('event'))
    eventValues = eventManager.getEvent(request.args.get('event'))
    return render_template(
        "inviteFriends.html",
        friends=friendsToInvite,
        eventId=session['eventId'],
        eventBR=eventValues['biorhythmType']
    )

@app.route("/modifyEvent",  methods=["GET", "POST"])
def modifyEvent():
    if request.method == 'POST':
        if('friendId' in request.form):
            eventManager.uninviteFriendFromEvent(request.args.get('event'), request.form['friendId'])    
        elif('cancel' in request.form):
            eventManager.deleteEvent(request.form['cancel'])
            return redirect('/dashboard')
        elif('eventTime' in request.form):
            eventManager.updateEvent(request.args.get('event'), {
                'title': request.form['title'],
                'description': request.form['description'],
                'biorhythmType': biorhythmManager.getBioRhythmTypeForEvent(session['userId'], request.form['eventDate']),
                'eventDate': request.form['eventDate'],
                'eventTime': request.form['eventTime'],
            })
    session['userId'] = '622d0e529523a13ef2ad42f8'
    session['eventId'] = request.args.get('event')
    biorhythm = biorhythmManager.getBioRhythm('622d0e529523a13ef2ad42f8')
    eventValues = eventManager.getEvent(request.args.get('event'))
    return render_template(
    "modifyEvent.html",
    biorhythm=biorhythm,
    eventId=session['eventId'],
    eventTitle=eventValues['title'],
    eventDescription=eventValues['description'],
    eventDate=eventValues['eventDate'],
    eventTime=eventValues['eventTime'],
    invitedUsers=eventValues['invitedUsers'],
    eventBR=eventValues['biorhythmType']
    )     

