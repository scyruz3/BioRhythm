from operator import methodcaller
from os import stat
from biorhythm import app
from biorhythm.manager import friendManager, userManager
from flask import request, Response


@app.route("/friend-requests", methods=["POST"])
def post_friend_invite():
    userID = request.json.get('userID')
    friendID = request.json.get('friendID')

    friendManager.send_friend_invite(userID, friendID)
    return Response(status=201)


@app.route("/friend-requests/find", methods=["POST"])
def find_friend_invite():
    userID = request.json.get('userID')
    friendID = request.json.get('friendID')

    friendManager.find_request(userID, friendID)
    return Response(status=200)
