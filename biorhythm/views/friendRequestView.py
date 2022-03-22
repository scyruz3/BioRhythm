from operator import methodcaller
from os import stat
from biorhythm import app
from biorhythm.manager import friendManager, userManager
from flask import request, Response


@app.route("/users/<userID>/friend-requests", methods=["POST"])
def post_friend_invite(userID):
    friendID = request.json.get('friendID')

    friendManager.send_friend_invite(userID, friendID)
    return Response(status=201)
