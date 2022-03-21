from os import stat
from biorhythm import app
from biorhythm.manager import friendManager
from flask import request, Response


@app.route("/user/<userID>/friend-requests", method=["POST"])
def post_friend_invite(userID):
    friendID = request.json.get('friendID')

    friendManager.send_friend_invite(userID, friendID)
    return Response(status=201)
