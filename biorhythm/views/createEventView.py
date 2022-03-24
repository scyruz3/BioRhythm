from biorhythm import app
from flask import redirect, render_template, request, session, url_for
from biorhythm.manager import biorhythmManager, eventManager
from biorhythm.services import validateDate
from biorhythm.middleware.authMiddleware import protectedRoute


@app.route("/newEvent", methods=["GET", "POST"])
@protectedRoute
def newEvent(current_user):
    if request.method == "POST":
        if (
            request.form["title"] != ""
            and request.form["description"] != ""
            and request.form["eDate"] != ""
            and request.form["etime"] != ""
        ):
            if validateDate.validateHour(request.form["etime"]) == "valid":
                newEvent = {
                    "creator": current_user["userId"],
                    "title": request.form["title"],
                    "description": request.form["description"],
                    "biorhythmType": biorhythmManager.getBioRhythmTypeForEvent(
                        current_user["userId"], request.form["eDate"]
                    ),
                    "confirmedUsers": [],
                    "eventDate": request.form["eDate"],
                    "eventTime": request.form["etime"],
                    "invitedUsers": [],
                }
                session["eventId"] = eventManager.postEvent(newEvent)
                return redirect(url_for("inviteFriends", event=session["eventId"]))
            else:
                return render_template(
                    "createEvent.html",
                    errorMessage="Please enter a valid hour",
                    title=request.form["title"],
                    description=request.form["description"],
                    eventDate=request.form["eDate"],
                )
        else:
            return render_template(
                "createEvent.html",
                errorMessage="Please fill all forms",
                title=request.form["title"],
                description=request.form["description"],
                eventDate=request.form["eDate"],
                eventTime=request.form["etime"],
            )

    else:
        return render_template(
            "createEvent.html", title="", description="", eventDate="", eventTime=""
        )


@app.route("/inviteFriends", methods=["GET", "POST"])
@protectedRoute
def inviteFriends(current_user):
    session["eventId"] = request.args.get("event")
    if request.method == "POST":
        if "friendId" in request.form:
            eventManager.inviteFriendToEvent(
                session["eventId"], request.form["friendId"]
            )
        elif "list" in request.form:
            friendsToInvite = biorhythmManager.getFriendsToInviteByBioRhythm(
                session["eventId"]
            )
            eventManager.inviteAllFriends(session["eventId"], friendsToInvite)

    friendsToInvite = biorhythmManager.getFriendsToInviteByBioRhythm(
        request.args.get("event")
    )
    eventValues = eventManager.getEvent(request.args.get("event"))
    return render_template(
        "inviteFriends.html",
        friends=friendsToInvite,
        eventId=session["eventId"],
        eventBR=eventValues["biorhythmType"],
    )


@app.route("/modifyEvent", methods=["GET", "POST"])
@protectedRoute
def modifyEvent(current_user):
    if request.method == "POST":
        if "friendId" in request.form:
            eventManager.uninviteFriendFromEvent(
                request.args.get("event"), request.form["friendId"]
            )
        elif "cancel" in request.form:
            eventManager.deleteEvent(request.form["cancel"])
            return redirect("/dashboard")
        elif "eventTime" in request.form:
            if (
                request.form["title"] != ""
                and request.form["description"] != ""
                and request.form["eventDate"] != ""
                and request.form["eventTime"] != ""
            ):
                if validateDate.validateHour(request.form["eventTime"]) == "valid":
                    eventManager.updateEvent(
                        request.args.get("event"),
                        {
                            "title": request.form["title"],
                            "description": request.form["description"],
                            "biorhythmType": biorhythmManager.getBioRhythmTypeForEvent(
                                session["userId"], request.form["eventDate"]
                            ),
                            "eventDate": request.form["eventDate"],
                            "eventTime": request.form["eventTime"],
                        },
                    )
                else:
                    eventValues = eventManager.getEvent(session["eventId"])
                    return render_template(
                        "modifyEvent.html",
                        errorMessage="Please enter a valid hour",
                        eventId=session["eventId"],
                        eventTitle=eventValues["title"],
                        eventDescription=eventValues["description"],
                        eventDate=eventValues["eventDate"],
                        eventTime=eventValues["eventTime"],
                        invitedUsers=eventValues["invitedUsers"],
                        eventBR=eventValues["biorhythmType"],
                    )
            else:
                eventValues = eventManager.getEvent(session["eventId"])
                return render_template(
                    "modifyEvent.html",
                    errorMessage="Please fill all forms",
                    eventId=session["eventId"],
                    eventTitle=eventValues["title"],
                    eventDescription=eventValues["description"],
                    eventDate=eventValues["eventDate"],
                    eventTime=eventValues["eventTime"],
                    invitedUsers=eventValues["invitedUsers"],
                    eventBR=eventValues["biorhythmType"],
                )

    session["eventId"] = request.args.get("event")
    biorhythm = biorhythmManager.getBioRhythm(current_user["userId"])
    eventValues = eventManager.getEvent(request.args.get("event"))
    return render_template(
        "modifyEvent.html",
        biorhythm=biorhythm,
        eventId=session["eventId"],
        eventTitle=eventValues["title"],
        eventDescription=eventValues["description"],
        eventDate=eventValues["eventDate"],
        eventTime=eventValues["eventTime"],
        invitedUsers=eventValues["invitedUsers"],
        eventBR=eventValues["biorhythmType"],
    )
